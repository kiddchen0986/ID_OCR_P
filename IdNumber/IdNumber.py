import json
from datetime import datetime
# from Region import write_region


class IdNumber:
    def __init__(self, IdNumber):
        self.IdNumber = IdNumber
        self.area_id = IdNumber[:6]
        self.birth_day = IdNumber[6:14]

    def get_area_name(self):
        find = False
        try:
            with open("region.json", encoding="GBK") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            print(e)

        for leve1_region, leve1_details in dict(data).items():
            if find is True:
                break
            for leve1_info in leve1_details:
                for region_info in leve1_info:
                    if region_info == "省份代号":
                        if leve1_info["省份代号"] == self.area_id[:2]:
                            if leve1_info["城市代号"] == self.area_id[2:4]:
                                for leve2_region, leve3_regions in dict(leve1_info).items():
                                    if find is True:
                                        break
                                    if type(leve3_regions) is dict:
                                        for leve3_region, leve3_ID in dict(leve3_regions).items():
                                            if leve3_ID == self.area_id[4:6]:
                                                area_name = leve1_region + leve2_region + leve3_region
                                                find = True
                                                break
                            else:
                                continue
                        else:
                            break
        return area_name

    def get_birthday(self):
        return self.birth_day[:4] + "-" + self.birth_day[4:6] + "-" + self.birth_day[6:8]

    def get_age(self):
        current_year = datetime.now().year
        return current_year - int(self.birth_day[:4])

    def get_sex(self):
        sex = "Male" if int(self.IdNumber[-2]) % 2 == 1 else "female"
        return sex

    def get_check_digit(self):
        sum_data = 0
        times = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]

        for i, v in enumerate(times):
            sum_data += int(self.IdNumber[i]) * v

        check_digit = sum_data % 11
        return check_digit

    def get_tail_value(self):
        tail = [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2]
        for i, v in enumerate(tail):
            if i == self.get_check_digit():
                return v

    def verify_id(self):
        status = False
        tail = [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2]
        for i, v in enumerate(tail):
            if i == self.get_check_digit():
                if v == int(self.IdNumber[-1]):
                    status = True
        return status
