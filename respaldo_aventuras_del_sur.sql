-- MySQL dump 10.13  Distrib 8.4.11, for Win64 (x86_64)
--
-- Host: localhost    Database: inventario_aventura_db
-- ------------------------------------------------------
-- Server version	8.4.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Perfil de Usuario',7,'add_perfil'),(26,'Can change Perfil de Usuario',7,'change_perfil'),(27,'Can delete Perfil de Usuario',7,'delete_perfil'),(28,'Can view Perfil de Usuario',7,'view_perfil'),(29,'Can add Categoría',8,'add_categoria'),(30,'Can change Categoría',8,'change_categoria'),(31,'Can delete Categoría',8,'delete_categoria'),(32,'Can view Categoría',8,'view_categoria'),(33,'Can add Experiencia',9,'add_experiencia'),(34,'Can change Experiencia',9,'change_experiencia'),(35,'Can delete Experiencia',9,'delete_experiencia'),(36,'Can view Experiencia',9,'view_experiencia'),(37,'Can add Inscripción / Reserva',10,'add_inscripcion'),(38,'Can change Inscripción / Reserva',10,'change_inscripcion'),(39,'Can delete Inscripción / Reserva',10,'delete_inscripcion'),(40,'Can view Inscripción / Reserva',10,'view_inscripcion');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$HfPO5OrhzULCeUxMkhC6E3$H4srMV3oKyERTEhhreKkc6bMNpmsaWZQY9hMrA7LhEI=',NULL,1,'admin','Administrador','Ecoparque','admin@aventurasdelsur.cl',1,1,'2026-11-14 17:03:52.456653'),(2,'pbkdf2_sha256$870000$Pahe4PDTl8gidvBqvo3oXI$VG0rzwoR26nTQvijTKjM3suMODM/VY43nBTVNrWW00Q=',NULL,0,'guia_carlos','Carlos','Muñoz','carlos.guia@aventurasdelsur.cl',0,1,'2026-11-14 17:03:53.571025'),(3,'pbkdf2_sha256$870000$gbJWawDKVyb74k3N75Rd8R$jaxsVD5aH/5lBY2zJrfZjg/B615Xj0brPsRfJrSITdw=',NULL,0,'guia_camila','Camila','Rojas','camila.guia@aventurasdelsur.cl',0,1,'2026-11-14 17:03:54.616018'),(4,'pbkdf2_sha256$870000$02fsJSTRuVilHPHUasXErS$tsMEV3tSCYwrmF41Y6O8123tfxOY42WNoMwbEaK+5AY=',NULL,0,'turista_sofia','Sofía','Valdés','sofia.valdes@correo.cl',0,1,'2026-11-14 17:03:55.728553'),(5,'pbkdf2_sha256$870000$ne4JSw7nfLOXtL1rNqyemF$6mtaFSarKwGvAili5S5ILE92/rrwDm3QRJVKekOUdco=',NULL,0,'turista_diego','Diego','Morales','diego.morales@correo.cl',0,1,'2026-11-14 17:03:57.004549');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cuentas_perfil`
--

DROP TABLE IF EXISTS `cuentas_perfil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cuentas_perfil` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rol` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `telefono` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `especialidad` varchar(120) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `cuentas_perfil_user_id_38159a56_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cuentas_perfil`
--

LOCK TABLES `cuentas_perfil` WRITE;
/*!40000 ALTER TABLE `cuentas_perfil` DISABLE KEYS */;
INSERT INTO `cuentas_perfil` VALUES (1,'ADMINISTRADOR','+56 9 8000 1000','',1),(2,'GUIA','+56 9 7111 2222','Trekking y Alta Montaña',2),(3,'GUIA','+56 9 7333 4444','Kayak y Canopy Ecoturístico',3),(4,'TURISTA','+56 9 6555 1111','',4),(5,'TURISTA','+56 9 6777 8888','',5);
/*!40000 ALTER TABLE `cuentas_perfil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'cuentas','perfil'),(8,'experiencias','categoria'),(9,'experiencias','experiencia'),(10,'experiencias','inscripcion'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-11-14 17:03:41.077248'),(2,'auth','0001_initial','2026-11-14 17:03:41.911421'),(3,'admin','0001_initial','2026-11-14 17:03:42.125884'),(4,'admin','0002_logentry_remove_auto_add','2026-11-14 17:03:42.139862'),(5,'admin','0003_logentry_add_action_flag_choices','2026-11-14 17:03:42.154861'),(6,'contenttypes','0002_remove_content_type_name','2026-11-14 17:03:42.329035'),(7,'auth','0002_alter_permission_name_max_length','2026-11-14 17:03:42.420444'),(8,'auth','0003_alter_user_email_max_length','2026-11-14 17:03:42.453082'),(9,'auth','0004_alter_user_username_opts','2026-11-14 17:03:42.464098'),(10,'auth','0005_alter_user_last_login_null','2026-11-14 17:03:42.553533'),(11,'auth','0006_require_contenttypes_0002','2026-11-14 17:03:42.556545'),(12,'auth','0007_alter_validators_add_error_messages','2026-11-14 17:03:42.567531'),(13,'auth','0008_alter_user_username_max_length','2026-11-14 17:03:42.652135'),(14,'auth','0009_alter_user_last_name_max_length','2026-11-14 17:03:42.735373'),(15,'auth','0010_alter_group_name_max_length','2026-11-14 17:03:42.762154'),(16,'auth','0011_update_proxy_permissions','2026-11-14 17:03:42.776151'),(17,'auth','0012_alter_user_first_name_max_length','2026-11-14 17:03:42.874577'),(18,'cuentas','0001_initial','2026-11-14 17:03:42.994119'),(19,'experiencias','0001_initial','2026-11-14 17:03:43.440196'),(20,'sessions','0001_initial','2026-11-14 17:03:43.496086'),(21,'cuentas','0002_alter_perfil_options_alter_perfil_especialidad_and_more','2026-11-14 20:06:53.617660'),(22,'experiencias','0002_alter_categoria_options_alter_experiencia_options_and_more','2026-11-14 20:06:53.706569');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiencias_categoria`
--

DROP TABLE IF EXISTS `experiencias_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiencias_categoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiencias_categoria`
--

LOCK TABLES `experiencias_categoria` WRITE;
/*!40000 ALTER TABLE `experiencias_categoria` DISABLE KEYS */;
INSERT INTO `experiencias_categoria` VALUES (1,'Trekking','Rutas guiadas por senderos cordilleranos, bosques nativos y miradores panorámicos.',1),(2,'Canopy','Circuitos de tirolesas entre copas de árboles centenarios con equipamiento certificado.',1),(3,'Kayak','Travesías en lagunas cristalinas y ríos de aguas tranquilas del sur.',1),(4,'Arriendo de Equipos','Alquiler de equipamiento técnico de montaña, bicicletas MTB y camping.',1);
/*!40000 ALTER TABLE `experiencias_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiencias_experiencia`
--

DROP TABLE IF EXISTS `experiencias_experiencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiencias_experiencia` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `titulo` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `precio` decimal(10,0) NOT NULL,
  `cupo_maximo` int unsigned NOT NULL,
  `fecha_hora` datetime(6) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `categoria_id` bigint NOT NULL,
  `creador_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `experiencias_experie_categoria_id_b03f452f_fk_experienc` (`categoria_id`),
  KEY `experiencias_experiencia_creador_id_70b19025_fk_auth_user_id` (`creador_id`),
  CONSTRAINT `experiencias_experie_categoria_id_b03f452f_fk_experienc` FOREIGN KEY (`categoria_id`) REFERENCES `experiencias_categoria` (`id`),
  CONSTRAINT `experiencias_experiencia_creador_id_70b19025_fk_auth_user_id` FOREIGN KEY (`creador_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `experiencias_experiencia_chk_1` CHECK ((`cupo_maximo` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiencias_experiencia`
--

LOCK TABLES `experiencias_experiencia` WRITE;
/*!40000 ALTER TABLE `experiencias_experiencia` DISABLE KEYS */;
INSERT INTO `experiencias_experiencia` VALUES (1,'Sendero Mirador Los Cóndores','Caminata de dificultad media con vista panorámica al valle y avistamiento de aves.',18000,12,'2026-11-18 02:03:55.676722',1,1,2),(2,'Travesía Bosque Milenario','Recorrido interpretativo entre coihues y araucarias centenarias.',15000,15,'2026-11-20 03:03:55.676722',1,1,2),(3,'Ascenso Cerro El Roble','Expedición de jornada completa hasta la cumbre norte de la reserva.',28000,8,'2026-11-22 01:03:55.676722',1,1,2),(4,'Pack Completo Trekking Nocturno','Arriendo de linternas frontales, bastones y equipo térmico para ruta estelar.',12000,20,'2026-11-24 13:03:55.676722',1,4,2),(5,'Circuito Canopy Vuelo del Águila','7 plataformas y 1.200 metros de cable sobre el dosel del bosque nativo.',25000,10,'2026-11-17 04:03:55.676722',1,2,3),(6,'Kayak Laguna Esmeralda al Amanecer','Navegación tranquila por aguas turquesas rodeadas de flora nativa.',22000,10,'2026-11-19 01:03:55.676722',1,3,3),(7,'Expedición Río Cristalino en Kayak','Descenso guiado de nivel básico-intermedio con instrucción previa.',30000,8,'2026-11-21 07:03:55.676722',1,3,3),(8,'Arriendo Bicicleta MTB + Casco Pro','Arriendo por medio día para recorrer los circuitos señalizados del ecoparque.',14000,15,'2026-11-23 03:03:55.676722',1,4,3);
/*!40000 ALTER TABLE `experiencias_experiencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiencias_inscripcion`
--

DROP TABLE IF EXISTS `experiencias_inscripcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiencias_inscripcion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_inscripcion` datetime(6) NOT NULL,
  `estado_pago` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `valoracion` smallint unsigned DEFAULT NULL,
  `comentario` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `experiencia_id` bigint NOT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `experiencias_inscripcion_usuario_id_experiencia_id_996e38c7_uniq` (`usuario_id`,`experiencia_id`),
  KEY `experiencias_inscrip_experiencia_id_2fbecc6b_fk_experienc` (`experiencia_id`),
  CONSTRAINT `experiencias_inscrip_experiencia_id_2fbecc6b_fk_experienc` FOREIGN KEY (`experiencia_id`) REFERENCES `experiencias_experiencia` (`id`),
  CONSTRAINT `experiencias_inscripcion_usuario_id_9d6f5da2_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `experiencias_inscripcion_chk_1` CHECK ((`valoracion` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiencias_inscripcion`
--

LOCK TABLES `experiencias_inscripcion` WRITE;
/*!40000 ALTER TABLE `experiencias_inscripcion` DISABLE KEYS */;
INSERT INTO `experiencias_inscripcion` VALUES (1,'2026-11-14 17:03:58.124333','Confirmado',5,'¡Increíble vista y excelente guía!',1,4),(2,'2026-11-14 17:03:58.130352','Confirmado',5,'El canopy es adrenalina pura y muy seguro.',5,4),(3,'2026-11-14 17:03:58.138350','Pendiente',NULL,'',6,4),(4,'2026-11-14 17:03:58.144602','Confirmado',4,'Muy buen recorrido por el bosque nativo.',2,5),(5,'2026-11-14 17:03:58.181230','Pendiente',NULL,'',7,5),(6,'2026-11-14 17:03:58.188248','Confirmado',NULL,'',8,5);
/*!40000 ALTER TABLE `experiencias_inscripcion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-14 17:43:36
