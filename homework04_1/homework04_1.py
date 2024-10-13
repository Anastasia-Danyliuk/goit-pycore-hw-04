from pathlib import Path


def total_salary(path):
    with open(path, "r") as file:
        sum_salary = 0
        mid_salary = 0
        for el in file.readlines():
            line = el.strip()
            name_salary = line.split(",")
            salary = name_salary[1]
            sum_salary += int(salary)
        mid_salary = int(sum_salary / 3)
        result = [mid_salary, sum_salary]
    return result


try:
    result = total_salary("salary.txt")
    print(
        f"Загальна сума заробітної плати: {result[1]}, Середня заробітна плата: {result[0]}"
    )
except FileNotFoundError:
    print("File not Found")
except IOError:
    print("File is damaged")

