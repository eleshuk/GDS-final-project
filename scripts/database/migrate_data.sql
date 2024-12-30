USE database_carbon;

LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Documents/ISA_Data_Science/Semester_1/final_assignments/soil_class.csv'
INTO TABLE soil_class
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

SELECT * FROM soil_class;

LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Documents/ISA_Data_Science/Semester_1/final_assignments/soil_subclass.csv'
INTO TABLE soil_subclass
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

SELECT * FROM soil_subclass;