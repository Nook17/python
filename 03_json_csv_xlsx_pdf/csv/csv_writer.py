#!/usr/bin/env python3
import csv


def main():
    # csv_list()
    csf_dict()


def csv_list():
    header = ['name', 'age', 'gender']
    data = [['Kojo', 11, 'M'],
            ['Kama', 13, 'F'],
            ['Nook', 42, 'M']]
    filename = 'sample_output_list.csv'
    write_csv_to_list(filename, header, data)


def csf_dict():
    header = ['name', 'age', 'gender']
    data = [{'name': 'Kojo', 'age': 11, 'gender': 'M'},
            {'name': 'Nook', 'age': 42, 'gender': 'M'},
            {'name': 'Kama', 'age': 13, 'gender': 'F'}]
    filename = 'sample_output_dict.csv'
    write_csv_to_dictionaries(filename, header, data)


def write_csv_to_list(filename, header, data):
    try:
        with open(filename, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            csv_writer.writerows(data)
    except (IOError, OSError) as csv_file_error:
        print("don't open file csv. {}".format(csv_file_error))


def write_csv_to_dictionaries(filename, header, data):
    try:
        with open(filename, 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=header)
            csv_writer.writeheader()
            csv_writer.writerows(data)
    except (IOError, OSError) as csv_file_error:
        print("don't open file csv. {}".format(csv_file_error))


if __name__ == '__main__':
    main()
