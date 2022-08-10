import unittest

from project.hero import Hero


class HeroTests(unittest.TestCase):

    USERNAME = "Kanye"
    LEVEL = 5
    HEALTH = 100.00
    DAMAGE = 20.00

    def setUp(self):
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test__init(self):
        self.assertEqual(self.USERNAME, self.hero.username)
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(self.HEALTH, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)

    def test__battle_if_same_username(self):
        enemy = Hero(self.USERNAME, 6, 20, 30)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test__battle_if_health_less_or_equal_to_zero(self):
        hero = Hero("Jack", 6, 0, 100)
        enemy = Hero("Random", 6, 20, 30)

        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)
        self.assertEqual(
            "Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test__battle_if_enemy_health_greater_or_equal_to_zero(self):
        enemy_username = "whatever"
        enemy = Hero(enemy_username, 6, 0, 30)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual(
            f"You cannot fight {enemy_username}. He needs to rest", str(ex.exception))

    def test__battle_when_both_heroes_die(self):
        hero = Hero("a", 10, 10, 10)
        enemy = Hero("B", 10, 10, 10)

        result = hero.battle(enemy)
        expected_health = 10 - (10 * 10)

        self.assertEqual("Draw", result)
        self.assertEqual(expected_health, enemy.health)

    def test__battle_when_enemy_dies(self):
        enemy_level, enemy_health, enemy_damage = 5, 100, 10
        enemy = Hero("C", enemy_level, enemy_health, enemy_damage)
        enemy_expected_health = enemy_health - \
            (self.hero.damage * self.hero.level)
        expected_hero_health = self.HEALTH - (enemy_level * enemy_damage) + 5

        result = self.hero.battle(enemy)

        self.assertEqual("You win", result)
        self.assertEqual(enemy_expected_health, enemy.health)
        self.assertEqual(self.LEVEL + 1, self.hero.level)
        self.assertEqual(self.DAMAGE + 5, self.hero.damage)
        self.assertEqual(expected_hero_health, self.hero.health)

    def test__battle_when_hero_dies(self):
        hero_level, hero_health, hero_damage = 5, 100, 10
        hero = Hero("Ligma", hero_level, hero_health, hero_damage)

        self.enemy = Hero("Deez", self.LEVEL, self.HEALTH, self.DAMAGE)

        hero_expected_health = hero_health - \
            (self.enemy.damage * self.enemy.level)
        expected_enemy_health = self.HEALTH - (hero_level * hero_damage) + 5

        result = hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(hero_expected_health, hero.health)
        self.assertEqual(self.LEVEL + 1, self.enemy.level)
        self.assertEqual(self.DAMAGE + 5, self.enemy.damage)
        self.assertEqual(expected_enemy_health, self.enemy.health)

    def test_hero_str_returns_proper_msg(self):
        actual_result = str(self.hero)
        expected_result = f"Hero {self.USERNAME}: {self.LEVEL} lvl\n" \
            f"Health: {self.HEALTH}\n" \
            f"Damage: {self.DAMAGE}\n" \

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
