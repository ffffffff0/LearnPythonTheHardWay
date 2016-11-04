from sys import exit

#在right和left之中的选择
def gold_room():
    print("This room is full of gold . How much do you take ?")
    next = input("> ")
    if "0" in next or "1" in next :
        how_much = int(next)
    else:
        dead("Man , learn to type a number")

    if how_much < 50:
        print("Nice , you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

#left的选择
def bear_room():
    print("There is a bear here")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")
        if next == "take honey":
            dead("The bear looks at you then slaps you face off")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has monved from the door .You can go through it now")
            bear_moved = True
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")

#right的选择
def cthulhu_room():
    print("Here you see  the great evil Ctthlju")
    print("He , it ,whatever  stares at you and you goinsane")
    print("Do you  flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

#死亡函数,并打印文字
def dead(why):
    print (why,"good job!")
    exit(0)

#开始程序,并提供选择
def start():
    print("You are in a dark room")
    print("There is a door to your right and left")
    print("which one do you take ?")

    next = input("> ")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble aroud the room until you starve")

#启动程序
start()
          
          
