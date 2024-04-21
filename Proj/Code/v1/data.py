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
for country, categories in detailed_losses.items():
    print(f"{country}:")
    for category, value in categories.items():
        print(f"  {category}: {value}")
    print()

