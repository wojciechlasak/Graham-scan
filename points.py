# -*- coding: utf-8 -*-
import math

class Point:
    """
    Klasa reprezentująca punkty na płaszczyźnie
    """

    def __init__(self, x, y):
        """
        Konstruktor
        """
        self.x = x
        self.y = y
   
    def __str__(self):
        """
        Reprezentacja jako string
        """
        return "({},{})".format(self.x, self.y)
    def __repr__(self):
        """
        Reprezentacja jako string
        """
        return "Point({},{})".format(self.x, self.y)
    
    def __eq__(self, other):
        """
        Porownanie
        """
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        """
        Dodawanie punktow
        """
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Odejmowanie punktow
        """
        return Point(self.x - other.x, self.y - other.y)

    def length(self):
        """
        Dlugosc wektora
        """
        return math.sqrt(self.x*self.x + self.y*self.y)
        

