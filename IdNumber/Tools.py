
# 3609834xxxxxxxx5733, i.e. missing birthday
def get_valid_birthday():
    birthdays = []
    years_prefix = ['19', '20']
    for year_prefix in years_prefix:
        for year_suffix in range(100):
            year_suffix = '0' + str(year_suffix) if year_suffix < 10 else str(year_suffix)
            for month in range(1, 13):
                month = '0' + str(month) if month < 10 else str(month)
                for day in range(1, 32):
                    day = '0' + str(day) if day < 10 else str(day)
                    birthday = year_prefix + year_suffix + month + day
                    birthdays.append(birthday)
    return birthdays
