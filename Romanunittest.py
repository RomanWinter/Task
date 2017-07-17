import unittest
from RomanRobot import Robot


class TestRomanRobot(unittest.TestCase):
    def setUp(self):
        self.test_robot = Robot()

    def test_if_value_error_raised(self):
        with self.assertRaises(ValueError):
            self.test_robot.parse_command("forward forward")

    def test_nothing_happens_on_wrong_command(self):
        """
        This is to ensure robot won't move on wrong command:
        """
        self.test_robot.parse_command("lallalala")
        self.assertEqual(self.test_robot.robot, {'x': 0, 'y': 0})

    def test_nothing_happens_on_wrong_command_2(self):
        """
        This is to ensure robot won't move on wrong command:
        """
        self.test_robot.parse_command("this is not a command")
        self.assertEqual(self.test_robot.robot, {'x': 0, 'y': 0})

    def test_moving_robot_forward(self):
        self.test_robot.move_robot('forward', 0)
        self.assertIsNot(self.test_robot.robot['y'], 10)

    def test_moving_robot_backward(self):
        self.test_robot.move_robot('backward', 2)
        self.assertIsNot(self.test_robot.robot['y'], 0)

    def test_moving_robot_forward_100(self):
        self.test_robot.move_robot('forward', 100)
        self.assertEqual(self.test_robot.robot['y'], 100)

    def test_moving_robot_right(self):
        self.test_robot.move_robot('right', 50)
        self.assertEqual(self.test_robot.robot['x'], 50)

    def test_moving_robot_left_90(self):
        self.test_robot.move_robot('left', 90)
        self.assertEqual(self.test_robot.robot['x'], -90)

    def test_moving_robot_backward_10(self):
        self.test_robot.move_robot('backward', 10)
        self.assertEqual(self.test_robot.robot['y'], -10)

    def test_moving_robot_forward_90(self):
        self.test_robot.move_robot('forward', 100)
        self.assertNotEqual(self.test_robot.robot['y'], 90)

    def test_moving_robot_backward__10(self):
        self.test_robot.move_robot('backward', 10)
        self.assertNotEqual(self.test_robot.robot['y'], 10)

    def test_moving_robot_forward_99(self):
        self.test_robot.move_robot('forward', 100)
        self.assertIsNotNone(self.test_robot.robot['y'], 99)

    def test_moving_robot_backward_5(self):
        self.test_robot.move_robot('backward', 5)
        self.assertIsNotNone(self.test_robot.robot['y'], 4)

    def test_test_robot_SystemExit(self):
        self.assertRaises(SystemExit)


if __name__ == '__main__':
    unittest.main()
