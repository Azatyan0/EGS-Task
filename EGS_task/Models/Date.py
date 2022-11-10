""" The "Date" class was created to test for valid days, months, and years.

    The "day_checker" method to check if the days are correct, here I took into account cases where each month has a certain
    number of days and a leap year that affects the number of days in February.

    The "month_checker" method to check if the months are correct.

    The "year_checker" method to check if the years are correct.

    The "is_leap_year" method to check if year is a leap year or not
"""


class Date:
    __day = None
    __month = None
    __year = None

    def __day_checker(self, day):
        if self.__month is None or self.__year is None:
            return False
        if int(self.__month) == 2:
            if self.__is_leap_year(int(self.__year)):
                return bool(int(day) <= 29)
            else:
                return bool(int(day) <= 28)
        else:
            if int(self.__month) in [1, 3, 5, 7, 8, 10, 12] and int(day) > 31:
                return False
            elif int(self.__month) in [4, 6, 9, 11] and int(day) > 30:
                return False
            else:
                return True

    def day_setter(self, set_day):
        if self.__day_checker(set_day):
            self.__day = set_day
        else:
            print("Not Valid Day")

    def day_getter(self):
        return self.__day

    def __month_checker(self, month):
        if int(month) not in range(1, 13):
            return False
        else:
            return True

    def month_setter(self, set_month):
        if self.__month_checker(set_month):
            self.__month = set_month
        else:
            print("Not Valid Month")

    def month_getter(self):
        return self.__month

    def __year_checker(self, year):
        year = year
        if int(year) not in range(2024):
            return False
        else:
            return True

    def year_setter(self, set_year):
        if self.__year_checker(set_year):
            self.__year = set_year
        else:
            print("Not Valid Year")

    def year_getter(self):
        return self.__year

    def __is_leap_year(self, year):
        year_int = int(year)
        if (year_int % 400 == 0) and (year_int % 100 == 0):
            return True
        elif (year_int % 4 == 0) and (year_int % 100 != 0):
            return True
        else:
            return False
