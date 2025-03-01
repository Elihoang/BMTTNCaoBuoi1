sogiolam = float(input('nhập số giờ làm mỗi tuần '))
luonggio = float(input('Nhập lương theo giờ tiêu chuẩn '))
giotieuchuan = 44;
giovuottuan = max(0, sogiolam - giotieuchuan)
thuclanh = giotieuchuan * luonggio + giovuottuan * luonggio * 1.5

print(f'số tiền thực lãnh của nhân viên: {thuclanh}')
