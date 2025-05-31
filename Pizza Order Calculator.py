bill = 0
size=input("please choose your pizza size(L,S,M)")
if size == "L":
    bill += 25
elif size == "M":
    bill += 20
elif size == "S" :
    bill += 15
else : 
    print("you typed a wrong letter")
peperoni=input("do you want peperoni on your pizza?(type Y for yes and N for No)")
if peperoni == "Y" :
    if size == "S" :
        bill += 2
    elif size == "M" :
       bill += 3
    elif size == "L" :
        bill += 4
extra_cheese=input("do you want extra cheese? ") 
if extra_cheese == "Y" :
    bill += 1
    print(f"your bill is ${bill}")
else :
    print(f"your bill is ${bill}")