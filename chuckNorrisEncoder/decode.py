import numpy as np

s = '0 00 00 0 0 0 00 000 0 00 00 0 0 000000 00 0 0 00 00 00 0 00 00 0000 0 0 00 0 0 0 00 00000 0 00 00 0 0 00 00 0 0 0000 00 0 0 0 00 0 0 000 00 0 0 000 00 0 0 00 00 00 0 0 00 00 0 00 00 0 0 0000'
print('revisando cadena')
for char in s:
    if(char != '0' and char != ' '):
        print('There is something wrong with the code, please verify')
print('separando cadena')
a = s.split(' ')
index = 0
count = 0
res = ''
arrayLen = len(a)
print('iniciando ciclo', a)
while(True):
    if (index < arrayLen):
        if(a[index] == '0'):
            count = len(a[index + 1])
            res += '1'*count
            index += 2
        elif(a[index] == '00'):
            count = len(a[index + 1])
            res += '0'*count
            index += 2
        print('res', res)
        #break
    else:
        break
a = np.array([x for x in res])
print(a)
a = a.reshape(-1, 7)
res2 = ''
s2 = ''
for i in a:
    for j in i:
        s2 += j
    res2 += chr(int(s2, 2))
    s2 = ''
print(res2)
