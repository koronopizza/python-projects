# im going to make a temp meter

humidity = int(input())

x = humidity

if (x == 0) and (x >= 30):

    print("very cold")

elif (x >= 31) and (x <= 63):

    print("put on some layers")

elif (x >= 64) and (x <= 79):

    print("the perfect summer day")

elif (x >= 80) and (x <= 90):

    print("caution very hot!")

elif (x >= 91) and (x <= 103):

    print("extreme caution very hot!!") 

elif (x >= 104) and (x <= 124):

    print("danger caution very hot!!!")

else: 
    (x > 125)

    print("caution very hot")       