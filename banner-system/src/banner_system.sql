-- MySQL dump 10.13  Distrib 8.0.15, for macos10.14 (x86_64)
--
-- Host: localhost    Database: banner_system
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `banner` int(15) NOT NULL,
  `password` varchar(200) NOT NULL,
  `isFaculty` tinyint(4) NOT NULL,
  `address` varchar(45) NOT NULL,
  `phone_number` bigint(30) NOT NULL,
  `city` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `state` varchar(45) NOT NULL,
  `zip_code` int(5) NOT NULL,
  `dob` varchar(45) NOT NULL,
  `balance` decimal(10,2) NOT NULL,
  `GPA` float NOT NULL,
  `credit_hours` float NOT NULL,
  `timestamp` decimal(20,6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `banner_UNIQUE` (`banner`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (9,'Tony','Stark',111111111,'pbkdf2:sha256:50000$ZvMLtD8p$83dbc51b8a532e403ae2ce216e6402a70a5c981810f1321fbe3d1b8279c58e98',1,'1601 East Market Street',5555555555,'Greensboro','stark@avengers.com','NC',27411,'1/22/1968',0.00,0,0,1556129443.717460),(10,'Test','Sample',222222222,'pbkdf2:sha256:50000$ciXG82z9$83362178acb0b93c910de2f66f1cdac0aaf0a3c5af2ab8f6760300672c6987ac',0,'1601 East Market Street',3092512286,'Greensboro','sample@test.com','NC',27401,'2019-03-27',12555.00,3.75,95.5,1556127360.000000),(11,'Langston','Dennis',123456789,'pbkdf2:sha256:50000$ncjAUGZK$024a05be53b9729a25ee07895d0ad2ba63d7b0c42a69d747116e54d314dcc27c',0,'1234 Fake Drive',1111111111,'Raleigh','dennis@ncat.edu','NC',27403,'2019-04-24',10500.00,3.5,27,1556128237.929980),(12,'demo','demo',123456788,'pbkdf2:sha256:50000$cRaOHVpg$24ade3fb86dd090024cde229a7d9a9cd57cd88163279ef3d1217961e78cfa48a',0,'123 Fake Drive',1111111111,'Greensboro','dennis@ncat.edu','NC',27403,'2019-04-24',100000.00,3,24.5,1556129546.607530);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-26 15:13:45
