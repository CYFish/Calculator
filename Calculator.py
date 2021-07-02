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
        self.__last_result_value = None
        self.__last_input_value = None
        self.__value_text = "0"
        self.__action = CalculateAction.NONE

    def __calculate(self):
        try:
            input_value = float(self.__value_text)
        except Exception as exception:
            print("{}:".format(type(exception).__name__), exception)
            self.__value_text = "0"
            return

        if input_value % 1 == 0:
            input_value = int(input_value)

        if self.__action == CalculateAction.ADD:
            self.__last_result_value += input_value
        elif self.__action == CalculateAction.SUBTRACT:
            self.__last_result_value -= input_value
        elif self.__action == CalculateAction.MULTIPLY:
            self.__last_result_value *= input_value
        elif self.__action == CalculateAction.DIVIDE:
            if input_value == 0:
                self.__value_text = "DIVIDED BY 0"
                return
            self.__last_result_value /= input_value
        elif self.__action == CalculateAction.NONE:
            self.__last_result_value = input_value

        if self.__last_result_value % 1 == 0:
            self.__last_result_value = int(self.__last_result_value)
        self.__value_text = str(self.__last_result_value)

    def __clear_all(self):
        self.__last_result_value = self.__last_input_value = None
        self.__value_text = "0"
        self.__action = CalculateAction.NONE

    def get_expression(self):
        if self.__action == CalculateAction.ALL_CLEAR:
            self.__action = CalculateAction.NONE
            return ""
        if self.__action == CalculateAction.NONE:
            return self.__value_text
        return "{} {}".format(self.__last_result_value, self.__action.value)

    def get_value_text(self):
        return self.__value_text

    def input_operator(self, operator_character):
        if operator_character == CalculateAction.ALL_CLEAR.value:
            self.__clear_all()
            self.__action = CalculateAction.ALL_CLEAR
            return

        if operator_character == CalculateAction.BACKSPACE.value:
            if self.__value_text != "0":
                try:
                    value = float(self.__value_text)
                except Exception as exception:
                    print("{}:".format(type(exception).__name__), exception)
                    self.__clear_all()
                    self.__action = CalculateAction.ALL_CLEAR
                    return
                else:
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

        if operator_character == CalculateAction.PERCENT.value:
            try:
                input_value = float(self.__value_text)
            except Exception as exception:
                print("{}:".format(type(exception).__name__), exception)
                self.__value_text = "0"
                return
            if input_value == 0:
                return
            input_value *= 0.01
            self.__value_text = str(input_value)
            return

        if operator_character == CalculateAction.EQUAL.value:
            self.__calculate()
            return

        if self.__action == CalculateAction.NONE:
            self.__last_result_value = float(self.__value_text)
            if self.__last_result_value % 1 == 0:
                self.__last_result_value = int(self.__last_result_value)

        try:
            self.__action = CalculateAction(operator_character)
        except Exception as exception:
            print("{}:".format(type(exception).__name__), exception)

    def input_number(self, number_character):
        if self.__last_result_value != 0:
            self.__value_text = number_character
            return

        if len(self.__value_text) > 14:
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
