# -*- coding: utf-8 -*-
import datetime
import multiprocessing


def read_file(name):
    all_data = []
    with open(name) as file:
        while file.read(1) != '':
            all_data.append(file.readline())


# Линейное считывание
# file_names = [f'./file {number}.txt' for number in range(1, 5)]
# start = datetime.datetime.now()
# for name in file_names:
#     read_file(name)
# end = datetime.datetime.now()
#
# print(f'Время выполнения линейного считывания: {end - start}')
# Конец блока линейного считывания

# Многопроцессорное считывание
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        all_files = []
        for number in range(1, 5):
            all_files.append(f'./file {number}.txt')
        start = datetime.datetime.now()
        data_list = pool.map(read_file, all_files)
    end = datetime.datetime.now()
    print(f'Время выполнения многопроцессорного считывания: {end - start}')
# Конец блока многопроцессорного считывания
