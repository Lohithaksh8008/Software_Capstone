-- MySQL dump 10.13  Distrib 8.0.27, for macos11 (x86_64)
--
-- Host: 127.0.0.1    Database: bank_transaction
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `registration`
--

DROP TABLE IF EXISTS `registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registration` (
  `id` int NOT NULL AUTO_INCREMENT,
  `custId` varchar(100) DEFAULT NULL,
  `cname` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` varchar(100) NOT NULL,
  `accno` varchar(100) NOT NULL,
  `balance` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration`
--

LOCK TABLES `registration` WRITE;
/*!40000 ALTER TABLE `registration` DISABLE KEYS */;
INSERT INTO `registration` VALUES (4,'BANK878','Fathima','cse.takeoff@gmail.com','Neelu@123','890989098',8200),(5,'BANK282','Lakshmi','nagamchenchulakshmi@gmail.com','Lakshmi@506','678909876',4900);
/*!40000 ALTER TABLE `registration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `saccno` varchar(100) DEFAULT NULL,
  `semail` varchar(100) DEFAULT NULL,
  `rname` varchar(100) DEFAULT NULL,
  `remail` varchar(100) DEFAULT NULL,
  `raccno` varchar(100) DEFAULT NULL,
  `ctg` varchar(100) DEFAULT NULL,
  `transtype` varchar(100) DEFAULT NULL,
  `swift` varchar(100) DEFAULT NULL,
  `amount` int DEFAULT '0',
  `date1` varchar(100) DEFAULT NULL,
  `time1` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (15,'678909876','nagamchenchulakshmi@gmail.com','Fathima','cse.takeoff@gmail.com','890989098','Work','Other Country','IDIBPI0956',100,'11-02-2021 07:29 AM','07:29 AM'),(16,'678909876','nagamchenchulakshmi@gmail.com','Fathima','cse.takeoff@gmail.com','890989098','Work','Other Country','IDIBPI0956',100,'11-02-2021 07:44 AM','07:23 AM'),(17,'890989098','cse.takeoff@gmail.com','Lakshmi','nagamchenchulakshmi@gmail.com','678909876','Travel','Other State','IDIBPI0956',200,'11-02-2021 09:49 AM','09:42 AM'),(18,'890989098','cse.takeoff@gmail.com','Lakshmi','nagamchenchulakshmi@gmail.com','678909876','Travel','Other State','IDIBPI0956',200,'11-02-2021 09:49 AM','09:44 AM'),(19,'890989098','cse.takeoff@gmail.com','Lakshmi','nagamchenchulakshmi@gmail.com','678909876','Travel','Other State','IDIBPI0956',200,'11-02-2021 09:49 AM','09:45 AM'),(20,'890989098','cse.takeoff@gmail.com','Lakshmi','nagamchenchulakshmi@gmail.com','678909876','Travel','Other State','IDIBPI0956',200,'11-02-2021 09:49 AM','09:45 AM'),(21,'678909876','nagamchenchulakshmi@gmail.com','Lakshmi','nagamchenchulakshmi@gmail.com','890989098','Food&Drinks','Food&Local Transaction','IDIBPI0956',200,'04-20-2022 12:12 PM','12:34 PM');
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-22 20:43:29
