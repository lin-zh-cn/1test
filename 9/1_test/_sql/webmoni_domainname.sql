/*
Navicat MySQL Data Transfer

Source Server         : 139.199.77.249
Source Server Version : 50505
Source Host           : 139.199.77.249:3306
Source Database       : OPcenter

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2018-05-16 09:05:39
*/

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
