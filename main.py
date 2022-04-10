import os

from id_validator import validator
from IdNumber.IdNumber import *
from IdNumber.Tools import *
from IdNumber.Region import *


def print_id_info():
    if os.path.exists("region.json") is not True:
        write_region("IdNumber/ID_Region_Info.txt", "region.json")

    ID = IdNumber("360983198503105733")
    area_name = ID.get_area_name()
    birthday = ID.get_birthday()
    age = ID.get_age()
    sex = ID.get_sex()
    is_valid = ID.verify_id()
    check_digit = ID.get_check_digit()
    print("区域：{}\n生日：{}\n年龄：{}\n性别：{}\n有效ID：{}\n除11后值：{}".format(area_name, birthday, age, sex, is_valid, check_digit))
    return ID


if __name__ == "__main__":
    print_id_info()

    print("1: Tail missing, 2: Birth day missing")
    choice = input("You choice: \n")

    newIdString = []
    if str(choice) == "1":
        IdString = "36220419850310573"
        tail_value = IdNumber(IdString).get_tail_value()
        newIdString.append(IdString + str(tail_value))
    elif str(choice) == '2':
        IdString = "360983XXXXXXXX5727"
        birth_days = get_valid_birthday()
        for birth_day in birth_days:
            newIdString.append(IdString[:6] + birth_day + IdString[-4:])

    validIdNumber = []
    for ID in newIdString:
        if IdNumber(ID).verify_id():
            if validator.is_valid(ID):
                validIdNumber.append(ID)
                print("The valid ID is {}".format("\n".join(validIdNumber)))
    with open("valid_ID_Number.txt", "w") as fw:
        fw.write("\n".join(validIdNumber))
