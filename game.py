from goblin import Goblin
from hero import Hero

ARENA_NAME = "Random ahh stadium"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("THRAGG THE DESTROYER")
    goblin2 = Goblin("bob")
    hero = Hero("Dude Person")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print(f"The hero {hero.name} enters the arena with {hero.health} health.")

    attacknum = hero.attack()
    goblin.take_damage(attacknum)

    
    

if __name__ == "__main__":
    main()
