bleed = int(input())    # this is the input from the user
poison = int(input())
madness = int(input())

status = "your status is"    #variable for your status

if bleed >= 100:            # if bleeding is equal to 100
 
 status = status + " bleeding"   # your status is bleeding
 
if poison >= 100:           # if poison is equal to 100
  
  status = status + " poison"

if madness >= 100:
    
    status = status + " madness"
    
print(status)
