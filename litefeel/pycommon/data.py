import openpyxl
import csv


def save_csv(filename, rows: list[list]):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)


def save_xlsx(filename, rows: list[list]):
    wb = openpyxl.Workbook()
    ws = wb.active
    for row in rows:
        ws.append(row)
    wb.save(filename)