from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def no_of_sides(self):
        pass


class Rectangle(Polygon):

    def no_of_sides(self):
        print("4 sides")


class OperatorOverload(object):

    @staticmethod
    def hello(self):
        print("FirstOne")


class Second(OperatorOverload):

    @staticmethod
    def some(self):
        print("hi")


r = Rectangle()
r.no_of_sides()
