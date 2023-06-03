from datetime import datetime
name=input("enter yor name: ")
#list of items
lists='''
         rice Rs 25/kg
         salt Rs 20/kg
         panner Rs 100/kg
         oil RS 110/liter
         wheat flour RS 45/kg
         sugar Rs 30/kg
         cumin seeds Rs 50/kg
      '''
#declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
#rates for items
items={'rice':25,'salt':20,'panner':100,'oil':110,'wheat flour':45,'sugar':30,'cumin seeds':50}
option=int(input("for list of items"))
if option==1:
    print(lists)
    for i in range(len(lists)):
        inp1=int(input("press 1 to buy and press 2 to exit: "))
        if inp1==2:
            break
        elif inp1==1:
            item=input("enter items : ")
            quantity=int(input("enter quantity :" ))
            if item in items.keys():
                price=quantity*(items[item])
                pricelist.append((item,quantity,items,price))
                totalprice+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                gst=(totalprice*0.05)
                finalamount=gst+totalprice
            else:
                print("invalid input")
else:
    print("entered wrong number")
inp=input("Bill the items yes/no : ")
if inp=="yes":
    pass
    if finalamount!=0:
        print(25*"=","SUPER MARKET",35*"=")                    
        print(28*" ","VISAKHAPATNAM")                    
        print("Name :",name,30*" ","Date : ",datetime.now())                    
        print(75*"-")   
        print("sno",8*' ','items',8*' ','quantity',3*' ','price')
        for i in range(len(pricelist)):
            print(i,4*' ',5*' ',ilist[i],10*' ',qlist[i],10*' ',plist[i])                 
        print(75*'-')
        print(50*' ','Totalamount :','Rs',totalprice)
        print("gst amount:",40*' ','Rs',gst)
        print(75*' ')
        print(50*' ','finalamount :','Rs',finalamount)
        print(75*"-")
        print(20*" ","Thanks for visiting")
        print(75*"-")
    else:
        print("Done")
else:
    print("Done")            
            