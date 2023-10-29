while(True):
    
    print(" 1 . Summation              ")
    print(" 2 . Difference             ")
    print(" 3 . Product                ")
    print(" 4 . Division               ")
    print(" 5 . Modulus                ")   
    print(" 6 . Exit                   ")
    
    choice = int(input("enter your choice $"))
    if(choice==1):
        nums=list(map(int,input("enter digits $ ").split(" ")))
        sum= 0
        for i in nums:
            sum= sum + i
       
        print("@ Sumation =  ",sum," @")
        

    elif(choice==2):
        n1 = int(input("enter 1st digit $ "))
        n2 = int(input("enter 2nd digit $ "))
        sub = n1 - n2
        print("@ Subtraction =  ",sub," @")
        

    elif(choice==3):
        nums=list(map(int,input("enter digits $").split(" ")))
        mul = 1
        for i in nums:
            mul = mul * i
        
        print("@ Product =  ",mul," @")
        

    elif(choice==4):
        n1 = int(input("enter 1st digit $ "))
        n2 = int(input("enter 2nd digit $ "))
        div = n1 / n2
        print("@ Division =  ",div," @")
        

    elif(choice==5):
        n1 = int(input("enter 1st digit $ "))
        n2 = int(input("enter 2nd digit $ "))
        mod = n1 % n2
        print("@ Modulus =  ",mod," @")

    elif(choice==6):
        exit(0)

    else:
       print("invalid choice , please enter choice between 1 - 6 only")
    
