/*
SQLyog Community v13.2.0 (64 bit)
MySQL - 8.0.33 : Database - bug
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bug` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `bug`;

/*Table structure for table `adminsapp_admins` */

DROP TABLE IF EXISTS `adminsapp_admins`;

CREATE TABLE `adminsapp_admins` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `adminsapp_admins` */

insert  into `adminsapp_admins`(`id`,`username`,`password`) values 
(1,'admin','a');

/*Table structure for table `adminsapp_employee` */

DROP TABLE IF EXISTS `adminsapp_employee`;

CREATE TABLE `adminsapp_employee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `empid` int NOT NULL,
  `empname` varchar(100) NOT NULL,
  `job` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(100) NOT NULL,
  `dateofjoin` date NOT NULL,
  `salary` int NOT NULL,
  `gender` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `adminsapp_employee` */

insert  into `adminsapp_employee`(`id`,`empid`,`empname`,`job`,`email`,`password`,`dateofjoin`,`salary`,`gender`,`role`) values 
(1,1,'karthik','devloper','Developer718@gmail.com','dd','2025-03-24',20000,'Male','devloper'),
(2,2,'joshna','tester','Tester718@gmail.com','tt','2025-03-24',20000,'Female','tester'),
(3,3,'Vinodh manager','manager','manager718@gmail.com','mm','2025-03-24',20000,'Male','manager'),
(4,4,'Analyst','analyst','Analyst718@gmail.com','a','2025-03-24',20000,'Male','analyst'),
(6,5,'Kalyan','Manager','kalyan@gmail.com','123','2025-03-04',100000000,'male','manager'),
(7,19,'Bharathi','Developer','bharathi@gmail.com','123','2025-03-18',500000,'female','devloper'),
(8,20,'Vamshi Y','software Tester','vamshi@gmail.com','12','2025-03-11',500000,'Male','tester'),
(9,21,'Ramu','manager','ramu@gmail.com','12','2025-03-04',10000000,'Male','analyst');

/*Table structure for table `adminsapp_news` */

DROP TABLE IF EXISTS `adminsapp_news`;

CREATE TABLE `adminsapp_news` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `adminsapp_news` */

insert  into `adminsapp_news`(`id`,`title`,`description`,`date`) values 
(6,'Test Case','While looking in to Test Scenarios will write Test Cases','2025-03-26 09:03:40.887823');

/*Table structure for table `adminsapp_project` */

DROP TABLE IF EXISTS `adminsapp_project`;

CREATE TABLE `adminsapp_project` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `code` varchar(100) NOT NULL,
  `technology` varchar(100) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `fromdate` date NOT NULL,
  `todate` date NOT NULL,
  `manager` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `adminsapp_project` */

insert  into `adminsapp_project`(`id`,`title`,`code`,`technology`,`domain`,`description`,`fromdate`,`todate`,`manager`) values 
(1,'Skill Shoppy1','Skill Shoppy Code','python','python','Its a Ecommerce Domain Platform','2025-03-26','2025-03-31','manager718@gmail.com'),
(4,'projects','projects1','python','python','Python','2025-03-26','2025-03-31','manager718@gmail.com'),
(6,'Medicaree','2928','Insurance','Healthhhh','Health Insurance','2025-03-26','2025-03-31','kalyan@gmail.com');

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add admins',7,'add_admins'),
(26,'Can change admins',7,'change_admins'),
(27,'Can delete admins',7,'delete_admins'),
(28,'Can view admins',7,'view_admins'),
(29,'Can add employee',8,'add_employee'),
(30,'Can change employee',8,'change_employee'),
(31,'Can delete employee',8,'delete_employee'),
(32,'Can view employee',8,'view_employee'),
(33,'Can add project',9,'add_project'),
(34,'Can change project',9,'change_project'),
(35,'Can delete project',9,'delete_project'),
(36,'Can view project',9,'view_project'),
(37,'Can add news',10,'add_news'),
(38,'Can change news',10,'change_news'),
(39,'Can delete news',10,'delete_news'),
(40,'Can view news',10,'view_news'),
(41,'Can add contact',11,'add_contact'),
(42,'Can change contact',11,'change_contact'),
(43,'Can delete contact',11,'delete_contact'),
(44,'Can view contact',11,'view_contact'),
(45,'Can add task',12,'add_task'),
(46,'Can change task',12,'change_task'),
(47,'Can delete task',12,'delete_task'),
(48,'Can view task',12,'view_task'),
(49,'Can add testcase',13,'add_testcase'),
(50,'Can change testcase',13,'change_testcase'),
(51,'Can delete testcase',13,'delete_testcase'),
(52,'Can view testcase',13,'view_testcase'),
(53,'Can add bug',14,'add_bug'),
(54,'Can change bug',14,'change_bug'),
(55,'Can delete bug',14,'delete_bug'),
(56,'Can view bug',14,'view_bug'),
(57,'Can add requirements',15,'add_requirements'),
(58,'Can change requirements',15,'change_requirements'),
(59,'Can delete requirements',15,'delete_requirements'),
(60,'Can view requirements',15,'view_requirements');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(7,'adminsapp','admins'),
(8,'adminsapp','employee'),
(10,'adminsapp','news'),
(9,'adminsapp','project'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(14,'employeeapp','bug'),
(15,'employeeapp','requirements'),
(13,'employeeapp','testcase'),
(11,'managementapp','contact'),
(12,'managementapp','task'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2025-03-24 09:59:05.630390'),
(2,'auth','0001_initial','2025-03-24 09:59:06.253851'),
(3,'admin','0001_initial','2025-03-24 09:59:06.396339'),
(4,'admin','0002_logentry_remove_auto_add','2025-03-24 09:59:06.407392'),
(5,'admin','0003_logentry_add_action_flag_choices','2025-03-24 09:59:06.416470'),
(6,'adminsapp','0001_initial','2025-03-24 09:59:06.441822'),
(7,'adminsapp','0002_employee','2025-03-24 09:59:06.473313'),
(8,'adminsapp','0003_project','2025-03-24 09:59:06.501139'),
(9,'adminsapp','0004_news','2025-03-24 09:59:06.522499'),
(10,'adminsapp','0005_alter_news_date','2025-03-24 09:59:06.553254'),
(11,'contenttypes','0002_remove_content_type_name','2025-03-24 09:59:06.630740'),
(12,'auth','0002_alter_permission_name_max_length','2025-03-24 09:59:06.688246'),
(13,'auth','0003_alter_user_email_max_length','2025-03-24 09:59:06.715368'),
(14,'auth','0004_alter_user_username_opts','2025-03-24 09:59:06.724687'),
(15,'auth','0005_alter_user_last_login_null','2025-03-24 09:59:06.781704'),
(16,'auth','0006_require_contenttypes_0002','2025-03-24 09:59:06.784706'),
(17,'auth','0007_alter_validators_add_error_messages','2025-03-24 09:59:06.793317'),
(18,'auth','0008_alter_user_username_max_length','2025-03-24 09:59:06.850618'),
(19,'auth','0009_alter_user_last_name_max_length','2025-03-24 09:59:06.912005'),
(20,'auth','0010_alter_group_name_max_length','2025-03-24 09:59:06.934224'),
(21,'auth','0011_update_proxy_permissions','2025-03-24 09:59:06.946036'),
(22,'auth','0012_alter_user_first_name_max_length','2025-03-24 09:59:07.003902'),
(23,'employeeapp','0001_initial','2025-03-24 09:59:07.034183'),
(24,'employeeapp','0002_alter_testcase_date_of_creation','2025-03-24 09:59:07.063975'),
(25,'employeeapp','0003_auto_20211101_1254','2025-03-24 09:59:07.119718'),
(26,'employeeapp','0004_rename_severity_bug_sevearity','2025-03-24 09:59:07.163790'),
(27,'employeeapp','0005_auto_20211101_1624','2025-03-24 09:59:07.194457'),
(28,'employeeapp','0006_alter_bug_date','2025-03-24 09:59:07.223897'),
(29,'employeeapp','0007_status','2025-03-24 09:59:07.244143'),
(30,'employeeapp','0008_remove_status_bug_id','2025-03-24 09:59:07.257927'),
(31,'employeeapp','0009_delete_status','2025-03-24 09:59:07.266940'),
(32,'employeeapp','0010_requirements','2025-03-24 09:59:07.332745'),
(33,'employeeapp','0011_requirements_email','2025-03-24 09:59:07.363567'),
(34,'employeeapp','0012_testcase_requirements','2025-03-24 09:59:07.425372'),
(35,'employeeapp','0013_alter_testcase_requirements','2025-03-24 09:59:07.500981'),
(36,'employeeapp','0014_auto_20240528_1014','2025-03-24 09:59:07.547189'),
(37,'employeeapp','0015_testcase_comments','2025-03-24 09:59:07.571373'),
(38,'employeeapp','0016_auto_20240528_1142','2025-03-24 09:59:07.687490'),
(39,'employeeapp','0017_bug_developer_email','2025-03-24 09:59:07.708245'),
(40,'managementapp','0001_initial','2025-03-24 09:59:07.729932'),
(41,'managementapp','0002_task','2025-03-24 09:59:07.753830'),
(42,'sessions','0001_initial','2025-03-24 09:59:07.791699'),
(43,'adminsapp','0006_alter_admins_password','2025-03-25 13:30:38.643492'),
(44,'employeeapp','0018_alter_bug_description','2025-03-26 06:28:05.525049');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('8g919jcdxpw8epzyf5f4w096txfry30n','e30:1txh3r:tnEyajvEeJWuZcPDiO_Ge1HpHY7NUmFDpqm-Wdl-zMg','2025-04-10 06:49:55.092594'),
('alqq09vjqct9mo4oa92psyd6wz11l304','eyJlbWFpbCI6IlRlc3RlcjcxOEBnbWFpbC5jb20iLCJyb2xlIjoidGVzdGVyIn0:1twyiz:VTrQg9D2Q9PDLhg9HHEdAiZiuBUda4IlE4G-H3LdP0c','2025-04-08 07:29:25.241193'),
('zo6h64n6y75kfewputbaqp3tk183p812','e30:1twhHy:2TNumFWiFtMehYWvUv_eqZudWT3hsp1hPsYVWfKrC-k','2025-04-07 12:52:22.979645');

/*Table structure for table `employeeapp_bug` */

DROP TABLE IF EXISTS `employeeapp_bug`;

CREATE TABLE `employeeapp_bug` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `testcase_id` int NOT NULL,
  `description` longtext NOT NULL,
  `test_path` varchar(300) NOT NULL,
  `screenshot` varchar(100) NOT NULL,
  `sevearity` varchar(300) NOT NULL,
  `priority` varchar(300) NOT NULL,
  `status` varchar(300) NOT NULL,
  `date` date NOT NULL,
  `tested_by_email` varchar(254) NOT NULL,
  `browser` varchar(350) NOT NULL,
  `environment` varchar(350) NOT NULL,
  `errordetails` varchar(350) NOT NULL,
  `os` varchar(350) NOT NULL,
  `reproductionsteps` varchar(350) NOT NULL,
  `title` varchar(100) NOT NULL,
  `developer_email` varchar(350) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `employeeapp_bug` */

insert  into `employeeapp_bug`(`id`,`testcase_id`,`description`,`test_path`,`screenshot`,`sevearity`,`priority`,`status`,`date`,`tested_by_email`,`browser`,`environment`,`errordetails`,`os`,`reproductionsteps`,`title`,`developer_email`) values 
(1,2,'Bug About To Login In the instagram1 esBug raised in Date Picker it should accept the dynamic esBug raised in Date Picker it should accept the dynamic valueesBug raised in Date Picker it should accept the dynamic valueesBug raised in Date Picker it should accept the dynamic valueesBug raised in Date Picker it should accept the dynamic valueesBug raised in Date Picker it should accept the dynamic valueesBug raised in Date Picker it should accept the dynamic valueesBug raised in Date Picker it should accept the dynamic valueesBug raised in Date Picker it should accept the dynamic valueesBug raised in Date Picker it should accept the dynamic valueesBug raised in Date Picker it should accept the dynamic valueesBug raised in Date Picker it should accept the dynamic value value','http://127.0.0.1:8000/add_bug/','images/b3.jpeg','high','high','reopen','2025-03-27','Tester718@gmail.com','Chrome','Selenium','Login Validationsss','MS-Windows','Navigate to the Login page Enter a valid email in Enter the correct password click Observe the behavior','Skill Shopy','Developer718@gmail.com'),
(2,3,'Bug','http://127.0.0.1:8000/add_bug/','images/b1_lBZ3T5w.webp','medium','medium','fixed','2025-03-27','Developer718@gmail.com','Firefox','Selenium','Login Validations','MS-Windows','Navigate to the Login page Enter a valid email in Enter the correct password click Observe the behavior','Bug','Developer718@gmail.com');

/*Table structure for table `employeeapp_requirements` */

DROP TABLE IF EXISTS `employeeapp_requirements`;

CREATE TABLE `employeeapp_requirements` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` varchar(350) NOT NULL,
  `priority` varchar(300) NOT NULL,
  `ndatetime` datetime(6) NOT NULL,
  `projects_id` bigint NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `employeeapp_requirem_projects_id_b41043d8_fk_adminsapp` (`projects_id`),
  CONSTRAINT `employeeapp_requirem_projects_id_b41043d8_fk_adminsapp` FOREIGN KEY (`projects_id`) REFERENCES `adminsapp_project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `employeeapp_requirements` */

insert  into `employeeapp_requirements`(`id`,`title`,`description`,`priority`,`ndatetime`,`projects_id`,`email`) values 
(1,'Skill Shoppy','I need I the requirement s like bugs and testcases','medium','2025-03-24 10:53:40.852961',1,'Analyst718@gmail.com'),
(2,'Project','Project','high','2025-03-24 12:28:50.656427',4,'Analyst718@gmail.com'),
(3,'Medicare','Medicare is a health insurance project where user able to book a call with doctor','high','2025-03-25 10:43:02.834740',6,'ramu@gmail.com'),
(4,'Health','Call with doctor request from LOA','medium','2025-03-25 10:43:49.397854',6,'ramu@gmail.com');

/*Table structure for table `employeeapp_testcase` */

DROP TABLE IF EXISTS `employeeapp_testcase`;

CREATE TABLE `employeeapp_testcase` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `project_name` varchar(350) NOT NULL,
  `module_name` varchar(350) NOT NULL,
  `senario` varchar(350) NOT NULL,
  `description` varchar(350) NOT NULL,
  `input_data` varchar(350) NOT NULL,
  `type_of_exception` varchar(350) NOT NULL,
  `pre_condition` varchar(350) NOT NULL,
  `expected_actual_result` varchar(350) NOT NULL,
  `status` varchar(300) NOT NULL,
  `date_of_creation` date NOT NULL,
  `tester_email` varchar(254) NOT NULL,
  `requirements` varchar(350) NOT NULL,
  `priority` varchar(300) NOT NULL,
  `teststeps` varchar(100) NOT NULL,
  `comments` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `employeeapp_testcase` */

insert  into `employeeapp_testcase`(`id`,`project_name`,`module_name`,`senario`,`description`,`input_data`,`type_of_exception`,`pre_condition`,`expected_actual_result`,`status`,`date_of_creation`,`tester_email`,`requirements`,`priority`,`teststeps`,`comments`) values 
(1,'Skill Shoppy1','Loginn','Login Of Instagrams','Verify The Login Page of Instagram','username password','Functional','Validate Url','Navigate To home Page','Fail','2025-03-27','Tester718@gmail.com','Skill Shoppy','low','Enter Validate Username And Validate Password Click On The Button','About The TestCase11'),
(2,'Skill Shoppy','Login','Skill Shoppy','Validation','username password','Functional','Validate Url','Navigate To home Page','Fail','2025-03-27','Tester718@gmail.com','Skill Shoppy','high','Enter Validate Username And Validate Password Click On The Button','About The Comments'),
(3,'projects','Login','Test Case','login','username password','Functional','Validate Url','Navigate To home Paged','Fail','2025-03-27','Tester718@gmail.com','Project','high','Enter Validate Username And Validate Password Click On The Button','Comments');

/*Table structure for table `managementapp_contact` */

DROP TABLE IF EXISTS `managementapp_contact`;

CREATE TABLE `managementapp_contact` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `managementapp_contact` */

insert  into `managementapp_contact`(`id`,`message`,`name`,`email`,`subject`) values 
(1,'About Bug And Test Case Management System','Karthik Dheeravath','karthikdheeravath718@gmail.com','Bug And Test Case Management System'),
(2,'About Bug And Test Case Management System','Karthik Dheeravath','karthikdheeravath718@gmail.com','Bug And Test Case Management System'),
(3,'About Bug And Test Case Management System','Karthik Dheeravath','karthikdheeravath718@gmail.com','Bug And Test Case Management System'),
(4,'message','Karthik Dheeravath','karthikdheeravath718@gmail.com','python');

/*Table structure for table `managementapp_task` */

DROP TABLE IF EXISTS `managementapp_task`;

CREATE TABLE `managementapp_task` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `manager_email` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `employee_email` varchar(254) NOT NULL,
  `project` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `enddate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `managementapp_task` */

insert  into `managementapp_task`(`id`,`manager_email`,`status`,`employee_email`,`project`,`description`,`enddate`) values 
(1,'manager718@gmail.com','improgress','Developer718@gmail.com','projects','Go Through The Login Validations Of The Instagram','2025-03-31'),
(2,'manager718@gmail.com','completed','Tester718@gmail.com','Skill Shoppy1','Test The Testcases Of the Login Instgram','2025-03-31'),
(3,'manager718@gmail.com','new','Analyst718@gmail.com','Skill Shoppy1','Check The analyst','2025-03-31'),
(4,'manager718@gmail.com','completed','vamshi@gmail.com','Medicaree','Do Testing for Medicare Application1','2025-03-25'),
(5,'manager718@gmail.com','improgress','bharathi@gmail.com','Skill Shoppy1','Do coding for Medicare application','2025-03-25');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
