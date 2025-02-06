from datetime import datetime
order=0
grand_total=0
while True:
    print(""" 
              KK'S CAFE MENU
            1)pizza
            2)sandwich
            3)burger
            4)chicken roll
          """)
    items=[]
    costs=[]
    quantities=[]
    orders=[]
    while True:
        user=int(input("enter item id or 0 to exit: "))
        if user==1:
            item="pizza"
            cost=200
        elif user==2:
            item="sandwich"
            cost=80
        elif user==3:
            item="Burger"
            cost=60
        elif user==4:
            item="chicken roll"      
            cost=100
        elif user==0:
            print("Thanks for ordering! Generating a bill")
            break
        else:
            print("Incorrect item id!")
            continue
        quantity=int(input("enter quantity in digits : "))      
        if quantity>0:
            items.append(item)
            costs.append(cost)
            quantities.append(quantity)
        else:
            print("please give quantity in number format! Re-enter the item")    
    sum1=[costs[i]*quantities[i]  for i in range(len(costs))]    
    total=sum(sum1)
    gst=total*0.18
    Total=total+gst
    date=datetime.now().strftime("%d/%m/%Y,%H:%M:%S")
    grand_total+=Total
    order+=1
    
    print(f"""
          
                                 KK'S cafe
    .................................................................................
                                                                  date:{date}
                                                                 order:{order}
    ..................................................................................
         SN    ITEMS                QUANTITY            COST         AMOUNT 
    ...................................................................................    """)
    for i,(item,cost,quantity,amount) in enumerate(zip(items,costs,quantities,sum1),start=1):
        print(f"""      {i:<2}     {item:<15}         {quantity:<10}        {cost:<6}       {amount:<6}""")
    print(f""" 
    ................................................................................
                                                                 TOtal:{total:<10}
                                                                   GST:{gst:.2f}
                                                       TOTAl(INS0_GST):{Total:<10}      
    ...............................................................................
    GRAND_total:{grand_total}
    ...............................................................................""")      
    newoorder=input("Do you want to take another order(yes/no): ").lower()
    if newoorder=="no":
        print(f"Total Revenue Generated Today is : {grand_total}")
        break 

    
          


















