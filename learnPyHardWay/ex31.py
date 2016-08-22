print "you are entering a dark room, with two doors. In which door you want to enter"
door = raw_input(">>> ")
try:
    door = int(door)
    if door == 1:
        print "There is a bear here"
        print "1. Scream"
        print "2. Run"
        bear = raw_input(">>> ")
        if bear == "1":
            print "Bear got scared"
        elif bear == "2":
            print "You are scared"
        else:
            print "you are stuck with a bear"

    elif door == 2:
        print "Leads you to a room full of snakes"
        print "1. Light up the room with fire"
        print "2. Do nothing, you are doomed"
        snake = raw_input(">>> ")
        if snake == "1":
            print "You are saved buddy"
        elif snake == "2":
            print "Thats a sad end"
    else:
        print "You have only two rooms"
except:
    print "Cant you enter a number"