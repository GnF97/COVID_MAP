
import gmaps
import googlemaps
import pandas as pd
import math
from math import sqrt
import config

pdf = [5+i for i in range(101)]
color_list = [f"{'rgba'}{(0, 0, 0+i, 0.5)}" for i in range(len(pdf))]

gmaps_key = googlemaps.Client(key= config.API_KEY)


# lalala = [' \x0c \x0c \x0c \x0c \x0c \x0c \x0c \x0c \x0c \x0c \x0c', ' \x0c \x0c \x0c \x0c \x0c', ' |盂\n\x0c \x0c 成功市場\n仁愛區成功一路88號\n\x0c', ' 成功市場\n仁愛區成功一路88號\n\x0c', ' 台鐵區間車 (三坑一台北車站)\n\x0c', ' 台鐵區間車 (台北車站一三坑)\n\x0c', ' 成功市場\n仁愛區成功一路88號\n\x0c', ' 全聯福利中心/精一店\n仁愛區精一路15號\n\x0c', ' 成功市場\n仁愛區成功一路88號\n\x0c', ' 成功市場\n仁愛區成功一路88號\n\x0c', ' 輕鬆宴餐廳\n仁愛區愛一路35號2樓\n\x0c', ' 台鐵區間車 (三坑一台北)\n\x0c', ' 台鐵區間車 (台北一三坑)\n\x0c', ' 王大夫診所\n仁愛區南榮路4號\n\n成功市場\n仁愛區成功一路88號\n\x0c', '  \n\x0c', ' 成功市場\n仁愛區成功一路88號\n\x0c']



def coord_trfr(address):
    r = gmaps_key.geocode(f"{address}")
    if len(r) != 0:
        r_reuslt = r[0]["geometry"]["location"]
        if 22 <= r_reuslt["lat"] <= 26 and 120 <= r_reuslt["lng"] <= 122: 
            return r_reuslt["lat"], r_reuslt["lng"]


def cal_distc(cords):
  # cords will take in a list with two coords
  R = sqrt(132.8*(10**4))
  # R should be inputted
  lat0, lng0 = cords[0][0]*math.pi/180, cords[0][1]*math.pi/180
  lat1, lng1 = cords[1][0]*math.pi/180, cords[1][1]*math.pi/180
  a = math.sin(lat1-lat0)**2+math.cos(lat0)*math.cos(lat1)*math.sin(lng1-lng0/2)**2
  c = 2*math.atan2(sqrt(a),sqrt(1-a))
  return R*c

def distc_coord(cord_sets):
  cords = list(cord_sets.values())
  R = 2106
  d_list = [cal_distc([cords[i],cords[i+1]]) for i in range(len(cords)) if i+1 < len(cords)]
  ii = d_list.index(min([d for d in d_list if d <= R]))
  cord_sets = {key:val for key, val in cord_sets.items() if cal_distc([val,cords[ii]]) < R}
  return cord_sets

def load_loc(prcd_pdf):
    loc_dict = {}
    for loccc in prcd_pdf:
        locc = loccc.split('\n')
        if len(loccc) != len(locc):
            for i in range(len(locc)):
                loc = coord_trfr(locc[i])
                if loc != None and loc not in loc_dict.values():
                    # drop too far points, through country boundery
                    loc_dict[locc[i]] = loc
                    break
    return loc_dict

def storage_unit(prcd_pdf):
    loc_dict = distc_coord(load_loc(prcd_pdf))
    df = pd.DataFrame(columns=['patient_id', 'footprint', 'coord'])
    df['footprint'] = list(loc_dict.keys())
    df['coord'] = list(loc_dict.values())
    # require to tackle
    df['patient_id'] = 2564
    return df['coord']

# print(type(storage_unit(lalala)))
