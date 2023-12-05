-- This script prepares a MySQL server for the project
-- Create project deving database with the name : shop_dev_db
CREATE DATABASE IF NOT EXISTS shop_dev_db ;
-- Create a new user named : shop_dev with all priveledges on the db shop_dev_db
-- with the password : shop_dev_pwd if it doesn't exist
CREATE USER IF NOT EXISTS 'shop_dev'@'localhost' IDENTIFIED BY 'shop_dev_pwd';
-- Granting all priviledges to the new user
GRANT ALL PRIVILEGES ON shop_dev_db.* TO 'shop_dev'@'localhost';
FLUSH PRIVILEGES;
-- Granting the SELECT priviledge for the user shop_dev in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'shop_dev'@'localhost';
FLUSH PRIVILEGES;