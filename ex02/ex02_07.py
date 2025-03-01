print('nhập văn bản (nhập done để kết thúc )')
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print('\nvăn bản khi chuyển chữ hoa ')
for line in lines:
    print(line.upper())
