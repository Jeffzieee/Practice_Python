class OperatorOverload(object):

    @staticmethod
    def hello(self):
        print("FirstOne")


class Second(OperatorOverload):

    @staticmethod
    def some(self):
        print("hi")


x = Second()
x.hello()
