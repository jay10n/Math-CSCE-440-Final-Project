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

for country, categories in detailed_losses.items():
    print(f"{country}:")
    for category, value in categories.items():
        print(f"  {category}: {value}")
    print()

