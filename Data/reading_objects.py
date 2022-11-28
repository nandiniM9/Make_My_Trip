import xlrd
from Library.config import config

def read_locators():
    workbook=xlrd.open_workbook(config.Xl_path)
    worksheet=workbook.sheet_by_name('HomeStay')
    rows=worksheet.get_rows()
    print(rows)
    header=next(rows)
    d={}
    l1=[]
    for row in rows:
        d[row[0].value]=(row[1].value,row[2].value)
    print(d)
    return d
read_locators()