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
    ALL_CLEAR = "AC"
    EQUAL = "="


class Calculator:
    def __init__(self):
        self.__last_value = None
        self.__value_text = "0"
        self.__action = CalculateAction.NONE

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
        self.__last_value = None
        self.__value_text = "0"
        self.__action = CalculateAction.NONE

    def get_expression(self):
        if self.__action == CalculateAction.ALL_CLEAR:
            return ""
        if self.__action == CalculateAction.NONE:
            return self.__value_text
        return "{} {}".format(self.__last_value, self.__action.value)
        # if self.__last_value is None:
        #     return "{} {}".format(self.__last_value, self.__action.value)
        # return "{} {} =".format(self.__last_value, self.__action.value, self.__value_text)

    def get_value_text(self):
        return self.__value_text

    def input_operator(self, operator_character):
        if operator_character == CalculateAction.BACKSPACE.value:
            if self.__value_text != "0":
                self.__value_text = self.__value_text[0:-1]
            if self.__value_text == "":
                self.__value_text = "0"
            return

        if operator_character == CalculateAction.PLUS_MINUS.value:
            if self.__value_text == 0:
                return
            value = float(self.__value_text)
            if value % 1 == 0:
                value = int(value)
            value *= -1
            self.__value_text = str(value)
            return

        if operator_character == CalculateAction.EQUAL.value:
            self.__calculate()
            return
        if operator_character == CalculateAction.EQUAL.ALL_CLEAR:
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
            value = float(self.__value_text)
            if value % 1 != 0 and (number_character == "." or not number_character.isdigit()):
                return
            self.__value_text += number_character
