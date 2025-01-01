USE database_carbon;

LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Downloads/soil_class.csv'
INTO TABLE soil_class
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

SELECT * FROM soil_class;

LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Downloads/soil_subclass.csv'
INTO TABLE soil_subclass
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

SELECT * FROM soil_subclass;


LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Documents/ISA_Data_Science/Semester_1/final_assignments/soil_aptitude.csv'
INTO TABLE soil_aptitude
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

SELECT * FROM soil_aptitude;


LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Documents/ISA_Data_Science/Semester_1/final_assignments/soil_unit_v3.csv'
INTO TABLE soil_unit
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@SoilUnitID, @Name, @Description, @Texture, @Salinity, @Colour, @Humic, @Molic, @Calcareous, @Normal, @Cambic, @AddCharacteristics)
SET
SoilUnitID = @SoilUnitID,
Name = @Name,
Description = @Description,
Texture = @Texture,
Salinity = @Salinity,
Colour = @Colour,
Humic = @Humic,
Molic = @Molic,
Calcareous = @Calcareous,
Normal = @Normal,
Cambic = @Cambic,
AddCharacteristics = @AddCharacteristics;

SELECT * FROM soil_unit LIMIT 5;
ALTER TABLE soil_unit ADD INDEX pc_soilunitid (SoilUnitID);


-- from this point we started using a temp table before putting into the real table. The rest have been removed --
CREATE TEMPORARY TABLE tmp_soil_type LIKE soil_type;

LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Documents/ISA_Data_Science/Semester_1/final_assignments/soil_type.csv' 
INTO TABLE tmp_soil_type
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@SoilTypeID, @RegionID, @SoilUnitID, @SoilClassID, @SoilSubClassID, @AptitudeID)
SET
SoilTypeID = @SoilTypeID,
SoilUnitID = @SoilUnitID,
SoilClassID = @SoilClassID,
SoilSubClassID = @SoilSubClassID,
AptitudeID = @AptitudeID;

SELECT * FROM tmp_soil_type;

LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Documents/ISA_Data_Science/Semester_1/final_assignments/soil_type.csv'
INTO TABLE soil_type
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@SoilTypeID, @SoilUnitID, @SoilClassID, @SoilSubClassID, @AptitudeID)
SET
SoilTypeID = @SoilTypeID,
SoilUnitID = @SoilUnitID,
SoilClassID = @SoilClassID,
SoilSubClassID = @SoilSubClassID,
AptitudeID = @AptitudeID;

SELECT * FROM soil_type LIMIT 5;
ALTER TABLE soil_type ADD INDEX pc_soiltypeid (SoilTypeID);
ALTER TABLE soil_type ADD INDEX fc_soilunitid (SoilUnitID);


LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Documents/ISA_Data_Science/Semester_1/final_assignments/crops_table.csv'
INTO TABLE crop
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@CropID, @Name, @CarbonFootprint, @WaterRequirement, @ProfitabilityIndex, @RotationCompatibility)
SET
CropID = @CropID,
Name = @Name,
CarbonFootprint = @CarbonFootprint,
WaterRequirement = @WaterRequirement,
ProfitabilityIndex = @ProfitabilityIndex,
RotationCompatibility = @RotationCompatibility;

SELECT * FROM crop LIMIT 5;
ALTER TABLE crop ADD INDEX pc_cropid (CropID);



LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Documents/ISA_Data_Science/Semester_1/final_assignments/crop_yield.csv'
INTO TABLE crop_yield
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@YieldID, @CropID, @Year, @YieldAmount)
SET
YieldID = @YieldID,
CropID = @CropID,
YieldAmount = @YieldAmount,
Year = @Year;

SELECT * FROM crop_yield LIMIT 5;
ALTER TABLE crop_yield ADD INDEX pc_yieldid (YieldID);
ALTER TABLE crop_yield ADD INDEX fc_cropid (CropID);


LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Documents/ISA_Data_Science/Semester_1/final_assignments/MarketData.csv'
INTO TABLE market_value
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@MarketValueID, @CropID, @Year, @PricePerTon, @DemandIndex)
SET
MarketValueID = @MarketValueID,
CropID = @CropID,
Year = @Year,
PricePerTon = @PricePerTon,
DemandIndex = @DemandIndex;

SELECT * FROM market_value LIMIT 5;
ALTER TABLE market_value ADD INDEX pc_marketvalueid (MarketValueID);
ALTER TABLE market_value ADD INDEX fc_cropid (CropID);


LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Documents/ISA_Data_Science/Semester_1/final_assignments/municipalities.csv'
INTO TABLE municipality
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@MunicipalityID, @Name)
SET
MunicipalityID = @MunicipalityID,
Name = @Name;

SELECT * FROM municipality LIMIT 5;
ALTER TABLE municipality ADD INDEX pc_municipalityid (MunicipalityID);


LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Documents/ISA_Data_Science/Semester_1/final_assignments/weather_copy.csv'
INTO TABLE weather
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@WeatherID, @MunicipalityID, @Date, @TemperatureMax, @TemperatureMin, @Precipitation)
SET
WeatherID = @WeatherID,
MunicipalityID = @MunicipalityID,
Date = @Date,
TemperatureMax = @TemperatureMax,
TemperatureMin = @TemperatureMin,
Precipitation = @Precipitation;

SELECT * FROM weather LIMIT 5;
ALTER TABLE weather ADD INDEX pc_weatherid (WeatherID);
ALTER TABLE weather ADD INDEX fc_municipalityrid (MunicipalityID);


LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Documents/ISA_Data_Science/Semester_1/final_assignments/region.csv'
INTO TABLE region
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@RegionID, @Freguesia, @ClimateZone, @DesertificationRisk, @MunicipalityID)
SET
RegionID = @RegionID,
Freguesia = @Freguesia,
ClimateZone = @ClimateZone,
DesertificationRisk = @DesertificationRisk,
MunicipalityID = @MunicipalityID;

SELECT * FROM region LIMIT 5;
ALTER TABLE region ADD INDEX pc_regionid (RegionID);



LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Documents/ISA_Data_Science/Semester_1/final_assignments/crop_compatibility.csv'
INTO TABLE crop_soil_compatibility
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@CompatibilityID, @CropID, @SoilTypeID)
SET
CompatibilityID = @CompatibilityID,
CropID = @CropID,
SoilTypeID = @SoilTypeID;

SELECT * FROM crop_soil_compatibility LIMIT 5;
ALTER TABLE crop_soil_compatibility ADD INDEX pc_compatibilityid (CompatibilityID);


LOAD DATA LOCAL INFILE '/Users/mekaelastevenson/Documents/ISA_Data_Science/Semester_1/final_assignments/region_soil_types.csv'
INTO TABLE region_soil_types
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@RegionSoilTypeID, @RegionID, @SoilTypeID)
SET
RegionSoilTypeID = @RegionSoilTypeID,
RegionID = @RegionID,
SoilTypeID = @SoilTypeID;

SELECT * FROM region_soil_types LIMIT 5;
ALTER TABLE region_soil_types ADD INDEX pc_regionsoiltypeid (RegionSoilTypeID);