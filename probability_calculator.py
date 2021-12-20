import random
import copy


# Free code camps Scientific Computing with Python - project Probability Calculator
class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.key = value
            for i in range(value):
                self.contents.append(str(key))

    def draw(self, number_of_balls):
        str_balls = []

        if number_of_balls < len(self.contents):
            for i in range(number_of_balls):
                # index -> [0, len(self.contents[
                index = random.randint(0, len(self.contents) - 1)
                pop = self.contents.pop(index)
                str_balls.append(pop)
        else:
            return self.contents
        return str_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    number_correct = 0

    for i in range(num_experiments):

        # need deepcopy to keep through iterations
        deep_expected_balls = copy.deepcopy(expected_balls)
        deep_hat = copy.deepcopy(hat)
        output = deep_hat.draw(num_balls_drawn)

        for colour in output:
            deep_expected_balls[colour] = deep_expected_balls.get(colour, 0) - 1

        if all(values < 1 for values in deep_expected_balls.values()):
            number_correct += 1

    return number_correct / num_experiments
