from colorama import Fore
from EGS_task.Reader import Reader
from EGS_task.Solution import Solution

dates = Reader().json2dict("Test_Inputs.json")

all_case = len(dates)
passed_case = 0
over_all_stat = "PASSED"
for i, date in enumerate(dates.keys()):

    print(Fore.WHITE + f"{i + 1}. Compare actual and expected results for  '{date}' string")
    actual = Solution.is_valid_date(date)
    dates[date].actual_res_setter(actual)
    if dates[date].actual_res_getter() == dates[date].expected_res_getter():
        print(Fore.GREEN + "Pass")
        passed_case = passed_case + 1
    else:
        over_all_stat = "FAILED"
        print(Fore.RED + "Fail")

print(Fore.WHITE + f"\n\nPASS RATE: {all_case}/{passed_case} \nOVERALL STATUS : {over_all_stat}")
