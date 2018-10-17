import math, cmath, sys, os

def Ldb(a,Cm):
    if(fv>150 and fv<=1500):
        L=69.55+26.16*math.log10(fv)-13.82*math.log10(hbv)-a+(44.9-(6.55*math.log10(hbv)))*math.log10(dv)
    elif(fv>1500 and fv<=2100):
        L = 46.3 + 33.9 * math.log10(fv) - 13.82 * math.log10(hbv) - a + Cm + (44.9 - (
        6.55 * math.log10(hbv))) * math.log10(dv)
    return float(L)
#Définition de Hb
def Hb():
    invalid= True
    while invalid:
        hb = float(input("Enter the Height in meters of the transmitter (from 30 to 300m) : "))
        #Vérification de hb
        if(hb<30 or hb>300):
            print("The height should be between 30 and 300m, please try again")
            invalid=True
        else:
            invalid=False
    return hb

#Définition de Hm
def Hm():
    invalid = True
    while invalid:
        hm = float(input("Enter the height in meter of the receiver (from 1 to 20m): "))
        if (hm < 1 or hm > 20):
            print("The height should be between 1 and 20m, please try again")
            invalid = True
        else:
            invalid = False
    return hm

#Définition de d
def d():
    invalid = True
    while invalid:
        d = float(input("Enter the value of the distance between transmitter and receiver (1 to 20 km): "))
        if (d < 1 or d > 20):
            print("Distance must be between 1 and 20km, please try again")
            invalid = True
        else:
            invalid = False
    return d

def f():
    f = float(input("Enter the value of the frequency (in MHz): "))
    return f
#Menu
def menu():
    print("-----------------------------------------------------------------------")
    print("1 --Small or medium size city")
    print("2 --Large city")
    print("3 --End")
loop=True
while loop:
    menu()
    choice = int(input("Choose a menu entry: "))
    #If city of medium or small size
    Cmv=0
    if (choice == 1):
        os.system("clear")
        print("Small size")
        hbv=Hb()
        hmv=Hm()
        dv=d()
        fv=f()
        Ahm = (1.1 * math.log10(fv) - 0.7) * hmv - (1.56 * math.log10(fv) - 0.8)
        #print(float(Ahm))
        print(Ldb(a=Ahm,Cm=Cmv))
        print("-----------------------------------------------------------------------")
    #Otherwise large city
    elif (choice == 2):
        Cmv=3
        os.system("clear")
        hbv = Hb()
        hmv = Hm()
        dv = d()
        fv = f()
        #If f less than 200
        if (int(fv) <= 200):
                Ahm = (8.29 * math.pow(math.log10((1.54 * int(hmv))), 2) - 1.1)
            #If f greater than 200
        else:
            if(int(fv<=1500)):
                Ahm = (3.2 * math.pow(math.log10((11.75 * int(hmv))), 2) - 4.97)
            else:
                Ahm = (1.1 * math.log10(fv) - 0.7) * float(hmv) - (1.56 * math.log10(fv) - 0.8)
        print(float(Ahm))
        print(Ldb(a=Ahm,Cm=Cmv))
        print("-----------------------------------------------------------------------")
    elif(choice == 3):
        loop = False
        print("See ya")
        sys.exit
    else:
        print("Incorrect choice")
        menu()



