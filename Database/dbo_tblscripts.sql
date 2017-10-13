CREATE DATABASE  IF NOT EXISTS `dbo` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `dbo`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: dbo
-- ------------------------------------------------------
-- Server version	5.7.19-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tblscripts`
--

DROP TABLE IF EXISTS `tblscripts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tblscripts` (
  `ScriptID` int(11) NOT NULL AUTO_INCREMENT,
  `ScriptName` varchar(45) NOT NULL,
  `ScriptDescription` varchar(45) DEFAULT NULL,
  `UserFileUploadCount` int(11) NOT NULL DEFAULT '0',
  `UserInputCount` int(11) NOT NULL DEFAULT '0',
  `File1Name` varchar(45) DEFAULT NULL,
  `File2Name` varchar(45) DEFAULT NULL,
  `File1Desc` varchar(45) DEFAULT NULL,
  `File2Desc` varchar(45) DEFAULT NULL,
  `File3Name` varchar(45) DEFAULT NULL,
  `File3Desc` varchar(45) DEFAULT NULL,
  `Input1Name` varchar(45) DEFAULT NULL,
  `Input1Desc` varchar(45) DEFAULT NULL,
  `Input2Name` varchar(45) DEFAULT NULL,
  `Input2Desc` varchar(45) DEFAULT NULL,
  `Input3Name` varchar(45) DEFAULT NULL,
  `Input3Desc` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ScriptID`),
  UNIQUE KEY `ScriptID_UNIQUE` (`ScriptID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblscripts`
--

LOCK TABLES `tblscripts` WRITE;
/*!40000 ALTER TABLE `tblscripts` DISABLE KEYS */;
INSERT INTO `tblscripts` VALUES (1,'DemoScript1','Sleep 30s',0,0,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'DemoScript2','Add matrix by 1',1,0,'Matrix',NULL,'The Matix you want add 1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(3,'DemoScript3','Add matrix by user defined value',1,1,'Matrix',NULL,'The Matix you want modified',NULL,NULL,NULL,'Value','the change of each cell',NULL,NULL,NULL,NULL),(4,'R notebook on DESeq2','A modified version of R notebook',1,0,'GSVFile',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `tblscripts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-13 16:04:01
