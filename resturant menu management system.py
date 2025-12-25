fast_food={"Burger":200,"Pizza":300}
BBQ={"Tikka":200,"Boti":250}
Chinees={"chowmein":180,"Fried Rice":220}
summary={}
while True:
    print("Welcome to Smart Restaurant Ordering System :")
    print("Please follow the steps to place your order :")
    print("select the food catagory :")
    print("1....> Fast Food :")
    print("2....> BBQ       :")
    print("3...> Chinees    :")
    c=int(input("Select the catagory or to view the orders press 0 :"))
    if c==1:
        print("1....> Burger(200) :")
        print("2....> Pizza(300)  :")
        o1=input("Enter your choice Pizza or Burger :")
        if o1=="Burger":
            q=int(input("Enter the quantity :"))
            t_q=q*200
            summary[o1]=t_q
            print("Your order is placed :")
            x1=input("x for Exist: o for continue order or 0 to view order list :")
            if x1=="x":
                print("Your order is being created just wait :")
                break
            elif x1=="0":
                for i in summary.items():
                    print(i)
                y=input("Do you want to further order or exist Yes/No :")
                if y=="No":
                    print("Your order is being created just wait :")
                    break
                elif y=="Yes":
                    print("Enter the details :")
        elif o1=="Pizza":
            q=int(input("Enter the quantity :"))
            t_q=q*300
            summary[o1]=t_q
            print("Your order is placed :")
            x1=input("x for Exist: o for continue order or 0 to view order list :")
            if x1=="x":
                print("Your oder is being created just wait:")
                break
            elif x1=="0":
                for i in summary.items():
                    print(i)
                y=input("Do you want to futher order or exist Yes/No")
                if y=="No":
                    print("Your order is being created just wait :")
                    break
                elif y=="Yes":
                    print("Enter the details :")
    elif c==2:
        print("1....> Tikka(200) :")
        print("2....> Botti(250) :")
        o2=input("Enter the choice Tikka or Botti :")        
        if o2=="Tikka":
            q=int(input("Enter the quantity :"))
            t_q=q*200
            summary[o2]=t_q
            print("Your order is placed :")
            x1=input("x for Exist: o for continue order or 0 to view order list :")
            if x1=="x":
                print("Your oder is being created just wait:")
                break
            elif x1=="0":
                for i in summary.items():
                    print(i)
                y=input("Do you want to futher order or exist Yes/No")
                if y=="No":
                    print("Your order is being created just wait :")
                    break
                elif y=="Yes":
                    print("Enter the details :")            
        elif o2=="Botti":
             q=int(input("Enter the quantity :"))
             t_q=q*250
             summary[o2]=t_q
             print("Your order is placed :")
             x1=input("x for Exist: o for continue order or 0 to view order list :")
             if x1=="x":
                print("Your oder is being created just wait:")
                break
             elif x1=="0":
                for i in summary.items():
                    print(i)
                y=input("Do you want to futher order or exist Yes/No")
                if y=="No":
                    print("Your order is being created just wait :")
                    break
                elif y=="Yes":
                    print("Enter the details :")
        else:
            print("Invalid input :")    
    elif c==3:
        print("1....> Chowmein(180) :")
        print("2....> Fried Rice(220) :")
        o2=input("Enter the choice Chowmein or Fried Rice :")        
        if o2=="Chowmein":
            q=int(input("Enter the quantity :"))
            t_q=q*180
            summary[o2]=t_q
            print("Your order is placed :")
            x1=input("x for Exist: o for continue order or 0 to view order list :")
            if x1=="x":
                print("Your oder is being created just wait:")
                break
            elif x1=="0":
                for i in summary.items():
                    print(i)
                y=input("Do you want to futher order or exist Yes/No")
                if y=="No":
                    print("Your order is being created just wait :")
                    break
                elif y=="Yes":
                    print("Enter the details :")
        elif o2=="Fried Rice":
            q=int(input("Enter the quantity in plates :"))
            t_q=q*220             
            summary[o2]=t_q
            print("Your order is placed :")
            x1=input("x for Exist: o for continue order or 0 to view order list :")
            if x1=="x":
                print("Your oder is being created just wait:")
                break
            elif x1=="0":
                for i in summary.items():
                    print(i)
                y=input("Do you want to futher order or exist Yes/No")
                if y=="No":
                    print("Your order is being created just wait :")
                    break
                elif y=="Yes":
                    print("Enter the details :")
        else:
            print("Invalid input :")
    elif c==0:
        for i in summary.items():
            print(i)
    else:
        print("Enter the correct order ")






    
    
    






