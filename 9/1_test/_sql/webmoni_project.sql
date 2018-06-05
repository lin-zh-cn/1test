/*
Navicat MySQL Data Transfer

Source Server         : 139.199.77.249
Source Server Version : 50505
Source Host           : 139.199.77.249:3306
Source Database       : OPcenter

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2018-05-16 09:07:04
*/

SET FOREIGN_KEY_CHECKS=0;

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
