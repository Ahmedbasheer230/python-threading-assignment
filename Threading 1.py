import threading
import time


def print_numbers(name):
    for i in range(1, 6):
        print(f"{name}: {i}")
time.sleep(1)


# Create threads
thread1 = threading.Thread(target=print_numbers, args=("Thread-1",))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2",))


# Start threads
thread1.start()
thread2.start()


# Wait for threads to finish
thread1.join()
thread2.join()


print("Threading example completed")