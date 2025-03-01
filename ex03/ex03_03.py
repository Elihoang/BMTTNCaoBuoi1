def taoTupele(list):
    return tuple(list)


dslist = input('nhập danh sách các số cách nhau bằng dấu phẩy :')
numbers = list(map(int, dslist.split(',')))

my_tuple = taoTupele(numbers)
print('tuple từ list : ', my_tuple)
