while True:
    a = input("\nWelcome to I am Groot Cafe")
    G = input("Enter What would you Like To Have Tea or Coffee\nFor TEA '1'\nFor COFFEE '2'\nEnter No.: ")
    if(G == '1'):
        print("\nWhich Tea do You want")
        b = input("Press '1' For Milk Tea \nPress '2' for Green Tea\nEnter No.: ")
        if(b== '1'):
            print("\nPlease select Your Milk Tea Quantity")
            c = input("Press 1 for SMALL '(RS.70)'\nPress 2 for MEDIUM '(100)'\nPress 3 for LARGE '(130)'\nEnter No.: ")
            if(c == '1'):
                print("How many SMALL cups do you want")
                d = int(input("Enter Number of cups: "))
                e = 70
                print("Your total is",d*e)
                print("Thank you for your visit")
            elif(c == '2'):
                print("How many MEDIUM cups do you want")
                f = int(input("Enter Number of cups: "))
                g = 100
                print("Your total is",f*g)
                print ("Thank you for your visit")
            elif(c == '3'):
                print("How many LARGE cups do you want")
                h = int(input("Enter Number of cups: "))
                i = 130
                print("Your total is",h*i)
                print("Thank you for your visit")
            else:
                 print("I am Groot")
        elif(b== '2'):
            print("\nPlease select Your Green Tea Quantity")
            x = input("Press 1 for SMALL '(RS.80)'\nPress 2 for MEDIUM '(110)'\nPress 3 for LARGE '(150)'\nEnter No.: ")
            if(x == '1'):
                print("How many SMALL cups do you want")
                y = int(input("Enter Number of cups: "))
                z = 80
                print("Your total is",y*z)
                print("Thank you for your visit")
            elif(x == '2'):
                print("How many MEDIUM cups do you want")
                t = int(input("Enter Number of cups: "))
                s = 110
                print("Your total is",t*s)
                print("Thank you for your visit")
            elif(x == '3'):
                print("How many LARGE cups do you want")
                w = int(input("Enter Number of cups: "))
                v = 150
                print("Your total is",w*v)
                print("Thank you for your visit")
            else:
                print("I am Groot")            
    if(G == '2'):
        print("\nWhich Tea do You want")
        j = input("Press '1' For ICE LATTE \nPress '2' for EXPRESSO\nEnter No.: ")
        if(j== '1'):
            print("\nPlease select Your ICE LATTE Quantity")
            k = input("Press 1 for SMALL '(RS.100)'\nPress 2 for MEDIUM '(120)'\nPress 3 for LARGE '(160)'\nEnter No.: ")
            if(k == '1'):
                print("How many SMALL cups do you want")
                l = int(input("Enter Number of cups: "))
                m = 100
                print("Your total is",l*m)
                print("Thank you for your visit")
            elif(k == '2'):
                print("How many MEDIUM cups do you want")
                n = int(input("Enter Number of cups: "))
                o = 120
                print("Your total is",n*o)
                print("Thank you for your visit")
            elif(k == '3'):
                print("How many LARGE cups do you want")
                p = int(input("Enter Number of cups: "))
                q = 160
                print("Your total is",p*q)
                print("Thank you for your visit")
            else:
                print("I am Groot")
        elif(j== '2'):
            print("\nPlease select Your EXPRESSO Quantity")
            r = input("Press 1 for SMALL '(RS.70)'\nPress 2 for MEDIUM '(100)'\nPress 3 for LARGE '(120)'\nEnter No.: ")
            if(j == '1'):
                print("How many SMALL cups do you want")
                u = int(input("Enter Number of cups: "))
                r = 70
                print("Your total is", u*r)
                print("Thank you for your visit")
            elif(j == '2'):
                print("How many MEDIUM cups do you want")
                x = int(input("Enter Number of cups: "))
                S = 100
                print("Your total is", x*S)
                print ("Thank you for your visit")
            elif(j == '3'):
                print("How many LARGE cups do you want")
                X = int(input("Enter Number of cups: "))
                Y = 120
                print("Your total is =", X*Y1)
                print("Thank you for your visit")
            else:
                print("I am Groot")
            ch = int(input("Press 1 for Continue.\nPress 2 for exit "))
            if(ch==1):
                continue
            else:
                break

                                    
                            
                       
                         
                
