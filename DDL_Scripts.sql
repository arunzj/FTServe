create database ftserve;
use ftserve;

#user table
create table ftserve.users(
user_name varchar(50) primary key,
password varchar(50),
type varchar(20));
#items table
CREATE TABLE `items` (
  `item_ID` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `price` decimal(4,2) NOT NULL,
  `category` varchar(45) NOT NULL,
  `staus` varchar(45) NOT NULL DEFAULT 'NA',
  `image_url` varchar(120) NOT NULL,
  `description` tinytext NOT NULL,
  PRIMARY KEY (`item_ID`));
#table table
CREATE TABLE `ftserve`.`tablestable_ID` (
  `table_ID` INT NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`table_ID`));
#customer table
CREATE TABLE `ftserve`.`cutomers` (
  `customer_ID` INT NOT NULL AUTO_INCREMENT,
  `table_ID` INT NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`customer_ID`) );
#bill table
CREATE TABLE `ftserve`.`bills` (
  `bill_ID` INT NOT NULL AUTO_INCREMENT,
  `customer_ID` INT NOT NULL,
  `amount` DECIMAL(4,2) NOT NULL DEFAULT 0.0,
  `status` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`bill_ID`));
#orders table 
CREATE TABLE `orders` (
  `order_ID` int NOT NULL AUTO_INCREMENT,
  `item_ID` int NOT NULL,
  `quantity` int NOT NULL,
  `customer_ID` int NOT NULL,
  `status` varchar(45) NOT NULL DEFAULT 'NA',
  `order_time` timestamp NOT NULL,
  PRIMARY KEY (`order_ID`)
);


