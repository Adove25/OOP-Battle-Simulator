from goblin import Goblin
from hero import Hero

ARENA_NAME = "Random ahh stadium"
def battle(hero: Hero, enemy: Goblin,enemy2: Goblin):
    while hero.is_alive() and (enemy.is_alive() or enemy2.is_alive()):
        attacknum = hero.attack()
        print(f"{hero.name} attacks!" )
        if enemy.is_alive():
            enemy.take_damage(attacknum)
        if enemy.is_alive():
            attacknum = hero.attack()
            enemy2.take_damage(attacknum)
        if enemy.is_alive() or enemy2.is_alive():
            if enemy.is_alive():
                print(f"the goblin {enemy.name} attacks!")
                attacknum = enemy.attack()
                hero.take_damage(attacknum)
            if enemy2.is_alive():
                print(f"the goblin {enemy2.name} attacks!")
                attacknum = enemy2.attack()
                hero.take_damage(attacknum)
    if hero.is_alive():
        print(f"{hero.name} Has won!")
    else:
        print(f"{enemy.name} and {enemy2.name} have won!")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"The crowd is going wild in {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates open and...")

    goblin = Goblin("THRAGG THE DESTROYER")
    goblin2 = Goblin("bob")
    hero = Hero("Dude Person")

    print(f"{goblin.name} enters the arena with {goblin.health} health!")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health!")
    print(f"The hero {hero.name} enters the arena with {hero.health} health!")
    battle(hero,goblin,goblin2)

    
    

if __name__ == "__main__":
    main()
