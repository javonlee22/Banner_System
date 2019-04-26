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
  `password` varchar(20) NOT NULL,
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `banner_UNIQUE` (`banner`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Javon','Lee',950305907,'javon1996',0,'610 S Chapman St',3092512286,'Greensboro','jmlee123@aggies.ncat.edu','NC',27401,'01/23/1996',23343.94,4,120),(2,'Peter','Griffin',555555555,'qwerty123',1,'1601 East Market Street',5555555555,'Greensboro','grifin@ncat.edu','NC',27411,'01/12/1967',0.00,0,0),(3,'Langston','Dennis',123456789,'hello',0,'123 Fake Drive',123456789,'Greensboro','dennis@ncat.edu','NC',27403,'2019-02-04',30000.00,3,94),(5,'TEST','TESTING',222222222,'test',0,'THIS IS A TEST',5555555555,'Greensboro','test@test.com','NC',27403,'2018-11-12',15000.00,2.5,108);
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

-- Dump completed on 2019-03-02 17:28:41
