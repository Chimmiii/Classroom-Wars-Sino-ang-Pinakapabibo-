import random

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
PURPLE = "\033[35m"
GREY = "\033[90m"

# Short Introduction for the User
print(f"""\nWelcome to {BOLD}{YELLOW}'Classroom Wars: Sino ang Pinakapabibo?'! 🎓{RESET} Step into the world of a typical Filipino classroom, where 
students and teachers battle it out to claim the title of Pinakapabibo. Choose your character, strategize your moves, and let the fun begin! ✨""")

title_art = """

 ▄████▄  ██▓    ▄▄▄        ██████   ██████  ██▀███   ▒█████   ▒█████   ███▄ ▄███▓    █     █░ ▄▄▄       ██▀███    ██████ 
▒██▀ ▀█ ▓██▒   ▒████▄    ▒██    ▒ ▒██    ▒ ▓██ ▒ ██▒▒██▒  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒   ▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▒██    ▒ 
▒▓█    ▄▒██░   ▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▓██ ░▄█ ▒▒██░  ██▒▒██░  ██▒▓██    ▓██░   ▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒░ ▓██▄   
▒▓▓▄ ▄██▒██░   ░██▄▄▄▄██   ▒   ██▒  ▒   ██▒▒██▀▀█▄  ▒██   ██░▒██   ██░▒██    ▒██    ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄    ▒   ██▒
▒ ▓███▀ ░██████▒▓█   ▓██▒▒██████▒▒▒██████▒▒░██▓ ▒██▒░ ████▓▒░░ ████▓▒░▒██▒   ░██▒   ░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒▒██████▒▒
░ ░▒ ▒  ░ ▒░▓  ░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ░  ░   ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░
  ░  ▒  ░ ░ ▒  ░ ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ░▒ ░ ▒░  ░ ▒ ▒░   ░ ▒ ▒░ ░  ░      ░     ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒  ░ ░
░         ░ ░    ░   ▒   ░  ░  ░  ░  ░  ░    ░░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒  ░      ░        ░   ░    ░   ▒     ░░   ░ ░  ░  ░  
░ ░         ░  ░     ░  ░      ░        ░     ░         ░ ░      ░ ░         ░          ░          ░  ░   ░           ░  
░                                                                                                                        
"""
win = """
██████╗ ██╗███╗   ██╗ █████╗ ██╗  ██╗ █████╗ ██████╗  █████╗ ██████╗ ██╗██████╗  ██████╗     ██╗███████╗
██╔══██╗██║████╗  ██║██╔══██╗██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔═══██╗    ██║██╔════╝
██████╔╝██║██╔██╗ ██║███████║█████╔╝ ███████║██████╔╝███████║██████╔╝██║██████╔╝██║   ██║    ██║███████╗
██╔═══╝ ██║██║╚██╗██║██╔══██║██╔═██╗ ██╔══██║██╔═══╝ ██╔══██║██╔══██╗██║██╔══██╗██║   ██║    ██║╚════██║
██║     ██║██║ ╚████║██║  ██║██║  ██╗██║  ██║██║     ██║  ██║██████╔╝██║██████╔╝╚██████╔╝    ██║███████║
╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═╝╚═════╝  ╚═════╝     ╚═╝╚══════╝                                                                                                                                                                                               
"""

# Filipino stereotypes as roles with unique abilities and stats
roles = {
    "Class Clown": {
        "description": "The life of the classroom that makes everyone laugh, through using jokes and pranks on opponents.\n",
        "skills": {
            "Cartolina Bang!": {"type": "attack", "damage": (15, 20), "stamina_cost": 15, "description": "A loud prank causing damage."},
            "Haha, Funny": {"type": "heal", "damage": (1, 3), "heal": 20, "stamina_cost": 25, "description": "A joke so funny, it heals you."},
            "Corny ng Joke": {"type": "ultimate", "damage": 45, "stamina_cost": 40, "description": "A joke so bad it deals massive damage."},
        },
    },
    "Queen Bee": {
        "description": "The confident, popular student who always joins pageants and search contests with her followers always on her side.\n",
        "skills": {
            "Bow Down": {"type": "attack", "damage": (15, 20), "stamina_cost": 15, "description": "Forces the opponent to bow in submission."},
            "The Clique": {"type": "shield", "damage": 0, "stamina_cost": 30, "description": "Summons her clique to shield herself."},
            "Queen's Command": {"type": "ultimate", "damage": 55, "stamina_cost": 45, "description": "Commands her clique to attack."},
        },
    },
    "Teacher's Pet": {
        "description": "The student who is highly favored by the teachers, snitching on everyone in the class.\n",
        "skills": {
            "Damot!": {"type": "attack", "damage": (15, 20), "stamina_cost": 15, "description": "A selfish move that damages opponents."},
            "Extra Credit": {"type": "heal", "damage": 0, "heal": 20, "stamina_cost": 25, "description": "Gains extra credit to heal."},
            "Snitch": {"type": "ultimate", "damage": 60, "stamina_cost": 50, "description": "Reports the opponent for massive damage."},
        },
    },
    "Rich Kid (RK)": {
        "description": "The student who flaunts his wealth to get an advantage. Expertise is in healing but deals little damage.\n",
        "skills": {
            "Bribe Opponent": {"type": "attack", "damage": 25, "stamina_cost": 15, "description": "Throws money to damage the opponent."},
            "iPhone Pro Max flex": {"type": "heal", "damage": 10, "heal": 30, "stamina_cost": 10, "description": "Heals by showing off an expensive gadget."},
            "Unli Allowance": {"type": "ultimate", "damage": 0, "heal": 50, "stamina_heal": 50, "stamina_cost": 50, "description": "Recovers health and stamina using unlimited allowance."},
        },
    },
    "Varsity Student": {
        "description": "A powerhouse with moves that balance agility, strength, and endurance, excelling in offensive strikes and self-preservation techniques.\n",
        "skills": {
            "Varsity Walk": {"type": "dodge", "damage": 0, "stamina_cost": 25, "description": "Dodges the opponent's attack gracefully."},
            "Kaya ko to!": {"type": "heal", "damage": 0, "heal": 30, "stamina_cost": 20, "description": "Boosts morale and heals health."},
            "Champion's Glory": {"type": "ultimate", "damage": 40, "shield": 20, "stamina_cost": 50, "description": "Deals massive damage and gains a shield."},
        },
    },
    "Teacher RB": {
        "description": "Utilizes authority and wisdom to drain stamina, heal allies, and protect with shields.\n",
        "skills": {
            "Surprise Quiz": {"type": "attack", "damage": 30, "stamina_cost": 20, "description": "Catches the opponent off guard with a quiz."},
            "1-3 pm Lecture": {"type": "heal", "damage": 35, "heal": 15, "stamina_cost": 25, "description": "Heals health with a soothing lecture."},
            "Go to the Principal!": {"type": "ultimate", "damage": 60, "stamina_cost": 40, "description": "Punishes the opponent with principal-level authority."},
        },
    },
}

# Items that can be used during a turn
items = {
    "Chalk": {"type": "buff", "attack_buff": 10, "duration": 1, "description": "Increases attack by 10 for one turn."},
    "Eraser": {"type": "buff", "defense_buff": 10, "duration": 1, "description": "Increases defense by 10 for one turn."},
    "Scissors": {"type": "attack", "damage": 40, "description": "Deals a sharp 40 damage."},
    "Book": {"type": "stamina", "stamina_gain": 20, "description": "Recovers 20 stamina points."},
}

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

# Display health and stamina with a bar
def display_stats(player_name, health, stamina):
    max_health = 100
    max_stamina = 100
    bar_length = 20  # Adjust bar length for clarity

    filled_health = int((health / max_health) * bar_length)
    health_bar = GREEN + "#" * filled_health + RESET + "-" * (bar_length - filled_health)

    filled_stamina = int((stamina / max_stamina) * bar_length)
    stamina_bar = BLUE + "#" * filled_stamina + RESET + "-" * (bar_length - filled_stamina)

    return f"{BOLD}{player_name}{RESET} Health: [{health}] {health_bar}  Stamina: [{stamina}] {stamina_bar}"

# Execute a skill during a player's turn
def use_skill(player_name, opponent_name, player_stats, opponent_stats, skill_name, role):
    skill = roles[role]["skills"][skill_name]
    stamina_cost = skill["stamina_cost"]

    if player_stats["stamina"] < stamina_cost:
        print(f"{player_name} does not have enough stamina to use {skill_name}!")
        return

    player_stats["stamina"] -= stamina_cost

    if skill["type"] == "attack":
        damage = random.randint(*skill["damage"]) if isinstance(skill["damage"], tuple) else skill["damage"]
        net_damage = max(0, damage - opponent_stats.get("defense_buff", 0))
        opponent_stats["health"] -= net_damage
        print(f"{player_name} used {skill_name}, dealing {net_damage} damage to {opponent_name}!")

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

# Main game loop
def game_loop():
    print(f"{title_art}")

    # Player 1 setup
    player1_name = input("Enter Player 1's name: ").strip()
    player1_role = choose_role()
    player1_stats = {"health": 100, "stamina": 100}

    # Player 2 setup
    player2_name = input("Enter Player 2's name (or 'Computer' for AI): ").strip()
    is_computer = player2_name.lower() == "computer"
    player2_role = random.choice(list(roles.keys())) if is_computer else choose_role()
    player2_stats = {"health": 100, "stamina": 100}

    if is_computer:
        print(f"\n{GREY}{player2_name} has chosen the role: {player2_role}!{RESET}")

    # Game loop
    while True:
        # Display stats
        print("\n" + display_stats(player1_name, player1_stats["health"], player1_stats["stamina"]))
        print(display_stats(player2_name, player2_stats["health"], player2_stats["stamina"]))

        # Player 1's turn
        print(f"\n{BOLD}{CYAN}{player1_name}'s Turn!{RESET}")
        try:
            action_choice = int(input(f"{BOLD}Enter 1 to use a skill, 2 to use an item:{RESET} "))
            if action_choice == 1:
                display_skills(player1_role)
                skill_choice = int(input(f"{BOLD}Enter the number of the skill to use:{RESET} "))
                skill_name = list(roles[player1_role]["skills"].keys())[skill_choice - 1]
                use_skill(player1_name, player2_name, player1_stats, player2_stats, skill_name, player1_role)
            elif action_choice == 2:
                display_items()
                item_choice = int(input(f"{BOLD}Enter the number of the item to use:{RESET} "))
                item_name = list(items.keys())[item_choice - 1]
                use_item(player1_name, player1_stats, player2_stats, item_name)
            else:
                print(f"{RED}Skill Issue! Turn skipped.{RESET}")
        except (ValueError, IndexError):
            print(f"{RED}Skill Issue! Turn skipped.{RESET}")

        # Check if Player 2 is defeated
        if check_defeat(player2_name, player2_stats):
            print(f"{YELLOW}{win}{GREEN}{BOLD}{player1_name}!{RESET}")
            break

        # Player 2's turn
        print(f"\n{BOLD}{PURPLE}{player2_name}'s Turn!{RESET}")
        if is_computer:
            print(f"\n{BOLD}{GREY}{player2_name}'s Turn!{RESET}")
            if player2_stats["stamina"] > 0:
                skill_name = random.choice(list(roles[player2_role]["skills"].keys()))
                print(f"{GREY}{player2_name} chooses to use the skill: {skill_name}!{RESET}")
                use_skill(player2_name, player1_name, player2_stats, player1_stats, skill_name, player2_role)
            else:
                item_name = "Book"
                print(f"{GREY}{player2_name} uses the item: {item_name}!{RESET}")
                use_item(player2_name, player2_stats, player1_stats, item_name)

        else:
            try:
                action_choice = int(input(f"{BOLD}Enter 1 to use a skill, 2 to use an item:{RESET} "))
                if action_choice == 1:
                    display_skills(player2_role)
                    skill_choice = int(input(f"{BOLD}Enter the number of the skill to use:{RESET} "))
                    skill_name = list(roles[player2_role]["skills"].keys())[skill_choice - 1]
                    use_skill(player2_name, player1_name, player2_stats, player1_stats, skill_name, player2_role)
                elif action_choice == 2:
                    display_items()
                    item_choice = int(input(f"{BOLD}Enter the number of the item to use:{RESET} "))
                    item_name = list(items.keys())[item_choice - 1]
                    use_item(player2_name, player2_stats, player1_stats, item_name)
                else:
                    print(f"{RED}Invalid choice! Turn skipped.{RESET}")
            except (ValueError, IndexError):
                print(f"{RED}Invalid input! Turn skipped.{RESET}")

        # Check if Player 1 is defeated
        if check_defeat(player1_name, player1_stats):
            print(f"{YELLOW}{win}{GREEN}{BOLD}{player2_name}!{RESET}")
            break

# Run the game
if __name__ == "__main__":
    game_loop()    