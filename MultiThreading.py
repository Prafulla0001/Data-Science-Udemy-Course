### Multithreading
## When to use Multi Threading
## 1. I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
## 2. Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number : {i}")
        time.sleep(1)


def print_letters():
    for letter in "abcde":
        print(f"Letter : {letter}")
        time.sleep(1)

        
# print_numbers()
# print_letters()

t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_letters)

start_time = time.time()

t1.start()
t2.start()

t1.join()  ## to join the thread with the external main thread for continuing the process
t2.join()

finished_time = time.time() - start_time
print("Finished Time : ", finished_time)