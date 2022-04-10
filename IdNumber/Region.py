from collections import OrderedDict
from IdNumber import FileHandle


def region_2_json(file_path):
    info = FileHandle.read(file_path)
    ordered_dict = OrderedDict()
    for i in range(len(info)):
        leve2_region = {}
        data = info[i].replace('\n', '').split(',')

        proCode, cityCode, streetCode = data[0], data[2], data[4]
        leve1_address, leve2_address, leve3_address = data[1], data[3], data[5]
        cityCode_existed = False
        city_existed = False
        k = 0
        # dataa = {}
        if ordered_dict.get(leve1_address):
            if ordered_dict[leve1_address]:
                for k in range(len(ordered_dict[leve1_address])):
                    ordered_dict[leve1_address][k]['省份代号'] = proCode
                    if cityCode == ordered_dict[leve1_address][k]['城市代号']:
                        cityCode_existed = True
                        if leve2_address in ordered_dict[leve1_address][k].keys():
                            city_existed = True
                            break
            if cityCode_existed:
                if city_existed:
                    ordered_dict[leve1_address][k][leve2_address][leve3_address] = streetCode
                else:
                    ordered_dict[leve1_address][k][leve2_address] = {}
                    ordered_dict[leve1_address][k][leve2_address][leve3_address] = streetCode

            else:
                leve2_region['城市代号'] = cityCode
                leve2_region[leve2_address] = {}
                leve2_region[leve2_address][leve3_address] = streetCode
                ordered_dict[leve1_address].append(leve2_region)

        else:
            ordered_dict[leve1_address] = []

            leve2_region["城市代号"] = cityCode
            leve2_region[leve2_address] = {}
            leve2_region[leve2_address][leve3_address] = streetCode
            ordered_dict[leve1_address].append(leve2_region)
    return ordered_dict


def write_region(file_src, file_dest):
    FileHandle.write(region_2_json(file_src), file_dest)

