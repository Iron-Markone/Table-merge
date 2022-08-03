

# # 合并多个excel数据表格

# 1、获取文件夹下的所有文件名称



#导入0s
import os  
import pandas as pd
import openpyxl
import xlrd




#改变当前的工作路径到所有文件所在的文件夹下
# dir = "C:/Users/Administrator/Desktop/fba订单11.24"
path_file = str(input('请输入文件所在目录：'))
need_dir = os.chdir(path_file)





# 列出所有文件的名称 以列表呈现
need_file_name = os.listdir(need_dir)
print('所有的表格名：%s'%need_file_name)




# 2、将不同表格的数据进行合并



# 定义 空的数据列表
data_li = []
title_dir = input('请输入表头目录和文件名(表头另放一个目录)：')
title = pd.read_excel(title_dir)
title = list(title)

# 取出每个文件的名称
for file_name in need_file_name:
    if file_name[-3:] == 'xls' or file_name[-3:] == 'lsx':
    # 读取每个文件的数据 
        data = pd.read_excel(os.path.join(path_file, file_name),usecols = title )    
    elif file_name[-3:] == 'csv':
        data = pd.read_csv(os.path.join(path_file, file_name),engine = 'python',usecols = title )
    # 获取表格的列名
    col_name = data.columns.tolist()
    #在表格的第一列加上一列 filename ，列的内容是表格的名称
    col_name.insert(0,'filename')         #insert() 括号内的0是索引的位置，filename是添加的列的名称
    #reindex 函数的作用是对列名进行重排和增加列名
    data = data.reindex(columns=col_name)
    data['filename'] = file_name
#     print(data.head())
    # 将数据添加到 空的数据列表中
    data_li.append(data)





print('合并的表格数为：%d'%len(data_li))   # 列表长度返回为表格的数目 ，说明构建成功




# 拼接所有文件的数据
all_data = pd.concat(data_li,ignore_index = True,sort = False)  


# 3、保存至新的文件



new_filename = str(input('请输入新文件名，保存数据(后缀.xlsx):'))
all_data.to_excel(new_filename,index=False)     #index=False 表示不需要保存索引列

