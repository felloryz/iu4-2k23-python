from dataclasses import dataclass


@dataclass
class Function:
    line_number: int
    name_function: str
    value_function: str
    variable_function: dict  # ключ - имя переменной, значение - тип переменной




class ParsFunction:

    # функции, достающие из строки нужные элементы (имя функции, возвращаемый тип и т.д.)
    def get_line(self, funct_line: str) -> int:
        ...
        return 0

    def get_name(self, funct_line: str) -> str:
        ...
        return ''

    def get_value(self, funct_line: str) -> str:
        ...
        return ''

    def get_variable(self, funct_line: str) -> str:
        ...
        return ''

    # проверка, подходит ли данная строчка для разбиения
    def line_function(self) -> bool:
        ...
        return True

    # метод, по результату проверки раскидывающий аргументы из строчки
    # на вход значение проверки, сама строчкА, номер этой строки
    # возвращает собранный экземпляр (не уверена в данном методе)
    def line_parse(self, exam: bool, line: str, num: int):
        ...
        return Function