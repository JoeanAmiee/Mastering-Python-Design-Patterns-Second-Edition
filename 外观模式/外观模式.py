from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State', 'new running sleeping restart zombie')


class User:
    pass


class Process:
    pass


class File:
    pass


class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):
    def __init__(self):
        """初始化文件服务器所需的操作"""
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print(f'booting the {self}')
        '''启动文件服务器所需的操作'''
        self.state = State.running

    def kill(self, restart=True):
        print(f'Killing {self}')
        '''终止文件服务器所需的操作'''
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        """检查权限、用户权限等的有效性。"""
        print(
            f"trying to create the file '{name}' for user '{user}' with permissions {permissions}")


class ProcessServer(Server):
    def __init__(self):
        """初始化进程服务器所需的操作"""
        self.name = 'ProcessServer'
        self.state = State.new

    def boot(self):
        print(f'booting the {self}')
        '''启动进程服务器所需的操作'''
        self.state = State.running

    def kill(self, restart=True):
        print(f'Killing {self}')
        '''终止进程服务器所需的操作'''
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        """检查用户权限，生成PID等。"""
        print(f"trying to create the process '{name}' for user '{user}'")


class WindowServer:
    pass


class NetworkServer:
    pass


class OperatingSystem:
    """外观"""

    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)


def main():
    os = OperatingSystem()
    os.start()
    os.create_file('foo', 'hello', '-rw-r-r')
    os.create_process('bar', 'ls /tmp')


if __name__ == '__main__':
    main()
