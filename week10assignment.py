def sort_loot(loot_log):
    dict = {}
    for line in loot_log:
        type, name, price = line.split(":")
        values = (name, price)

        if type not in dict:
            dict[type] = []
        dict[type].append(values)
    return dict

def appraise_inventory(loot_dict):
    result = {}
    for key, value in loot_dict.items():
        for name, price in value:
            if key in result:
                result[key] += int(price)
            else:
                result[key] = int(price)
    for item_type, gold_value in result.items():
        print(f"{item_type}: {gold_value} Gold")


loot_log = [
    "Weapon:Iron Sword:150",
    "Potion:Health Potion:10",
    "Armor:Leather Vest:80",
    "Weapon:Steel Dagger:120",
    "Potion:Mana Potion:15",
    "Armor:Iron Helm:50"
]
sort_loot(loot_log)
appraise_inventory(sort_loot(loot_log))
