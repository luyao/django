-- MySQL dump 10.11
--
-- Host: 10.0.2.21    Database: mysite
-- ------------------------------------------------------
-- Server version	5.0.95

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_message`
--

DROP TABLE IF EXISTS `auth_message`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `auth_message_fbfc09f1` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_message`
--

LOCK TABLES `auth_message` WRITE;
/*!40000 ALTER TABLE `auth_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add message',4,'add_message'),(11,'Can change message',4,'change_message'),(12,'Can delete message',4,'delete_message'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add site',7,'add_site'),(20,'Can change site',7,'change_site'),(21,'Can delete site',7,'delete_site'),(22,'Can add log entry',8,'add_logentry'),(23,'Can change log entry',8,'change_logentry'),(24,'Can delete log entry',8,'delete_logentry'),(25,'Can add product',9,'add_product'),(26,'Can change product',9,'change_product'),(27,'Can delete product',9,'delete_product'),(28,'Can add line item',10,'add_lineitem'),(29,'Can change line item',10,'change_lineitem'),(30,'Can delete line item',10,'delete_lineitem');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL auto_increment,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'luyao','','','yaolu1103@gmail.com','sha1$3bece$efb1b1fbd1550300ba79826daf2a71546a59fa29',1,1,1,'2013-06-29 17:13:06','2013-06-29 17:13:06');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL auto_increment,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) default NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'message','auth','message'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'site','sites','site'),(8,'log entry','admin','logentry'),(9,'product','sspayment','product'),(10,'line item','sspayment','lineitem');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('23975a713d88786b2bbaeeb529525afc','MzkwNzkxN2M4NTZhY2Q4NTQ0YWUyYWUyMmNlMWRiZDRiYTE2OWQ1MzqAAn1xAVUEY2FydGNzc3Bh\neW1lbnQuY2FydApDYXJ0CnECKYFxA31xBChVBWl0ZW1zcQVdcQYoY2RqYW5nby5kYi5tb2RlbHMu\nYmFzZQptb2RlbF91bnBpY2tsZQpxB2NteXNpdGUuc3NwYXltZW50Lm1vZGVscwpMaW5lSXRlbQpx\nCF1jZGphbmdvLmRiLm1vZGVscy5iYXNlCnNpbXBsZV9jbGFzc19mYWN0b3J5CnEJh1JxCn1xCyhV\nCnByb2R1Y3RfaWRxDIoBAVUGX3N0YXRlcQ1jZGphbmdvLmRiLm1vZGVscy5iYXNlCk1vZGVsU3Rh\ndGUKcQ4pgXEPfXEQKFUGYWRkaW5ncRGIVQJkYnESVQdkZWZhdWx0cRN1YlUKdW5pdF9wcmljZXEU\nY2RlY2ltYWwKRGVjaW1hbApxFVUFNTIuOTmFUnEWVQ5fcHJvZHVjdF9jYWNoZXEXaAdjbXlzaXRl\nLnNzcGF5bWVudC5tb2RlbHMKUHJvZHVjdApxGF1oCYdScRl9cRooVQtkZXNjcmlwdGlvbnEbWAAA\nAABVBXRpdGxlcRxYDAAAAG5ldyB0ZXN0IDFzdFUFcHJpY2VxHWgWaA1oDimBcR59cR8oaBGJaBJo\nE3ViVQlpbWFnZV91cmxxIFgAAAAAVQJpZHEhigEBdWJoIU5VCHF1YW50aXR5cSJLBXViaAdoCF1o\nCYdScSN9cSQoaAyKAQJoDWgOKYFxJX1xJihoEYhoElUHZGVmYXVsdHEndWJoFGgVVQYxOTkuOTmF\nUnEoaBdoB2gYXWgJh1JxKX1xKihoG1gAAAAAaBxYDAAAAG5ldyB0ZXN0IDJuZGgdaChoDWgOKYFx\nK31xLChoEYloEmgndWJoIFgAAAAAaCGKAQJ1YmghTmgiSwN1YmVVC3RvdGFsX3ByaWNlcS1oFVUG\nODY0LjkyhVJxLnVicy4=\n','2013-07-14 14:51:00'),('30b70f5306d9c3961330edd22127e9e2','YjM0NjQzYTQxNjg5MWZhOTRlYTUwOWMzNzQ0NjMzY2RlMGM1Yjg3ZjqAAn1xAVUEY2FydHECY3Nz\ncGF5bWVudC5jYXJ0CkNhcnQKcQMpgXEEfXEFKFUFaXRlbXNxBl1VC3RvdGFsX3ByaWNlcQdLAHVi\ncy4=\n','2013-07-13 18:18:52');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL auto_increment,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sspayment_lineitem`
--

DROP TABLE IF EXISTS `sspayment_lineitem`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `sspayment_lineitem` (
  `id` int(11) NOT NULL auto_increment,
  `product_id` int(11) NOT NULL,
  `unit_price` decimal(8,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `sspayment_lineitem_bb420c12` (`product_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `sspayment_lineitem`
--

LOCK TABLES `sspayment_lineitem` WRITE;
/*!40000 ALTER TABLE `sspayment_lineitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `sspayment_lineitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sspayment_product`
--

DROP TABLE IF EXISTS `sspayment_product`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `sspayment_product` (
  `id` int(11) NOT NULL auto_increment,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `image_url` varchar(200) NOT NULL,
  `price` decimal(8,2) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `sspayment_product`
--

LOCK TABLES `sspayment_product` WRITE;
/*!40000 ALTER TABLE `sspayment_product` DISABLE KEYS */;
INSERT INTO `sspayment_product` VALUES (1,'new test 1st','','','52.99'),(2,'new test 2nd','','','199.99');
/*!40000 ALTER TABLE `sspayment_product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-07-01 13:33:51
