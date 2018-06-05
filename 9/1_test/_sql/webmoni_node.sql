/*
Navicat MySQL Data Transfer

Source Server         : 139.199.77.249
Source Server Version : 50505
Source Host           : 139.199.77.249:3306
Source Database       : OPcenter

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2018-05-16 09:07:51
*/

SET FOREIGN_KEY_CHECKS=0;

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
