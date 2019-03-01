import sys
import math

message = '%'
b = ''
# convertimos c a binario
# ord() retorna el codigo uncode
# 
# 
for a in enumerate(message):
    print(a[1])
    #b += ''.join(format(ord(a[1]), 'b'))
    b += "{0:07b}".format(ord(a[1]))
 

b = list(b)
print(b, len(b))

# reglas 
# 0 0 (the first series consists of only a single 1)
# 00 0000 (the second series consists of four 0)
# 0 00 (the third consists of two 1)
# 1000011


result = ''
index = 0
index_2 = 0
count = 1

while(True):
    
        
    index_2 = index + count

    if (index_2 < len(b)):
        
        if (b[index_2] == b[index]):
            count +=1  
        else:
            if b[index] == '1':
                result += '0 ' + ('0'*count)+' '
                count = 1
                index = index_2
                index_2 = 0  
            else:   
                result += '00 ' + ('0'*count)+' '
                count = 1
                index = index_2
                index_2 = 0
            
        
    else:
        
        if b[index] == '1':
            result += '0 ' + ('0'*count)+' '
            
        else:
            result += '00 ' + ('0'*count)+' '
        
        break

print(result)
