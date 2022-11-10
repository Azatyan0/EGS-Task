"""The "Solution" is a class where written "is_valid_date" method which checks whether the
input string consists valid date format or not"""

import re
from EGS_task.Models.Date import Date
from EGS_task.Models.Time import Time


class Solution:

    @staticmethod
    def is_valid_date(input_str):
        date = Date()
        time = Time()

        matches = re.findall(r"([0-9]{2}\.[0-9]{2}\.[0-9]{1,4}) ([0-9]{2}:[0-9]{2}:[0-9]{2})", input_str)
        result = False

        for pattern in matches:
            date_pattern = pattern[0].split(".")
            time_pattern = pattern[1].split(":")

            date.year_setter(date_pattern[2])
            date.month_setter(date_pattern[1])
            date.day_setter(date_pattern[0])

            time.second_setter(time_pattern[2])
            time.minute_setter(time_pattern[1])
            time.hour_setter(time_pattern[0])

            if date.day_getter() and date.month_getter() and date.year_getter() and time.second_getter() \
                    and time.minute_getter() and time.hour_getter():
                result = True
                break

        return result
