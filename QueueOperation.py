l=[]

while True:
    c=int(input("""
    1 Push Element
    2 Pop first Element
    3 First Element
    4 Last Element
    5 Display Element
    6 Exit
    """))

    if c==1:
        n=int(input("Enter the Value"))
        l.append((n))
        print(l)


    elif c==2:
        if len(l)==0:
            print('Empty Queue')
        else:
            del l[0]
            print(l)

    elif c==3:
        if len(l)==0:
            print('Empty Queue')
        else:
            print("First Element", +l[0])


    elif c==4:
        if len(l)==0:
            print('Empty Queue')
        else:
           b=len(l)
           print("Last Element ", +l[b-1])



    elif c==5:
        print("Display Element ", l)

    elif c==6:
        break


    else:
        print("Invalid Option")






