def main():
    cassandra = Warrior()
    sera = Rogue()
    vivienne = Mage()
    print('Cassandra is in your party:')
    for character in (cassandra, sera, vivienne):
        in_fight(character)


class Character:
    def active(self):
        return self.strings['active']

    def passive(self):
        return self.strings['passive']


class Warrior(Character):
    strings = dict(
        active = 'melee weapon',
        passive = 'heavy armor',
    )


class Rogue(Character):
    strings = dict(
        active = 'projectile weapon',
        passive = 'stealth',
    )


class Mage(Character):
    strings = dict(
        active = 'staff',
        passive = 'buff spell',
    )


def in_fight (character):
    print(character.active())
    print(character.passive())


if __name__ == '__main__': main()