class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        self.test = 'Test value'


def main():
    ''' 
    Init Singleton
    '''
    s1 = Singleton()
    s2 = Singleton()
    print(s1)
    print(s2)
    print(s1 == s2)
    print(s1.test)


if __name__ == "__main__":
    main()
