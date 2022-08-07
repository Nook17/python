#!/usr/bin/env python3
import csv


def read_csv(filename):
    try:
        with open(filename, newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for record in csv_reader:
                print(record)
    except (IOError, OSError) as file_read_error:
        print("can't open file csv. :".format(file_read_error))


if __name__ == '__main__':
    read_csv('market_cap.csv')