class ZombieIsDead(Exception):
    """Raised when, for some reason, zombie cannot attack (e.g. it's dead)"""


class TooLittleHealth(Exception):
    """Raised when zombie has too little health for an action"""


class Zombie(object):
    """A zombie, able to attack other zombies and boost its power"""
    health = None  # 0-100
    power = None  # 1-10
    tmp_power = None
    berserk_used = None

    def __init__(self, power=5):
        self.health = 100
        self.power = power
        self.tmp_power = 0
        self.berserk_used = False

    @property
    def is_dead(self):
        """Indicates whether zombie is dead (truly dead)"""
        return self.health <= 0

    def attack(self, another):
        """Attacks another zombie"""
        if self.is_dead:
            raise ZombieIsDead('This zombie is dead')
        if another.is_dead:
            raise ZombieIsDead('There\'s no point in fighting dead zombie')
        damage = self.power
        if self.tmp_power:
            damage += self.tmp_power
            self.tmp_power = 0
        if self.health < 5 and not self.berserk_used:
            self.berserk_used = True
            damage *= 2
        another.health -= damage
        # Other zombie retaliates
        if not another.is_dead:
            self.health -= int(round(2.0 * another.power / 3.0))

    def boost(self, amount):
        """Converts some health into raw zombie power"""
        if self.is_dead:
            raise ZombieIsDead
        health_to_convert = amount * 3
        if self.health <= health_to_convert:
            raise TooLittleHealth
        self.health -= health_to_convert
        self.tmp_power += amount
