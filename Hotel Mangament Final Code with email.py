import random
import datetime
from email.message import EmailMessage
import ssl
import smtplib



# Global List Declaration
name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
discount=[]
proof=[]
rc = []
lc= []
gc=[]
cc=[]
bc=[]
p=[]
roomno = []
custid = []
day = []

# Global Variable Declaration
i = 0
# Home Function
def Home():
        
        print("\t\t\t\t\t\t WELCOME TO HOTEL ROYAL PARK\n")
        print("\t\t\t 1 Booking\n")
        print("\t\t\t 2 Rooms Info\n")
        print("\t\t\t 3 Restaurant\n")
        print("\t\t\t 4 Cafe\n")
        print("\t\t\t 5 Bar\n")
        print("\t\t\t 6 Laundry\n")
        print("\t\t\t 7 Games\n")
        print("\t\t\t 8 Payment\n")
        print("\t\t\t 9 Records\n")
        print("\t\t\t 0 Exit\n")
       

        ch=int(input("->"))
        
        if ch == 1:
                print(" ")
                Booking()
        
        elif ch == 2:
                print(" ")
                Rooms_Info()
        
        elif ch == 3:
                print(" ")
                restaurant()

        elif ch == 4:
                print(" ")
                cafe()

        elif ch == 5:
                print(" ")
                bar()
        
        elif ch == 6:
                print(" ")
                Laundry()
        
        elif ch == 7:
                print(" ")
                Game()

        elif ch == 8:
                print(" ")
                Payment()

        elif ch == 9:
                print(" ")
                Record()
        
        
        else:
                exit()

# Function used in booking

def date(c):
        
        if c[2] >= 2022 and c[2] <= 2022:
                
                if c[1] != 0 and c[1] <= 12:
                        
                        if c[1] == 2 and c[0] != 0 and c[0] <= 31:
                                
                                if c[2]%4 == 0 and c[0] <= 29:
                                        pass
                                
                                elif c[0]<29:
                                        pass
                                
                                else:
                                        print("Invalid date\n")
                                        name.pop(i)
                                        phno.pop(i)
                                        add.pop(i)
                                        rc.pop(i)
                                        lc.pop(i)
                                        gc.pop(i)
                                        cc.pop(i)
                                        bc.pop(i)
                                        checkin.pop(i)
                                        checkout.pop(i)
                                        Booking()
                        
                        
                        # if month is odd & less than equal
                        # to 7th month
                        elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:
                                pass
                        
                        # if month is even & less than equal to 7th
                        # month and not 2nd month
                        elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2:
                                pass
                        
                        # if month is even & greater than equal
                        # to 8th month
                        elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:
                                pass
                        
                        # if month is odd & greater than equal
                        # to 8th month
                        elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:
                                pass
                        
                        else:
                                print("Invalid date\n")
                                name.pop(i)
                                phno.pop(i)
                                add.pop(i)
                                rc.pop(i)
                                lc.pop(i)
                                gc.pop(i)
                                cc.pop(i)
                                bc.pop(i)
                                checkin.pop(i)
                                checkout.pop(i)
                                Booking()
                                
                else:
                        print("Invalid date\n")
                        name.pop(i)
                        phno.pop(i)
                        add.pop(i)
                        lc.pop(i)
                        gc.pop(i)
                        cc.pop(i)
                        bc.pop(i)
                        checkin.pop(i)
                        checkout.pop(i)
                        Booking()
                        
        else:
                print("Invalid date\n")
                name.pop(i)
                phno.pop(i)
                add.pop(i)
                lc.pop(i)
                gc.pop(i)
                cc.pop(i)
                bc.pop(i)
                checkin.pop(i)
                checkout.pop(i)
                Booking()


# Booking function
def Booking():
        
                # used global keyword to
                # use global variable 'i'
                global i
                print(" BOOKING ROOMS")
                print(" ")
                
                while 1:
                        n = str(input("Name: "))
                        p1 = str(input("Phone No.: "))
                        a = str(input("Address: "))
                        print("Type of ID")
                        print("1 Aadhar Card")
                        print("2 Voter ID Card")
                        print("3 Passport")
                        pr= str(input("ID: "))
                        if pr == "1":
                            aadhar=str(input("Enter your Aadhar Card Number: "))
                            proof.append(aadhar)
                        elif pr =="2":
                            voter=str(input("Enter your Voter ID Card Number: "))
                            proof.append(voter)
                        elif pr == "3":
                            passport=str(input("Enter Your Passport number: "))
                            proof.append(passport)
                        else:
                            print("Wrong Choice")
                        
                        
                                 
                        
                        # checks if any field is not empty
                        if n!="" and p1!="" and a!="":
                                name.append(n)
                                add.append(a)
                                
                                
                                break
                                
                        else:
                                print("\tName, Phone no. and Address  cannot be empty..!!")
                        
                cii=str(input("Check-In (DD/MM/YYYY): "))
                checkin.append(cii)
                cii=cii.split('/')
                ci=cii
                ci[0]=int(ci[0])
                ci[1]=int(ci[1])
                ci[2]=int(ci[2])
                date(ci)
                
                coo=str(input("Check-Out (DD/MM/YYYY): "))
                checkout.append(coo)
                coo=coo.split('/')
                co=coo
                co[0]=int(co[0])
                co[1]=int(co[1])
                co[2]=int(co[2])
                
                # checks if check-out date falls after
                # check-in date
                if co[1]<ci[1] and co[2]<ci[2]:
                        
                        print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
                        name.pop(i)
                        add.pop(i)
                        lc.pop(i)
                        gc.pop(i)
                        cc.pop(i)
                        bc.pop(i)
                        checkin.pop(i)
                        checkout.pop(i)
                        Booking()
                elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
                        
                        print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
                        name.pop(i)
                        add.pop(i)
                        lc.pop(i)
                        gc.pop(i)
                        cc.pop(i)
                        bc.pop(i)
                        checkin.pop(i)
                        checkout.pop(i)
                        Booking()
                else:
                        pass
                
                date(co)
                d1 = datetime.datetime(ci[2],ci[1],ci[0])
                d2 = datetime.datetime(co[2],co[1],co[0])
                d = (d2-d1).days
                day.append(d)
                
                print("----SELECT ROOM TYPE----")
                print(" 1. Standard Non-AC")
                print(" 2. Standard AC")
                print(" 3. 3-Bed Non-AC")
                print(" 4. 3-Bed AC")
                print(("\t\tPress 0 for Room Prices"))
                
                ch=int(input("->"))
                
                # if-conditions to display alloted room
                # type and it's price
                if ch==0:
                        print(" 1. Standard Non-AC - Rs. 3500")
                        print(" 2. Standard AC - Rs. 4000")
                        print(" 3. 3-Bed Non-AC - Rs. 4500")
                        print(" 4. 3-Bed AC - Rs. 5000")
                        ch=int(input("->"))
                if ch==1:
                        room.append('Standard Non-AC')
                        print("Room Type- Standard Non-AC")
                        price.append(3500)
                        print("Price- 3500")
                elif ch==2:
                        room.append('Standard AC')
                        print("Room Type- Standard AC")
                        price.append(4000)
                        print("Price- 4000")
                elif ch==3:
                        room.append('3-Bed Non-AC')
                        print("Room Type- 3-Bed Non-AC")
                        price.append(4500)
                        print("Price- 4500")
                elif ch==4:
                        room.append('3-Bed AC')
                        print("Room Type- 3-Bed AC")
                        price.append(5000)
                        print("Price- 5000")
                else:
                        print(" Wrong choice..!!")


                # randomly generating room no. and customer
                # id for customer
                rn = random.randrange(40)+300
                cid = random.randrange(40)+10
                
                
                # checks if alloted room no. & customer
                # id already not alloted
                while rn in roomno or cid in custid:
                        rn = random.randrange(60)+300
                        cid = random.randrange(60)+10
                        
                rc.append(0)
                lc.append(0)
                gc.append(0)
                cc.append(0)
                bc.append(0)
                p.append(0)
                                
                if p1 not in phno:
                        phno.append(p1)
                elif p1 in phno:
                        for n in range(0,i):
                                if p1== phno[n]:
                                        if p[n]==1:
                                                phno.append(p1)
                elif p1 in phno:
                        for n in range(0,i):
                                if p1== phno[n]:
                                        if p[n]==0:
                                                print("\tPhone no. already exists and payment yet not done..!!")
                                                name.pop(i)
                                                add.pop(i)
                                                lc.pop(i)
                                                gc.pop(i)
                                                cc.pop(i)
                                                bc.pop(i)
                                                checkin.pop(i)
                                                checkout.pop(i)
                                                Booking()
                print("")
                print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
                print("Room No. - ",rn)
                print("Customer Id - ",cid)
                roomno.append(rn)
                custid.append(cid)
                i=i+1
                n=int(input("0-BACK\n ->"))
                if n==0:
                        Home()
                else:
                        exit()

# ROOMS INFO
def Rooms_Info():
        print("          ------ HOTEL ROOMS INFO ------")
        print("")
        print("STANDARD NON-AC")
        print("---------------------------------------------------------------")
        print("Room amenities include: 1 Double Bed, Television, Telephone,")
        print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
        print("an attached washroom with hot/cold water.\n")
        print("STANDARD NON-AC")
        print("---------------------------------------------------------------")
        print("Room amenities include: 1 Double Bed, Television, Telephone,")
        print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
        print("an attached washroom with hot/cold water + Window/Split AC.\n")
        print("3-Bed NON-AC")
        print("---------------------------------------------------------------")
        print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
        print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
        print("Side table, Balcony with an Accent table with 2 Chair and an")
        print("attached washroom with hot/cold water.\n")
        print("3-Bed AC")
        print("---------------------------------------------------------------")
        print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
        print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
        print("1 Side table, Balcony with an Accent table with 2 Chair and an")
        print("attached washroom with hot/cold water + Window/Split AC.\n\n")
        print()
        n=int(input("0-BACK\n ->"))
        if n==0:
                Home()
        else:
                exit()

# RESTAURANT FUNCTION
def restaurant():
        ph=int(input("Customer Id: "))
        global i
        f=0
        r=0
        for n in range(0,i):
                if custid[n]==ph and p[n]==0:
                        f=1
                        print("------------------------------------------------------------------------------------------------------------")
                        print("                                              HOTEL ROYAL PARK")
                        print("------------------------------------------------------------------------------------------------------------")
                        print("                                               Restraunt Menu")
                        print("------------------------------------------------------------------------------------------------------------")
                        print("\n SOUPS                                   MAIN COURSE                          RICE                        ")       
                        print("-----------------------------------       -------------------------------       ----------------------------")       
                        print("1  Tomato Soup.............. 150.00       21 Dal Fry.............. 200.00       41 Plain Rice........ 150.00")      
                        print("2  Hot and Sour Soup........ 150.00       22 Dal Makhani.......... 250.00       42 Zeera Rice........ 150.00")       
                        print("3  Veg Noodle Soup.......... 150.00       23 Dal Tadka............ 200.00       43 Peas Pulao........ 200.00")                                        
                        print("4  Sweet Corn Soup.......... 150.00       24 Shahi Paneer......... 350.00       44 Vegetable Pulao... 250.00")                                       
                        print("5  Veg Munchow Soup......... 150.00       25 Kadhai Paneer........ 350.00       45 Chicken Biryani... 450.00")                                       
                        print("6  Chicken Munchow Soup..... 200.00       26 Paneer Butter Masala. 350.00       46 Mutton Biryani.... 500.00")                                        
                        print("                                          27 Malai Kofta.......... 350.00                                   ")      
                        print(" STARTERS                                 28 Mix Veg.............. 350.00        SALAD                      ")                                               
                        print("-----------------------------------       29 Kadhai Chicken....... 450.00        ---------------------------")                                                                          
                        print("7  Tandoori Soya Chaap...... 250.00       30 Butter Chicken....... 450.00        47 Green Salad...... 150.00")                                                                         
                        print("8  Tandoori Paneer Tikka.... 350.00       31 Mutton Curry......... 500.00        48 Fruit Salad...... 200.00")                                                                         
                        print("9  Mushroom Tikka........... 300.00       32 Mutton Rogan Gosh.... 500.00        49 Onion Salad...... 100.00")                                                                         
                        print("10 Hara Bhara Kabab......... 250.00       33 Fish Curry........... 500.00                                   ")                                                                       
                        print("11 Cheese Kabab............. 300.00       34 Egg Curry............ 300.00        RAITA                      ")                                                                      
                        print("12 Honey Chilli Cauilflower. 200.00                                              ---------------------------")                                                                         
                        print("13 Honey Chilli Potato...... 200.00       INDIAN BREADS                          50 Pineapple Raita.. 200.00")                                                                         
                        print("14 French Fries............. 200.00       -------------------------------        51 Boondi Raita..... 150.00")
                        print("15 Fish Tikka............... 400.00       35 Tandoori Roti......... 25.00        52 Mix Raita........ 200.00") 
                        print("16 Fish Finger.............. 400.00       36 Tandoori Butter Roti.. 25.00                                   ")
                        print("17 Chicken Tandoori......... 400.00       37 Lacha Parantha........ 50.00        INDIAN SWEETS              ")
                        print("18 Chilli Chicken........... 400.00       38 Naan.................. 50.00        ---------------------------")
                        print("19 Chicken Seekh Kabab...... 400.00       39 Butter Naan........... 75.00        53 Gulab Jamun...... 100.00")
                        print("20 Chicken Lollipop......... 400.00       40 Garlic Naan........... 75.00        54 Rasmalai......... 150.00")
                        print("Press 0 -to end ")
                        ch=1
                        while(ch!=0):
                                
                                ch=int(input(" -> "))
                               
                                if ch==35 or ch==36:
                                        rs=25
                                        r=r+rs
                                elif ch==37 or ch==38:
                                        rs=50
                                        r=r+rs
                                elif ch==39 or ch==40:
                                        rs=75
                                        r=r+rs
                                elif ch==49 or ch==53:
                                        rs=100
                                        r=r+rs
                                elif ch==41 or ch==42 or ch==47 or ch==51 or ch==54 or (ch>=1 and ch<=5):
                                        rs=150
                                        r=r+rs
                                
                                elif ch==6 or (ch>=12 and ch<=14) or ch==21 or ch==23 or ch==43 or ch==48 or ch==50 or ch==52:
                                        rs=200
                                        r=r+rs

                                elif ch==7 or ch==10 or ch==22 or ch==44:
                                       
                                        rs=250
                                        r=r+rs

                                elif ch==9 or ch==11 or ch==34:
                                        rs=300
                                        r=r+rs

                                elif ch==8 or (ch>=24 and ch<=28):
                                        rs=350
                                        r=r+rs

                                elif (ch>=15 and ch<=20):
                                        rs=400
                                        r=r+rs

                                elif ch==29 or ch==30 or ch==45:
                                        rs=450
                                        r=r+rs

                                elif (ch>=31 and ch<=33) or ch==46:
                                        rs=500
                                        r=r+rs

                                elif ch==0:
                                        pass
                                else:
                                        print("Wrong Choice..!!")
                        print("Total Bill: ",r)
                       
                        
                        # updates restaurant charges and then
                        # appends in 'rc' list
                        r=r+rc.pop(n)
                        rc.append(r)
                        
                else:
                        pass
        
        if f == 0:
                print("Invalid Customer Id")
        n=int(input("0-BACK\n ->"))
        if n==0:
                Home()
        else:
                exit()
        
# CAFE FUNCTION
def cafe():
        ph=int(input("Customer Id: "))
        global i
        f=0
        c=0
        for n in range(0,i):
                if custid[n]==ph and p[n]==0:
                        f=1
                        print("------------------------------------------------------------------")
                        print("                           HOTEL ROYAL PARK")
                        print("------------------------------------------------------------------")
                        print("                              Cafe Menu")
                        print("------------------------------------------------------------------")
                        print("HOT COFFEE                            COOKIES                     ")       
                        print("---------------------------------     ----------------------------")       
                        print("1  Espresso............... 150.00     18 Biscotti........... 50.00")      
                        print("2  Classic Filter Coffee.. 150.00     19 Sugar Cookie....... 50.00")       
                        print("3  Macchiato.............. 150.00     20 Chocolate Chip..... 50.00")                                              
                        print("4  Cafe Americano......... 150.00     21 Honey & Oatmeal.... 50.00")                                         
                        print("5  Cafe Mocha............. 150.00                                 ")                                           
                        print("6  Cappuccino............. 150.00     WRAP                        ")                                        
                        print("7  Cafe Latte............. 150.00     ----------------------------")      
                        print("                                      22 Paneer Wrap....... 250.00")                                               
                        print("COLD COFFEE                           23 Veg Wrap.......... 200.00")                                                                          
                        print("---------------------------------     24 Chicken Wrap...... 300.00")                                                                         
                        print("8  Cafe Frappe............ 200.00                                 ")                                                                         
                        print("9  Dark Frappe............ 250.00     SANDWICHES                  ")                                                                         
                        print("10 Cappuccino Cold Coffee. 200.00     ----------------------------")                                                                       
                        print("11 Cold Brewed Coffee..... 250.00     25 Cheese Corn....... 150.00")                                                                      
                        print("12 Mocha Smothie.......... 300.00     26 Tandoori Paneer... 200.00")                                                                                                                                         
                        print("                                      27 Grilled Cheese.... 150.00")
                        print("COOKIES                               28 Barbeque Chicken.. 250.00")
                        print("---------------------------------     29 Tandoori Chicken.. 250.00")                                                       
                        print("13 Kadak Chai........... 100.00                                   ")
                        print("14 Masala Chai.......... 150.00       BURGER                      ")
                        print("15 Green Tea............ 150.00       ----------------------------")
                        print("16 Darjeeling Tea....... 150.00       30 Veg Cheese........ 200.00")
                        print("17 Assam Tea............ 150.00       31 Chicken Cheese.... 300.00")
                        print("Press 0 -to end ")
                        ca=1
                        while(ca!=0):
                                
                                ca=int(input(" -> "))
                               
                                if (ca>=18 and ca<=21):
                                        cs=50
                                        c=c+cs
                                elif ca==13:
                                        cs=100
                                        c=c+cs
                                elif (ca>=1 and ca<=7) or (ca>=14 and ca<=17) or ca==25 or ca==27:
                                        cs=150
                                        c=c+cs
                                elif ca==8 or ca==10 or ca==23 or ca==26 or ca==30:
                                        cs=200
                                        c=c+cs
                                
                                elif ca==9 or ca==11 or ca==22 or ca==28 or ca==29:
                                        cs=250
                                        c=c+cs

                                elif ca==12 or ca==24 or ca==31:
                                        cs=300
                                        c=c+cs

                                elif ca==0:
                                        pass
                                else:
                                        print("Wrong Choice..!!")
                        print("Total Bill: ",c)
                       
                        
                        # updates restaurant charges and then
                        # appends in 'rc' list
                        c=c+cc.pop(n)
                        cc.append(c)    
                else:
                        pass
        if f == 0:
                print("Invalid Customer Id")
        n=int(input("0-BACK\n ->"))
        if n==0:
                Home()
        else:
                exit()
        
# BAR FUNCTION
def bar():
        ph=int(input("Customer Id: "))
        global i
        f=0
        b=0
        for n in range(0,i):
                if custid[n]==ph and p[n]==0:
                        f=1
                        print("-----------------------------------------------------------------------------------------------------")
                        print("                                       HOTEL ROYAL PARK")
                        print("-----------------------------------------------------------------------------------------------------")
                        print("                                            Bar Menu")
                        print("-----------------------------------------------------------------------------------------------------")
                        print("STANDARD SCOTCH (30ml)                 BRANDY(30ml)                     MOCKTAILS                    ")       
                        print("----------------------------------     ----------------------------     -----------------------------")       
                        print("1  Black Dog Black Reserve. 400.00     16 Honey Bee......... 300.00     31 Blush Pina Colada.. 250.00")      
                        print("2  Black and White......... 400.00     17 Henessy VS........ 500.00     32 Blue Angle......... 250.00")       
                        print("3  VAT 69.................. 400.00                                      33 Purple Rain........ 250.00")                                              
                        print("4  100 Pipers.............. 400.00     DOMESTIC BEER(330ml)             34 Cranberry Fizz..... 250.00")                                         
                        print("                                       ----------------------------     35 Passion on Fire.... 250.00")
                        print("PREMEIUM WHISKEY                       18 Kingfisher Ultra.. 350.00     36 Friut Punch........ 250.00")                                                                    
                        print("----------------------------------     19 Kingfisher Light.. 300.00     37 Virgin Mojito...... 250.00")                                                                    
                        print("5  Antiquity Blue.......... 350.00     20 Kingfisher Strong. 300.00     38 Strawberry Suprise. 250.00")      
                        print("6  Signature Premier....... 350.00     21 Heineken.......... 350.00                                  ")                 
                        print("7  Signature Rare.......... 300.00                                      COCKTAILS                    ")                                                                          
                        print("8  Blenders Pride Reserve.. 350.00     IMPORTED BEER(330ml)             -----------------------------")                                                                         
                        print("9  Blenders Pride.......... 300.00     ----------------------------     39 Cosmopolitan....... 500.00")                                                                         
                        print("                                       22 Corona............ 500.00     40 Black Russian...... 500.00")                                                                         
                        print("PRESTIGE WHISKEY(30ml)                 23 Inedit Damn....... 500.00     41 Bloody Mary........ 500.00")                                                                       
                        print("----------------------------------     24 Budwieser......... 450.00     42 Bull Frog.......... 500.00")                                                                      
                        print("10 Royal Challenge Bolt.... 250.00                                      43 Mud Slide.......... 500.00")                                                                                                             
                        print("11 Royal Challenge......... 250.00     RUNNERS                                                       ")
                        print("                                       ----------------------------     RUM BASE COCKTAILS           ")
                        print("RUM                                    25 Red Bull.......... 200.00     -----------------------------")                            
                        print("----------------------------------     26 Lemon Ice Tea..... 150.00     44 Mojito............. 600.00")                                                      
                        print("12 Captain Morgan.......... 300.00     27 Diet Pepsi........ 100.00     45 Pina Colada........ 600.00")                            
                        print("13 Bacardi White........... 300.00     28 Tonic Water....... 150.00     46 Weng Weng.......... 600.00")
                        print("14 Bacardi Flavour......... 300.00     29 Soda.............. 100.00     47 Daiquiri........... 600.00")
                        print("15 Old Monk................ 250.00     30 Aerated Drinks.... 100.00     48 Mai Tai............ 600.00")
                        print("Press 0 -to end ")
                        ba=1
                        while(ba!=0):
                                
                                ba=int(input(" -> "))
                               
                                if ba==29 or ba==30:
                                        bs=100
                                        b=b+bs
                                elif ba==26 or ba==28:
                                        bs=150
                                        b=b+bs
                                elif ba==25:
                                        bs=200
                                        b=b+bs
                                elif ba==10 or ba==11 or ba==15 or (ba>=31 and ba<=38):
                                        bs=250
                                        b=b+bs
                                
                                elif ba==7 or ba==9 or (ba>=12 and ba<=14) or ba==16 or ba==19 or ba==20:
                                        bs=300
                                        b=b+bs

                                elif ba==5 or ba==6 or ba==8 or ba==18 or ba==21:
                                        bs=350
                                        b=b+bs

                                elif (ba>=1 and ba<=4):
                                        bs=400
                                        b=b+bs

                                elif ba==24:
                                        bs=450
                                        b=b+bs

                                elif ba==17 or ba==22 or ba==23 or (ba>=39 and ba<=43):
                                        bs=500
                                        b=b+bs

                                elif (ba>=44 and ba<=48):
                                        bs=600
                                        b=b+bs

                                elif ba==0:
                                        pass
                                else:
                                        print("Wrong Choice..!!")
                        print("Total Bill: ",b)
                       
                        
                        # updates restaurant charges and then
                        # appends in 'rc' list
                        b=b+bc.pop(n)
                        bc.append(b)    
                else:
                        pass
        if f == 0:
                print("Invalid Customer Id")
        n=int(input("0-BACK\n ->"))
        if n==0:
                Home()
        else:
                exit()
        
# Laundry FUNCTION
def Laundry():
        ph=int(input("Customer Id: "))
        global i
        f=0
        l=0
        for n in range(0,i):
                if custid[n]==ph and p[n]==0:
                        f=1
                        print("---------------------------")
                        print("   HOTEL ROYAL PARK")
                        print("---------------------------")
                        print("     Laundry Card")
                        print("---------------------------")
                        print(" 1 Shirt.......... 250.00")        
                        print(" 2 T Shirt........ 200.00")        
                        print(" 3 Trouser........ 250.00")       
                        print(" 4 Shorts......... 150.00")       
                        print(" 5 Coat........... 500.00")        
                        print(" 6 Girls Suit..... 400.00")        
                        print("Press 0 -to end ")
                        lh=1
                        while(lh!=0):
                                
                                lh=int(input(" -> "))
                                
                                # if-elif-conditions to assign item
                                # prices listed in menu card
                                if lh == 1:
                                    ls=250
                                    l=l+ls
                                elif lh == 2:
                                    ls=200
                                    l=l+ls
                                elif lh == 3:                                  
                                    ls=250
                                    l=l+ls
                                elif lh == 4:
                                    ls=150
                                    l=l+ls
                                elif lh == 5:
                                    ls=500
                                    l=l+ls
                                elif lh == 6:
                                    ls=400
                                    l=l+ls
                                elif lh==0:
                                        pass
                                else:
                                        print("Wrong Choice..!!")
                        print("Total Laundry Bill: ",l)
                    
                        
                        # updates laundry charges and then
                        # appends in 'lc' list
                        l=l+lc.pop(n)
                        lc.append(l)    
                else:
                        pass
        if f == 0:
                print("Invalid Customer Id")
        n=int(input("0-BACK\n ->"))
        if n==0:
                Home()
        else:
                exit()

# Games FUNCTION
def Game():
        ph=int(input("Customer Id: "))
        global i
        f=0
        g=0
        for n in range(0,i):
                if custid[n]==ph and p[n]==0:
                        f=1
                        print("---------------------------")
                        print("    HOTEL ROYAL PARK")
                        print("---------------------------")
                        print(" Games Rate Card(per hour)")
                        print("---------------------------")
                        print(" 1 Table Tennis......250.00")        
                        print(" 2 Bowling......... 1000.00")        
                        print(" 3 Snooker.......... 500.00")       
                        print(" 4 Video Games...... 500.00")       
                        print(" 5 Soccer Table..... 300.00")                
                        print("Press 0 -to end ")
                        gh=1
                        while(gh!=0):
                                
                                gh=int(input(" -> "))
                                
                                # if-elif-conditions to assign item
                                # prices listed in menu card
                                if gh == 1:
                                    gs=250
                                    g=g+gs
                                elif gh == 2:
                                    gs=1000
                                    g=g+gs
                                elif gh == 3:                                  
                                    gs=500
                                    g=g+gs
                                elif gh == 4:
                                    gs=500
                                    g=g+gs
                                elif gh == 5:
                                    gs=300
                                    g=g+gs                            
                                elif gh==0:
                                        pass
                                else:
                                        print("Wrong Choice..!!")
                        print("Total Bill: ",g)
                        
                        # updates laundry charges and then
                        # appends in 'lc' list
                        g=g+gc.pop(n)
                        gc.append(g)    
                else:
                        pass
        if f == 0:
                print("Invalid Customer Id")
        n=int(input("0-BACK\n ->"))
        if n==0:
                Home()
        else:
                exit()
                
# RECORD FUNCTION
def Record():
        staffname=str(input("Enter your userame: "))
        if staffname == "Sparsh":
                staffpass=str(input("Enter the passcode: "))
                if staffpass == "1234":
                        if phno!=[]:
                                print("  *** HOTEL RECORD ***\n")
                                print("|      Name      |Cust.Id| Phone No. |   Address  |  Check-In  |  Check-Out  |Room Type| Price |Restaurant|Cafe|Bar|Laundry|Games|  ID  |")
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                
                                for n in range(0,i):
                                        print("|",name[n],"|",custid[n],"\t|", phno[n] ,"\t|",  add[n],"\t|",checkin[n]  ,"|",  checkout[n] ,"|", room[n],"|", (price[n]*day[n]),"|", rc[n],"|",cc[n],"|",bc[n],"|",lc[n],"|", gc[n],"|",proof[n])
                
                                        print("------------------------------------------------------------------------------------------------------------------------------")
        
                        else:
                                print("No Records Found")
                        n = int(input("0-BACK\n ->"))
                        if n == 0:
                                Home()
                
                        else:
                                exit()
                else:
                        print("Wrong Passcode")
                        n=int(input("0-BACK\n ->"))
                        if n == 0:
                                Home()
                        else:
                                exit()
                        
                        
        else:
                print("Wrong Username")
                n= int(input("0-BACK\n ->"))
                if n== 0:
                        Home()
                else:
                        exit()

                        

# PAYMENT FUNCTION                      
def Payment():
        
        ph=str(input("Phone Number: "))
        global i
        f=0
        
        for n in range(0,i):
                if ph==phno[n] :
                        
                        # checks if payment is
                        # not already done
                        if p[n]==0:
                                f=1
                                d=0
                                dis=input("Coupon Code (if not press 0): ")
                                if dis == "ABCDE":
                                    d=d+3000
                                    print("Disocunt of 3000 applied")
                                elif dis == "UVXYZ":
                                    d=d+5000
                                    print("Discount of 5000 applied")
                                elif dis=="0":
                                        pass
                                
                                else:
                                    print("Wrong Coupon Code") 
                                print(" Payment")
                                print(" --------------------------------")
                                print(" MODE OF PAYMENT")
                                
                                print(" 1- Credit/Debit Card")
                                print(" 2- Paytm/PhonePe")
                                print(" 3- Using UPI")
                                print(" 4- Cash")
                                x=int(input("-> "))
                                
                                er=str(input(" Enter your Email ID: "))
                                cost=((price[n]*day[n])+rc[n]+lc[n]+gc[n])
                                g_g=(cost-d)
                                h_h=(0.18 * g_g)
                                total=g_g+h_h
                                print("\n Amount(Inclusive of all Taxes): ",total)
                                print("\n                Pay For Hotel Royal Park")
                                print(" (y/n)")
                                ch=str(input("->"))
                                
                                if ch=='y' or ch=='Y':
                                        print("\n\n --------------------------------")
                                        print("       HOTEL ROYAL PARK")
                                        print(" --------------------------------")
                                        print("             Bill")
                                        print(" --------------------------------")
                                        print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
                                        print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t")
                                        print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t")
                                        print(" Restaurant Charges: ",rc[n])
                                        print(" Cafe Charges: ",cc[n])
                                        print(" Bar Charges: ",bc[n])
                                        print(" Game Charges: ",gc[n])
                                        print(" Laundary Charges: ",lc[n])
                                        print(" --------------------------------")
                                        print(" Discount: ",d)
                                        print(" --------------------------------")                                        
                                        print(" Taxable Amount: ",g_g)                                       
                                        print(" Total Tax(18% GST): ",h_h)
                                        print(" --------------------------------")
                                        print("\n Total Amount: ",total,"\t")
                                        print(" --------------------------------")
                                        print("          Thank You")
                                        print("          Visit Again :)")
                                        print(" --------------------------------\n")
                                        p.pop(n)
                                        p.insert(n,1)
                                        
                                        # pops room no. and customer id from list and
                                        # later assigns zero at same position
                                        roomno.pop(n)
                                        custid.pop(n)
                                        roomno.insert(n,0)
                                        custid.insert(n,0)

                                        #EMAIL
                                        email_sender = 'hotelmanagementpython@gmail.com'
                                        email_password = 'enjkkolzmdryhsnm'
                                        email_receiver = er
                                        subject='Hotel Royal Park Bill'
                                        body='''
                                        print("\n\n --------------------------------")
                                        print("       HOTEL ROYAL PARK")
                                        print(" --------------------------------")
                                        print("             Bill")
                                        print(" --------------------------------")
                                        print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
                                        print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t")
                                        print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t")
                                        print(" Restaurant Charges: ",rc[n])
                                        print(" Cafe Charges: ",cc[n])
                                        print(" Bar Charges: ",bc[n])
                                        print(" Game Charges: ",gc[n])
                                        print(" Laundary Charges: ",lc[n])
                                        print(" --------------------------------")
                                        print(" Discount: ",d)
                                        print(" --------------------------------")                                        
                                        print(" Taxable Amount: ",g_g)                                       
                                        print(" Total Tax(18% GST): ",h_h)
                                        print(" --------------------------------")
                                        print("\n Total Amount: ",total,"\t")
                                        print(" --------------------------------")
                                        print("          Thank You")
                                        print("          Visit Again :)")
                                        print(" --------------------------------\n")
                                        '''
                                        

                                        
                                        

                                        em= EmailMessage()
                                        em['From']=email_sender
                                        em['To']= email_receiver
                                        em['Subject']=subject
                                        em.set_content(body)

                                        context=ssl.create_default_context()

                                        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                                            smtp.login(email_sender, email_password)
                                            smtp.sendmail(email_sender, email_receiver, em.as_string())
                                        
                                        
                                        
                        else:
                                
                                for j in range(n+1,i):
                                        if ph==phno[j] :
                                                if p[j]==0:
                                                        pass
                                                
                                                else:
                                                        f=1
                                                        print("\n\tPayment has been Made :)\n\n")
        if f==0:        
                print("Invalid Customer Id")
                
        n = int(input("0-BACK\n ->"))
        if n == 0:
                Home()
        else:
                exit()                    
                        



# Driver Code
Home()
