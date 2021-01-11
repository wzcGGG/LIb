'''
图书信息初始化
'''
import xlrd
import datetime
from database import new_book
import pandas as pd


def date(dates):  #定义转化日期戳的函数,dates为日期戳
    delta = datetime.timedelta(days=dates)
    today = datetime.datetime.strptime(
        '1899-12-30', '%Y-%m-%d') + delta  #将1899-12-30转化为可以计算的时间格式并加上要转化的日期戳
    return datetime.datetime.strftime(today, '%Y-%m')  #制定输出日期的格式


# excel文件
bk = xlrd.open_workbook(
    r'D:\study\大三上\软件工程\软工课设\library_system\model\book_list.xlsx')
#打开工作表
sh = bk.sheets()[0]
book_msg = {
    'BID': '',
    'BNAME': '',
    'AUTHOR': '',
    'PUBLICATION_DATE': '',
    'PRESS': '',
    'POSITION': '',
    'SUM': 5,
    'CLASSIFICATION': ''
}
# 遍历所有行
for i in range(1, sh.nrows):
    a = []
    # 遍历所有列
    for j in range(sh.ncols):
        # 将excel每一列的值用，隔开
        if j == 0:
            book_msg["BID"] = str(int((sh.cell(i, j).value)))
        elif j == 1:
            book_msg["BNAME"] = str(sh.cell(i, j).value)
        elif j == 2:
            book_msg["AUTHOR"] = str(sh.cell(i, j).value)
        elif j == 3:
            book_msg["PUBLICATION_DATE"] = date(int((sh.cell(i, j).value)))
        elif j == 4:
            book_msg["PRESS"] = str(sh.cell(i, j).value)
        elif j == 5:
            book_msg["POSITION"] = str(sh.cell(i, j).value)
        elif j == 6:
            book_msg["SUM"] = int(sh.cell(i, j).value)
        elif j == 7:
            book_msg["CLASSIFICATION"] = str(sh.cell(i, j).value)
    new_book(book_msg)
