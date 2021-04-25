import  xlrd

from RPA_Console_testEnv.common.readConfig import  ReadConfig

excel_file=ReadConfig().getOptionValue('taskName','task_manual_name')


def readExcel():
    #excel_file=r'C:\Users\caiwenjie\PycharmProjects\selenium_demo\RPA_Console_testEnv\utils\uploadfiles\console_task.xlsx'
    book=xlrd.open_workbook(excel_file)
    sheet_book=book.sheet_by_index(0)
    rows = sheet_book.nrows
    cols = sheet_book.ncols
    print(rows,cols)
    list_=sheet_book.col_values(0,0,rows)#第一列，第一行、最后一行。
    print(list_)



if __name__=="__main__":
    readExcel()


