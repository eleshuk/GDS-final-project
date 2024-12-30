CREATE USER 'luis'@'%' IDENTIFIED BY 'password';
SHOW GRANTS for luis;
GRANT ALL PRIVILEGES ON `database_carbon`.* TO 'luis'@'%';
FLUSH PRIVILEGES;

SELECT CURRENT_USER;

CREATE USER 'liz'@'%' IDENTIFIED BY 'password';
SHOW GRANTS for liz;
GRANT ALL PRIVILEGES ON `database_carbon`.* TO 'liz'@'%';
FLUSH PRIVILEGES;
