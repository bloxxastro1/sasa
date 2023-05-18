def sasa (t,x,y):
    a = ('addition', 'subtraction', 'multiplication', 'division', 'floor_division', 'mode')
    print (a)
    if t == 0:
        print (x+y)
    elif t == 1:
        print (x-y)
    elif t == 2:
        print (x*y)
    elif t == 3:
        print (x/y)
    elif t == 4:
        print (x//y)
    elif t== 5:
        print (x%y)
    else:
        print ("choose from 0 to 5 ")


