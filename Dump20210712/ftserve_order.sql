-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: mysql-instance1.ctrffvygguml.us-east-1.rds.amazonaws.com    Database: ftserve
-- ------------------------------------------------------
-- Server version	8.0.20

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `order_ID` int NOT NULL AUTO_INCREMENT,
  `item_ID` varchar(45) NOT NULL,
  `quantity` int NOT NULL,
  `customer_ID` int NOT NULL,
  `status` varchar(45) NOT NULL DEFAULT 'OTKN',
  `order_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_ID`),
  KEY `item_refernce_idx` (`item_ID`),
  KEY `cutomer_refernce_idx` (`customer_ID`),
  CONSTRAINT `cutomer_refernce` FOREIGN KEY (`customer_ID`) REFERENCES `customer` (`customer_ID`),
  CONSTRAINT `item_refernce` FOREIGN KEY (`item_ID`) REFERENCES `item` (`item_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,'MSH PPR FRY',2,1,'SRVD','2021-06-12 15:26:00'),(2,'CRT JUC',1,1,'SRVD','2021-06-12 15:26:00'),(3,'MSH PPR FRY',1,2,'OTKN','2021-06-12 15:30:00'),(4,'GB 65',1,2,'PRPD','2021-06-12 15:30:00'),(5,'MSH PPR FRY',1,4,'OTKN','2021-06-12 16:30:00'),(6,'PAN 65',2,4,'PRNG','2021-06-12 16:20:00'),(7,'PAN 65',1,1,'SRVD','2021-06-27 11:59:31'),(8,'CRT JUC',2,4,'PRNG','2021-06-27 12:32:27'),(9,'MIN LIM JUC',1,4,'PRNG','2021-06-27 12:40:38');
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-12 21:29:15
