# 一款儿童游戏，一款成人游戏。我们将根据用户的输入，在运行时决定创建和启动哪款游戏。
# 抽象工厂会负责游戏创建的部分。

# Frog game
# 男主角是一只喜欢吃虫子的青蛙。
class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    # 描述青蛙与障碍物（例如，虫子、谜题和其他青蛙）的交互。
    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Frog encounters {obstacle} and {act}!'
        print(msg)


# 障碍物只能是一只虫子。当遇到一只虫子时，青蛙只支持一种行为——吃掉虫子。
class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


# FrogWorld类是一个抽象工厂。它的主要任务是创建游戏中的主角与障碍物。
# 保持创建方法的独立性及名称的通用性（例如，make_character()和make_obstacle()）
class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Frog World -------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


# Wizard game
# 巫师与怪物（如orks兽人）战斗，而不是吃虫子。
class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Wizard battles against {obstacle} and {act}!'
        print(msg)


class Ork:
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard World -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


# Game environment
# 游戏的主入口。它接受一个工厂作为输入，并使用它来创建游戏世界。
class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    # 初始化主角与障碍物之间的交互。
    def play(self):
        self.hero.interact_with(self.obstacle)


# 提示用户给出一个有效的年龄。
def validate_age(name):
    try:
        age = input(f'Welcome {name}. How old are you? ')
        age = int(age)
    except ValueError as err:
        print(f"Age {age} is invalid, please try again...")
        return False, age
    return True, age


# 询问用户的姓名和年龄，并根据用户的年龄决定应该玩哪款游戏。
def main():
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
