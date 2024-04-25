from time import time
import multiprocessing


def factorize(number):
    list_of_div = []
    div = 1
    while div <= number:
        if number % div == 0:
            list_of_div.append(div)
        div += 1
    return list_of_div

def factorize_async(*numbers):
    num_processes = multiprocessing.cpu_count()
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(factorize, numbers)
    return results


if __name__ == "__main__":
    
    start_time = time()
    a  = factorize(128)
    b  = factorize(255)
    c = factorize(99999)
    d  = factorize(10651060)
    print("Time sync: ", time()-start_time)

    start_time = time()
    a, b, c, d  = factorize_async(128, 255, 99999, 10651060)
    print("Time async: ", time()-start_time)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]