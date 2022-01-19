import threading
import time
import argparse
import numpy as np
from numpy.random import uniform


def thread_sum(array, start, end):
    result = conventional_sum(array[start:end])
    result_list.append(result)


def convert_array_to_reciprocal(arr):
    return np.reciprocal(arr)


def make_thread(array, size, n):
    thread_list = []
    for i in range(n):
        th = threading.Thread(target=thread_sum, args=(
            array, i*(size//n), (i+1)*(size//n)))
        thread_list.append(th)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()


def parser():
    import_cmd = argparse.ArgumentParser()
    import_cmd.add_argument('--thread')
    import_cmd.add_argument('--array')
    args = import_cmd.parse_args()
    thread = int(args.thread)
    arraysize = int(args.array)
    return thread, arraysize


def pembulatan(n):
    return round(n, 4)


def conventional_sum(arr):
    res = 0
    for num in arr:
        res += num
    return res


def generate_random_arr(size):
    return uniform(1.0, 101.0, size)


def main(number_of_iterations):
    iterasi = 0
    cout_with = 0
    cout_without = 0
    for _ in range(number_of_iterations):
        iterasi += 1
        n, size = parser()

        t_awal_generate_random_array = time.perf_counter()
        arr_not_res = generate_random_arr(size)
        arr = convert_array_to_reciprocal(arr_not_res)
        t_end_generate_random_array = time.perf_counter()
        t_generate_random_array = pembulatan(
            t_end_generate_random_array - t_awal_generate_random_array)

        print(f'Menggenerate array {size} processing dan reciprocal.')
        print(f'Waktu pengerjaan {t_generate_random_array} detik.')

        t_thread_start = time.perf_counter()
        make_thread(arr, size, n)
        res_sum = pembulatan(conventional_sum(result_list))
        t_thread_end = time.perf_counter()
        t_total = pembulatan(t_thread_end - t_thread_start)

        print(f'Menghitung sum dari array reciprocal processing.')
        print(f'Waktu pengerjaan dengan {n} thread = {t_total} detik.')

        t_start_py_sum = time.perf_counter()
        py_sum = pembulatan(conventional_sum(arr))
        t_end_py_sum = time.perf_counter()
        t_py_sum = t_end_py_sum - t_start_py_sum

        print(
            f'Waktu pengerjaan tanpa thread: {pembulatan(t_py_sum)} detik.')

        print(f'Sum Result With Thread: {res_sum}')
        print(f'Sum Result Without Thread: {py_sum}')

        if t_py_sum < t_total:
            beda = t_total - t_py_sum
            cout_without += 1
            print(f'Without Thread Lebih Cepat {pembulatan(beda)} detik!\n')
        else:
            beda = t_py_sum - t_total
            cout_with += 1
            print(f'With Thread Lebih Cepat {pembulatan(beda)} detik!\n')

        result_list.clear()
    print(
        f'Dari {iterasi} iterasi. With Thread Lebih Cepat {cout_with}x, Lebih Lama {cout_without}x.')


if __name__ == '__main__':
    result_list = []
    while True:
        try:
            n = int(input('Mau Berapa Iterasi? '))
            break
        except ValueError:
            print('Invalid Input!\n')
    print()
    main(n)
