green = int(input())
blue = int(input())
red = int(input())

status = "your status is"

if green > 0 and green <= 25:
 
 status = status + " your new"
 
if blue >= 26 and blue <= 75:
  
  status = status + " your average"

if red >= 76 and red <=100:
    
    status = status + " your seasoned"
    
print(status)