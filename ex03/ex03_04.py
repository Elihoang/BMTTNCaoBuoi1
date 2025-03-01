def truycapphantu(tuple_data):
    first = tuple_data[0]
    last = tuple_data[-1]
    return first, last


tuple = eval(input('nhập tuple () '))
first, last = truycapphantu(tuple)

print('phần tử đầu tiên ', first)
print('phần tử cuối cùng ', last)
