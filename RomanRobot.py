from sys import stdin, exit as sys_exit


class Robot(object):
    def __init__(self):
        """
        This is a class constructor.
        """
        self.robot = {'x': 0, 'y': 0}

    def move_robot(self, direction, amount):
        """
        Calculates where to move the robot depending on directions given.
        Updates global self.robot dictionary.
        """
        if direction == 'right':
            self.robot['x'] += amount
        elif direction == 'left':
            self.robot['x'] -= amount
        elif direction == 'forward':
            self.robot['y'] += amount
        elif direction == 'backward':
            self.robot['y'] -= amount

    def parse_command(self, line):
        """
        Process the command.
        """
        command = line.split()
        length = len(command)

        if length == 1:
            if command[0] == 'distance':
                print(round((self.robot['x'] ** 2 + self.robot['y'] ** 2) ** 0.5))
            elif command[0] == 'exit':
                sys_exit()

        elif length == 2:
            direction, amount = command[0], int(command[1])
            self.move_robot(direction, amount)

    def main(self):
        """
        This is a main method of the class. Entry point.
        """
        for line in stdin:
            self.parse_command(line)


if __name__ == '__main__':

    TEST_ROBOT = Robot()

    try:
        TEST_ROBOT.main()
    except (ValueError, KeyboardInterrupt):
        pass
