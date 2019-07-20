/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : world

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 16/07/2019 19:22:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for announcement
-- ----------------------------
DROP TABLE IF EXISTS `announcement`;
CREATE TABLE `announcement`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NULL DEFAULT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `images` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `createTime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of announcement
-- ----------------------------
INSERT INTO `announcement` VALUES (1, NULL, 'test', '123', 'images', NULL);
INSERT INTO `announcement` VALUES (2, NULL, 'test', '123', 'images', NULL);
INSERT INTO `announcement` VALUES (3, NULL, 'test', '123', 'images', NULL);
INSERT INTO `announcement` VALUES (4, NULL, 'title', 'content_t', '', NULL);
INSERT INTO `announcement` VALUES (5, NULL, 'title', 'content_t', '', NULL);
INSERT INTO `announcement` VALUES (6, NULL, 'title', 'content_t', '', NULL);
INSERT INTO `announcement` VALUES (7, NULL, 'title', 'content_t', '', NULL);
INSERT INTO `announcement` VALUES (8, NULL, 'title', 'content_t', 'E:\\python\\world/data/upload/images20190714190102小程序.jpg', NULL);
INSERT INTO `announcement` VALUES (9, NULL, 'title', 'content_t', 'E:\\python\\world/data/upload/images/小程序.jpg_20190714_190201', NULL);
INSERT INTO `announcement` VALUES (10, NULL, 'title', 'content_t', 'E:\\python\\world/data/upload/images/20190714_190311_小程序.jpg', NULL);
INSERT INTO `announcement` VALUES (11, NULL, 'title', 'content_t', 'E:\\python\\world/data/upload/images/20190714_190347-小程序.jpg', NULL);

-- ----------------------------
-- Table structure for area_auth
-- ----------------------------
DROP TABLE IF EXISTS `area_auth`;
CREATE TABLE `area_auth`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id ',
  `fanyi` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `level` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `code2` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `location` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `parent` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `note` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of area_auth
-- ----------------------------
INSERT INTO `area_auth` VALUES (1, NULL, '中国', '1', 'china', 'china_1', '/1', '0', '字段顶级上增');
INSERT INTO `area_auth` VALUES (2, NULL, '安徽', '2', NULL, 'anhui_2', '/1/2', '1', '地域修改,迁移');
INSERT INTO `area_auth` VALUES (3, NULL, '香港', '2', NULL, 'xianggang_3', '/1/3', '1', '只有增加,修改,删除,查找');
INSERT INTO `area_auth` VALUES (4, NULL, '台湾', '2', NULL, 'taiwan_4', '/1/4', '1', '整体挪移与历史权限记录');
INSERT INTO `area_auth` VALUES (5, NULL, '合肥', '3', NULL, NULL, '/1/2/5', '2', '挪移与删除新增');
INSERT INTO `area_auth` VALUES (6, NULL, '宿州', '3', NULL, NULL, '/1/2/6', '2', '挪移与location');
INSERT INTO `area_auth` VALUES (7, NULL, '萧县', '4', NULL, NULL, '/1/2/6/7', '6', '人属于权限还是权限下有人');
INSERT INTO `area_auth` VALUES (8, NULL, '砀山县', '4', NULL, NULL, NULL, '6', NULL);
INSERT INTO `area_auth` VALUES (9, NULL, '黄口', '5', NULL, NULL, '/1/2/6/7/9', '7', '增删改查上增加用户模块,日志模块,管理员模块,占山头模块');
INSERT INTO `area_auth` VALUES (10, NULL, '新庄', '5', NULL, NULL, '/1/2/6/7/10', '7', NULL);
INSERT INTO `area_auth` VALUES (11, NULL, '梁庄', '6', NULL, NULL, '/1/2/7/10/11', '10', '权限匹配 /2/');
INSERT INTO `area_auth` VALUES (12, NULL, 'add', '7', NULL, NULL, '/1/2/7/10/11/12', '11', NULL);
INSERT INTO `area_auth` VALUES (13, NULL, 'update', '7', NULL, NULL, NULL, '11', '接口权限,日志权限');
INSERT INTO `area_auth` VALUES (14, NULL, 'del', '7', NULL, NULL, NULL, '11', NULL);
INSERT INTO `area_auth` VALUES (15, NULL, 'get', '7', NULL, NULL, NULL, '11', '叉树分析');
INSERT INTO `area_auth` VALUES (16, NULL, 'adduser', '8', NULL, NULL, NULL, '12', NULL);
INSERT INTO `area_auth` VALUES (17, NULL, 'addschool', '8', NULL, NULL, '/1/2/7/10/11/12/17', '12', NULL);

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NULL DEFAULT NULL,
  `auth_code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `auth_code2` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
INSERT INTO `auth_group` VALUES (1, 1, '/1', '1');
INSERT INTO `auth_group` VALUES (2, 1, '/1/2/7/10/11/12/17', '17');

-- ----------------------------
-- Table structure for auth_test
-- ----------------------------
DROP TABLE IF EXISTS `auth_test`;
CREATE TABLE `auth_test`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `auth` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `auth2` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `note` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `area` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_test
-- ----------------------------
INSERT INTO `auth_test` VALUES (1, '中国立国', '/1', '1', NULL, '1');
INSERT INTO `auth_test` VALUES (2, '中国阅兵', '/1', '1', NULL, '1');
INSERT INTO `auth_test` VALUES (3, '安徽舞狮', '/1/2', '2', NULL, '2');
INSERT INTO `auth_test` VALUES (4, '梁庄新建学校', '/1/2/7/10/11/12/17', '17', '/1 与 权限17 -> /1/2/7/10/11/12/17', '17');

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NULL DEFAULT NULL,
  `announcement_id` int(11) NULL DEFAULT NULL,
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `createTime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `createTime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `images` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for organization_auth
-- ----------------------------
DROP TABLE IF EXISTS `organization_auth`;
CREATE TABLE `organization_auth`  (
  `id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for people_auth
-- ----------------------------
DROP TABLE IF EXISTS `people_auth`;
CREATE TABLE `people_auth`  (
  `id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for record
-- ----------------------------
DROP TABLE IF EXISTS `record`;
CREATE TABLE `record`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `images` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `video` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `createTime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `birthday` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `sex` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `icon` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `phone` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `active` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'test', '123', NULL, '1', '', 'default.jpg', NULL, '1');
INSERT INTO `user` VALUES (2, 'root', '123', NULL, NULL, NULL, NULL, NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
