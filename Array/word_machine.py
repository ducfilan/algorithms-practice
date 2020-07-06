from enum import Enum


class OperationTypes(Enum):
    NUMBER = 1,
    POP = 2,
    DUP = 3,
    ADD = 4,
    SUB = 5


class Operation(object):
    def _is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def __init__(self, operation_str):
        if self._is_number(operation_str):
            self.operation_type = OperationTypes.NUMBER
            int_value = int(operation_str)

            if int_value < 0 or int_value > (pow(2, 20) - 1):
                raise ValueError('Value must be 20-bit unsigned interger!')

            self.value = int_value

        elif operation_str == 'POP':
            self.operation_type = OperationTypes.POP

        elif operation_str == 'DUP':
            self.operation_type = OperationTypes.DUP

        elif operation_str == '+':
            self.operation_type = OperationTypes.ADD

        elif operation_str == '-':
            self.operation_type = OperationTypes.SUB

        else:
            raise ValueError('Invalid value!')


class OperationParser(object):
    def __init__(self, operations_str):
        self._operations_str = operations_str

    def parse(self):
        return map(lambda operation_str: Operation(operation_str), self._operations_str.split())


class WordMachine(object):
    def __init__(self, operations_str):
        self._operations = OperationParser(operations_str).parse()
        self._stack = []
        self._upper_limit = pow(2, 20) - 1
        self._lower_limit = 0

    def _is_value_overflow(self, num):
        return num < self._lower_limit or num > self._upper_limit

    def _push(self, value):
        self._stack.append(value)

    def _pop(self):
        return self._stack.pop()

    def _dup(self):
        if len(self._stack) == 0:
            raise Exception('Empty stack!')

        self._stack.append(self._stack[-1])

    def _add(self):
        if len(self._stack) < 2:
            raise Exception('Not enough values!')

        topmost_element_1 = self._pop()
        topmost_element_2 = self._pop()
        sum_2_topmost_elements = topmost_element_1 + topmost_element_2

        if self._is_value_overflow(sum_2_topmost_elements):
            raise Exception('Value is overflowed!')

        self._push(sum_2_topmost_elements)

    def _sub(self):
        if len(self._stack) < 2:
            raise Exception('Not enough values!')

        topmost_element_1 = self._pop()
        topmost_element_2 = self._pop()
        sub_2_topmost_elements = topmost_element_1 - topmost_element_2

        if self._is_value_overflow(sub_2_topmost_elements):
            raise Exception('Value is overflowed!')

        self._push(sub_2_topmost_elements)

    def do_process(self):
        for operation in self._operations:
            if operation.operation_type == OperationTypes.NUMBER:
                self._push(operation.value)

            elif operation.operation_type == OperationTypes.POP:
                self._pop()

            elif operation.operation_type == OperationTypes.DUP:
                self._dup()

            elif operation.operation_type == OperationTypes.ADD:
                self._add()

            elif operation.operation_type == OperationTypes.SUB:
                self._sub()

        return self._pop()

def solution(S):
    try:
        word_machine = WordMachine(S)
        return word_machine.do_process()
    except:
        return -1


print(solution('13 DUP 4 POP 5 DUP + DUP + -'))
