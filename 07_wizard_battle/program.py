import random
import time

from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('WIZARD BATTLE')
    print('=============')


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 10),
        Wizard('Evil Wizard', 200)
    ]

    hero = Wizard('Gandolf', 100)

    timeout = 3

    while True:
        active_creature = random.choice(creatures)
        print(active_creature)
        cmd = input('Do you [a]ttack, [r]unaway or [l]ook around? ')

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print(
                    'The wizard runs and hides taking time to recover ({} secs)…'.format(timeout))
                time.sleep(timeout)
                print('The wizard returns revitalized!')
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees 🤔')
        elif cmd == 'l':
            print('The wizard {} takes in surroundings and sees: '.format(hero.name))
            for c in creatures:
                print('* A {} of level {}'.format(c.name, c.level))
        else:
            print('Ok, exiting game… bye!')
            break

        if not creatures:
            print('You have deffeted all creatures 💪!')
            break


if __name__ == "__main__":
    main()
