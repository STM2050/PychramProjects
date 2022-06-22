my_dict_1 = {'1': '1', '2': '4', '3': '9', '4': '16', '5': '25', '6': '36', '7': '49', '8': '64'}

print(my_dict_1)

n = int(input())
my_dict_1 = {}
for i in range(1,n+1):
    my_dict_1[i] = i*i
print(my_dict_1)
