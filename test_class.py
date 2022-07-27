import asyncio

import httpx

vect_dic: dict[str,int] = {}


class Test:
    def __init__(self):
        self.name: str = 'kingname'

    async def req(self, url):
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
            result = resp.json()
            print(result)


test = Test()
asyncio.run(test.req('http://xxx'))
