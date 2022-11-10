""" The "Time" class was created to test for valid seconds, minutes, and hours.

    The "hour_checker" method to check if the hours are correct.

    The "minute_checker" method to check if the minutes are correct.

    The "second_checker" method to check if the seconds are correct.

"""


class Time:
    __second = None
    __minute = None
    __hour = None

    def __second_checker(self, second):
        if int(second) not in range(60):
            return False
        else:
            return True

    def second_setter(self, set_second):
        if self.__second_checker(set_second):
            self.__second = set_second
        else:
            print("Not Valid Second")

    def second_getter(self):
        return self.__second

    # function to check if the minute is valid
    def __minute_checker(self, minute):
        if int(minute) not in range(60):
            return False
        else:
            return True

    def minute_setter(self, set_minute):
        if self.__minute_checker(set_minute):
            self.__minute = set_minute
        else:
            print("Not Valid Minute")

    def minute_getter(self):
        return self.__minute

    def __hour_checker(self, hour):
        if int(hour) not in range(24):
            return False
        else:
            return True

    def hour_setter(self, set_hour):
        if self.__hour_checker(set_hour):
            self.__hour = set_hour
        else:
            print("Not Valid Year")

    def hour_getter(self):
        return self.__hour
