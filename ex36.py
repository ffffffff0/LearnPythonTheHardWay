from sys import exit

def reward():
    print("waht is you lost gold ,silver or iron?")
    flowers = ["flower","flower","flower","rose","rose","money"]
    next = input("> ")
    if "gold" in next or "iron" in next:
        print("well down ,boy ,you win!")
        print("flower"*5)
        exit(0)
        for flower in flowers:
            print(flower)
        exit(0)
    elif "silver" in next:
        dead("boy, too yong too simple")
    else:
        dead("boy,you will be over!")


def dead(why):
    print(why, "too young")
    exit(0)

def yangguandao():
    print("welcome to yangguandao !")
    print("young man ,i am a god")
    print("Do you have lost something?")
    print("careful  answer!")

    lost = False
    while True:
        next = input("> ")

        if next == "yes":
            print("you say yes,you should say YES ")
            lost = True
        elif next == "no":
            print("you can go ")
            exit(0)
        elif next == "YES" and lost:
            reward()
        else:
            dead("boy, you must have a choose,to be or  not to be")

def guimenguan():
    print("welcome to guimenguan")
    print("young man ,there have a black bear")
    print("the bear have much honey")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")

    lost_bear = False

    while True:
        next = input("> ")

        if next == "take honey":
            print("young man ,you are brave ")
            dead("but you will be over")
        elif next == "taunt bear":
            print("young man ,the doot wil be open")
            lost_bear = True
        elif next == "open door" and lost_bear:
            print("flower"*10)
            print("well down , young man you win")
            exit(0)
        else:
            dead("young man, you word not in my dictionary")

def start():
    print("young man,this is have two road")
    print("left or right ???")
    print("you must have a choose")
    next = input("> ")

    if next == "left":
        yangguandao()
    elif next == "right":
        guimenguan()
    else:
        dead("I got no idea what that means.")
        


start()
            


    
    
