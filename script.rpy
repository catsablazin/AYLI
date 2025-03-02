# The script of the game goes in this file.

# defining characters 
define reader = Character("[readerName]", color = "#808080")
define l = Character("[lucyName]", color = "#ff0400")
define hk = Character("[hackuName]", color = "#bdbed7")
define ha = Character("[haliName]", color = "#9e0e8b")
define v = Character("[vynName]", color = "#1a1a1a")
define r = Character("[raiName]", color = "#b06400")

# names
default readerName = "You"
default lucyName = "Creepy kid"
default hackuName = "Unconsious person"
default haliName = "Pissed off girl"
default vynName = "Heart sunglasses wearer"
default raiName = "Cautious dude"

# trust levels
default lucyTrust = 1
default hackuTrust = 0
default raiTrust = -1
default haliTrust = 0
default vynTrust = 0

# evidence
default clockClue = False # destroyed grandfather clock is found
default footPrintClue = False # found footprints
default cameraClue = False # found vyn's camera
default deathClue = False # finding out that shugo is bleeding out
default hairClue = False # found white hair
default numClues = 0

#important
default glassClue = False # the big glass shard that was used to kill shugo

# rooms that were visited
default roomHali = False
default roomVyn = False
default roomLucy = False
default roomRai = False
default roomHacku = False

# eye opening
define eyesopen = ImageDissolve("eye", 5.0)
define eyesclose = ImageDissolve("eye", 2.0, reverse = True)
define fade = Fade(0.5, 1.0, 0.5)

label start:
    #play music "ringing"
    scene black
    "..."
    scene reader room with eyesopen
    "...Urgh"
    scene reader room with eyesclose

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene reader room
    show kani
    play music "thinking-music.mp3"

    jump introduction
    $ readerName = renpy.input("What is your name?")
    $ readerName = readerName.strip()
        
    #cannot be these names 
    while readerName == "Lucy" or readerName == "lucy" or readerName == "Hali" or readerName == "hali" or readerName == "Hacku" or readerName == "hacku" or readerName == "Vyn" or readerName == "vyn" or readerName == "Rai" or readerName == "rai":
        "Hmm.."
        $ readerName = renpy.input("That doesn't seem right, enter another name")
        $ readerName = readerName.strip()
    
    hk "Pleased to meet you, [readerName]!"
    $ hackuName = "Hacku"
    hk "My name is Hacku."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    ha "Nice to meet you [readerName]."
    $ haliName = "Hali"
    ha "I am Hali."

    v "Ello [readerName]!"
    $ vynName = "Vyn"
    v "The name is Vyn."

    l "Yay! A new friend!!"
    $ lucyName = "Lucy"
    l "My name is Lucy!"

    r "..."
    $ raiName = "Rai"
    r "I'm Rai"
    r "I guess."

    return


label introduction:
    #scene mansion house 3
    "{i}SLAM{i}" with hpunch
    "!!!"
    reader "Oh... the door just closed all of a sudden."
    
    #mini choice thing
    menu:
        "What should I do now?"

        "Try to open the door":
            #play door struggle
            "The door doesn't budge."
            reader "Ugh, whatever."
            "You give up and start to walk down the hallway."
        "Continue to walk down the hallway":
            "You start to walk down the hallway."
    "test test more test"
    return
    #scene hallway with fade yay




label faint:
    scene black with fade
    #play the ringing noise
    reader "I feel so dizzy right now.."
    "My body swayed as a I heard something fall onto the ground."
    "If it wasn't clear enough, I was the thing that fell onto the ground."
    reader "Shit.. my head hurts so bad.."
    "Well.."
    "That wasn't suposes to happen."
    "{b}Bad Ending{/b}."
    
    menu:
        "Do you want to start again?"

        "Yes":
            jump start
        "No":
            return


label greetings:


label name:


label checkLucy:
    #kitchen / or garade whatever, whereever there is art ig

label checkRai:
    #the furthest room from whereever lucy is

label checkHali:
    #one room next to vyn

label checkVyn:
    #on the couch or fireplace (the main room while everyone else splits away)

label checkHacku:
    #one of the open bedrooms that was mysteriously left open
    #the murder weapon glass shard is in there

label endCredits:
    #scene my room
    #show happy me
    "Thank you for playing my game!"

    #show 
    "This is the first time I ever made my own game"
    "I'd like to thank my friends for testing my game"
    "Y'all are the best"
    #show bow me
