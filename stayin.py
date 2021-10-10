import random
chicken=3
corn=3
olives=3
bread=3
spaghetti=3
soyasauce=3
cheese=3
fish=3
tomato=3
gt=0
dirt=0
cat="not there"
event=random.randint(1,6)
if event==1:
    event="cockroach"
    roaches="active"
    status="safe"
    cockroaches=0
if event==2:
    event="grumbly grumble"
    status="safe"
if event==4:
    event="cat"
    status="safe"
    cat="gone"
hunger=100
fms="clean"
guard=1
mhealth=100
phealth=100
timing=600
morningmed=0
afternoonmed=0
nightmed=0
name=input("what is your name?")
eqipment=["facemask", "gloves", "medication"]
print("your stuff:a facemask, gloves and medication", "you have covid 19 and you must give yourself the medication once in the afternoon, once in the night and once during the morning. Every action takes 15 minutes")
die="false"
while die=="false":
    while timing<=21000:
        act=input("what would you like to do?")
        if act=="desc":
            n="open"
            desc=input("what would you like me to describe?")
            if desc=="medication":
                print("your medication won't cure you but  it will help fight off the virus. It is important for you to take it on time")
            if desc=="facemask":
                print("This will stop you from transmitting the virus to other people. wear it at all times.")
            if desc=="gloves":
                print("This helps keep you sanitized")
        if cat=="true" and act=="pet":
            print("You pet the cat...it activates your allergies. Though the cat is so cute and it makes you happy to pet it")
            mhealth=+25
            phealth=phealth-25
        if act=="take":
            take=input("what would you like to take")
            if take=="food":
                    
                eat=("you take out your food what would you like to do with it?")
                if food>0:
                        
                    if eat=="eat":
                            
                        food=food-1
                        hunger=hunger+foodval[i]
                        foodval.remove(foodval[i])
                        i=i-1
                        dice=random.randint(1,7)
                        if dice==3:
                                
                            phealth=phealth-30
                            print("you... may have accidentally eaten a cockroach")
                            mhealth=mhealth-30
                    elif eat=="inspect":
                        if event=="cockroach" and cockroaches>0:
                                
                            dice=random.randint(1,7)
                            if dice==3:
                                f="there"
                                while f=="there":                                        
                                    coc=input("you found and caught the cockroach. What would you like to do with it?")
                                    if coc=="kill":                                                                                     
                                        print("the cockroach is desd")
                                        food=food-1
                                        mhealth=mhelath-5
                                        f="Notthere"
                                    elif coc=="throw away":
                                        print("you threw it away for some other unluck person")
                                        food=food-1
                                        mhealth=mhealth-5
                                        f="notthere"
                                    else:
                                        print("re-enter")                                    
                        elif event=="grumbly grumble":
                            dice=random.randint(1,7)
                            if dice==4:                                
                                hunger=hunger-30
                        elif status=="safe":                            
                            if foodcondition=="spolied":                                                                    
                                print("The food is spolied, you throw it out")
                                food=food-1
                                mhealth=mhealth-5
                            else:                                
                                print("The food isn't spoiled")
                else:
                    print("you have no food, but you can still make food.")
            elif take=="facemask":
                fm=input("what would you like to do with your facemask?")
                if fm=="put on":
                    print("You put on your face mask.")
                    guard=2
                    mhealth=mhealth+10
                    f="facemask"
                elif fm=="inspect":
                    if fms=="dirty":
                        print("the  face mask is dirty. Clean it")
                else:
                    print("re-enter")
                    n="open"
            elif take=="medication":
                print("you took your meds")
                time=timing//10
                if time>=6 and time<=12:
                    morningmed=morningmed+1
                elif time>12 and time<=18:
                    afternoonmed=afternoonmed+1
                elif time>18 and time<=21:
                    nightmed=nightmed+1
            elif take=="gloves":
                print("you wear your gloves. You  somehow feel safer")
                guard=guard+1
                mhealth=mhealth+5
                h="gloves"
            else:
                print("re-enter")
                n="open"
        if act=="wash":
            wash=input("what would you like to wash?")
            if wash=="hands":
                print("You wash your hands. Be sure to sanitize.")
                dirt=dirt-10
            elif wash=="facemask":
                print("you properly wash your  facemask with soap making sure to get any contaminents out.")
                fms="clean"
            if wash=="bath":
                print("you have a nice bath!")
                dirt=dirt-50
                fms="clean"
                gs="clean"
                      
            else:
                print("re-enter")
                n="open"
        if act=="look":        
            print("You look around your room. There is your bed and your desk next to it. Text books are usually nested there but not today. You hav been forced to stay at home and school is out so there is not much to do. There is a cupboard above the desk and shelves bellow. The daunting kitchen is still behind you. Hopefully you have enough ingridients to make food. The window sill lies just above your stove.There are a few cupboars besides the stove and one sink.")
        #roaches is the variable that checks if there are still cockroaches
            if roaches=="active" and cockroaches>0:
                place=input("You still need to find the cockroaches, where would you like to look")
                dice=random.randint(1,11)
                if place=="cupboard":
                    if dice==5:
                        coc=input("you found and caught the cockroach. What would you like to do with it?")
                        if coc=="kill":
                            print("the cockroach is dead")
                            cockroach=cockroach-1
                        elif coc=="throw away":
                            print("you threw it away for some other unluck person")
                            cockroach=cockroach-1
                    else:
                        print("no roach")
                elif place=="shelves":
                    if dice==7:
                        coc=input("you found and caught the cockroach. What would you like to do with it?")
                        if coc=="kill":
                            print("the cockroach is desd")
                            cockroach=cockroach-1
                        elif coc=="throw away":
                            print("you threw it away for some other unluck person")
                            cockroach=cockroach-1
                    else:
                        print("no roach")
                elif place=="stove":
                    if dice==3:
                        coc=input("you found and caught the cockroach. What would you like to do with it?")
                        if coc=="kill":
                            print("the cockroach is desd")
                            cockroach=cockroach-1
                        elif coc=="throw away":
                            print("you threw it away for some other unluck person")
                            cockroach=cockroach-1
                    else:
                        print("no roach")
                elif place=="bed":
                    if dice==8:
                        coc=input("you found and caught the cockroach. What would you like to do with it?")
                        if coc=="kill":
                            print("the cockroach is desd")
                            cockroach=cockroach-1
                        elif coc=="throw away":
                            print("you threw it away for some other unluck person")
                            cockroach=cockroach-1
                    else:
                        print("no roach")
                else:
                    print("please re-enter")
                    n="Open"
            elif event=="cat":
                print("There is some fur on the window sill.")
        if act=="go":
            go=input("where would you like to go?")
            if go=="Bed":
                bed=input("you go to your bed, what would you like to do here?")
                if bed=="sleep":
                    sleep=int(input("enter how many minutes you would like to sleep for."))
                    timing=(sleep/15)*250+timing
                elif bed=="sit":
                    print("you sit down and reflect on life.")
            elif go=="desk":
                desk=input("you go to your desk and take a seat. What would you like to do?")
                if desk=="study":
                    print("You decide to study.")
                    mhealth=mhealth+5
                elif desk=="read":
                    print("you read a book It is calming")
                    mhealth=mhealth+5
            elif go=="kitchen":
                kitchen=input("what would you like to do in the kitchen")
                if kitchen=="wash":
                    print("you decide to wash the kitchen")
                    dirt=dirt-10
                    if cockroaches>0:
                        roache=("you found a cockroach, what would you like to do with it?")
                        cockroach=cockroach-1
                        if roache=="kill":
                            print("You kill it")
                        if roache=="throw  out":
                            print("you throw it out for some other unlucky person")
        if act=="cook":
            print("Choose your ingridients!")
            i1=print("choose from, chicken, spaghetti and fish. pick 1 for chicken, 2 for spaghetti and 3 for fish. 0 if you don't want to add anything.")
            i2=print("choose from, cheese, bread and soy sauce. pick 1 for cheese, 2 for bread and 3 for soy sauce. 0 if you don't want to add anything.")
            i3=print("choose from, olives, tomato and corn. pick 1 for olives, 2 for tomato and 3 for corn. 0 if you don't want to add anything.")
#remember to add all the checks to see if  the ingridient is out
            if i1==1:
                if chicken>0:
                    foodval=foodval+30
                    chicken=chicken-1
                if chicken<1:
                    print("You've run out of chicken")
            elif i1==2:
                if spaghetti>0:
                    foodval=foodval+20
                    spaghetti=spaghetti-1
                if spaghetti<1:
                    print("You've run out of spaghetti")
            elif i1==3:
                if fish>0:
                    foodval=foodval+10
                    fish=fish-1
                if chicken<1:
                    print("You've run out of fish")
            elif i2==1:
                if cheese>0:
                    foodval=foodval+25
                    cheese=cheese-1
            elif i2==2:
                if bread>0:
                    foodval=foodval+15
                    bread=bread-1
            elif i2==3:
                if soysauce>0:
                    foodval=foodval+5
                    soysauce=soysauce-1
            elif i3==1:
                if olives>0:
                    foodval=foodval+20
                    olives=olives-1
            elif i3==2:
                if tomato>0:
                    foodval=foodval+14
                    tomato=tomato-1
            elif i3==3:
                if corn>0:
                    foodval=foodval+3
                    corn=corn-1
            elif i1==0 and i2==0 and i3==0:
                print("guess you don't want to eat then.")
            elif foodval>0:
                foodval.append(foodval)
                i=i+1
            else:
                print("please re-enter")
                n="open"
        realtime=timing//100
        if realtime%4==0 and event=="cockroaches":
        
            cockroaches=cockroaches+random.randint(1,4)
            print("Oh no, a cockroach infestation. You now have:", cockroaches)
        l=random.randint(1,3)
        if gt==timing and event=="cat":
            cat="gone"
            print("the cat is now gone...")
        if timing%100==0 and l==2 and event=="cat":
            print("the cat has come by your window, he'll stay here for the window. Don't pet it unless you want to activate your allergies. You feel happy already")
            t=timing
            mhealth=mhealth+5
            cat="present"
            gt=t+1000
        goingtime=gt
        n=random.randint(1,20)
        if n>=1 and n<=4:
            sleepy=input("you feel sleepy, would you like to sleep for half an hour? If not, you'll be faced with a worse  physical health")
            if sleepy=="sleep" or sleepy=="yes":
                timing=timing+250
            if sleepy=="don't sleep" or "no":
                phealth=phealth-15
        if n>=5 and n<=8:
            vent=input("the ventilation shaft is clogged. Would you like to clean it. The virus is airborn after all. you can pick from a yes or a no")
            if vent=="yes":
                dirt=dirt-10
                print("you got some dirt on you, atleast the room is well ventilated.")
                mhealth=mhealh+5
            if vent=="no":
                dirt=dirt-20
                guard=guard-1
                phealth=phealth-5
                print("you don't feel that good")
        if n>=9 and n<=12:
            dog=input("you here a dog barking out. Would you like to chase it away? warning:by saying yes, you will be both endangering yourself and other.")
            if dog=="yes":
                newguard=guard
                newguard=newguard-1
                phealth=phealth-(50-(newguard*10))
                dirt=dirt+10
                print("You scared the dog off.")
            if dog=="no":
                mhealh=mhealth-10
                print("the barks are very annoying but stop after a while.")
        if n>=13 and n<=16:
            person=input("there is a person at the door with food. Would you like to let them in. yes or no")
            if person=="yes":
                print("you let them in.")
                food=food+1
                if guard>=2:
                    print("you remain at a far away distance of 5 feet when interacting with said person and you are sure to not come in contact. You feel happy that they are safe.")
                    mhealth=mhealth+5
                if guard<2:
                    print("you stay close to the person. You may have given them the virus. You feel anxious that you did.")
                    mhealth=mhealth-5
            if person=="no":
                print("they go after a while")

        if n>=17 and n<=20:                
            productive=input("you feel your creative spirit fester! Would you like to do anything?")                      
            if productive=="no":                      
                print("you feel even worse than before.")
                mhealth=mhealth-20
            if productive=="yes":
                do=input("what would you like to do? would you like to read, draw or write")                  
                if do=="read":
                      print("you feel more vigorated after reading!")
                      mhealth=mhealth+6                      
                if do=="draw":
                      print("you feel more vigorated after drawing!")
                      mhealth=mhealth+random.randinnt(1,10)         
                if do=="write":
                      print("you feel more vigorated after reading!")
                      mhealth=mhealth+6
                else:
                    print("re-enter")
        if event=="grumbly grumble":
            if timing%100==0:
                hungry=hungry-10
        if timing%200==0 and event=!"cockroaches":
            hungry=hungry-10
        if cockroaches<1 and event=="cockroaches":
            roaches="inactive"
            print("huzzah, all the roaches are dead")

        mhealth=mhealth-(dirt/2)
        phealth=phealth-(dirt/2)
            
              
        if phealth>100:
            print("You are mentally better than ever")
        if mhealth>50 and phealth<=100:         
            print("you are mentally doing fine")
        if mhealth>0 and phealth<=50:  
            print("please take better mental care of yourself. Read a book or something.")
        if mhhealth<=0: 
            print("You are mentally unwell. You decide to sleep for the rest of your day. GAME OVER")
            die="true"
        if morningmed>1 or afternoonmed>1 or nightmed>1:              
            print("OH NO YOU TOOK TOO MUCH MEDICATION. You will now have to sleep. GAME  OVER")
            die="true"
        if phealth>100:
            print("You are physically better than ever")
        if phealth>50 and phealth<=100:         
            print("you are physically doing fine")
        if phealth>0 and phealth<=50:  
            print("please take better care of yourself. I suggest trying to stay clean.")
        if phhealth<=0:
            print("You are mentally unwell. You decide to sleep for the rest of your day. GAME OVER")
            die="true"
        if roaches=="active":
            if h=="gloves":
                rng1=random.randint(1,7)
                if rng>=3 and rng<=5:
                    gs="dirty"
            if f=="facemask":
                rng=random.randint(1,7)
                if rng>=1 and rng<=2:
                    fms="dirty"
        if dirt>50:
            foodcondition="spoiled"
        if fms=="dirty":
            dirt=dirt+5
        if gs=="dirty":
            dirt=dirt+5
    

        if n=="close":
            timing=timing+250
    
        print("time is", timing//100,":", (timing%100)/250*15)
    if mhealth>=50 and mhealth<=100:
        print("you did well mentally. Just stay in there. It  is all going to  be fine.")
    if mhealth>0 and mhealth<50:
        print("your mentally not that good. Take it better next time. Alright?")
    if mhealth>100:
        print("you did really well mentally today. That is great. I hope you continue being in a bright and sunny mood.")
    if phealth>=50 and phealth<=100:
        print("you did fine physically. You will hopefully get well soon.")
    if phealth>0 and phealth<50:
        print("your physically not doing all that well. I suggest trying to do our best by contining to eat healthy and  making sure your room is well sanitized.")
    if phealth>100:
        print("You did great physically, you might even be recovering at a rapid pace if I musy say myself.")
    if dirt>50:
        print("also, take a bath please!"


        
