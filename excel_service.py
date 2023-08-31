from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.styles.borders import Border, Side, BORDER_THICK
from openpyxl.utils import get_column_letter


def export_to_excel(results: dict, country: str, year: int, category: str):
    workbook = Workbook()
    sheet = workbook.active

    # create headers
    header_font = Font(bold=True, underline='single')
    sheet['A1'] = 'TYPE'
    sheet['A1'].font = header_font
    sheet['B1'] = '2023'
    sheet['A1'].font = header_font

    row_num = 2
    for key, value in results.items():
        sheet[f'A{row_num}'] = key
        sheet[f'B{row_num}'] = value
        row_num += 1

    workbook.save(f'{category}.xlsx')


def get_excel_column_for_year(year: int) -> str:
    if year == 2017:
        return 'B'
    elif year == 2018:
        return 'C'
    elif year == 2019:
        return 'D'
    elif year == 2020:
        return 'E'
    elif year == 2021:
        return 'F'
    elif year == 2022:
        return 'G'
    else:
        return 'H'


