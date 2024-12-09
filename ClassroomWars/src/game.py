import random
from roles import roles
from items import items
from utilities import choose_role, display_skills, display_items, display_stats, use_skill, use_item, check_defeat
from ascii_art import title_art, win
from ansi_colors import *

# Main game loop
def game_loop():
    print(f"{title_art}")
    
    # Short Introduction for the User
    print(f"""\nWelcome to {BOLD}{YELLOW}'Classroom Wars: Sino ang Pinakapabibo?'! 🎓{RESET} Step into the world of a typical Filipino classroom, where 
    students and teachers battle it out to claim the title of Pinakapabibo. Choose your character, strategize your moves, and let the fun begin! ✨""")

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
