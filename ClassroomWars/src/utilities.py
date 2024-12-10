import random
from ansi_color import *
from roles import roles
from items import items

# Function to handle roles and assign abilities
def choose_role():
    print(f"\n{BOLD}{CYAN}Choose your character:{RESET}")
    for idx, role in enumerate(roles.keys(), start=1):
        print(f"{BOLD}{idx}. {role}{RESET} - {roles[role]['description']}")
    while True:
        try:
            choice = int(input(f"\n{BOLD}Enter the number of your choice:{RESET} "))
            if 1 <= choice <= len(roles):
                chosen_role = list(roles.keys())[choice - 1]
                print(f"\n{GREEN}You chose: {chosen_role}{RESET}")
                return chosen_role
            else:
                print(f"{RED}Invalid choice! Please choose a valid number.{RESET}")
        except ValueError:
            print(f"{RED}Invalid input! Please enter a number.{RESET}")

# Function to display skills with descriptions
def display_skills(role):
    print(f"\n{CYAN}{BOLD}Skills for {role}:{RESET}")
    skills = roles[role]["skills"]
    for idx, (skill_name, skill_info) in enumerate(skills.items(), start=1):
        desc = skill_info["description"]
        details = f"{YELLOW}Damage: {skill_info.get('damage', 0)}{RESET}; {RED}Stamina: {skill_info['stamina_cost']}{RESET}"
        if "heal" in skill_info:
            details += f"; {GREEN}Heal: {skill_info['heal']}{RESET}"
        if "stamina_heal" in skill_info:
            details += f"; {BLUE}Stamina Heal: {skill_info['stamina_heal']}{RESET}"
        print(f"{idx}. {BOLD}{skill_name}{RESET} ({details}) - {desc}")

# Function to display items with descriptions
def display_items():
    for idx, (item_name, item_info) in enumerate(items.items(), start=1):
        desc = item_info["description"]
        print(f"{idx}. {item_name} - {desc}")

# Display health and stamina with a bar #Changes-hipos
def display_stats(player_name, health, stamina, shield):
    max_health = 100
    max_stamina = 100
    bar_length = 20  # Adjust bar length for clarity

    # Calculate health and shield proportions
    combined_health = min(health + shield, max_health)
    filled_health = int((health / max_health) * bar_length)
    filled_shield = int((combined_health / max_health) * bar_length) - filled_health

    # Construct health bar
    health_bar = GREEN + "◼" * filled_health + GREY + "◼" * filled_shield + RESET
    health_bar += "◻" * (bar_length - (filled_health + filled_shield))

    # Construct stamina bar
    filled_stamina = int((stamina / max_stamina) * bar_length)
    stamina_bar = BLUE + "◼" * filled_stamina + RESET + "◻" * (bar_length - filled_stamina)

    return f"{BOLD}{player_name}{RESET} Health: [{health}] {health_bar}  Stamina: [{stamina}] {stamina_bar}"

# Execute a skill during a player's turn
def use_skill(player_name, opponent_name, player_stats, opponent_stats, skill_name, role):
    skill = roles[role]["skills"][skill_name]
    stamina_cost = skill["stamina_cost"]

    if player_stats["stamina"] < stamina_cost:
        print(f"{player_name} does not have enough stamina to use {skill_name}!")
        return

    player_stats["stamina"] -= stamina_cost

    if skill["type"] == "shield":
        shield_amount = 20
        player_stats["shield"] = min(player_stats["shield"] + shield_amount, 100)
        print(f"{player_name} used {skill_name}, gaining a shield of {shield_amount}!")
    
    elif skill["type"] == "attack":
        damage = random.randint(*skill["damage"]) if isinstance(skill["damage"], tuple) else skill["damage"]
        net_damage = max(0, damage - opponent_stats.get("defense_buff", 0))
        
        # Apply damage to shield first
        if opponent_stats["shield"] > 0:
            shield_damage = min(net_damage, opponent_stats["shield"])
            opponent_stats["shield"] -= shield_damage
            net_damage -= shield_damage
            print(f"{opponent_name}'s shield absorbed {shield_damage} damage!")
        
        # Apply remaining damage to health
        if net_damage > 0:
            opponent_stats["health"] -= net_damage
            print(f"{opponent_name} took {net_damage} damage!")

    elif skill["type"] == "heal":
        heal_amount = skill["heal"]
        player_stats["health"] = min(player_stats["health"] + heal_amount, 100)
        print(f"{player_name} used {skill_name}, healing {heal_amount} HP!")

    elif skill["type"] == "ultimate":
        damage = skill["damage"]
        net_damage = max(0, damage - opponent_stats.get("defense_buff", 0))
        opponent_stats["health"] -= net_damage
        print(f"{player_name} used {skill_name}, dealing {net_damage} ultimate damage to {opponent_name}!")

# Function to use an item during a player's turn
def use_item(player_name, player_stats, opponent_stats, item_name):
    item = items[item_name]

    if item["type"] == "buff":
        buff_type = "attack_buff" if "attack_buff" in item else "defense_buff"
        buff_value = item[buff_type]
        player_stats[buff_type] = buff_value
        print(f"{player_name} used {item_name}, gaining {buff_value} {buff_type.replace('_', ' ')} for one turn!")

    elif item["type"] == "attack":
        damage = item["damage"]
        opponent_stats["health"] -= damage
        print(f"{player_name} used {item_name}, dealing {damage} damage to the opponent!")

    elif item["type"] == "stamina":
        stamina_gain = item["stamina_gain"]
        player_stats["stamina"] = min(player_stats["stamina"] + stamina_gain, 100)
        print(f"{player_name} used {item_name}, recovering {stamina_gain} stamina points!")

# Check if a player has been defeated or incapacitated
def check_defeat(player_name, player_stats):
    if player_stats["health"] <= 0:
        print(f"\n{RED}{player_name}{RESET} has been defeated!\n")
        return True
    elif player_stats["health"] < 20:
        print(f"\n{YELLOW}{player_name}{RESET} is on the verge of collapse with critical health!")
    return False
