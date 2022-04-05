import os
import json


def read_info(path):
    try:
        with open(path, "r", encoding="GBK") as fr:
            data = fr.readlines()
    except FileNotFoundError as e:
        print(e)

    return data


def write_file(data):
    with open("region.json", 'w', encoding="GBk") as fw:
        json.dump(data, fw, indent=4, ensure_ascii=False)


def region_2_json(path):
    info = read_info(path)
    leve1_region = {}
    for i in range(len(info)):
        leve2_region = {}
        data = info[i].replace('\n', '').split(',')

        proCode, cityCode, streetCode = data[0], data[2], data[4]
        leve1_address, leve2_address, leve3_address = data[1], data[3], data[5]
        cityCode_existed = False
        city_existed = False
        k = 0
        # dataa = {}
        if leve1_region.get(leve1_address):
            if leve1_region[leve1_address]:
                # leve1_region[leve1_address].append(leve1_region["省份代号"])
                for k in range(len(leve1_region[leve1_address])):
                    leve1_region[leve1_address][k]['省份代号'] = proCode
                    if cityCode == leve1_region[leve1_address][k]['城市代号']:
                        cityCode_existed = True
                        if leve2_address in leve1_region[leve1_address][k].keys():
                            city_existed = True
                            break
            if cityCode_existed:
                if city_existed:
                    leve1_region[leve1_address][k][leve2_address][leve3_address] = streetCode
                else:
                    leve1_region[leve1_address][k][leve2_address] = {}
                    leve1_region[leve1_address][k][leve2_address][leve3_address] = streetCode

            else:
                leve2_region['城市代号'] = cityCode
                leve2_region[leve2_address] = {}
                leve2_region[leve2_address][leve3_address] = streetCode
                leve1_region[leve1_address].append(leve2_region)

        else:
            # leve1_region["省份代号"] = proCode
            leve1_region[leve1_address] = []

            leve2_region["城市代号"] = cityCode
            leve2_region[leve2_address] = {}
            leve2_region[leve2_address][leve3_address] = streetCode
            leve1_region[leve1_address].append(leve2_region)

    write_file(leve1_region)


if __name__ == "__main__":
    region_2_json("ID_Region_Info.txt")
    print("Done")





