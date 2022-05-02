import openpyxl
import csv


def save_csv(filename, rows: list[list], header: list = None):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        for row in rows:
            writer.writerow(row)


def save_xlsx(filename, rows: list[list], header: list = None):
    wb = openpyxl.Workbook()
    ws = wb.active
    if header:
        ws.append(header)
    for row in rows:
        ws.append(row)
    wb.save(filename)
