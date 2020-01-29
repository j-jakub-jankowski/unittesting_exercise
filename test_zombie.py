import unittest
from scripts import zombie


class TestZombie(unittest.TestCase):
    def setUp(self):
        # create healthy, typical zombie
        self.healthy_zombie_1 = zombie.Zombie()
        self.healthy_zombie_2 = zombie.Zombie()
        # create dead zombie health = 0
        self.dead_zombie = zombie.Zombie()
        self.dead_zombie.health = 0
        # create berserk zombie health = 4
        self.berserk_zombie = zombie.Zombie()
        self.berserk_zombie.health = 4

    def test_attacking_zombie_is_dead(self):
        self.assertRaises(zombie.ZombieIsDead, self.dead_zombie.attack, self.healthy_zombie_1)

    def test_another_zombie_is_dead(self):
        self.assertRaises(zombie.ZombieIsDead, self.healthy_zombie_1.attack, self.dead_zombie)

    def test_normal_attack(self):
        self.healthy_zombie_1.attack(self.healthy_zombie_2)
        # zombie_2 attack = round(2.0 * 5 / 3.0) ~~ 3
        self.assertEqual(self.healthy_zombie_1.health, 97)
        # zombie_1 attack = power = 5
        self.assertEqual(self.healthy_zombie_2.health, 95)

    def test_berserk_attack(self):
        self.berserk_zombie.attack(self.healthy_zombie_1)
        self.assertEqual(self.healthy_zombie_1.health, 90)

    def test_boost_attack_but_too_little_health(self):
        self.assertRaises(zombie.TooLittleHealth, self.berserk_zombie.boost, 50)

    def test_boost_power(self):
        self.healthy_zombie_1.boost(20)
        self.assertEqual(self.healthy_zombie_1.tmp_power, 20)
        self.assertEqual(self.healthy_zombie_1.health, 40)

    def test_kill_zombie(self):
        self.healthy_zombie_1.boost(20)
        self.healthy_zombie_1.attack(self.berserk_zombie)
        # attack = 25 so 4-25 = -21
        self.assertEqual(self.berserk_zombie.health, -21)
        self.assertTrue(self.berserk_zombie.is_dead)

    # it is possible to attack yourself !!!
    def test_self_attack(self):
        self.healthy_zombie_1.attack(self.healthy_zombie_1)
        # first attack is made with damage = 5, second "retaliates" with damage =3
        self.assertEqual(self.healthy_zombie_1.health, 92)


if __name__ == '__main__':
    unittest.main()


