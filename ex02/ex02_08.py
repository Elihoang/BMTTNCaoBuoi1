def chiahetcho5(n):
    sothapphan = int(n, 2)
    if sothapphan % 5 == 0:
        return True
    else:
        return False


chuoinhiphan = input('nhap chuỗi nhị phân (phân tách bởi dấu phẩy) ')

sonhiphanlist = chuoinhiphan.split(',')
sochiahetcho5 = [so for so in sonhiphanlist if chiahetcho5(so)]

if len(sochiahetcho5) > 0:
    ketqua = ",".join(sochiahetcho5)
    print('Các số nhị phân chia het cho 5 la: ', ketqua)
else:
    print('ko có số nhị phân nào chia hết cho 5')
