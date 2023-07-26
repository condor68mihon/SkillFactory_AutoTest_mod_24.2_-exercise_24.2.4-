from app.calculator import Calculator


class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2  # проверка сложения

    def test_division_success(self):
        assert self.calc.division(self, 6, 2) == 3  # проверка деления

    def test_multiply_success(self):
        assert self.calc.multiply(self, 5, 9) == 45  # проверка умножения

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 7, 3) == 4  # проверка вычитания

    def teardown(self):
        print('Выполнение метода Teardown')
