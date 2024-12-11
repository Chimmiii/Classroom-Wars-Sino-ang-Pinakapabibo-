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
            "Varsity Walk": {"type": "attack", "damage": (10, 15), "stamina_cost": 25, "description": "Dodges the opponent's attack gracefully."},
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
