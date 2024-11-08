Menu_Item={
    'Pasta':90,
    'Coffee':50,
    'Pestry':40,
    'Petties':45,
    'Samosa':15,
    'Cutlet':25,
}

Order_Item=[]

while True:
    print("--------CAFE---MANAGEMENT---SYSTEM----------")
    print("Press 1. for order")

    choice=int(input("Enter your choice:-"))
    if(choice==1):
        Order_total=0
        Slect_item=input("Enter the item you want to order:-")
        if Slect_item in Menu_Item:
            Order_Item+=Slect_item
            Order_total+=Menu_Item[Slect_item]
        else:
            print("Please enter the valid item")
        Ask_order=input("Do you want to order another item?")
        if(Ask_order=='Yes'):
            Slect_item1=input("Enter the second item you want to add:-")
            if Slect_item1 in Menu_Item:
                Order_Item+=Slect_item1
                Order_total+=Menu_Item[Slect_item1]
        else:
            print("Thanks for coming here")
        print("Your ordered items are:",Order_Item)
        print("Total amount of the ordered item is:-", Order_total)

    else:
        print("Invalid choice")
        break