import threading
import random

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_prime_arr(arr):
    return [is_prime(elem) for elem in arr]

num_arr = [random.randint(100, 10000) for i in range(3000)]
thread1 = threading.Thread(target=get_prime_arr, args=(num_arr[:1001],))
thread2 = threading.Thread(target=get_prime_arr, args=(num_arr[1001:2001],))
thread3 = threading.Thread(target=get_prime_arr, args=(num_arr[2001:3000],))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
