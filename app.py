import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint

import pandas as pd
import pymysql
from flask import Flask, render_template, request, flash, session
from pytz import timezone

from regBackHandler import emailHandler
from forgetPwdHandler import forgotPswdEmailHandler
from Email_Phone_checker import check, check_string


db = pymysql.connect(user='root', password="123456789", port=3306, database="bank_transaction", charset="utf8")
cur = db.cursor()
app = Flask(__name__)
app.config['SECRET_KEY'] = '@!@^&*&^*^$#$#&^%&$@%^$@$*(()&^%%'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact_us')
def contact_us():
    return render_template('contact-us.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/reg')
def reg():
    return render_template('reg.html')


@app.route('/custhome')
def custhome():
    return render_template('custhome.html')


@app.route('/forget')
def forget():
    return render_template('forget.html')


@app.route('/trans')
def trans():
    email = session.get('email')
    sql = "select * from transactions where semail='{}' ORDER BY date1 ASC".format(email)
    x = pd.read_sql_query(sql, db)
    session['recentTrans'] = list(set(x.raccno))
    return render_template('trans.html')


@app.route('/history')
def history():
    email = session.get('email')
    sql = "select * from transactions where semail='{}' ORDER BY date1 ASC".format(email)
    x = pd.read_sql_query(sql, db)
    x.drop(['id', 'saccno', 'semail', 'remail', 'swift', 'time1'], axis=1, inplace=True)
    x['amount'] = x['amount'].astype(float).round(2)
    x['amount'] = "$" + x['amount'].astype(str)
    return render_template('history.html', row_val=x.values.tolist())


@app.route('/regback', methods=['POST', 'GET'])
def regback():
    if request.method == 'POST':
        c = request.form['cname']
        e = request.form['email']
        p = request.form['pwd']
        # a = request.form['accno']
        a = int(''.join(["{}".format(randint(0, 9)) for _ in range(0, 9)]))
        b = request.form['balance']
        if c is None or c == "" or c.isspace():
            flash("Please enter customer name", "warning")
            return render_template('reg.html')

        if e is None or e == "" or e.isspace() or not check(e):
            flash("Please enter customer email id", "warning")
            return render_template('reg.html')

        if p is None or p == "" or p.isspace() or check_string(p):
            flash(check_string(p), "warning")
            return render_template('reg.html')

        if b is None or b == "" or b.isspace():
            flash("Please enter initial amount", "warning")
            return render_template('reg.html')

        result = pd.read_sql_query("SELECT * from registration", db)
        if a in result.accno:
            a = int(''.join(["{}".format(randint(0, 9)) for _ in range(0, 9)]))
        elif e in result['email'].values:
            flash("email already existed", "warning")
            return render_template('reg.html')
        else:
            s = emailHandler(e)
            sql = "INSERT INTO registration (custId,cname,email,Password,accno,balance) values(%s,%s,%s,%s,%s,%s)"
            cur.execute(sql, (s, c, e, p, a, b))
            db.commit()
            flash("Successfully account created and Customer ID sent to your mail please check it.", "success")
            return render_template('index.html')
    return render_template('reg.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        c = request.form['custId']
        password1 = request.form['pwd']

        sql = "select * from registration where custId='%s' and email='%s' and password='%s' " % (c, email, password1)
        cur.execute(sql)
        results = cur.fetchall()
        session['email'] = email
        if len(results) > 0:
            custId = results[0][1]
            if custId == c:
                x = pd.read_sql_query("select cname,accno,balance from registration where email='%s' "
                                      "and custId='%s'" % (email, c), db)
                cname = x['cname'][0]
                accno = x['accno'][0]
                balance = int(x['balance'][0])
                session['accno'] = accno
                session['balance'] = "$" + str(float(balance))
                session['cname'] = cname
                return render_template('custhome.html', msg=results[0][2], c=cname, a=accno, b=balance)

            else:
                flash("Login failed", "warning")
                return render_template('tender.html')
        else:
            flash("CustomerID value mismatches please try again", "danger")
            return render_template('index.html')

    return render_template('index.html')


@app.route('/transback', methods=['POST', 'GET'])
def transback():
    try:
        if request.method == 'POST':
            rname = request.form['rname']
            toaccount = request.form['accno']
            conaccno = int(request.form['conaccno'])
            swift = request.form['swift']
            ctg = request.form['ctg']
            amount = request.form['amount']
            remail = request.form['remail']
            transtype = request.form['transtype']
            accno = session.get('accno')
            bal = session.get('balance')
            email = session.get('email')

            ind_time1 = datetime.now(timezone("US/Eastern")).strftime('%m-%d-%Y %I:%M %p')
            ind_time = datetime.now(timezone("US/Eastern")).strftime('%H:%S %p')

            x = pd.read_sql_query("select count(*) from registration where email='%s'" % remail, db)
            count = x.values[0][0]

            x = pd.read_sql_query("select balance from registration where email='%s'" % remail, db)
            t2 = int(x.values[0][0]) + int(amount)

            if int(toaccount) == int(conaccno):
                if count == 1:
                    sql = "insert into transactions(saccno,semail,rname,remail,raccno,ctg,transtype,swift,amount,date1" \
                          ",time1) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (accno, email, rname, remail, toaccount, ctg, transtype, swift, int(amount), ind_time1, ind_time)
                    cur.execute(sql, val)
                    db.commit()

                    msg = 'Thanks for choosing online Banking.\n$.{} is debited from A/c {} for {} on {}.\n\nRegards,' \
                          '\nOnline Bank Service.'.format(amount, accno, ctg, ind_time1)
                    forgotPswdEmailHandler(email, msg)

                    total = float(bal.replace('$', '')) - float(amount)
                    session['balance'] = "$" + str(float(total))
                    sq = "update registration set balance='{}' where email='{}'".format(total, email)
                    cur.execute(sq)
                    db.commit()

                    sq1 = "update registration set balance='{}' where email='{}'".format(t2, remail)
                    cur.execute(sq1)
                    db.commit()

                    query = "select * from registration where email='{}'".format(email)
                    cur.execute(query)
                    val = cur.fetchone()
                    session['balance'] = val[6]

                    msg = 'You have received {}$. Credited by {} om {}.\n\nRegards,\nOnline Bank Service.'.format(
                        amount, accno, ind_time1)
                    forgotPswdEmailHandler(remail, msg)
                    flash("Transaction completed", "success")
                    return render_template("trans.html")
                else:
                    flash("Account holder Email not found", "info")
                    return render_template("trans.html")
            else:
                flash("Account Number not found", "info")
                return render_template("trans.html")

        return render_template('trans.html')
    except Exception as e:
        flash("Invalid Details Provided: {}".format(e))
        return render_template("trans.html")


@app.route('/forgetback', methods=['POST', 'GET'])
def forgetback():
    if request.method == "POST":
        email = request.form['email']
        cpwd = request.form['cpwd']
        pwd = request.form['pwd']
        if pwd == cpwd:
            cur.execute("update registration set password='%s' where email='%s'" % (pwd, email))
            db.commit()
            msg = 'Your Email Id password is successfully changed. Now you can login.\n\nRegards,Online Bank Service.'
            forgotPswdEmailHandler(email, msg)
            flash("Successfully password reset ", "success")
            return render_template("forget.html")
        else:
            flash("Password and Confirm password mismatches so please try again ", "success")
            return render_template("forget.html")
    return render_template('forget.html')


if __name__ == '__main__':
    app.run(debug=True)
