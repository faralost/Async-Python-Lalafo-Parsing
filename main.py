import asyncio
import time

import httpx

from collect_data import collecting_result_data

CATEGORY_IDS = [2046, 2031, 2038, 2055, 5301, ]

start_time = time.time()


async def main():
    async with httpx.AsyncClient() as client:
        tasks = []

        for category_id in CATEGORY_IDS:
            tasks.append(
                asyncio.ensure_future(collecting_result_data(client=client, category_id=category_id, per_page=1)))

        results = await asyncio.gather(*tasks)

        result = []
        for res in results:
            result.extend(res)
        print(f'Collected {len(result)} items.')


if __name__ == '__main__':
    asyncio.run(main())

print("\n--- %s seconds ---" % (time.time() - start_time))
