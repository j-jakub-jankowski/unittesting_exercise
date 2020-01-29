import unittest
from scripts import zombie_with_corrections


class TestZombie(unittest.TestCase):
    def setUp(self):
        # create healthy, typical zombie
        self.healthy_zombie_1 = zombie_with_corrections.Zombie()
        self.healthy_zombie_2 = zombie_with_corrections.Zombie()
        # create dead zombie health = 0
        self.dead_zombie = zombie_with_corrections.Zombie()
        self.dead_zombie.health = 0
        # create berserk zombie health = 4
        self.berserk_zombie = zombie_with_corrections.Zombie()
        self.berserk_zombie.health = 4

    def test_self_attack(self):
        self.assertRaises(zombie_with_corrections.ZombieSelfAttack, self.healthy_zombie_1.attack, self.healthy_zombie_1)


if __name__ == '__main__':
    unittest.main()
