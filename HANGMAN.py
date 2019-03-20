"""
>>>  NAME            : R.ANURAG PILLAI
>>>  CLASS\SECTION   : XII-B
>>>  ROLL NUMBER     : 6645709
>>>  HOUSE           : KAVERI
>>>  SCHOOL          : DELHI PUBLIC SCHOOL, RISALI SECTOR, BHILAI
>>>  SUBJECT TEACHER : ZUNJANI SIR
"""

# module used

import random
import turtle
from pickle import dump, load

# intro

print"""
   ||    ||   //\\\   ||\   ||  //////  ||\    /||   //\\\   ||\   ||
   ||    ||  //  \\\  ||\\\  || ||       ||\\\  //||  //  \\\  ||\\\  ||
   |||||||| ||====|| || \\\ || ||  |||| || \\\// || ||====|| || \\\ ||
   ||    || ||    || ||  \\\|| ||   ||  ||      || ||    || ||  \\\||
   ||    || ||    || ||   \\||  \\\\\\\\||  ||      || ||    || ||   \||
"""
print "-"*70
print "ABOUT THE GAME"
print "-"*70
print
print "In Hangman, You need to guess the Word by entering one Letter at a time."
print
print "I)  You have 6 warnings within which you need to guess the word."
print "II) You will be given 2 hints :"
print "\t1 - First Hint : At The Starting of the game."
print "\t2 - Second Hint : After 3 Wrong Guesses."
print "-"*70

# hangman animation function

def frame():

    ''' starts drawing window '''
	
    turtle.setup(500,400,0,0)
    turtle.title("HANGMAN")
    turtle.pencolor((70,32,102))
    turtle.color((70,32,102))
    turtle.speed('0')
    turtle.pu()
    turtle.goto(-170,140)
    turtle.pd()
    turtle.write("""||    ||   //\\\   ||\   ||  //////  ||\    /||   //\\\   ||\   ||
||    ||  //  \\\  ||\\\  || ||       ||\\\  //||  //  \\\  ||\\\  ||
|||||||| ||____|| || \\\ || ||  |||| || \\\// || ||____|| || \\\ ||
||    || ||    || ||  \\\|| ||   ||  ||      || ||    || ||  \\\||
||    || ||    || ||   \\||  \\\\\\\\||  ||      || ||    || ||   \||""",font=("Courier New", 6, "bold"))
    turtle.pu()
    turtle.goto(0,0)
    turtle.pd()
    turtle.ht()
    turtle.lt(90)
    turtle.fd(80)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(240)
    turtle.lt(90)
    turtle.fd(30)
    turtle.rt(180)
    turtle.fd(60)

def face():

    ''' draws face '''
	
    turtle.pu()
    turtle.goto(0,0)
    turtle.setheading(180)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(21)
    turtle.end_fill()
    turtle.pu()
    turtle.circle(22,180)
    turtle.pd()
    
def body():

    ''' draws body '''
	
    turtle.setheading(270)
    turtle.fd(50)
    turtle.bk(50)

def hand1():

    ''' draws first hand '''
	
    a=turtle.pos()
    turtle.fd(15)
    turtle.lt(30)
    turtle.fd(30)
    turtle.rt(30)
    turtle.fd(3)
    turtle.pu()
    turtle.goto(a)
    turtle.pd()

def hand2():

    ''' draws second hand '''
	
    b=turtle.pos()
    turtle.fd(15)
    turtle.rt(30)
    turtle.fd(30)
    turtle.lt(30)
    turtle.fd(3)
    turtle.pu()
    turtle.goto(b)
    turtle.pd()

def leg1():

    ''' draws first leg '''
	
    c=turtle.pos()
    turtle.fd(50)
    turtle.lt(25)
    turtle.fd(35)
    turtle.rt(25)
    turtle.pu()
    turtle.goto(c)
    turtle.pd()

def leg2():

    ''' draws second leg '''
	
    d=turtle.pos()
    turtle.fd(50)
    turtle.rt(25)
    turtle.fd(35)
    turtle.lt(25)
    turtle.pu()
    turtle.goto(d)
    turtle.pd()

def func(x):

    ''' draws hangman based move variable used in play() function '''
	
    if x==1:
        face()
		
    if x==2:
        body()
		
    if x==3:
        hand1()
		
    if x==4:
        hand2()
		
    if x==5:
        leg1()
		
    if x==6:
        leg2()
        
# wordlist and other variables

global mode
global usr
global words_h
global words_e
global words

ofile=open("words.dat","rb")
words_group=load(ofile)          # word dictionary
words_e=(words_group[0])         # easy - words
words_h=(words_group[1])         # hard - words
ofile.close()

mode=0                      # difficulty [default - easy]
words=words_e
usr=None                    # None <--> Guest User

# functions

def userbase():

    ''' defines userbase '''
	
    ofile=open("user.dat","rb")
    d1=load(ofile)
    ofile.close()
	
    return d1

def change_pass(usr):

    ''' changes password for a user '''
	
    print"-"*70
    print "CHANGE PASSWORD"
    print"-"*70
	
    d1=userbase()
	
    print "Your Old Password is :",d1[usr][0]
    d1[usr][0]=raw_input("Enter New Password :")
    ofile=open("user.dat","wb")
    dump(d1,ofile)
    ofile.close()
	
    print "-"*70
    
def login():

    ''' for login of old users '''
	
    print"-"*70
    print"OLD USER"
    print"-"*70
	
    d1=userbase()
    usr=raw_input("Enter Username :")
	
    if usr in d1:
        n=0
		
        while n<>4:
		
            pass_key=raw_input("Enter Password :")
			
            if pass_key==d1[usr][0]:
                print
                print "Welcome -",usr
                print "-"*70
                return usr
                break
				
            else:
                print
                print "Wrong Password !!!!! Try Again......."
                n+=1
				
    else:
        print
        print "Invalid Username, Try Again Later"
		
    print "-"*70
    
def newuser():

    ''' to add new users '''
	
    print"-"*70
    print"NEW USER"
    print"-"*70
	
    d1=userbase()
    n=0
	
    while n<>4:
	
        usr=raw_input("Enter Username :")
		
        if usr not in d1:
		
            pass_key=raw_input("Enter Password :")
            d1[usr]=[pass_key,0,0,0,0,0]
            print "Welcome -",usr
            ofile=open("user.dat","wb")
            dump(d1,ofile)
            ofile.close()
			
            print "-"*70
            return usr
            break
			
        else:
		
            print "Username-",usr,"Already Taken, Please Try Another Login Id"
            n+=1
			
    print "-"*70
    
def stats():

    ''' to display stats '''
	
    d1=userbase()
	
    print"-"*70
    print"Statistics"
    print"-"*70
    print "NAME","\t","PLAYTIME","\t",
    print "WINS","\t","LOSES","\t","WINS IN EASY","\t","WINS IN HARD"
    print"-"*70
	
    for i in d1:
        print i,"\t",d1[i][1],"\t\t",d1[i][2],"\t",d1[i][3],"\t",d1[i][4],"\t\t",d1[i][5]
		
    print"-"*70
    
def win():

    ''' to change user stats after winning a game '''
	
    global usr
	
    if usr<>None:
	
        d1=userbase()
        d1[usr][1]+=1
        d1[usr][2]+=1
		
        if mode==0:
            d1[usr][4]+=1
        if mode==1:
            d1[usr][5]+=1
			
        ofile=open("user.dat","wb")
        dump(d1,ofile)
        ofile.close()
		
def lose():

    ''' to change user stats after losing a game '''
	
    global usr
	
    if usr<>None:
        d1=userbase()
        d1[usr][1]+=1
        d1[usr][3]+=1
        ofile=open("user.dat","wb")
        dump(d1,ofile)
        ofile.close()
        
def difficulty():

    ''' to change difficulty of game '''
	
    global mode
    global words
    global words_h
    global words_e
    global usr
	
    a=["EASY","HARD"]
    print"-"*70
    print "CHANGE DIFFICULTY"
    print"-"*70
    print "CURRENT DIFFICULTY -",a[mode]
    print "press 1 - to change difficulty"
    print "press 2 - to continue at same difficulty\n"
	
    e=input("Enter Reponse :")
	
    if e==1:
        if mode==0:
            mode=1
            print "Difficulty Changed To -",a[mode]
            words=words_h
        elif mode==1:
            mode=0
            print "Difficulty Changed To -",a[mode]
            words=words_e
    else:
        print"Difficulty -",a[mode]
		
    print"-"*70
  
def menu():

    ''' main menu for the game '''
	
    global mode
    global words
    global words_h
    global words_e
    global usr
	
    mode=0
    words=words_e
    usr=None
	
    while True:
	
        if usr==None:
		
            print "MAIN MENU"
            print "-"*70
            print
            print "Select any one option :"
            print
            print "1 - Old User"
            print "2 - New User"
            print "3 - Play as Guest"
            print "4 - Change Difficulty"
            print "5 - Statistics"
            print "6 - EXIT"
            print
			
            e=raw_input("Enter Response :")
            
            while e not in ["1","2","3","4","5","6"]:
                print "Wrong Response........"
                e=raw_input("Enter Response Again :")
                
            if e=="1":
                usr=login()
				
            if e=="2":
                usr=newuser()
				
            if e=="3":
                play()
				
            if e=="4":
                difficulty()
				
            if e=="5":
                stats()
				
            if e=="6":
                print "-"*70
                print "Thank You For Playing This Game ............."
                _e=raw_input("")                       ##############
                break
            
        else:
		
            print "MAIN MENU"
            print "-"*70
            print
            print "Select any one option :"
            print
            print "1 - Play"
            print "2 - Change Password"
            print "3 - Change Difficulty"
            print "4 - Statistics"
            print "5 - Log out"
            print "6 - EXIT"
            print
			
            e=raw_input("Enter Response :")
            
            while e not in ["1","2","3","4","5","6"]:
                print "Wrong Response........"
                e=raw_input("Enter Response Again :")
                
            if e=="1":
                play()
				
            if e=="2":
                change_pass(usr)
				
            if e=="3":
                difficulty()
				
            if e=="4":
                stats()
				
            if e=="5":
                usr=None
                print "-"*70
				
            if e=="6":
                print "-"*70
                print "Thank You For Playing This Game ............."
                _e=raw_input("")                        # press return to quit
                try:
                    turtle.bye()
                except:
                    break
                break
            

def play():

    ''' the main game of hangman '''

    global mode
    global words
    global words_h
    global words_e
    global usr

    print "-"*70
    print "HANGMAN GAME"
    print "-"*70
	
    turtle.pensize(10)
    turtle.colormode(255)
    turtle.bgcolor((253,247,227))
    frame()
    turtle.pensize(8)
	
    wordlist=words.keys()                               # words key from dictionary of word
    gw=wordlist[random.randint(0,len(words)-1)].upper() # word to guess
    gt=words[gw.lower()]                                # 2 hints for the word
	
    print
    print "                      "," _"*len(gw)
    print
	
    blk="_"*len(gw)                                     # blanks representing the word
    n=None
    move=0                                              # determines nos of warnings
    blank=list(blk)
    g=list(gw)
    ltr=[]
	
    print "!!--> HINT 1 :", gt[0].capitalize()
	
    while move<6 and "_" in blank:
	
        n=0
        print
        print "-->WARNING LEFT : ",(6-move)
        y=(raw_input("Enter A Letter : ")).upper()
        print
		
        if y!="" and y.isalpha():
            y=y[0]
            
            if y not in ltr:
                ltr.append(y)
				
                for i in range(len(g)):
                    if y==g[i]:
                        blank[i]=y
                        n+=1
						
                if y not in g:
                    move+=1
                    print "!!! LETTER NOT FOUND !!!"
					
                print"\t",
				
                for i in range (len(blank)):
                    print blank[i],
					
                func(move)
                print
				
            else:
                print"!!! Letter Already Tried Once, PLease Try Another Letter !!!"
                print 
				
        else:
		
            print "!! Please Enter A Proper Character !!"
            print 
			
        if move==3:
            print
            print "!!--> HINT 2 :", gt[1].capitalize()
			
    if move==6:
        print
        print"            !! YOU LOSE !!. The Word Was :",gw.upper()
        lose()
		
    else:
        print
        print"            !! YOU WIN !!. The Word Was :",gw.upper()
        win()
		
    print
    print "-"*70
	
    turtle.reset()

# Program Runtime

menu()

# ---- end of program code ----#
