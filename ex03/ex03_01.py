def tongsochan(list):
    tong = 0
    for num in list:
        if num % 2 == 0:
            tong += num
    return tong


dslist = input('nhập danh sách các số cách nhau bằng dấu ,: ')
n = list(map(int, dslist.split(',')))

tongchan = tongsochan(n)
print('tổng số chẵn trong list là ', tongchan)
