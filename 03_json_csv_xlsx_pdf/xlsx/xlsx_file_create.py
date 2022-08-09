#!/usr/bin/env python3
import xlsxwriter


def main():
    data = [['Nook', 42],
            ['Kojo', 11],
            ['Kama', 13],
            ['Fiolka', 48]]
    workbook = create_workbook('sample_workbook.xlsx')
    worksheet = create_worksheet(workbook)
    write_data(worksheet, data)
    average_age(worksheet, data)
    sum_age(worksheet, data)
    close_workbook(workbook)


def create_workbook(filename):
    workbook = xlsxwriter.Workbook(filename)
    return workbook


def create_worksheet(workbook):
    worksheet = workbook.add_worksheet()
    return worksheet


def write_data(worksheet, data):
    for row in range(len(data)):
        for col in range(len(data[row])):
            worksheet.write(row, col, data[row][col])


def average_age(worksheet, data):
    worksheet.write(len(data), 0, 'Avg. age')
    avg_formula = "=AVERAGE(B{}:B{})".format(1, len(data))
    worksheet.write(len(data), 1, avg_formula)


def sum_age(worksheet, data):
    worksheet.write(len(data)+1, 0, 'Sum. age')
    sum_formula = '=SUM(B{}:B{})'.format(1, len(data))
    worksheet.write(len(data)+1, 1, sum_formula)


def close_workbook(workbook):
    workbook.close()


if __name__ == '__main__':
    main()
