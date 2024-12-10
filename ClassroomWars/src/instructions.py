def display_instructions():
    print("\n" + "=" * 55)
    print("🎮 Welcome to Classroom Wars: Sino ang Pinakapabibo? 🎓")
    print("=" * 55 + "\n")
    
    print("📖 **Game Objective**:")
    print("Reduce your opponent's health to 0 using strategic moves, skills, and items while managing your stamina and shield. \n")
    
    print("📌 **Getting Started**:")
    print("""
    1. You can play against another player or the computer.
    2. Choose a character with unique abilities. Each character has different strengths and weaknesses.
    3. Stats to watch:
       - **Health**: Your life points. If it hits 0, you lose.
       - **Stamina**: Energy used for skills and items. Don't run out!
       - **Shield**: Protects you by absorbing damage before it affects your health.
    """)
    
    print("📌 **How to Play:**")
    print("""
    - Each player takes turns. During your turn, you can:
      1. **Use a Skill**: Perform an action like attacking, healing, or shielding.
      2. **Use an Item**: Buff yourself, deal damage, or recover stamina.
      3. **Surrender**: If you can't continue, you can give up the match.
      
    - Plan your moves wisely:
      - Use attacks to reduce your opponent's shield or health.
      - Defend yourself with shields or recover with healing skills.
      - Conserve stamina! Without stamina, you can't act.
    """)

    print("📌 **Rules:**")
    print("""
    1. Players cannot pick the same character. If the computer selects randomly, it ensures it's different.
    2. Damage goes to the shield first before affecting health.
    3. Items also consume stamina, so use them carefully.
    4. The game ends when one player's health reaches 0 or someone surrenders.
    """)

    print("📌 **Sample Turn Flow:**")
    print("""
    Player 1's Turn:
    - Health: 80, Shield: 20, Stamina: 60.
    - Uses the skill "Power Punch" (Deals 25 damage, costs 20 stamina).
    - Opponent's shield absorbs 20 damage, remaining 5 damage reduces their health.

    Player 2's Turn:
    - Health: 75, Shield: 0, Stamina: 50.
    - Uses an item "Shield Potion" (Adds 30 shield, costs 15 stamina).
    """)

    print("💡 **Tips for Success:**")
    print("""
    1. Conserve stamina for key actions.
    2. Balance offense and defense.
    3. Use skills and items that complement your strategy.
    4. Pay attention to your opponent's stats to predict their moves.
    5. Don't forget to heal or shield when needed!
    """)

    print("=" * 55)
    print("Have fun and may the best player win! 🎉\n")
