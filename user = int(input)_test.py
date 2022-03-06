bleed = int(input())
poison = int(input())
madness = int(input())

status = "your status is"

if bleed >= 100:
 
 status = status + " bleeding"
 
if poison >= 100:
  
  status = status + " poison"

if madness >= 100:
    
    status = status + " madness"
    
print(status)