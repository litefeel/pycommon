import openpyxl
import csv


def save_csv(filename, rows: list[list], header: list = None):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        for row in rows:
            writer.writerow(row)


def save_xlsx(
    filename: str, rows: list[list], header: list = None, images: list[tuple[str, str]] = None
):
    """Save data to xlsx file.

    Args:
        filename (str): filename
        rows (list[list]):
        header (list, optional): header. Defaults to None.
        images (list[tuple[str, str]], optional): [(path, anchor),...]. Defaults to None.
    """
    wb = openpyxl.Workbook()
    ws = wb.active
    if header:
        ws.append(header)
    for row in rows:
        ws.append(row)

    if images:
        for path, anchor in images:
            img = openpyxl.drawing.image.Image(path)
            ws.add_image(img, anchor)

    wb.save(filename)
