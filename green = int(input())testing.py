green = int(input())      # this will tell how much exp you have
blue = int(input())
red = int(input())

status = "your status is"

if green > 0 and green <= 25:   # this is the range of green
 
 status = status + " your new"
 
if blue >= 26 and blue <= 75:   # this is the range of blue
  
  status = status + " your average"

if red >= 76 and red <=100:     # this is the range of red
    
    status = status + " your seasoned"
    
print(status)
