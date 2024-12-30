CREATE DATABASE database_carbon;
SHOW tables;
USE database_carbon;

CREATE TABLE region (
    RegionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ClimateZone VARCHAR(50),
    DesertificationRisk VARCHAR(20) 
);

select *from region r;

CREATE TABLE weather (
    WeatherID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    RegionID INT NOT NULL,
    Date DATE NOT NULL,
    Temperature FLOAT,
    Rainfall FLOAT,
    FOREIGN KEY (RegionID) REFERENCES region(RegionID) 
);

select * from weather w ;


CREATE TABLE crop (
    CropID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    CarbonFootprint FLOAT,
    WaterRequirement FLOAT NOT NULL,
    ProfitabilityIndex FLOAT CHECK (ProfitabilityIndex BETWEEN 0 AND 1),
    RotationCompatibility INT
);

select * from crop;

CREATE TABLE market_value (
    MarketValueID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    CropID INT NOT NULL,
    Date DATE NOT NULL,
    PricePerTon FLOAT NOT NULL,
    DemandIndex FLOAT CHECK (DemandIndex BETWEEN 0 AND 1),
    FOREIGN KEY (CropID) REFERENCES crop(CropID) ON DELETE CASCADE
);

select * from market_value;

CREATE TABLE crop_yield (
    YieldID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    CropID INT NOT NULL,
    Year YEAR NOT NULL,
    YieldAmount FLOAT,
    FOREIGN KEY (CropID) REFERENCES crop(CropID) ON DELETE CASCADE
);

select * from crop_yield;

CREATE TABLE soil_aptitude (
	AptitudeID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(100) NOT NULL
);

select * from soil_aptitude;

CREATE TABLE soil_subclass (
	SoilSubClassID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(100) NOT NULL,
	Description VARCHAR(200) NOT NULL
);

select * from soil_subclass;

CREATE TABLE soil_class (
	SoilClassID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(10) NOT NULL,
	Limitations VARCHAR(30) NOT NULL,
	ErosionRisk VARCHAR(30) NOT NULL,
	SuitableUse VARCHAR(200) NOT NULL
);

select * from soil_class;

CREATE TABLE soil_unit (
	SoilUnitID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(10) NOT NULL,
	Description VARCHAR(200) NOT NULL,
	Texture VARCHAR(10),
	Salinity VARCHAR(10),
	Colour VARCHAR(40),
	Humic INT,
	Mollic INT,
	Limstone INT,
	Standard INT,
	Cambisol INT,
	AddCharacteristics VARCHAR(200)
);

select * from soil_unit;

-- do this last -- 
CREATE TABLE soil_type (
    SoilTypeID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    RegionID INT NOT NULL,
    SoilUnitID INT NOT NULL,
    SoilClassID INT,
    SoilSubClassID INT,
    AptitudeID INT, 
    FOREIGN KEY (RegionID) REFERENCES region(RegionID) ON DELETE CASCADE,
    FOREIGN KEY (SoilUnitID) REFERENCES soil_unit(SoilUnitID) ON DELETE CASCADE,
    FOREIGN KEY (SoilClassID) REFERENCES soil_class(SoilClassID),
    FOREIGN KEY (SoilSubClassID) REFERENCES soil_subclass(SoilSubClassID),
    FOREIGN KEY (AptitudeID) REFERENCES soil_aptitude(AptitudeID)
);

select * from soil_type s ;
show tables;

CREATE TABLE crop_soil_compatibility (
    CompatibilityID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    CropID INT NOT NULL,
    SoilTypeID INT NOT NULL,
    FOREIGN KEY (CropID) REFERENCES crop(CropID) ON DELETE CASCADE,
    FOREIGN KEY (SoilTypeID) REFERENCES soil_type(SoilTypeID) ON DELETE CASCADE
);

select * from crop_soil_compatibility;

SHOW TABLES;

describe region ;