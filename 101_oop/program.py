class MyObject:
    def __init__(self):
        self.__attribute = 0

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        if value < 10:
            self.__attribute = value


def main():
    obj = MyObject()
    print(obj.attribute)
    obj.attribute = 6
    print(obj.attribute)
    obj.attribute = 15
    print(obj.attribute)
    obj.attribute = 2
    print(obj.attribute)


if __name__ == "__main__":
    main()
