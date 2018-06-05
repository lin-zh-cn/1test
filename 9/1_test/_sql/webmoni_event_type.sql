/*
Navicat MySQL Data Transfer

Source Server         : 139.199.77.249
Source Server Version : 50505
Source Host           : 139.199.77.249:3306
Source Database       : OPcenter

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2018-05-16 09:05:57
*/

SET FOREIGN_KEY_CHECKS=0;

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
-- Records of webmoni_event_type
-- ----------------------------
INSERT INTO `webmoni_event_type` VALUES ('3', 'Connection timed out');
INSERT INTO `webmoni_event_type` VALUES ('5', 'Could not resolve');
INSERT INTO `webmoni_event_type` VALUES ('8', 'Empty reply from server');
INSERT INTO `webmoni_event_type` VALUES ('7', 'Failed connect');
INSERT INTO `webmoni_event_type` VALUES ('4', 'Failed to connect');
INSERT INTO `webmoni_event_type` VALUES ('1', 'No Check');
INSERT INTO `webmoni_event_type` VALUES ('0', 'OK');
INSERT INTO `webmoni_event_type` VALUES ('6', 'Operation timed out');
INSERT INTO `webmoni_event_type` VALUES ('2', 'Resolving timed out');
INSERT INTO `webmoni_event_type` VALUES ('99', 'Unknown error');
