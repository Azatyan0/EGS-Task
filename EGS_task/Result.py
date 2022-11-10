"""The "Result class was created to store actual and expected results"""


class Result:
    __expected_res = None
    __actual_res = None

    def __repr__(self):
        return f'(actual = {self.__actual_res}, expected = {self.__expected_res})'

    def expected_res_setter(self, exp):
        self.__expected_res = exp

    def expected_res_getter(self):
        return self.__expected_res

    def actual_res_setter(self, actual):
        self.__actual_res = actual

    def actual_res_getter(self):
        return self.__actual_res
