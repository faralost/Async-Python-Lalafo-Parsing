import time

from collect_data import collecting_result_data

CATEGORY_IDS = [2046, 2031, 2038, 2055, 5301, ]

start_time = time.time()

if __name__ == '__main__':
    result = []
    for category_id in CATEGORY_IDS:
        result.extend(collecting_result_data(category_id=category_id, per_page=1))
    print(result)
    print(len(result))

print("\n--- %s seconds ---" % (time.time() - start_time))
