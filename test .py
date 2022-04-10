i = 0
  # these are the variables    
x = "tacocat"
  # this is the count of the variable "tacocat"
y = len(x)-1 #6
  #this loop compares both sides of the variable    
while i < y + 1 : 
    if x[i] != x[y - i]:
        print('false!')
        break   # stops the loop
    i += 1      # increases the count or iteration
