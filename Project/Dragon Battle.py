# =========================
#       GAME STATS
# =========================

import random

# Dragon health
Dragon = 5000
Dragon_max_hp = 5000
# Weapon damage
Mace = 173
Spear = 154
Bow = 89
Ice_magic = 211
# Dragon healing
healed = False
healed2 = False
# Player HP
Player_HP = 500
# Potions
healing_potion = 50
healing_potion_count = 2

heavy_heal_pot = 150
heavy_heal_pot_count = 1

# =========================
#       FUNCTIONS
# =========================

def heal1(healing_potion):
    global Player_HP, healing_potion_count

    Player_HP += healing_potion
    healing_potion_count -= 1

    print(
         f"You used healing potion and healed!"
         f"\nYour health is now: {Player_HP}")

def heal2(heavy_heal_pot):
    global Player_HP, heavy_heal_pot_count

    Player_HP += heavy_heal_pot
    heavy_heal_pot_count -= 1

    print(
         f"You used heavy healing potion and healed!"
         f"\nYour health is now: {Player_HP}")

def attack(weapon_dmg, weapon_hits):
    global Dragon

    for i in range(weapon_hits):
        Dragon -= weapon_dmg

        if Dragon < 0:
            Dragon = 0

        print("Enemy HP:", Dragon)

        if Dragon == 0:
            break

def Dragon_attack(): 
    global Player_HP   
    Dragon_ATK_chance = random.randint(1, 5)
    if Dragon_ATK_chance == 3 or Dragon_ATK_chance == 4:
            Dragon_ATK_dmg = random.randint(10, 200)
            Player_HP -= Dragon_ATK_dmg
            print(f"The dragon attacked you! for {Dragon_ATK_dmg}, you\'re now at {Player_HP}")
    elif Dragon_ATK_chance == 5:
            Dragon_ATK_dmg_crit = random.randint(300, 450)
            Player_HP -= Dragon_ATK_dmg_crit
            print(f"The dragon attacked you! critical!!! {Dragon_ATK_dmg_crit}, you\'re now at {Player_HP}")
    else:
        print(f"the dragon back down... for now... you\'re at {Player_HP}")


# =========================
#       CHOOSE WEAPON
# =========================

while True:

    intro_weapons = input(
        "There's a dragon! It has 5000 HP! Choose your weapon:"
        "\nMace, Spear, Bow, Ice magic"
        "\nYour health is currently 500!"
        "\nYou have 2 healing potions and 1 heavy healing potion."
        "\nYour choice is: "
    ).strip().lower()

    if intro_weapons == "mace":
        weapon_dmg = Mace
        weapon_hits = 3
        break

    elif intro_weapons == "spear":
        weapon_dmg = Spear
        weapon_hits = 3
        break

    elif intro_weapons == "bow":
        weapon_dmg = Bow
        weapon_hits = 5
        break

    elif intro_weapons == "ice magic":
        weapon_dmg = Ice_magic
        weapon_hits = 3
        break

    else:
        print("Invalid... try again!")

# =========================
#       MAIN MENU
# =========================

while Dragon > 0 and Player_HP > 0:
    
    while True:

        inven_choices = input(
            f"\nChoose what you're gonna do next with your {intro_weapons}:"
            "\n1. Attack"
            "\n2. Check inventory"
            "\nYour choice is: "
        ).strip()

        if inven_choices == "1":

            attack(weapon_dmg, weapon_hits)
            if Dragon <= 0:
                print("YOU DEFEATED THE DRAGON!!!!")
                break

            Dragon_attack()

            if Player_HP <= 0:
                break
        elif inven_choices == "2":

            item_inv = input(
                "\nChoose your item:"
                "\n1. Go back to fight"
                "\n2. Light healing potion"
                "\n3. Heavy healing potion"
                "\nYour choice is: "
            )
            if item_inv == "1":
                continue
            
            elif item_inv == "2":
                if healing_potion_count == 0:
                    print("You ran out of this potion!")
                    continue
                else:
                    heal1(healing_potion)
                
            elif item_inv == "3":
                if heavy_heal_pot_count == 0:
                    print("You ran out of this potion!")
                    continue
                else:
                    heal2(heavy_heal_pot)
        
        else:
            print("Invalid option!")


if Player_HP <= 0:
    print("YOU LOST!!!!")


# ==================================================================
# (ORGANIZE WITH THE HELP OF AI)
# ==================================================================
# (This project was written by MXSYZ (me) from scratch)
# (AI assistance was used for debugging and learning purposes only)
# ==================================================================