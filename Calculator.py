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


class InputType(Enum):
    OPERAND = "OPERAND"
    OPERATOR = "OPERATOR"


class Calculator:
    def __init__(self):
        self.__last_input_type = InputType.OPERATOR
        self.__last_result_value = None
        self.__last_left_operand = None
        self.__last_right_operand = None
        self.__display_text = "0"
        self.__action = CalculateAction.NONE

    def __clear_all(self):
        self.__last_input_type = InputType.OPERATOR
        self.__last_result_value = self.__last_left_operand = self.__last_right_operand = None
        self.__display_text = "0"
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
        elif operator == CalculateAction.EQUAL:
            value = right_operand

        if value is None:
            return None
        if value % 1 == 0:
            return int(value)
        return value

    def get_expression(self, equal_pressed: bool):
        if self.__action == CalculateAction.ALL_CLEAR:
            self.__action = CalculateAction.NONE
            return ""
        if self.__last_result_value is None:
            return ""
        if self.__action == CalculateAction.NONE:
            if not equal_pressed:
                return self.__display_text
            return "{} =".format(self.__last_result_value)
        if not equal_pressed:
            return "{} {}".format(self.__last_result_value, self.__action.value)
        return "{} {} {} =".format(self.__last_left_operand, self.__action.value, self.__last_right_operand)

    def get_display_text(self):
        return self.__display_text

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
        previous_input_type, self.__last_input_type = self.__last_input_type, InputType.OPERATOR
        previous_action = self.__action

        # [AC]
        if operator_character == CalculateAction.ALL_CLEAR.value:
            self.__clear_all()
            self.__action = CalculateAction.ALL_CLEAR
            return
        # [←]
        if operator_character == CalculateAction.BACKSPACE.value:
            self.__last_input_type = InputType.OPERAND
            if self.__display_text == "0":
                return

            value = self.get_value_by_text(self.__display_text)
            if value is None or value == 0:
                self.__display_text = "0"
                return

            self.__display_text = self.__display_text[0:-1]
            if self.__display_text == "" or self.__display_text == "-":
                self.__display_text = "0"
            return

        # [±]
        if operator_character == CalculateAction.PLUS_MINUS.value:
            self.__last_input_type = InputType.OPERAND
            value = self.get_value_by_text(self.__display_text)
            if value is None or value == 0:
                self.__display_text = "0"
                return
            value *= -1
            self.__display_text = str(value)
            return

        # [%]
        if operator_character == CalculateAction.PERCENT.value:
            self.__last_input_type = InputType.OPERAND
            input_value = self.get_value_by_text(self.__display_text)
            if input_value is None or input_value == 0:
                self.__display_text = "0"
                return
            input_value *= 0.01
            self.__display_text = str(input_value)
            return

        # [+] [-] [×] [÷] [=]
        input_value = self.__last_right_operand
        if operator_character == CalculateAction.EQUAL.value:  # [=]
            # keep the previous action
            self.__last_left_operand = self.__last_result_value
            self.__last_right_operand = None
        else:  # [+] [-] [×] [÷]
            try:
                self.__action = CalculateAction(operator_character)
            except Exception as exception:
                print("{}:".format(type(exception).__name__), exception)

            if previous_input_type == InputType.OPERATOR:
                return

        if previous_input_type == InputType.OPERAND or input_value is None:
            input_value = self.get_value_by_text(self.__display_text)
            if input_value is None:
                self.__display_text = "0"
                return

        if self.__last_left_operand is None:
            self.__last_left_operand = input_value
        else:
            self.__last_right_operand = input_value

        self.__last_result_value = self.calculate(previous_action, self.__last_left_operand, self.__last_right_operand)

        # set the display text
        if self.__last_result_value is None:
            self.__display_text = "ERROR"
            self.__action = CalculateAction.NONE
        else:
            self.__display_text = str(self.__last_result_value)

    def input_number(self, number_character):
        last_input_type, self.__last_input_type = self.__last_input_type, InputType.OPERAND

        if last_input_type == InputType.OPERATOR:
            self.__display_text = number_character
        else:
            # the max length is 12
            if len(self.__display_text) > 11:
                return
            if self.__display_text == "0":
                if number_character == ".":
                    self.__display_text += number_character
                else:
                    self.__display_text = number_character
            else:
                # only 1 decimal point
                if "." in self.__display_text and (number_character == "." or not number_character.isdigit()):
                    return
                self.__display_text += number_character

        self.__last_left_operand = self.get_value_by_text(self.__display_text)
        if self.__display_text is None:
            self.__display_text = "0"
