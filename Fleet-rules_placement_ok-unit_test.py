import unittest
import Fleet
import Ship
import Coordinate


class MyTestCase(unittest.TestCase):
    def test_blocking_ships(self):
        fleet = Fleet.Fleet
        
        current_ship_position = Coordinate.Coordinate(1, 1)
        current_ship = Ship.Ship("B", "H", current_ship_position)

        test_ship_position = Coordinate.Coordinate(1, 1)
        test_ship = Ship.Ship("B", "H", test_ship_position)
        
        self.assertFalse(fleet.rules_placement_ok(current_ship, test_ship), msg="Ship blocking check does not work")

    def test_not_blocking_ships(self):
        fleet = Fleet.Fleet

        current_ship_position = Coordinate.Coordinate(1, 1)
        current_ship = Ship.Ship("B", "H", current_ship_position)

        test_ship_position = Coordinate.Coordinate(3, 3)
        test_ship = Ship.Ship("B", "H", test_ship_position)

        self.assertTrue(fleet.rules_placement_ok(current_ship, test_ship), msg="Ship not blocking check does not work")
        """"""


if __name__ == '__main__':
    unittest.main()
