/*
Navicat MySQL Data Transfer

Source Server         : 139.199.77.249
Source Server Version : 50505
Source Host           : 139.199.77.249:3306
Source Database       : OPcenter

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2018-05-16 09:05:49
*/

SET FOREIGN_KEY_CHECKS=0;

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
