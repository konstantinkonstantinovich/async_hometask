import asyncio
import aiohttp
from datetime import datetime


async def api_one(session):
    first = 'https://www.metaweather.com/api/location/44418/2013/4/27/'
    req = await session.request(method='GET', url=first)
    data = await req.json(content_type=None)
    result_array = list()
    for i in range(len(data)):
        temp1 = data[i]['min_temp']
        temp2 = data[i]['max_temp']
        if temp2 is None:
            temp2 = 0
        if temp1 is None:
            temp1 = 0    
        temp = (temp1 + temp2) /2
        result_array.append(temp)
    return result_array


async def api_two(session):
    second = 'https://www.cheapshark.com/api/1.0/deals'
    r = await session.request(method='GET', url=second)
    data1 = await r.json(content_type=None)
    result_arr = list()
    print(data1[3]['salePrice'])
    for i in range(len(data1)):
        tmp = data1[i]['salePrice']
        result_arr.append(tmp)
    result_arr.sort()
    return result_arr


async def api_third(session):
    api = 'https://api.met.no/weatherapi/locationforecast/2.0/compact.json?lat=49.988358&lon=36.232845'
    headers = {
        'User-Agent': 'Mozilla/5.0(X11;Ubuntu;Linuxx86_64;rv:87.0)Gecko/20100101Firefox/87.0'
    }
    r = await session.request(method='GET', url=api, headers=headers)
    data = await r.json(content_type=None)
    hours_in_day = 24
    time = 0
    res = []
    while time <= 84:
        if time >= 60:
            hours_in_day = 4
        res.append(data['properties']['timeseries'][time]['data']['instant']['details']['air_temperature'])
        time += hours_in_day
    return res


async def main():
    async with aiohttp.ClientSession() as session:
        p = await asyncio.gather(
            api_one(session),
            api_two(session),
            api_third(session)
        )
        res = [round(sum(val) / len(p), 1) for val in zip(*p)]
        print(res)


if __name__ == '__main__':
    begin = datetime.now()
    asyncio.run(main())
    print('Finished')
    print(datetime.now() - begin)