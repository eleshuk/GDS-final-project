CREATE DATABASE database_carbon;
SHOW tables;
USE database_carbon;

CREATE TABLE region (
    RegionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Freguesia VARCHAR(100) NOT NULL,
    ClimateZone VARCHAR(50),
    DesertificationRisk VARCHAR(20),
    MunicipalityID INT
);

select *from region r;

CREATE TABLE municipality (
	MunicipalityID INT NOT NULL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL
);

SELECT * FROM municipality;

CREATE TABLE weather (
    WeatherID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    MunicipalityID INT NOT NULL,
    Date DATE NOT NULL,
    TemperatureMax FLOAT,
    TemperatureMin FLOAT,
    Precipitation FLOAT,
    FOREIGN KEY (MunicipalityID) REFERENCES municipality(MunicipalityID) 
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
    Year YEAR NOT NULL,
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
	Level VARCHAR(100) NOT NULL,
	Nomenclature VARCHAR(100) NOT NULL
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

ALTER TABLE soil_unit
RENAME COLUMN Mollic to Molic;

ALTER TABLE soil_unit
RENAME COLUMN Limstone to Calcareous;

ALTER TABLE soil_unit
RENAME COLUMN Cambisol to Cambic;

ALTER TABLE soil_unit
RENAME COLUMN Standard to Normal;

select * from soil_unit;

-- do this last -- 
CREATE TABLE soil_type (
    SoilTypeID INT NOT NULL PRIMARY KEY,
    SoilUnitID INT NOT NULL,
    SoilClassID INT,
    SoilSubClassID INT,
    AptitudeID INT, 
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

CREATE TABLE region_soil_types (
    RegionSoilTypeID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    RegionID INT NOT NULL,
    SoilTypeID INT NOT NULL,
    FOREIGN KEY (RegionID) REFERENCES region(RegionID) ON DELETE CASCADE,
    FOREIGN KEY (SoilTypeID) REFERENCES soil_type(SoilTypeID) ON DELETE CASCADE
);

select * from region_soil_types;

SHOW TABLES;
