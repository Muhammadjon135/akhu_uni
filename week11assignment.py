# Format: {Spell: {"base_cost": int, "type": str}}
spells = {
    "Fireball": {"base_cost": 10, "type": "Mage"},
    "Heal":     {"base_cost": 5,  "type": "Cleric"}
}

# Format: {Name: {"mana": float, "class": str}}
players = {
    "Gandalf": {"mana": 50.0, "class": "Mage"},  # Half cost for Mage spells
    "Aragorn": {"mana": 20.0, "class": "Warrior"} # Full cost
}

actions = [
    ("Gandalf", "Fireball", 4), # Valid. Cost: (4*10)/2 = 20. Rem: 30.
    ("Aragorn", "Heal", 5),     # Error: Cost 25 > 20. (Full cost because Warrior != Cleric)
    ("Legolas", "Arrow", 1),    # Error: Player not found.
    ("Gandalf", "IceBeam", 1),  # Error: Unknown spell.
    ("Gandalf", "Fireball", -1), # Error: Power level must be positive integer.
]

def cast_spell(players_db, spellbook, player_name, spell_name, power_level):
    total_cost = 0.0
    
    if player_name not in players_db:
        raise KeyError("Player not found")
    elif spell_name not in spellbook:
        raise KeyError("Unknown spell")
    elif  power_level < 1 or type(power_level) != int:
        raise ValueError("Power level must be positive integer")

    calculation = (power_level * spellbook[spell_name]["base_cost"])

    if players_db[player_name]["class"] == spellbook[spell_name]["type"]:
        total_cost = calculation/2
    else:
        total_cost = calculation
        
    if total_cost > players_db[player_name]["mana"]:
        raise ValueError("Not enough mana")
    
    return total_cost
        
def process_combat_turn(players_db, spellbook, action_list):
    fizzled_spells = 0
    total_consumed = 0.0
    for player_name, spell_name, mana_available in action_list:
        try:
            total_cost = cast_spell(players_db, spellbook, player_name, spell_name, mana_available)
            total_consumed += total_cost
        except (KeyError, ValueError) as e:
            print(f"Cast Failed for {player_name}: {e}")
            fizzled_spells += 1
    return {'total_mana_consumed': total_consumed, 'fizzled_spells': fizzled_spells}    
        
print(process_combat_turn(players, spells, actions))
