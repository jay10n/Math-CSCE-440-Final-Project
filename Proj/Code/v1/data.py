import pandas as pd

file_path = 'data_excel.xlsx'
data = pd.read_excel(file_path)

last_row = data.iloc[-1]

detailed_losses = {
    "Russia": {
        "Tanks": last_row["Russia_Tanks"],
        "AFV": last_row["Russia_AFV"],
        "IFV": last_row["Russia_IFV"],
        "APC": last_row["Russia_APC"],
        "IMV": last_row["Russia_IMV"],
        "Engineering": last_row["Russia_Engineering"],
        "Communications": last_row["Russia_Coms"],
        "Vehicles": last_row["Russia_Vehicles"],
        "Aircraft": last_row["Russia_Aircraft"],
        "Infantry": last_row["Russia_Infantry"],
        "Logistics": last_row["Russia_Logistics"],
        "Armor": last_row["Russia_Armor"],
        "Anti-Air": last_row["Russia_Antiair"],
        "Artillery": last_row["Russia_Artillery"],
    },
    "Ukraine": {
        "Tanks": last_row["Ukraine_Tanks"],
        "AFV": last_row["Ukraine_AFV"],
        "IFV": last_row["Ukraine_IFV"],
        "APC": last_row["Ukraine_APC"],
        "IMV": last_row["Ukraine_IMV"],
        "Engineering": last_row["Ukraine_Engineering"],
        "Communications": last_row["Ukraine_Coms"],
        "Vehicles": last_row["Ukraine_Vehicles"],
        "Aircraft": last_row["Ukraine_Aircraft"],
        "Infantry": last_row["Ukraine_Infantry"],
        "Logistics": last_row["Ukraine_Logistics"],
        "Armor": last_row["Ukraine_Armor"],
        "Anti-Air": last_row["Ukraine_Antiair"],
        "Artillery": last_row["Ukraine_Artillery"],
    }
}
russia_military_assets_losses_for_from_russian_media = {
    "Russia": {
        "Tanks": "1180",
        "AFV": "estimated_numbers",
        "IFV": "2470",
        "APC": "2470",
    }
}
russia_military_assets_losses_for_from_ukrianian_media = {
    "Personnel": 447510,
    "Tanks": 7074,
    "AFVs": 13551,
    "Artillery": 11316,
    "MLRS": 1036,
    "AntiAir": 749,
    "Aircraft": 347,
    "Helicopters": 325,
    "UAVs": 8956,    
    "CruiseMissiles": 2064,
    "Ships": 26,      
    "Submarines": 1, 
    "Vehicles": 15071,
    "SpecialEquipment": 1864 ,
}

initial_state_2022 = {
    "Russia": {
        "TotalPopulation": 142320790,
        "AvailableManpower": 69737187,
        "FitForService": 46681219,
        "ReachingMilitaryAgeAnnually": 1280887,
        "ActivePersonnel": 850000,
        "ReservePersonnel": 250000,
        "ParamilitaryForces": 250000,
        "DefenseBudget": 154000000000,
        "ExternalDebt": 479844000000,
        "ForeignReserve": 432700000000,
        "PurchasingPower": 3875690000000,
        "TotalAircraft": 4173,
        "FighterAircraft": 772,
        "DedicatedAttack": 739,
        "Transports": 445,
        "Trainers": 522,
        "SpecialMission": 132,
        "Helicopters": 1543,
        "AttackHelicopters": 544,
        "TankStrength": 12420,
        "ArmoredVehicles": 30122,
        "SelfPropelledArtillery": 6574,
        "TowedArtillery": 7571,
        "MobileRocketProjectors": 3391,
        "FleetStrength": 605,
        "AircraftCarriers": 1,
        "Submarines": 70,
        "Destroyers": 15,
        "Frigates": 11,
        "Corvettes": 86,
        "PatrolVessels": 59,
        "MineWarfare": 49,
        "Airports": 1218,
        "MerchantMarine": 2873,
        "PortsTerminals": 8,
        "LaborForce": 69923000,
        "Roadways": 1283387,
        "Railways": 87157,
        "OilProduction": 10760000,
        "OilConsumption": 3650000,
        "ProvenReserves": 80000000000,
        "SquareLandArea": 17098242,
        "SharedBorder": 22408,
        "Coastline": 37653,
        "Waterways": 102000
    },
    "Ukraine": {
        "TotalPopulation": 43745640,
        "AvailableManpower": 22310276,
        "FitForService": 15617193,
        "ReachingMilitaryAgeAnnually": 481202,
        "ActivePersonnel": 200000,
        "ReservePersonnel": 250000,
        "ParamilitaryForces": 50000,
        "DefenseBudget": 11870000000,
        "ExternalDebt": 117410000000,
        "ForeignReserve": 18810000000,
        "PurchasingPower": 515000000000,
        "TotalAircraft": 318,
        "FighterAircraft": 69,
        "DedicatedAttack": 29,
        "Transports": 32,
        "Trainers": 71,
        "SpecialMission": 5,
        "Helicopters": 112,
        "AttackHelicopters": 34,
        "TankStrength": 2596,
        "ArmoredVehicles": 12303,
        "SelfPropelledArtillery": 1067,
        "TowedArtillery": 2040,
        "MobileRocketProjectors": 490,
        "FleetStrength": 38,
        "AircraftCarriers": 0,
        "Submarines": 0,
        "Destroyers": 0,
        "Frigates": 1,
        "Corvettes": 1,
        "PatrolVessels": 13,
        "MineWarfare": 1,
        "Airports": 187,
        "MerchantMarine": 409,
        "PortsTerminals": 6,
        "LaborForce": 17990000,
        "Roadways": 169694,
        "Railways": 21733,
        "OilProduction": 32000,
        "OilConsumption": 233000,
        "ProvenReserves": 395000000,
        "SquareLandArea": 603550,
        "SharedBorder": 5618,
        "Coastline": 2782,
        "Waterways": 2150
    }
}

initial_state_2024 = {
    "Russia": {
        "TotalPopulation": 141698923,
        "AvailableManpower": 69432472,
        "FitForService": 46477247,
        "ReachingMilitaryAgeAnnually": 1275290,
        "ActivePersonnel": 1320000,
        "ReservePersonnel": 2000000,
        "ParamilitaryForces": 250000,
        "DefenseBudget": 109000000000,
        "ExternalDebt": 500000000000,
        "ForeignReserve": 632242000000,
        "PurchasingPower": 4078000000000,
        "TotalAircraft": 4255,
        "FighterAircraft": 809,
        "DedicatedAttack": 730,
        "Transports": 453,
        "Trainers": 552,
        "SpecialMission": 145,
        "AerialTankers": 19,
        "Helicopters": 1547,
        "AttackHelicopters": 559,
        "TankStrength": 14777,
        "ArmoredVehicles": 161382,
        "SelfPropelledArtillery": 6208,
        "TowedArtillery": 8356,
        "MobileRocketProjectors": 3065,
        "FleetStrength": 781,
        "AircraftCarriers": 1,
        "Submarines": 65,
        "Destroyers": 14,
        "Frigates": 12,
        "Corvettes": 83,
        "PatrolVessels": 122,
        "MineWarfare": 47,
        "Airports": 1218,
        "MerchantMarine": 2917,
        "PortsTerminals": 8,
        "LaborForce": 72444000,
        "Roadways": 1283387,
        "Railways": 85494,
        "OilProduction": 10750000,
        "OilConsumption": 3700000,
        "ProvenReservesOil": 80000000000,
        "NaturalGasProduction": 701544189000,
        "NaturalGasConsumption": 460612169000,
        "ProvenReservesGas": 47805215000000,
        "CoalProduction": 447332000,
        "CoalConsumption": 266038000,
        "ProvenReservesCoal": 162166000000,
        "SquareLandArea": 17098242,
        "SharedBorder": 22407,
        "Coastline": 37653,
        "Waterways": 102000
    },
    "Ukraine": {
        "TotalPopulation": 43306477,
        "AvailableManpower": 22086303,
        "FitForService": 15460412,
        "ReachingMilitaryAgeAnnually": 476371,
        "ActivePersonnel": 900000,
        "ReservePersonnel": 1200000,
        "ParamilitaryForces": 100000,
        "DefenseBudget": 42000000000,
        "ExternalDebt": 120000000000,
        "ForeignReserve": 30697000000,
        "PurchasingPower": 379893000000,
        "TotalAircraft": 321,
        "FighterAircraft": 72,
        "DedicatedAttack": 30,
        "Transports": 24,
        "Trainers": 73,
        "SpecialMission": 3,
        "AerialTankers": 0,
        "Helicopters": 130,
        "AttackHelicopters": 33,
        "TankStrength": 1777,
        "ArmoredVehicles": 22110,
        "SelfPropelledArtillery": 1205,
        "TowedArtillery": 1012,
        "MobileRocketProjectors": 491,
        "FleetStrength": 104,
        "AircraftCarriers": 0,
        "Submarines": 0,
        "Destroyers": 0,
        "Frigates": 0,
        "Corvettes": 0,
        "PatrolVessels": 33,
        "MineWarfare": 3,
        "Airports": 187,
        "MerchantMarine": 410,
        "PortsTerminals": 6,
        "LaborForce": 20463000,
        "Roadways": 169694,
        "Railways": 21733,
        "OilProduction": 60000,
        "OilConsumption": 250000,
        "ProvenReservesOil": 395000000,
        "NaturalGasProduction": 19511040000,
        "NaturalGasConsumption": 26413486000,
        "ProvenReservesGas": 1104355000000,
        "CoalProduction": 23908000,
        "CoalConsumption": 41181000,
        "ProvenReservesCoal": 34375000000,
        "SquareLandArea": 603550,
        "SharedBorder": 5581,
        "Coastline": 2782,
        "Waterways": 1672
    }
}
 


for country, categories in detailed_losses.items():
    print(f"{country}:")
    for category, value in categories.items():
        print(f"  {category}: {value}")
    print()

import pandas as pd


def load_data(file_path):
    try:
        return pd.read_excel(file_path)
    except FileNotFoundError:
        print("The file was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def extract_losses(data):
    if data is None:
        return None

    last_row = data.iloc[-1]
    categories = ["Tanks", "AFV", "IFV", "APC", "IMV", "Engineering", "Communications", "Vehicles", "Aircraft",
                  "Infantry", "Logistics", "Armor", "Anti-Air", "Artillery"]
    losses = {country: {cat: last_row[f"{country}_{cat}"] for cat in categories} for country in ["Russia", "Ukraine"]}
    return losses


def print_losses(losses):
    if losses is None:
        return

    for country, categories in losses.items():
        print(f"{country}:")
        for category, value in categories.items():
            print(f"  {category}: {value}")
        print()


# Main execution
file_path = 'data_excel.xlsx'
data = load_data(file_path)
detailed_losses = extract_losses(data)
print_losses(detailed_losses)
