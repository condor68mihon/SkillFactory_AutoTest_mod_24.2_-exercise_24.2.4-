# SkillFactory_AutoTest_mod_24.2_-exercise_24.2.4
Positive tests for each calculator method (exercise_24.2.4)

1.Создан новый проект с необходимыми директориями и файлами.
2.Написано по одному позитивному тесту для каждого метода калькулятора.

Методы калькулятора:
- adding # проверка сложения
- division # проверка деления
- multiply # проверка умножения
- subtraction # проверка вычитания

Файл с кодом калькулятора создан в корневом каталоге, в папке app под названием calculator:
  from app.calculator import Calculator

Файл с тестами создан в корневом каталоге, в папке tests под названием test.py:

   В методе setup реализуются приготовления для запуска тестов: настройка окружения, подготовка тестовых данных, инициализация соединения с БД и т.д.. 

Архитектура файла с тестами: внутри модуля объявляются
  предварительный шаг setup: Инициализируем приложение калькулятор:
    def setup(self):
        self.calc = Calculator

  функции тестов:
    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2  # проверка сложения

    def test_division_success(self):
        assert self.calc.division(self, 6, 2) == 3  # проверка деления

    def test_multiply_success(self):
        assert self.calc.multiply(self, 5, 9) == 45  # проверка умножения

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 7, 3) == 4  # проверка вычитания

  окончательный шаг teardown: Выполняется даже в случае неудачи и используется, например, для освобождения внешних ресурсов
    def teardown(self):
        print('Выполнение метода Teardown')

  Запускаем тесты (варианты):
  - из среды разработки PyCharm, кликнув зелёную кнопку Run на панели управления
  - из командной строки/терминала. Для этого переходим в папку с  тестами и пишем команду
     pytest test_24_2_4.py
  
  Отчёт PyTest о результатах выполнения тестов:
  - успешно пройденный тест отмечен зелёным цветом
  - тест с ошибкой — красным, как и место возникновения ошибки
  - результат, возвращаемый функцией
  
