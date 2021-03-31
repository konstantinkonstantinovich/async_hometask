import json
import requests
import asyncio
from datetime import datetime


# second = 'https://www.cheapshark.com/api/1.0/deals'
# r = requests.get(second)
# data1 = r.json()
# result_arr = list()
# print(data1[3]['salePrice'])
# for i in range(len(data1)):
#     tmp = data1[i]['salePrice']
#     result_arr.append(tmp)
# result_arr.sort()
# print(result_arr)    
    
# #print(result_arr)

def api_one():
    first = 'https://www.metaweather.com/api/location/44418/2013/4/27/'
    req = requests.get(first)
    data = req.json()
    result_array = list()
    for i in range(len(data)):
        temp1 = data[i]['min_temp']
        temp2 = data[i]['max_temp']
        if temp2 is None:
            temp2 = 0
        if temp1 is None:
            temp1 = 0    
        temp = (temp1 + temp2) /2
        result_array.append(int(temp))
    return result_array


def api_two():
    second = 'https://www.cheapshark.com/api/1.0/deals'
    r = requests.get(second)
    data1 = r.json()
    result_arr = list()
    print(data1[3]['salePrice'])
    for i in range(len(data1)):
        tmp = data1[i]['salePrice']
        result_arr.append(tmp)
    result_arr.sort()
    return result_arr

def api_third():
    api = 'https://api.met.no/weatherapi/locationforecast/2.0/compact.json?lat=49.988358&lon=36.232845'
    headers = {
        'User-Agent': 'Mozilla/5.0(X11;Ubuntu;Linuxx86_64;rv: 87.0)Gecko/20100101Firefox/87.0'
    }
    r = requests.get(api, headers=headers)
    data = r.json()
    t = 24
    j = 0
    res = []
    while j <= 84:
        if j >= 60:
            t = 4
        res.append(data['properties']['timeseries'][j]['data']['instant']['details']['air_temperature'])
        j += t
    return res

if __name__ == '__main__':
    begin = datetime.now()
    p = (api_one(), api_two(), api_third())
    print(datetime.now() - begin)    