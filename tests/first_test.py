import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_myltiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calcilate_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 5, 3) == 2

    def test_adding_calculate_correctly(self):
        assert self. calc.adding(self, 10, 5) == 15
