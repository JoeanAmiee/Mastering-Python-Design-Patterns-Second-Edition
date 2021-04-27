import abc
import urllib.parse
import urllib.request


class ResourceContent:
    """
    定义抽象接口
    维护一个实现者的对象引用
    """

    def __init__(self, imp):
        self._imp = imp

    def show_content(self, path):
        self._imp.fetch(path)


class ResourceContentFetcher(metaclass=abc.ABCMeta):
    """
    为获取内容的实现类定义接口
    """

    @abc.abstractmethod
    def fetch(path):
        pass


class URLFetcher(ResourceContentFetcher):
    """
    实现实现者接口并定义其具体实现
    """

    def fetch(self, path):
        # path is an URL
        req = urllib.request.Request(path)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)


class LocalFileFetcher(ResourceContentFetcher):
    """
    实现实现者接口并定义其具体实现
    """

    def fetch(self, path):
        # path is the filepath to a text file
        with open(path) as f:
            print(f.read())


def main():
    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content('http://python.org')

    print('===================')

    localfs_fetcher = LocalFileFetcher()
    iface = ResourceContent(localfs_fetcher)
    iface.show_content('file.txt')


if __name__ == "__main__":
    main()
