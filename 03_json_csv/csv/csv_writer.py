#!/usr/bin/env python3

import csv

def write_csv(filename, header, data):
    try:
        with open(filename, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            csv_writer.writerows(data)
    except (IOError, OSError) as csv_file_error:
        print("don't open file csv. {}".format(csv_file_error))


if __name__ == '__main__':
    header = ['name', 'age', 'gender']
    data = [['Kojo', 11, 'M'],
            ['Kama', 13, 'F'],
            ['Nook', 42, 'M']]
    filename = 'sample_output.csv'
    write_csv(filename, header, data)
