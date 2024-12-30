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
            "description":"Demand index for crop. between 0 and 1"
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
            "description":"number of months post harvest that crop can be planted again"
        },
    }
    "required": ["CropID", "Name". "WaterRequirements"]
}

Table: crop_yield
{
    "properties" {
        "YieldID" {
            "type":"int",
            "description":""
        }, 
        "CropID" {
            "type":"int",
            "description":""
        }, 
        "Year" {
            "type":"year",
            "description":""
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
            "description":""
        }, 
        "Name" {
            "type":"varchar",
            "length": 10,
            "description":""
        }, 
        "Limitations" {
            "type":"varchar",
            "length": 30,
            "description":""
        },
        "ErosionRisk" {
            "type":"varchar",
            "length": 30,
            "description":""
        },
        "SuitableUse" {
            "type":"varchar",
            "length": 200,
            "description":""
        },
    }
    "required": ["SoilClassID", "Name". "Limitations", "ErosionRisk","SuitableUse"]
}

Table: soil_subclass
{
     "properties" {
        "SoilSubClassID" {
            "type":"int",
            "description":""
        }, 
        "Name" {
            "type":"varchar",
            "length": 100,
            "description":""
        }, 
        "Description" {
            "type":"varchar",
            "length": 200,
            "description":""
        }
    }
    "required": ["SoilSubClassID", "Name". "Description"]
}

Table: soil_unit
{
     "properties" {
        "SoilUnitID" {
            "type":"int",
            "description":""
        }, 
        "Name" {
            "type":"varchar",
            "length": 10,
            "description":""
        }, 
        "Description" {
            "type":"varchar",
            "length": 200,
            "description":""
        },
        "Texture" {
            "type":"varchar",
            "length": 10,
            "description":""
        },
        "Salinity" {
            "type":"varchar",
            "length": 10,
            "description":""
        },
        "Colour" {
            "type":"varchar",
            "length": 40,
            "description":""
        },
        "Humic" {
            "type":"int",
            "description":"",
        },
        "Mollic" {
            "type":"int",
            "description":"",
        },
        "Limestone" {
            "type":"int",
            "description":"",
        },
        "Standard" {
            "type":"int",
            "description":"",
        },
        "Cambisol" {
            "type":"int",
            "description":"",
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
            "description":""
        }, 
        "RegionID" {
            "type":"int",
            "description":""
        }, 
        "SoilUnitID" {
            "type":"int",
            "description":""
        }, 
        "SoilClassID" {
            "type":"int",
            "description":""
        }, 
        "SoilSubClassID" {
            "type":"int",
            "description":""
        }, 
    }
    "required": ["SoilTypeID", "RegionID". "SoilUnitID", "SoilClassID", "SoilSubClassID"]
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