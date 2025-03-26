# The script of the game goes in this file.

# defining characters 
define reader = Character("[readerName]")
define l = Character("[lucyName]")
define hk = Character("[hackuName]")
define ha = Character("[haliName]")
define v = Character("[vynName]")
define r = Character("[raiName]")

# names
default readerName = "You"
default lucyName = "Creepy kid"
default hackuName = "Unconsious person"
default haliName = "Angry girl"
default vynName = "Happy dude"
default raiName = "Cautious dude"

# trust levels, has to have at least 3 trust points
default lucyTrust = 1
default hackuTrust = 0
default raiTrust = 0
default haliTrust = 0
default vynTrust = 1

# evidence, has to have at least 4 pieces of evidence
default clockClue = False # destroyed grandfather clock is found
default footPrintClue = False # found footprints
default cameraClue = False # found vyn's camera
default deathClue = False # found out about shugo's cause of death
default hairClue = False # found white hair
default ventClue = False # find out how everyone passed out
default numClues = 0

#important
default glassClue = False # the big glass shard that was used to kill shugo

# rooms that were visited, true if not visited, false if visited
default roomHali = True
default roomVyn = True
default roomLucy = True
default roomRai = True
default allRooms = False

# eye opening
define eyesopen = ImageDissolve("eye", 5.0)
define eyesclose = ImageDissolve("eye", 5.0, reverse = True)
define fade = Fade(0.5, 1.0, 0.5)

label start:
    scene black
    "WARNINGS: depictions of murder, arguments about murders, a good amount of cursing, bad comedy, some blood and just anything you can expect from a story about a murderer."
    "This is a fictional story about a murder mystery, silliness and any similarity to real people are completely coincidental."
    menu:
        "Have you read the warnings and acknowledged them?"

        "Yes":
            "Yay!"
            "Now, let's start with the story."

        "No":
            "..."
            "Why are you here then?"
            "Go away."
            return

    #jump checkHacku
    #play music "ringing"
    scene black
    "..."
    scene reader room blurry with eyesopen
    "{i}...Urgh{i}"

    reader "{i}My head is ringing so loudly.{i}"
    "You bring your hand to the back of your head."
    reader "Ow, what the.."
    "You look at your hand and see some smeared blood along your palm."
    reader "{i}What happened to me?{i}"
    reader "{i}And where am I?{i}"
    reader "{i}Ugh, I need to get out of here, but my head really hurts.{i}"

    #you faint after not resting for 5 times in a row   
    menu:
        reader "{i}What should I do?{i}"
        "Look around the room":
            "You get up from the ground but quickly fall back down."
            menu:
                reader "{i}What should I do?{i}"
                "Look around the room":
                    "You get up from the ground but quickly fall back down."
                    menu:
                        reader "{i}What should I do?{i}"
                        "Look around the room":
                            "You get up from the ground but quickly fall back down."
                            menu:
                                reader "{i}What should I do?{i}"
                                "Look around the room":
                                    "You get up from the ground but quickly fall back down."
                                    menu:
                                        reader "{i}What should I do?{i}"
                                        "Look around the room":
                                            "You get up from the ground but quickly fall back down."
                                            jump faint

                                        "Take a small rest":
                                            "You lay down a bit and breathe, letting your head stop ringing."

                                "Take a small rest":
                                    "You lay down a bit and breathe, letting your head stop ringing."

                        "Take a small rest":
                            "You lay down a bit and breathe, letting your head stop ringing."

                "Take a small rest":
                    "You lay down a bit and breathe, letting your head stop ringing."

        "Take a small rest":
            "You lay down a bit and breathe, letting your head stop ringing."

    #stop ringing
    #play music "thinking-music.mp3"
    scene reader room 1 with pixellate
    "You feel better, so you stand up."
    "You look around the room."

    reader "Where the hell am I?"

    menu:
        "Look around the room":
            reader "Hmm.. I guess looking around wouldn't hurt."
            jump lookAround

        "Go straight to the door":
            reader "I better hurry and get out of here."
            reader "No time to look around."
            play sound "footsteps-long.mp3"
            "You walk towards the door."
            jump introduction

default checkLight = False
default checkSofa = False
default checkGlass = False

label lookAround:

    menu:
        "What should you look at first?"

        "Sofa":
            $ checkSofa = True
            play sound "footsteps-short.mp3"
            "You look around the sofa."
            "You find nothing. There is also a lot of dust on it."
            reader "ACHOO!" with vpunch
            
            menu:
                "What should you look at next?"

                "Light":
                    $ checkLight = True
                    "You look at the light."
                    "It isn't very bright and looks like it'll fall apart at any second. It's best to stay cautious."

                    menu:
                        "What should you look at next?"

                        "Rug":
                            jump glassRug
                        
                        "Go to the door":
                            reader "I'm done looking around."
                            reader "I should get out of here."
                            play sound "footsteps-long.mp3"
                            jump introduction

                "Rug":
                    jump glassRug

                "Go to the door":
                    reader "I'm done looking around."
                    reader "I should get out of here."
                    play sound "footsteps-long.mp3"
                    jump introduction

        "Light":
            $ checkLight = True
            "You look at the light."
            "It isn't very bright and looks like it'll fall apart at any second. It's best to stay cautious."
           
            menu:
                "What should you look at next?"

                "Sofa":
                    $ checkSofa = True
                    play sound "footsteps-short.mp3"
                    "You look around the sofa."
                    "You find nothing and there is a lot of dust on it."
                    reader "ACHOO!" with vpunch

                    menu:
                        "What should you look at next?"

                        "Rug":
                            jump glassRug
                        
                        "Go to the door":
                            reader "I'm done looking around."
                            reader "I should get out of here."
                            play sound "footsteps-long.mp3"
                            jump introduction

                "Rug":
                    jump glassRug

                "Go to the door":
                    reader "I'm done looking around."
                    reader "I should get out of here."
                    play sound "footsteps-long.mp3"
                    jump introduction

        "Rug":
            jump glassRug
        
        "Go to the door":
            reader "I'm done looking around."
            reader "I should get out of here."
            play sound "footsteps-long.mp3"
            jump introduction

label glassRug:
    play sound "footsteps-short.mp3"
    "You look around the rug."
    reader "{i}Huh? What's this?{i}"

    #glass shard cg
    "There is a glass shard under the rug."
    menu:
        reader "{i}Should I take that? It looks really sharp.{i}"

        "Take it":
            reader "{i}Well, no harm if I just leave it in my pocket.{i}"
            reader "{i}I just have to remember it's there so I don't cut myself.{i}"
            #picking up glass sound
            "You took the glass shard and put it carefully into your pocket."
            $ glassClue = True
            scene reader room 2
        
        "Leave it":
            reader "{i}Nah, I don't want to accidentally cut myself.{i}"
            "You left the glass shard alone."

    #scene reader room
    if checkSofa == False and checkLight == False:
        menu:
            "What should you look at next?"
            
            "Sofa":
                play sound "footsteps-short.mp3"
                $ checkSofa = True
                "You look around the sofa."
                "You find nothing and there is a lot of dust on it."
                reader "ACHOO!" with vpunch
                
                menu:
                    "What should you look at next?"

                    "Light":
                        "You look at the light."
                        "It isn't very bright and looks like it'll fall apart at any second. It's best to stay cautious."
                    
                    "Go to the door":
                        reader "I'm done looking around."
                        reader "I should get out of here."
                        play sound "footsteps-long.mp3"
                        jump introduction
                
            "Light":
                $ checkLight = True
                "You look at the light."
                "It isn't very bright and looks like it'll fall apart at any second. It's best to stay cautious."

                menu:
                    "What should you look at next?"

                    "Sofa":
                        play sound "footsteps-short.mp3"
                        $ checkSofa = True
                        "You look around the sofa."
                        "You find nothing and there is a lot of dust on it."
                        reader "ACHOO!" with vpunch

                    "Go to the door":
                        reader "I'm done looking around."
                        reader "I should get out of here."
                        play sound "footsteps-short.mp3"
                        jump introduction

            "Go to the door":
                reader "I'm done looking around."
                reader "I should get out of here."
                play sound "footsteps-long.mp3"
                jump introduction       

    elif checkSofa == True and checkLight == False:
        menu: 
            "What should you look at next?"
            
            "Light":
                $ checkLight = True
                "You look at the light."
                "It isn't very bright and looks like it'll fall apart at any second. It's best to stay cautious."

            "Go to the door":
                reader "I'm done looking around."
                reader "I should get out of here."
                play sound "footsteps-long.mp3"
                jump introduction       

    elif checkSofa == False and checkLight == True:
        menu:
            "What should you look at next?"

            "Sofa":
                play sound "footsteps-short.mp3"
                $ checkSofa = True
                "You look around the sofa."
                "You find nothing and there is a lot of dust on it."
                reader "ACHOO!" with vpunch

            "Go to the door":
                reader "I'm done looking around."
                reader "I should get out of here."
                play sound "footsteps-long.mp3"
                jump introduction
    
    reader "{i}I think that's all.{i}"
    reader "{i}It's so dusty in here too, I don't want to spend another minute in here.{i}"

    play sound "footsteps-long.mp3"
    "You start walking to the door."

    jump introduction


label introduction:
    play sound "door-open.mp3"
    scene black with fade
    #scene reader hallway with fade

    play sound "door-slam-1.mp3"
    "{i}{b}SLAM{b}{i}" with vpunch
    "!!!"
    reader "{i}Oh... the door just closed all of a sudden.{i}"
    
    #mini choice thing
    menu:
        reader "{i}What should I do now?{i}"

        "Try to open the door":
            play sound "rattling-door.mp3"
            "The door doesn't budge."
            reader "Ugh, whatever."
            "You give up and start to walk down the hallway."

        "Continue to walk down the hallway":
            "You start to walk down the hallway."
    play sound "footsteps-long.mp3"

    #scene change to main hallway
    "You hear some voices. It sounds like there's an argument."

    #show hali annoyed, vyn talking, lucy thinking, rai ignoring
    ha "Ugh, whatever. I'm not going to listen to an insane person like you."

    v "Hah! Jokes on you, I take that as a compliment."

    #show hali angry
    ha "I'm saying it as an insult!"

    reader "{i}Oh god..{i}"

    menu:
        reader "{i}Should I approach them?{i}"

        "Go up to them and introduce yourself":
            "You start making your way to the group of people."
            "One of them turns around and meets your eyes."
            reader "Um.. Hello?"
            reader "Sorry to interrupt.."
        
        "Wait a bit":
            "You wait a bit further away from them but one of them spots you."
            #show lucy excited
            l "Hey! Another person over there!"
            
    #show hali surpirsed
    ha "Holy shit!"

    #show hali annoyed
    ha "Great, another person because that's just what we needed."
    ha "A creepy cabin that we're all probably going to be killed in and more strangers."

    #show vyn smile
    v "Hahahaha, don't mind her."

    #show hali annoyed 2
    ha "You don't even know me?"
    ha "Stop acting like we're friends."

    v "She's so silly."
    #show vyn hand up
    v "Anyways, sup bro!"

    menu:
        "The person raises his hand for a high five from you."

        "High five the stranger":
            #clap noise
            #show vyn smile
            v "Hell yea man."
            $ vynTrust = vynTrust + 1
        
        "Do nothing":
            v "Awh, but all good bro."

    $ vynName = "Vyn"
    v "Anyways, my name is Vyn."
    v "Nice to meet cha!"

    reader "{i}Oh right, names{i}"
    $ readerName = renpy.input("{i}What was my name again?{i}")
    $ readerName = readerName.strip()
    while readerName == "Lucy" or readerName == "lucy" or readerName == "Hali" or readerName == "hali" or readerName == "Hacku" or readerName == "hacku" or readerName == "Vyn" or readerName == "vyn" or readerName == "Rai" or readerName == "rai" or readerName == "Shugo" or readerName == "shugo":
        "Hmm.."
        $ readerName = renpy.input("That doesn't seem right, enter another name.")
        $ readerName = readerName.strip()

    reader "My name is [readerName], nice to meet you Vyn."

    show lucy wave
    l "Hi hi friend!"
    $ lucyName = "Lucy"
    l "My name is Lucy! I hope we can be good friends!"

    #show rai annoyed
    r "Why the hell would you want to be friends with people who might be the reason why we're even trapped here."
    r "You're also insane for wearing shorts in this type of weather."

    #show lucy happy
    l "Because I love making friends! The more the merrier!"
    l "Also, it isn't cold outside."

    #show rai annoyed 2
    r "You're insane."
    r "Forty degrees is cold as fuck."
    #show rai agrue
    r "And even if it is, it's not weather to be wearing shorts in."

    #show vyn smug
    v "I think our bro is just sensitive to the cold."
    v "Don't be mean to gramps."

    #show rai annoyed
    r "Dude? You're literally wearing-"
    #show rai eye roll
    r "Ugh, forget it."
    $ raiName = "Rai"
    r "I'm Rai or whatever. I don't trust any of you."

    #show hali annoyed 1 
    ha "No one asked for your opinion."

    reader "If it makes you feel better, I think it's a bit cold outside."

    #show rai grateful
    r "Thanks dude."

    #show hali annoyed 2
    ha "No it's not idiot."
    ha "God, I'm surrounded by morons."
    #show hali talking
    $ haliName = "Hali"
    ha "Hi there, I'm Hali and I hope you aren't as annoying as the other people here."

    #show lucy sad
    l "Am I annoying too?"

    #show hali confident
    #show lucy happy
    ha "You're not as bad as that bitch with the stupid heart glasses."

    v "She loves me chat, don't worry."

    #show hali angry
    ha "UGH!"
    ha "I can't with this. I'm going to the other room already."
    #walking noise
    #unshow hali

    reader "There are other rooms?"

    #show rai talking
    r "Yea, we were about to go into it but then those two started to fight."

    reader "Oh, do you all know each other?"

    #show lucy thinking
    l "Nope! We don't know each other, but I think they're all nice."
    #show lucy excited
    l "So we should all be friends!"

    #show rai annoyed
    r "Shut it pipsqueak."
    #show rai talking
    r "Vyn, Hali and I woke up in the same room, but the door locked behind us when we want out."

    reader "{i}Woke up?{i}"
    reader "{i}So that means what happened to me also happened to them."
    reader "Wait, what about Lucy?"

    r "She was already out here."
    
    #show lucy talkings
    l "I woke up here in the hallway!"

    #show rai annoyed
    r "Yea sure, I totally trust you."
    r "Ugh, I just wanna get out of here. I can already tell that some weird shit is going on here."

    "KAAAHHHHHHHHHHHHHH!!!" with vpunch
    #show rai scared
    #show lucy scared

    reader "!!!"
    reader "Who was that??"

    #show rai worried
    r "It might have been Hali."
    r "Come on, let's hurry to the other room."

    #running sound
    #scene body with fade
    #surpise sound
    #scene main room
    #show lucy scared, rai distrubed, hali freaked out, vyn neutral

    "You run to the open door where Rai and Lucy were standing."
    reader "Oh my.."

    l "!!!!"

    ha "Oh my god oh my god, this can't be happening."

    r "Fuck, I was suposes to see my girl, why did I hace to get roped into this."

    #vyn shows up in the cg
    v "Hey guys, move! What are we even looking at?"

    ha "The- THE DEAD FUCKING BODIES????"
    ha "Oh my god, I'm going to throw up."

    "Before you could say anymore, Vyn ran past the door and up to where Hali was sitting."
    
    #vyn going up in the cg
    v "Jeeez, looks like someone didn't have a good day."

    r "What the hell are you doing?? Don't touch it!"

    v "I wasn't gonnnaaa."

    reader "{i}Wow, he doesn't have a serious bone in his body.{i}"

    ha "ARGH!"
    ha "DO YOU NOT REALIZE HOW SERIOUS THIS IS??"

    v "Well I mean-"

    l "Wait! One of them is still alive!"

    r "How the hell can you tell?"

    l "Their nose moved and they're still breathing."

    r "What the fuck.."

    #scene body close up hacku
    "You follow Lucy and go up to the supposed dead body."
    reader "{i}They are still breathing!{i}"
    "Looking at their clothes, you see traces of dirt and like it's been dragged or been through something."

    menu:
        reader "{i}Should I try to wake them up?{i}"

        "Shake them awake":
            "You shake them a bit."
        
        "Do nothing":
            r "What the hell are you doing [reader]?"
            r "Move over, I'll wake them up."
            $ raiTrust = raiTrust - 1

    #no more cg
    hk "Ugh.."
    hk "What..?"
    hk "Where am I?"
    hk "Who are you people?"

    r "That's what we should be askin' you."
    r "What the hell are you doing next to a dead body?"

    hk "Huh? A body?"
    hk "..."
    hk "Woah, what the.."

    l "Hi! Nice to meet you stranger!"
    l "My name is Lucy and I hope we can be friends!"

    r "What the hell?"
    r "Now is not the time to befriend murderers!"

    hk "But do you have any other evidence other than that?"

    r "The fuck? Bruh, who else other than the murderer would say that?"

    v "Ey, bro don't mind that dude."
    v "He doesn't trust anyone here LOL."

    ha "What the fuck? Did you just say LOL out loud?"

    v "What's wrong with that?"

    ha "I can't do this anymore."

    reader "Uh.. Hey.."
    reader "So, what's your name?"

    $ hackuName = "Hacku"
    hk "My name is Hacku."

    l "Oooooooh cool!"

    menu:
        r "Are we still not going to like, tie them up or anything?"

        "Suggest to tie them up":
            $ hackuTrust = hackuTrust - 1
            hk "Hey! I didn't get to defend myself or anything."
            hk "You guys are just making accusations and that isn't good for situations like this."

            r "So, you've been in situations like this?"

            ha "No, they're just not stupid."

            v "Ey, let's calm down."

            ha "Shut up, I don't want to hear anything from you."

        "Suggest to not be hasty":
            $ hackuTrust = hackuTrust + 1
            hk "Thank you... uh what's your name again?"

            reader "It's [readerName]."
            reader "Are you ok?"

            hk "My everything hurts a bit, but I'll manage. Thank you."

            "You lent your hand to help them get up."

        "Do nothing":
            r "Well?"

            v "Nah, I think bro is cool."

            r "..."
            r "Ugh, whatever."
            r "I'm watching you Chachu."

            ha "It's Hacku."

            #rai eye roll
            r "Whatever."
    
    v "So the dead guy.."
    v "What do we do?"

    ha "What??" 
    ha "We call the police, duh."

    v "I don't have my phone though."

    ha "WHAT!!"
    "Hali frantically checks her pockets."
    ha "Holy shit, mines gone too."

    ha "Same."

    r "Don't got mine eithre."

    reader "..."
    "You feel around in your pocket."
    if glassClue == True:
        "You only feel the glass shard you got from your room."
    else:
        "You have nothing in your pocket."
    reader "I got nothing too."

    l "I think I left my phone in my house."

    ha "Speaking of houses, do you guys happen to know where we are?"

    v "My vacation house obviously."

    ha "Ugh, can you take this seriously for once?"

    v "Ok fine."
    v "We're at your mom's house."

    ha "I'm so done. There is a literal dead body in the middle of thie goddamn room."

    v "Hey! I am taking this seriously. I even have my serious face on."

    ha "THAT'S IT!"

    #scene hali punch
    ha "If you don't have any fucking serious bones in your body, then they may as well be broken because they're useless."
    ha "JUST."
    ha "LIKE."
    ha "YOU."

    v "Woah chill dude!"
    v "You can't hit someone with glasses, that's attempted murder maybe you're the murderer!"

    ha "I'm about to be a murderer if you don't shut the hell up!"

    hk "Hey! Chill out!"

    #fade black
    reader "Hacku's right, guys stop fighting!"

    ha "If he is not taking this shit seriously, he may as well be knocked out."

    l "I'm sure he's taking this seriously! In his own way!"

    v "Yea! In my own way Haliey!"

    ha "Don't call me that."

    r "Ok, shut up."

    reader "Guys..."

    hk "Are there other rooms here?"

    r "Probably?"
    r "Why, you can't be considering we split up. This is not a horror film."

    hk "I thought you didn't trust any of us, hm?"

    r "I don't, but that doesn't mean I want to stay alone in this murder house."

    l "Don't worry! I'll follow you so we can have like a buddy system!"

    r "The hell?"
    r "What are you, twelve?"

    l "Seventeen!"

    v "Damn! You're a baby!"

    l "Am not!"

    ha "Awhhh, baby."

    r "Ugh, enough of that."

    reader "Should we look for clues around the house then?"

    hk "Yes, we should."

    ha "As long as I'm not in a room with this bastard."

    v "You hurt my heart Halili"
    v "ARGHHHH MY HEART!"

    ha "FUCK OFF! GO HAVE A HEART ATTACK AND DIE!"

    "Hali storms off into one of the other rooms."

    hk "Let's split the rooms then."

    r "What?? If one of us is the murderer then-"

    hk "It's best to trust for now and be betrayed later."
    hk "Because right now, we need to get out of this cabin and find a phone or something."

    reader "What about the body?"

    hk "I have some experience with handling them."

    r "HUH?"
    r "What the fuck do you do with them??"

    hk "..."
    hk "I work at a mortuary, so I deal with them a lot."

    l "Ooooh! So you get to make a lot of dead friends!"

    r "Dude."
    r "I will never trust her if she says weird shit like that."

    reader "Well there are three other rooms so we could split up."

    r "I'm going alone."
    #walking

    v "Welp, who wants the other two."

    hk "I think that you and Lucy should take the other rooms."
    hk "[readerName], you should go to all of them and make sure that none of them are doing anything weird."
    hk "Since you seem the most level headed."
    "Hacku winks at you."

    reader "{i}???{i}"
    reader "Huh? Well alright."
    jump checkHacku

label checkHacku:
    default hackuClues = 0
    default firePlace = True
    default vent = True
    default painting = True
    default body = True

    reader "{i}Maybe I should start with this room.{i}"

    menu:
        reader "{i}What should I do first?{i}"

        "Talk to Hacku":

            reader "Find anything about the dude?"

            hk "Naw."
            hk "I also don't want to disturb him too much or move too many things around."

            reader "Oh, why?"
            
            hk "Never good to move too many things from the crime scene."

            reader "I see..."
            reader "Wait, how do you know all of this?"

            hk "Haha, I work with bodies a lot remember?"
            hk "Technically, this isn't my first crime scene so.."

            reader "Technically?"

            hk "..."
            hk "A story for another time."
            hk "So, how did you get to this cabin?"
            hk "From what I can tell from the status of this place, it isn't really a place where people would like to visit."

            reader "Oh, I actually don't remember."
            reader "When I woke up, I was in a room from the hallway we all came from."
            reader "Jeez, that makes me sound so suspicious."

            hk "Haha, no worries [readerName]."
            hk "I don't have too much memory as to how I ended up here either."

            reader "Really?"

            hk "Yep."
            hk "So, that makes us equally as suspicious."

            #show hacku smile
            "Hacku gives you a glowing smile"
            "They seemed a little lost for some reason though."
            reader "{i}Whew, I mean at least they're nicer and not creepy crazy like the others.{i}"

            hk "Alright! C'mon [readerName], let's look for more clues and when we get our memories back let's talk more."

            reader "Ok!"

            "Hacku seems to trust you a little more."
            $ hackuTrust = hackuTrust + 2

        "Look around":
            reader "{i}I should look around first.{i}"

    while hackuClues != 5:
        menu:
            reader "{i}What should you look at?{i}"

            "Fireplace" if firePlace:
                $ hackuClues += 1
                $ firePlace = False

                reader "{i}This is a really fancy fireplace.{i}"
                reader "{i}Something you could only see in movies probably.{i}"
                reader "{i}Nothing related to the situation though.{i}"

            "Open vent" if vent:
                $ hackuClues += 1
                $ vent = False

                reader "{i}What the..?{i}"
                reader "{i}Why is the vent open?{i}"
                reader "{i}There seems to be some sort of clear liquid leaking out from it.{i}"

                menu:
                    "How should you inspect it?"

                    "Taste it":
                        $ ventClue = True
                        $ numClues = numClues + 1
                        #play sound "lick"
                        "You reach your hand to touch the clear liquid and bring it to your mouth."
                        
                        reader "{i}Huh.. it's kind of sweet but it's very faint.{i}"
                        reader "{i}...{i}"
                        reader "{i}Why the hell did i just taste that, i'm so not surviving the apocalypse.{i}"
                        reader "{i}Wait..{i}" 
                        reader "{i}We were all unconscious at around the smae time, so we must have all been affected by the same thing.{i}" 
                        reader "{i}The murderer probably let a chemical in gas form go through the vents.{i}"
                        reader "{i}Then it became liquid because of the cold.{i}"
                        reader "{i}...{i}"
                        reader "{i}I feel so smart.{i}"

                    "Sniff it":
                        $ ventClue = True
                        $ numClues = numClues + 1
                        "You put you head near the vent and sniffed the liquid."

                        hk "???"
                        hk "PFFFT? [readerName], what are you doing?"

                        reader "Hey! I'm conducting an experiment."
                        reader "So uh, just ignore me."

                        "Suddenly you feel a bit conscious."

                        reader "{i}Blah! Whatever.{i}"
                        reader "{i}It smelled kind of like pool cleaner but not exactly pool cleaner.{i}"
                        reader "{i}Is there a pool here? No, that doesn't make sense for a random cabin to have a pool and I'm sure some one would have said something about it too.{i}"
                        reader "{i}If it smelled like pool cleaner then though, I doubt it was something normal.{i}"
                        reader "{i}It might have been a chemical that put us all to sleep in gas form.{i}"
                        reader "{i}And since the weather is cold, it probably became a liquid after awhile.{i}"
                        reader "Man.. this is so much thinking."

                    "Step away":
                        reader "{i}Probably best not to be near this.{i}"

            "Painting" if painting:
                $ hackuClues += 1
                $ painting = False

                menu:
                    #scene weird painting
                    "You look at the painting."

                    "What a weird painting":
                        reader "{i}Why would you even put this here, it's an eyesore.{i}"

                    "Pretty painting":
                        reader "{i}I kind of want to take it to put back in my room.{i}"
                        reader "{i}When I find my phone, I have to take a picture of it.{i}"

                reader "{i}I doubt it has anything to do with anything here though.{i}"

            "The body" if body:
                $ hackuClues += 1
                $ body = False

                #scene body
                "The skin of the person looks pale, but you can't tell if it's because of the lighting or if that's how it is."
                "Looking closely, you can see some bruises on their knuckles and more along their arms and a few on their face."
                "There is also a huge gash on their neck that is covered by a bandage, but it's soaked in blood."
                "It looks like something sharp was the cause of death, but you shouldn't decide that based on one look of the body."

                reader "{i}I wonder who this person was.{i}"
                reader "{i}I kinda feel bad for just calling him the body or the dead person." 

            "Finished looking around":
                reader "{i}I think I'm done look around.{i}"
                reader "{i}I guess I should check the other rooms.{i}"
                reader "Hey Hacku!"

                hk "Yea?"

                reader "I'm gonna go check the other rooms."

                "Hacku gave you a thumbs up."
                jump investigation

label investigation:
    #scene main room
    if roomHali == False and roomVyn == False and roomLucy == False and roomRai == False:
        $ allRooms = True

    if roomHali or roomVyn or roomLucy or roomRai:
        menu:
            reader "{i}Which room should I check on next?{i}"

            "Kitchen" if roomHali:
                jump checkHali
            
            "Dining room" if roomVyn:
                jump checkVyn
            
            "Garage" if roomLucy:
                jump checkLucy

            "Living room" if roomRai:
                jump checkRai

            "Go back to the main room" if allRooms:
                jump argument
      

label checkLucy:
    $ roomLucy = False
    "lucy"
    jump investigation
    #kitchen / or garade whatever, 

label checkRai:
    $ roomRai = False
    default raiClues = 0
    default rug = True
    default clock = True
    default table = True

    "You go inside the living room and see Rai looking at one of the bookshelves."

    menu:
        "What should you do?"

        "Talk to Rai":

            reader "Hey Rai."

            r "Oh, it's you."

            reader "Find anything yet?"

            r "Nah."
            r "It's just a bunch of old books about.."
            r "I can't even reader this."

            "You look over Rai's shoulder. He is flipping through a dusty book."
            "It contains a bunch of unrecognizable characters and words that looked like it was just someone's bad handwriting."

            r "I mean I could probably try to understand it."
            r "It looks like english, but the handwriting is so bad."

            reader "Yea.."

            #play sound book close
            "Rai shuts the book and puts it back on the shelf."

            r "Ugh.."
            r "I was supposed to meet up with my girl you know."

            reader "How'd you end up here then?"

            r "All I remember is I took a shortcut throguh these creepy ass woods."

            reader "Why would you do that...?"

            r "Ok well, if you knew my girlfriend then you'd know she's the most beautiful girl ever."
            r "If I ever kept her waiting, I wouldn't be able to call myself her boyfriend."
            
            reader "..."
            reader "{i}This dude is a simp.{i}"
            reader "I see.."

            r "Oi!"
            r "The hell's up with that face?"
            r "She had to move and I was trying to find the place so Moogle Maps told me to go through the forest."

            reader "The forest?"

            r "I don't know why either, but I was borderline running late so I had to get there quick."

            reader "I mean, I'm sure your girlfriend would have understood if you were a bit late."

            r "She would have but.."
            r "I don't want her to wait."
            r "Because I promised her."
            r "Man.."

            menu:
                "Rai pulls out a picture from inside the pocket of his jacket."

                "Can I see?":
                    reader "Mind if I take a look?"

                    r "Sure bro."

                    #cg of tiffany

                    r "I love her so much."
                    r "She's so pretty and kind and nice."
                    
                    reader "She's pretty."
                    
                    r "Yep."
                    r "That's my girlfriend."
                    r "And I'm damn proud to have pulled her."

                    $ raiTrust = raiTrust + 1

                "Say nothing.":
                    "Rai puts away the photo."

            r "Bah, anyways."
            r "Thanks for listening [readerName]."

            reader "No problem!"

            r "Aight, let's look around now."

            "Rai seems to trust you more."
            $ raiTrust = raiTrust + 2

        "Look around":
            "You start looking around."
            reader "{i}Hmm...{i}"
    
    while raiClues != 4:
        menu:
            "What should you look at?"

            "Rug" if rug:
                "odd"

            "Grandfather clock" if clock:
                "minigame"

            "Table" if table:
                "dusty"
            
            "Finished looking around":
                "ur done"
                jump investigation

label checkHali:
    $ roomHali = False
    "vyn"
    jump investigation
    #one room next to vyn

label checkVyn:
    $ roomVyn = False
    "vyn"
    jump investigation
    #on the couch or fireplace (the main room while everyone else splits away)


label argument:
    "not yet"


label endCredits:
    #scene my room
    #show happy me
    "Thank you for playing my game!"

    #show me talk ig
    "This is the first time I ever made my own game."
    "I'd like to thank my friends for testing my game."
    "Y'all are the best."
    #show bow me

label faint:
    #play the ringing noise

    reader "I feel so dizzy right now.."

    "My body swayed as a I heard something fall onto the ground."
    "If it wasn't clear enough, I was the thing that fell onto the ground."

    reader "Shit.. my head hurts so bad.."
    scene black with eyesclose

    "Well.."
    "That wasn't suposes to happen."
    "{b}Bad Ending 0{/b}."
    #achievement : Help! I've fallen and I can't get up!
    #bonus cg of you dead if i have time
    return
