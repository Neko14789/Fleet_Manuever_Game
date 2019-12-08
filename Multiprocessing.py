"""Multiprocessing Test"""

import concurrent.futures
import multiprocessing
import time

start = time.perf_counter()


def do_something(seconds):
    # seconds = 1
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = []
        for x in range(10):
            secs.append(x + 2)
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    # if __name__ == '__main__':
    #     with concurrent.futures.ProcessPoolExecutor() as executor:
    #         secs = [7, 6, 5, 4, 3, 2, 1]
    #         results = [executor.submit(do_something, sec) for sec in secs]
    #
    #         for f in concurrent.futures.as_completed(results):
    #             print(f.result())

    """if __name__ == '__main__':
        processes = []
        for x in range(10):
            p = multiprocessing.Process(target=do_something, args=[ x ])
            p.start()
            processes.append(p)

        for process in processes:
            process.join()"""

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')

"""with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)"""

# for result in results:
#     print(result)