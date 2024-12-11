import random
from roles import roles
from items import items
from utilities import choose_role, display_skills, display_items, display_stats, use_skill, use_item, check_defeat
from ascii_art import title_art, win
from ansi_color import *
from __init__ import GAME_VERSION, GAME_NAME
from instructions import display_instructions

# Main game loop
def game_loop():
    print(f"{title_art}")
    print(f"\n{GREY}{GAME_NAME} (Version {GAME_VERSION})!{RESET}")
    
    # Short Introduction for the User
    print(f"""\nWelcome to {BOLD}{YELLOW}'Classroom Wars: Sino ang Pinakapabibo?'! 🎓{RESET} Step into the world of a typical Filipino classroom, where 
    students and teachers battle it out to claim the title of Pinakapabibo. Choose your character, strategize your moves, and let the fun begin! ✨\n""")
    print("~*~" * 47) 

    while True:
        # Option to view instructions at the beginning
        print("\nOptions:")
        print("1. Start a new game")
        print("2. View instructions")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("")
                print("~*~" * 47)
                break
            elif choice == 2:
                display_instructions()
                print("")
                print("~*~" * 47)
            elif choice == 3:
                print("Goodbye! See you next time!")
                print("")
                print("~*~" * 47)
                return
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Player 1 setup
    player1_name = input("\nEnter Player 1's name: ").strip()
    player1_role = choose_role()
    player1_stats = {"health": 100, "stamina": 100,"shield":0}
    print("")
    print("~*~" * 47)

    # Player 2 setup
    player2_name = input("Enter Player 2's name (or 'Computer' for AI): ").strip()
    is_computer = player2_name.lower() == "computer"
    player2_stats ={"health": 100, "stamina": 100, "shield": 0}
    
    if is_computer:
        available_roles = [role for role in roles.keys() if role != player1_role]  # Exclude player1's role
        player2_role = random.choice(available_roles)
    else:
        player2_role = choose_role()
        player2_stats = {"health": 100, "stamina": 100, "shield": 0}

    if is_computer:
        print(f"\n{GREY}{player2_name} has chosen the role: {player2_role}!{RESET}")


    # Game loop
    while True:
        # Display stats
        print("\n" + display_stats(player1_name, player1_stats["health"], player1_stats["stamina"],player1_stats["shield"]))
        print(display_stats(player2_name, player2_stats["health"], player2_stats["stamina"],player2_stats["shield"]))

        # Player 1's turn
        print(f"\n{BOLD}{CYAN}{player1_name}'s Turn!{RESET}")
        try:
            action_choice = int(input(f"{BOLD}Enter 1 to use a skill, 2 to use an item, 3 to surrender:{RESET} "))
            if action_choice == 1:
                display_skills(player1_role)
                skill_choice = int(input(f"{BOLD}Enter the number of the skill to use:{RESET} "))
                skill_name = list(roles[player1_role]["skills"].keys())[skill_choice - 1]
                use_skill(player1_name, player2_name, player1_stats, player2_stats, skill_name, player1_role)
                print("")
                print("~*~" * 47)
            elif action_choice == 2:
                display_items()
                item_choice = int(input(f"{BOLD}Enter the number of the item to use:{RESET} "))
                item_name = list(items.keys())[item_choice - 1]
                use_item(player1_name, player1_stats, player2_stats, item_name)
                print("")
                print("~*~" * 47)
            elif action_choice == 3:
                print("")
                print("~*~" * 47)
                print(f"\n{RED}{player1_name} has surrendered!{RESET}\n")
                print(f"{YELLOW}{win}{BOLD}{player2_name}!{RESET}")
                break
            else:
                print(f"{RED}Skill Issue! Turn skipped.{RESET}")
                print("")
                print("~*~" * 47)
        except (ValueError, IndexError):
            print(f"{RED}Skill Issue! Turn skipped.{RESET}")
            print("")
            print("~*~" * 47)

        # Check if Player 2 is defeated
        if check_defeat(player2_name, player2_stats):
            print("")
            print("~*~" * 47)
            print(f"{YELLOW}{win}{BOLD}{player1_name}!{RESET}")
            break

        # Player 2's turn
        print(f"\n{BOLD}{PURPLE}{player2_name}'s Turn!{RESET}")
        if is_computer:
            print(f"\n{BOLD}{GREY}{player2_name}'s Turn!{RESET}")
            if player2_stats["stamina"] > 0:
                skill_name = random.choice(list(roles[player2_role]["skills"].keys()))
                print(f"{GREY}{player2_name} chooses to use the skill: {skill_name}!{RESET}")
                use_skill(player2_name, player1_name, player2_stats, player1_stats, skill_name, player2_role)
                print("")
                print("~*~" * 47)
            else:
                item_name = "Book"
                print(f"{GREY}{player2_name} uses the item: {item_name}!{RESET}")
                use_item(player2_name, player2_stats, player1_stats, item_name)
                print("")
                print("~*~" * 47)

        else:
            try:
                action_choice = int(input(f"{BOLD}Enter 1 to use a skill, 2 to use an item, 3 to surrender:{RESET} "))
                if action_choice == 1:
                    display_skills(player2_role)
                    skill_choice = int(input(f"{BOLD}Enter the number of the skill to use:{RESET} "))
                    skill_name = list(roles[player2_role]["skills"].keys())[skill_choice - 1]
                    use_skill(player2_name, player1_name, player2_stats, player1_stats, skill_name, player2_role)
                    print("")
                    print("~*~" * 47)
                elif action_choice == 2:
                    display_items()
                    item_choice = int(input(f"{BOLD}Enter the number of the item to use:{RESET} "))
                    item_name = list(items.keys())[item_choice - 1]
                    use_item(player2_name, player2_stats, player1_stats, item_name)
                    print("")
                    print("~*~" * 47)
                elif action_choice == 3:
                    print("")
                    print("~*~" * 47)
                    print(f"\n{RED}{player2_name} has surrendered!{RESET}\n")
                    print(f"{YELLOW}{win}{BOLD}{player1_name}!{RESET}")
                    break
                else:
                    print(f"{RED}Invalid choice! Turn skipped.{RESET}")
                    print("")
                    print("~*~" * 47)
            except (ValueError, IndexError):
                print(f"{RED}Invalid input! Turn skipped.{RESET}")
                print("")
                print("~*~" * 47)

        # Check if Player 1 is defeated
        if check_defeat(player1_name, player1_stats):
            print("")
            print("~*~" * 47)
            print(f"{YELLOW}{win}{BOLD}{player2_name}!{RESET}")
            break

# Run the game
if __name__ == "__main__":
    game_loop()    
