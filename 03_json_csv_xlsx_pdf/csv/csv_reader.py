#!/usr/bin/env python3
import csv


def main():
    read_csv_to_list('AS-21.csv')
    read_csv_to_dictionaries('AS-21.csv')


def read_csv_to_list(filename):
    try:
        with open(filename, newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for record in csv_reader:
                print(record)
    except (IOError, OSError) as file_read_error:
        print("can't open file csv. :".format(file_read_error))


def read_csv_to_dictionaries(filename):
    try:
        with open(filename, newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for record in csv_reader:
                # print(record)
                print(record['login'])
    except (IOError, OSError) as file_read_error:
        print("can't open file csv. :".format(file_read_error))


if __name__ == '__main__':
    main()