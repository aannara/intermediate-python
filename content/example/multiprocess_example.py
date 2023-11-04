import multiprocessing
import random

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_prime_arr(arr):
    return [is_prime(elem) for elem in arr]

if __name__ == "__main__":
    num_arr = [random.randint(100, 10000) for i in range(3000)]
    p1 = multiprocessing.Process(target=get_prime_arr, args=(num_arr[:1001],))
    p2 = multiprocessing.Process(target=get_prime_arr, args=(num_arr[1001:2001],))
    p3 = multiprocessing.Process(target=get_prime_arr, args=(num_arr[2001:3000],))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
