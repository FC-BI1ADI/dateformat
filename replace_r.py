def replace_r(str_s, str_to_replace, str_dest):
    # 反转字符串
    str_s = str_s[::-1]
    str_to_replace = str_to_replace[::-1]
    str_dest = str_dest[::-1]
    # 替换已反转的字符串
    str_d = str_s.replace(str_to_replace, str_dest,1)
    str_d = str_d[::-1]
    return str_d
# s1="\\\\FC-CLOUD\\Public\\Photo\\★2017.4.2-4.3  延庆 应梦寺-后河\\2017.4.2 数据.png"
# s2="2017.4.2"
# s3="20170402"
# print(replace_r(s1,s2,s3))