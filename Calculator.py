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

    def __clear_all(self):
        self.__last_result_value = self.__last_input_value = None
        self.__value_text = "0"
        self.__action = CalculateAction.NONE

    @staticmethod
    def calculate(operator: CalculateAction, left_operand: float, right_operand: float):
        value = None
        if operator == CalculateAction.ADD:
            value = left_operand + right_operand
        elif operator == CalculateAction.SUBTRACT:
            value = left_operand - right_operand
        elif operator == CalculateAction.MULTIPLY:
            value = left_operand * right_operand
        elif operator == CalculateAction.DIVIDE:
            if right_operand == 0:
                return None
            value = left_operand / right_operand
        elif operator == CalculateAction.NONE:
            value = right_operand

        if value % 1 == 0:
            return int(value)
        return value

    def get_expression(self):
        if self.__action == CalculateAction.ALL_CLEAR:
            self.__action = CalculateAction.NONE
            return ""
        if self.__action == CalculateAction.NONE:
            return self.__value_text
        return "{} {}".format(self.__last_result_value, self.__action.value)

    def get_value_text(self):
        return self.__value_text

    @staticmethod
    def get_value_by_text(value_text: str):
        try:
            value = float(value_text)
        except Exception as exception:
            print("{}:".format(type(exception).__name__), exception)
            return None

        if value % 1 == 0:
            return int(value)
        return value

    def input_operator(self, operator_character):
        if operator_character == CalculateAction.ALL_CLEAR.value:
            self.__clear_all()
            self.__action = CalculateAction.ALL_CLEAR
            return

        if operator_character == CalculateAction.BACKSPACE.value:
            if self.__value_text == "0":
                return

            value = self.get_value_by_text(self.__value_text)
            if value is None or value == 0:
                self.__value_text = "0"
                return

            self.__value_text = self.__value_text[0:-1]
            if self.__value_text == "" or self.__value_text == "-":
                self.__value_text = "0"
            return

        if operator_character == CalculateAction.PLUS_MINUS.value:
            value = self.get_value_by_text(self.__value_text)
            if value is None or value == 0:
                self.__value_text = "0"
                return
            value *= -1
            self.__value_text = str(value)
            return

        if operator_character == CalculateAction.PERCENT.value:
            input_value = self.get_value_by_text(self.__value_text)
            if input_value is None or input_value == 0:
                self.__value_text = "0"
                return
            input_value *= 0.01
            self.__value_text = str(input_value)
            return

        if operator_character == CalculateAction.EQUAL.value:
            # clear the last input value (the operand at the right hand side of the operator)
            self.__last_input_value = None

            input_value = self.get_value_by_text(self.__value_text)
            if input_value is None:
                self.__value_text = "0"
                return

            self.__last_result_value = self.calculate(self.__action, self.__last_result_value, input_value)

            if self.__last_result_value is None:
                self.__value_text = "ERROR"

            self.__value_text = str(self.__last_result_value)
            return

        if self.__action == CalculateAction.NONE:
            self.__last_result_value = self.get_value_by_text(self.__value_text)

        try:
            self.__action = CalculateAction(operator_character)
        except Exception as exception:
            print("{}:".format(type(exception).__name__), exception)

    def input_number(self, number_character):
        # bug: 輸入完運算符號 (operator) 後，再繼續輸入數字，未能清空上一個數字

        if self.__last_input_value is None:
            self.__value_text = number_character
        else:
            # the max length is 12
            if len(self.__value_text) > 11:
                return
            if self.__value_text == "0":
                if number_character == ".":
                    self.__value_text += number_character
                else:
                    self.__value_text = number_character
            else:
                # only 1 decimal point
                if "." in self.__value_text and (number_character == "." or not number_character.isdigit()):
                    return
                self.__value_text += number_character

        self.__last_input_value = self.get_value_by_text(self.__value_text)
        if self.__value_text is None:
            self.__value_text = "0"
