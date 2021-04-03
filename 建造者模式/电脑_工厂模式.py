MINI14 = '1.4GHz Mac mini'


class AppleFactory:
    class MacMini14:  # 禁止类直接实例化的简洁方法
        def __init__(self):
            self.memory = 4  # 以GB为单位
            self.hdd = 500  # 以GB为单位
            self.gpu = 'Intel HD Graphics 5000'

        def __str__(self):
            info = (f'Model: {MINI14}',
                    f'Memory: {self.memory}GB',
                    f'Hard Disk: {self.hdd}GB',
                    f'Graphics Card: {self.gpu}')
            return '\n'.join(info)

    def build_computer(self, model):
        if model == MINI14:
            return self.MacMini14()
        else:
            print(f"I don't know how to build {model}")


if __name__ == '__main__':
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI14)
    print(mac_mini)
