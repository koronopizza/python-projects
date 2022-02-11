i = 0
    
x = "tacocat"

y = len(x)-1 #6
#print(y)
    
while i < y + 1 : 
    if x[i] != x[y - i]:
        print('false!')
        break
    i += 1 