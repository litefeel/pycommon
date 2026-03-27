import csv

import openpyxl


def save_csv(filename, rows: list[list], header: list | None = None):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        for row in rows:
            writer.writerow(row)

def read_xlsx(filename: str) -> list[list]:
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    rows = []
    for row in ws.rows:
        rows.append([cell.value for cell in row])
    return rows

def save_xlsx(
    filename: str,
    rows: list[list],
    header: list | None = None,
    images: list[tuple[str, str]] | None = None,
):
    """Save data to xlsx file. 注意图片不能设置为嵌入单元格图片。
    如需设置嵌入单元格图片，则执行以下步骤:
    1. 打开Excel
    2. 选中任意一张图片
    3. Ctrl+A 选中所有图片
    4. 右键选择嵌入单元格图片

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
