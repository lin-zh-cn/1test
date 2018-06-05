/*
Navicat MySQL Data Transfer

Source Server         : 139.199.77.249
Source Server Version : 50505
Source Host           : 139.199.77.249:3306
Source Database       : OPcenter

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2018-05-16 09:06:35
*/

SET FOREIGN_KEY_CHECKS=0;

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
