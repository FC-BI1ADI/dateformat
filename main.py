# DateFormat用于将本地文件名中的分离日期修改为定制日期

# 导入相应模块
import os
import re



# 以分隔符为界将源日期切分为年、月、日三部分，然后进行格式重整并拼接为8位日期
def date_format(date_s):
    year, month, date = date_s.split(".")
    if len(month) < 2:
        month = '0' + month
    if len(date) < 2:
        date = '0' + date
    return year + month + date

def replace_r(str_s, str_to_replace, str_dest):
    # 反转字符串
    str_s = str_s[::-1]
    str_to_replace = str_to_replace[::-1]
    str_dest = str_dest[::-1]
    # 替换已反转的字符串
    str_d = str_s.replace(str_to_replace, str_dest,1)
    str_d = str_d[::-1]
    return str_d

# 设置起点路径，路径采用绝对路径
path = r'\\FC-CLOUD\Public\Photo'
dir_list = []
file_list = []
all_list = []
# 读取指定目录下的所有文件夹和文件
for root, dirs, files in os.walk(path, topdown=False):

    for name in files:  # 打印所有文件
        # print(os.path.join(root, name))
        file_list.append(os.path.join(root, name))
        all_list.append(os.path.join(root, name))
    for name in dirs:  # 打印所有目录
        # print(os.path.join(root, name))
        dir_list.append(os.path.join(root, name))
        all_list.append(os.path.join(root, name))
# 遍历所有目录和文件，将全路径的目录名和文件名分别放入列表dir_list和file_list
# print(all_list)
# 对all_list以元素长度进行排序，为后序的改名操作做准备
all_list.sort(key=lambda i: len(i), reverse=True)
# for i in range(len(all_list)):
#     print(i, ":", all_list[i])


# 设置正则表达式
# re_pattern = r'\d{4}[.]\d{1,2}[.]\d{1,2}'
# 遍历all_list进行文件名处理
for filename_s in all_list:

    if os.path.isdir(filename_s):
        print("[D]", end="")

    if os.path.isfile(filename_s):
        print("[F]", end="")
    # 输出filename_s
    print(filename_s, end=" || ")

    # （1）判断文件夹和文件名中是否含有分离日期，并返回起始位置和结束位置
    # 使用正则表达式判断是否存在指定格式的日期
    find_result = re.findall(r"\d{4}[.]\d{1,2}[.]\d{1,2}", filename_s)

    if find_result:
        # 输出查找结果的第1项
        # print(find_result[0])
        # 查找结果不为空时，处理最后一个日期字符串，进行格式转换，然后对源日期字符串进行转换
        str_to_replace = find_result[len(find_result) - 1]
        if len(find_result) > 1:
            filename_d = replace_r(filename_s, str_to_replace, date_format(str_to_replace))
        else:
            filename_d = filename_s.replace(str_to_replace, date_format(str_to_replace))
        # print(date_format(find_result[0]))
        # filename_d = re.sub(re_pattern, date_format(find_result[len(find_result) - 1]), filename_s, count=1)
        print("[%s ==> %s]" % (filename_s, filename_d))

        # 切出最后一部分路径，判断是否含有日期，若有则修改文件名，否则继续
        split_path = filename_s.split('\\')
        if len(split_path) >= 1:
            last_path = split_path[len(split_path) - 1]
            if re.findall(r"\d{4}[.]\d{1,2}[.]\d{1,2}", last_path):
                os.rename(filename_s, filename_d)


    else:
        print()
