import unittest
from RomanRobot import Robot


class TestRomanRobot(unittest.TestCase):

    def setUp(self):
        self.test_robot = Robot()

    def test_moving_robot_left(self):
            self.test_robot.move_robot('left', 90)
            self.assertEqual(self.test_robot.robot['x'], -90)

    def test_moving_robot_backward(self):
            self.test_robot.move_robot('backward', 10)
            self.assertEqual(self.test_robot.robot['y'], -10)


if __name__ == '__main__':
    unittest.main()