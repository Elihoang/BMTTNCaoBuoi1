def demsolan(list):
    count ={}
    for item in list:
        if item in count :
            count[item] +=1
        else:
            count[item]=1
    return count

string =input('nhập danh sách các từ ,cách nhau bằng dấu cách ')

word_list =string.split()

solanxh =demsolan(word_list)
print('so lan xuat hien các phần tử : ',solanxh)