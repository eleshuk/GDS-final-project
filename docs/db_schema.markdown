## Schema for each table

Table: market_value
{
    "properties": {
        "MarketValueID" {
            "type": "int",
            "description":"unique id for stock market data"
        },
        "CropID" {
            "type": "int",
            "description":"foreign id for crop that the market data is for"
        },
        "Date" {
            "type": "date",
            "description":"the date the data was recorded"
        }, 
        "PricePerTon" {
            "type": "float",
            "description":"market price per ton (€)"
        }, 
        "DemandIndex" {
            "type": "float",
            "options":["0", "1"],
            "description":"Demand index for crop"
        }
    } 
    "required": ["MarketValueID", "CropID". "Date". "PricePerTon"]
}

Table: crop
{
    "properties" {
        "CropID" {
            "type":"int",
            "description":"unique id for crop data"
        }, 
        "Name" {
            "type":"varchar"
            "length":100,
            "description":"name of crop"
        }, 
        "CarbonFootprint" {
            "type":"float",
            "minimum":-10,
            "maximum":10,
            "description":"scale -10 to 10, with -10 being large carbon storage potential, and 10 being large carbom emitter"
        },
        "WaterRequirements" {
            "type":"float",
            "description":"water requirement of crop in mm"
        },
        "ProfitabilityIndex" {
            "type":"float",
            "minimum":0,
            "maximum":1,
            "description":"profitability index for crop. between 0 and 1"
        },
        "RotationCompatibility" {
            "type":"int",
            "description":"crop rotation cycle"
        },
    }
    "required": ["CropID", "Name". "WaterRequirements"]
}

Table: crop_yield
{
    "properties" {
        "YieldID" {
            "type":"int",
            "description":"unique id for yield data"
        }, 
        "CropID" {
            "type":"int",
            "description":"unique id for crop data"
        }, 
        "Year" {
            "type":"year",
            "description":"year in which the crop yield was recorded or measured"
        },
        "YieldAmount" {
            "type":"float",
            "description":"crop yield in tonnes/hectare"
        }
    }
    "required": ["YieldID", "CropID". "YieldAmount"]
}

Table: region - EDIT
{
    "properties" {
        "RegionID" {
            "type":"int",
            "description":""
        }, 
        "Name" {
            "type":"varchar",
            "length":100
            "description":""
        }, 
        "DesertificationRisk" {
            "type":"varchar",
            "length": 20,
            "options":["susceptible", "not susceptible"],
            "description":""
        }
        "ClimateZone" {
            "type":"varchar",
            "length":50,
            "options":["Csb", "Csa", "mixed"],
            "description":""
        }
    }
    "required": ["RegionID", "Name"]
}

Table: weather
{
    "properties" {
        "WeatherID" {
            "type":"int",
            "description":"unique id for weather data"
        }, 
        "RegionID" {
            "type":"int",
            "description":"foreign key for region"
        }, 
        "Date" {
            "type":"date",
            "description":"date weather data was recorded"
        },
        "TemperatureMax" {
            "type":"varchar",
            "length":
            "description":"minimum temperature in degrees celsius"
        },
        "TemperatureMin" {
            "type":"float",
            "description":"maximum temperature in degrees celsius"
        }
        "Precipitation" {
            "type":"float",
            "description":"rainfall in millimetres"
        }
    }
    "required": ["CropID", "Name". "WaterRequirements"]
}

Table: soil_aptitude
{
     "properties" {
        "AptitudeID" {
            "type":"int",
            "description":""
        }, 
        "Level" {
            "type":"varchar",
            "length": 100,
            "description":""
        }, 
        "Nomenclature" {
            "type":"varchas",
            "length": 100,
            "description":""
        },
    }
    "required": ["AptitudeID", "Level". "Nomenclature"]
}

Table: soil_class
{
     "properties" {
        "SoilClassID" {
            "type":"int",
            "description":"unique id for soil class data"
        }, 
        "Name" {
            "type":"varchar",
            "length": 10,
            "description":"name of the soil unit"
        }, 
        "Limitations" {
            "type":"varchar",
            "length": 30,
            "options":["few or none", "moderate", "moderate to severe, "severe", "highly severe"],
            "description":"agricultural limitations presented by soil type"
        },
        "ErosionRisk" {
            "type":"varchar",
            "length": 30,
            "options":["no or low risk", "low to moderate", "moderate to high", "high to very high", "very high"],
            "description":"susceptibility and risk of erosion"
        },
        "SuitableUse" {
            "type":"varchar",
            "length": 200,
            "options":["intensive agriculture", "moderate intensity", "low intensity agriculture", "few or moderate", "severe to very severe"],
            "description":"suitability for agricultural use"
        },
    }
    "required": ["SoilClassID", "Name". "Limitations", "ErosionRisk","SuitableUse"]
}

Table: soil_subclass
{
     "properties" {
        "SoilSubClassID" {
            "type":"int",
            "description":"unique id for soil subclass"
        }, 
        "Name" {
            "type":"varchar",
            "length": 100,
            "options":["e", "h", "s"],
            "description":"soil subclass definitition"
        }, 
        "Description" {
            "type":"varchar",
            "length": 200,
            "description":"soil subclass description"
        }
    }
    "required": ["SoilSubClassID", "Name". "Description"]
}

Table: soil_unit
{
     "properties" {
        "SoilUnitID" {
            "type":"int",
            "description":"unique id for soil unit data"
        }, 
        "Name" {
            "type":"varchar",
            "length": 10,
            "description":"name of the soil unit"
        }, 
        "Description" {
            "type":"varchar",
            "length": 200,
            "description":"soil units description"
        },
        "Texture" {
            "type":"varchar",
            "length": 10,
            "options":["heavy", "medium", "light"],
            "description":"description of soil texture"
        },
        "Salinity" {
            "type":"varchar",
            "length": 10,
            "options":["high", "moderate", "low"],
            "description":"soil salinity"
        },
        "Colour" {
            "type":"varchar",
            "length": 40,
            "options":["red or yellow", "brown"],
            "description":"soil color description"
        },
        "Humic" {
            "type":"int",
            "options":["0", "1"],
            "description":"binary that indicates whether soil is humic or not",
        },
        "Mollic" {
            "type":"int",
            "description":"binary that indicates whether soil is molic or not",
        },
        "Limestone" {
            "type":"int",
            "options":["0", "1"],
            "description":"binary that indicates whether soil is calcareous or not",
        },
        "Standard" {
            "type":"int",
            "description":"",
        },
        "Cambisol" {
            "type":"int",
            "options":["0", "1"],
            "description":"binary that indicates whether soil is calcareous or not",
        },
        "AddCharacteristics" {
            "type":"varchar",
            "length": 300,
            "description":""
        },
    }
    "required": ["SoilUnitID", "Name". "Description"]
}

Table: soil_type
{
     "properties" {
        "SoilTypeID" {
            "type":"int",
            "description":"unique id for soil type data"
        }, 
        "RegionID" {
            "type":"int",
            "description":"unique id for region data"
        }, 
        "SoilUnitID" {
            "type":"int",
            "description":"uique id for soil unit data"
        }, 
        "SoilClassID" {
            "type":"int",
            "description":"unique id for soil class data"
        }, 
        "SoilSubClassID" {
            "type":"int",
            "description":"unique id for soil subclass data"
        }, 
    }
    "required": ["SoilTypeID", "RegionID", "SoilUnitID", "SoilClassID", "SoilSubClassID"]
}

Table: crop_soil_compatability
{
     "properties" {
        "CompatibilityID" {
            "type":"int",
            "description":"unique id for crop soil compatibility"
        }, 
        "CropID" {
            "type":"int",
            "description":"foreign id for crop table"
        }, 
        "SoilTypeID" {
            "type":"int",
            "description":"foreign id for soil type table"
        }
    }
    "required": ["CompatibilityID", "CropID". "SoilTypeID"]
}
