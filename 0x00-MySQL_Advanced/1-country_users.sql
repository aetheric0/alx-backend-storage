-- CREATES A TABLE 'users' with id, email, name, and country (enumberation: US, CO, TN) with constraints
CREATE TABLE IF NOT EXISTS `users` (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, email varchar(255) UNIQUE NOT NULL, name varchar(255), country ENUM('US', 'CO', 'TN') DEFAULT 'US')
