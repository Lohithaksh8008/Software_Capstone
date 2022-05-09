import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(Email):
    if re.fullmatch(regex, Email):
        return True
    else:
        return False


def check_string(s):
    if s.isspace() or s == "" or s is None:
        return "Please enter password"
    elif not any(x.isupper() for x in s):
        return 'String must have 1 upper case character.'
    elif not any(x.islower() for x in s):
        return 'String must have 1 lower case character.'
    elif not any(x.isdigit() for x in s):
        return 'String must have 1 number.'
    elif len(s) < 8:
        return 'String length should be atleast 8.'
    else:
        return None