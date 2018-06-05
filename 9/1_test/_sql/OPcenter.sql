-- ----------------------------
-- CREATE DATABASE OPcenter
-- ----------------------------
CREATE DATABASE IF NOT EXISTS OPcenter DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
-- ----------------------------
USE OPcenter;
-- ----------------------------
SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for webmoni_domainname
-- ----------------------------
DROP TABLE IF EXISTS `webmoni_domainname`;
CREATE TABLE `webmoni_domainname` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(60) NOT NULL,
  `project_name_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL,
  `check_id` int(11) NOT NULL,
  `warning` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`) USING BTREE,
  KEY `webmoni_domainname_6fa54945` (`project_name_id`) USING BTREE,
  KEY `webmoni_domainname_dc91ed4b` (`status_id`) USING BTREE,
  CONSTRAINT `webmoni_domainname_ibfk_1` FOREIGN KEY (`project_name_id`) REFERENCES `webmoni_project` (`id`),
  CONSTRAINT `webmoni_domainname_ibfk_2` FOREIGN KEY (`status_id`) REFERENCES `webmoni_event_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=164 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for webmoni_event_log
-- ----------------------------
DROP TABLE IF EXISTS `webmoni_event_log`;
CREATE TABLE `webmoni_event_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` datetime NOT NULL,
  `event_type_id` int(11) NOT NULL,
  `node_id` int(11) NOT NULL,
  `url_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `webmoni_event_log_5e891baf` (`event_type_id`),
  KEY `webmoni_event_log_c693ebc8` (`node_id`),
  KEY `webmoni_event_log_29608e0a` (`url_id`),
  CONSTRAINT `webmoni_event_lo_event_type_id_3390703b_fk_webmoni_event_type_id` FOREIGN KEY (`event_type_id`) REFERENCES `webmoni_event_type` (`id`),
  CONSTRAINT `webmoni_event_log_node_id_ecc027f5_fk_webmoni_node_id` FOREIGN KEY (`node_id`) REFERENCES `webmoni_node` (`id`),
  CONSTRAINT `webmoni_event_log_url_id_64f54de2_fk_webmoni_domainname_id` FOREIGN KEY (`url_id`) REFERENCES `webmoni_domainname` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=199 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for webmoni_event_type
-- ----------------------------
DROP TABLE IF EXISTS `webmoni_event_type`;
CREATE TABLE `webmoni_event_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_type` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `event_type` (`event_type`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for webmoni_monitordata
-- ----------------------------
DROP TABLE IF EXISTS `webmoni_monitordata`;
CREATE TABLE `webmoni_monitordata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `http_code` int(11) DEFAULT NULL,
  `namelookup_time` int(11) DEFAULT NULL,
  `connect_time` int(11) DEFAULT NULL,
  `pretransfer_time` int(11) DEFAULT NULL,
  `starttransfer_time` int(11) DEFAULT NULL,
  `total_time` int(11) DEFAULT NULL,
  `size_download` int(11) DEFAULT NULL,
  `header_size` int(11) DEFAULT NULL,
  `speed_download` int(11) DEFAULT NULL,
  `datetime` datetime NOT NULL,
  `node_id` int(11) NOT NULL,
  `url_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `webmoni_monitordata_c693ebc8` (`node_id`),
  KEY `webmoni_monitordata_29608e0a` (`url_id`),
  KEY `webmoni_monitordata_datetime_6519e757_uniq` (`datetime`),
  CONSTRAINT `webmoni_monitordata_node_id_f3350a82_fk_webmoni_node_id` FOREIGN KEY (`node_id`) REFERENCES `webmoni_node` (`id`),
  CONSTRAINT `webmoni_monitordata_url_id_345f6afc_fk_webmoni_domainname_id` FOREIGN KEY (`url_id`) REFERENCES `webmoni_domainname` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34070 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for webmoni_node
-- ----------------------------
DROP TABLE IF EXISTS `webmoni_node`;
CREATE TABLE `webmoni_node` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `node` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `node` (`node`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for webmoni_project
-- ----------------------------
DROP TABLE IF EXISTS `webmoni_project`;
CREATE TABLE `webmoni_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;