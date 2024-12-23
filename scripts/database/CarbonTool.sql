CREATE TABLE Region (
    RegionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ClimateZone VARCHAR(50),
    DesertificationRisk FLOAT CHECK (DesertificationRisk BETWEEN 0 AND 1)
);

select *from region r;

CREATE TABLE WeatherData (
    WeatherID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    RegionID INT NOT NULL,
    Year YEAR NOT NULL,
    Temperature FLOAT,
    Rainfall FLOAT,
    GrowingSeasonLength INT,
    FOREIGN KEY (RegionID) REFERENCES Region(RegionID) ON DELETE CASCADE
);

select * from weatherdata w ;

CREATE TABLE SoilType (
    SoilTypeID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    RegionID INT NOT NULL,
    pH FLOAT CHECK (pH BETWEEN 0 AND 14),
    OrganicMatter FLOAT,
    Texture VARCHAR(50),
    Fertility FLOAT CHECK (Fertility BETWEEN 0 AND 1),
    CarbonStorage FLOAT,
    FOREIGN KEY (RegionID) REFERENCES Region(RegionID) ON DELETE CASCADE
);

select * from soiltype s ;
show tables;

CREATE TABLE Crop (
    CropID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    CarbonFootprint FLOAT,
    WaterRequirement FLOAT,
    ProfitabilityIndex FLOAT CHECK (ProfitabilityIndex BETWEEN 0 AND 1),
    RotationCompatibility VARCHAR(255)
);

select * from Crop;

CREATE TABLE MarketData (
    MarketID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    CropID INT NOT NULL,
    Year YEAR NOT NULL,
    PricePerTon FLOAT,
    DemandIndex FLOAT CHECK (DemandIndex BETWEEN 0 AND 1),
    FOREIGN KEY (CropID) REFERENCES Crop(CropID) ON DELETE CASCADE
);

select * from MarketData;

CREATE TABLE YieldPerCrop (
    YieldID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    CropID INT NOT NULL,
    RegionID INT NOT NULL,
    WeatherID INT NOT NULL,
    Year YEAR NOT NULL,
    YieldAmount FLOAT,
    FOREIGN KEY (CropID) REFERENCES Crop(CropID) ON DELETE CASCADE,
    FOREIGN KEY (RegionID) REFERENCES Region(RegionID) ON DELETE CASCADE,
    FOREIGN KEY (WeatherID) REFERENCES WeatherData(WeatherID) ON DELETE CASCADE
);

select * from YieldPerCrop;

CREATE TABLE CarbonPrice (
    CarbonPriceID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Year YEAR NOT NULL,
    PricePerTonCO2 FLOAT
);

select * from CarbonPrice;

CREATE TABLE CropSoilCompatibility (
    CompatibilityID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    CropID INT NOT NULL,
    SoilTypeID INT NOT NULL,
    FOREIGN KEY (CropID) REFERENCES Crop(CropID) ON DELETE CASCADE,
    FOREIGN KEY (SoilTypeID) REFERENCES SoilType(SoilTypeID) ON DELETE CASCADE
);

select * from CropSoilCompatibility;

SHOW TABLES;

describe region ;













