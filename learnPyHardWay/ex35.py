from sys import exit

def gold_room():
    print "This is a room full of gold, how much do you want?"

    choice=raw_input(">>>")
    try:
        how_much=int(choice)
    except:
        dead("Cant you type a number")
    
    if how_much<50:
        print "Nice, you arnt greedy"
        exit(0)
    else:
        dead("You are GREEDY")

def bear_room():
    print "There is a bear here with lot of honey"
    print "what do you want to do?"
    bear_moved=False
    while True:
        choice = raw_input(">>>")

        if choice == "take honey":
            dead("Bear will slap you")
        elif choice == "taunt bear" and not bear_moved:
            print "Cool, the bear ran away"
            bear_moved=True
        elif choice == "taunt bear" and bear_moved:
            dead("Bear got angry, run!!!")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "What the hell is this"

def cthulhu_room():
    print "This is a cosmic evil cthulhu room"
    print "dont stare just run"
    choice = raw_input(">>>")
    if choice == "run":
        start()
    elif "stare" in choice:
        dead("You are finished")
    else:
        cthulhu_room()

def dead(why):
    print why, "Buddy"
    exit(0)

def start():
    print "you are in a dark room, with doors in left and right"
    print "which one are you taking?"

    choice = raw_input(">>>")
    if "left" in choice:
        bear_room()
    elif "right" in choice:
        cthulhu_room()
    else:
        dead("Why are you groping in dark?")

start()