import asyncio
import aiohttp
from more_itertools import chunked 





async def get_people(person_id):
    async with  aiohttp.ClientSession() as http_session:
        response = await http_session.get(f'https://swapi.py4e.com/api/people/{person_id}/')
        json_data = await response.json()
        # await http_session.close()
        return json_data

# вариант 1
# async def main():   
    coro = get_people(2)
    result = await coro
    print(result)


# вариант 2 
# async def main():   
#     result = await get_people(2)
#     print(result)

MAX_REQUEST = 5

async def main(): 
    coros = []
    for i in range(1, 101):
        coro = get_people(i)
        coros.append(coro)
    response = await asyncio.gather(*coros)

    print(response)



asyncio.run(main())     
# создание event loop

