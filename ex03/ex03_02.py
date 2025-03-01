def daonguoclist(list):
    return list[::-1]


dslist = input('nhập danh sách các số cách nhau bằng dấu , :')
numbers = list(map(int, dslist.split(',')))

listdaonguoc = daonguoclist(numbers)
print('list sau khi dao nguoc: ', listdaonguoc)
