"""Multithreading Test"""

import concurrent.futures
import time


def do_something(seconds):
    print(f'Sleeping {seconds} seconds(s)...')
    time.sleep(seconds)
    return f'Done Sleeping for {seconds} second(s)...'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [6, 5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)
