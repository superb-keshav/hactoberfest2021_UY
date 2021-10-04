a= input("To convert into fer write f \nTo convvert into celcius write c : ")
if a=="f":
    c=int(input("temp in cel"))
    print("the tempreture in fer is: " , ((9/5)*c+32) )
else :
    f=int(input("temp in fer: "))
    print("the temp in cel: ", (32*f-32)*(5/9) )
