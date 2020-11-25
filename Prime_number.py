number=int(input("Enter your number: "))
if number==2:
    print("Prime")
elif number%2==0:
    print("Not Prime")
elif number>1:
    for i in range(3,number):
        if number%i==0:
            print("Not Prime")
    else :
        print("Prime")