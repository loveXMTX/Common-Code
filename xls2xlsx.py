##Created By 2020-09-17
## 将xls转换为xlsx，并在首行和首列插入index
import os
import pandas as pd
#import numpy as np
# def addIndex():

# 	hang = list(range(220, 451, 5))
# 	lie = [''] + list(range(300,551,2))
# 	data.insert(0,'newcol',hang)
# 	data.loc[0] = lie



#此方法用将xls转化为xlsx
def transformat():
    global path #定义为全局变量
    path = os.getcwd()#获取当前工作路径
    file = os.listdir(path)#获取当前路径下的所有文件
    for f in file:
        file_name_be,suff = os.path.splitext(f)#对路径进行分割，分别为文件路径和文件后缀
        if suff  == '.xls':
            print('将对{}文件进行转换...'.format(f))
            data = pd.DataFrame(pd.read_excel(path + '/' + f,header=None))#读取xls文件

            #需要添加的行和列
            hang = list(range(220, 451, 5))
            lie = [''] + list(range(300, 551, 2))
            
            #添加行，对-1行赋值，然后将index+1，重新排序
            data.loc[-1] = hang
            data.index = data.index + 1
            data.sort_index(inplace=True)

            #添加列
            data.insert(0,'newcol',lie)

            data.to_excel(path + '/' + file_name_be + '_Transformat.xlsx',index = False,header=None)#格式转换
            print(' {} 文件已转化为 {} 保存在 {} 目录下\n'.format(f,file_name_be + '_Transformat.xlsx',path))

if __name__ == '__main__':
    transformat()