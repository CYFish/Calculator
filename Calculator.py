from enum import Enum


class CalculateAction(Enum):
    NONE = "NONE"
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "×"
    DIVIDE = "÷"
    PERCENT = "%"
    PLUS_MINUS = "±"
    BACKSPACE = "←"
    ALLCLEAR = "AC"
    EQUAL = "="


class Calculator:
    def __init__(self):
        self.__last_value = 0
        self.__value = 0
        self.__value_text = "0"
        self.__action = CalculateAction.NONE

    def __set_value_by_text(self):
        if self.__value_text == "ERROR":
            self.__value = 9999999999
        else:
            self.__value = float(self.__value_text)

    def __set_text_by_value(self):
        if self.__value == 9999999999:
            self.__value_text = "ERROR"
        else:
            self.__value_text = str(self.__value)

    def __calculate(self):
        if self.__value_text == "ERROR":
            self.__value_text = "0"
        input_value = float(self.__value_text)
        if input_value % 1 == 0:
            input_value = int(input_value)

        if self.__action == CalculateAction.ADD:
            self.__last_value += input_value
        elif self.__action == CalculateAction.SUBTRACT:
            self.__last_value -= input_value
        elif self.__action == CalculateAction.MULTIPLY:
            self.__last_value *= input_value
        elif self.__action == CalculateAction.DIVIDE:
            self.__last_value /= input_value
        elif self.__action == CalculateAction.NONE:
            self.__last_value = input_value

        if self.__last_value % 1 == 0:
            self.__last_value = int(self.__last_value)
        self.__value_text = str(self.__last_value)

    def __clear_all(self):
        self.__last_value = self.__value = 0
        self.__value_text = "0"
        self.__action = CalculateAction.NONE

    def get_value_text(self):
        return self.__value_text

    def get_value(self):
        return self.__value

    def input_operator(self, operator_character):
        if operator_character == CalculateAction.BACKSPACE.value:
            if self.__value_text != "0":
                self.__value_text = self.__value_text[0:-1]
            if self.__value_text == "":
                self.__value_text = "0"
            return

        if operator_character == CalculateAction.EQUAL.value:
            self.__calculate()
            return
        if operator_character == CalculateAction.EQUAL.ALLCLEAR:
            self.__clear_all()
            return

        if self.__action == CalculateAction.NONE:
            self.__last_value = float(self.__value_text)
            if self.__last_value % 1 == 0:
                self.__last_value = int(self.__last_value)

        try:
            self.__action = CalculateAction(operator_character)
        except Exception as error_message:
            print("{}:".format(type(error_message).__name__), error_message)

    def input_number(self, number_character):
        if self.__last_value != 0:
            self.__value_text = number_character
            return

        if len(self.__value_text) > 8:
            return
        if self.__value_text == "0":
            if number_character == ".":
                self.__value_text += number_character
            else:
                self.__value_text = number_character
        else:
            if self.__value % 1 != 0 and (number_character == "." or not number_character.isdigit()):
                return
            self.__value_text += number_character
        self.__set_value_by_text()

    def plus_minus(self):
        self.multiply(-1)