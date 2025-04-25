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

#other
default checkLight = False
default checkSofa = False
default checkGlass = False
default haliAngry = True
default cabinUgly = False
default checkedDoor = False
default taste = False
default sniff = False

# eye opening
define eyesopen = ImageDissolve("eye", 5.0)
define eyesclose = ImageDissolve("eye", 5.0, reverse = True)
define fade = Fade(0.5, 1.0, 0.5)

label start:
    scene black
    #jump introduction
    #jump checkLucy
    "WARNINGS: depictions of murder, arguments about murders, a good amount of cursing, bad comedy, some blood and just anything you can expect from a story about a murderer."
    "This is a fictional story about a murder mystery, silliness and any similarity to real people are completely coincidental."
    "There WILL be minor transitional effects. You can disable them in the options menu."
    "There will also be LOUD noises and sound effects. You can disable them in the options menu."
    "There is a mechantic called trust. During certain choice events, your trust with the charactor will be indicated in the top left-hand corner along with the name of the charactor."
    "It can increase or decrease based on your answers so, be sure to keep an eye out for it!"
    
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

    play music "ringing.mp3" loop
    scene black
    "..."
    scene bg reader room blurry with eyesopen
    "{i}...Urgh{i}"

    reader "{i}My head is ringing so loudly.{i}"
    "You bring your hand to the back of your head."
    reader "Ow, what the.."
    "You look at your hand and see some smeared blood along your palm."
    reader "{i}What happened to me?{i}"
    reader "{i}And where am I?{i}"
    reader "{i}Ugh, I need to get out of here, but my head really hurts.{i}"

    #potential bad ending 0
    menu:
        reader "{i}What should you do?{i}"
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

    stop music fadeout 1.0
    scene bg reader room glass with pixellate
    "You feel better, so you stand up."
    "You look around the room."

    reader "Where the hell am I?"

    menu:
        "What should you do?"
        
        "Look around the room":
            reader "Hmm.. I guess looking around wouldn't hurt."
            jump lookAround

        "Go straight to the door":
            reader "I better hurry and get out of here."
            reader "No time to look around."
            play sound "footsteps long.mp3"
            "You walk towards the door."
            jump introduction

label lookAround:
    menu:
        "What should you look at first?"

        "Sofa":
            $ checkSofa = True
            play sound "footsteps short.mp3"
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
                            play sound "footsteps long.mp3"
                            jump introduction

                "Rug":
                    jump glassRug

                "Go to the door":
                    reader "I'm done looking around."
                    reader "I should get out of here."
                    play sound "footsteps long.mp3"
                    jump introduction

        "Light":
            $ checkLight = True
            "You look at the light."
            "It isn't very bright and looks like it'll fall apart at any second. It's best to stay cautious."
           
            menu:
                "What should you look at next?"

                "Sofa":
                    $ checkSofa = True
                    play sound "footsteps short.mp3"
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
                            play sound "footsteps long.mp3"
                            jump introduction

                "Rug":
                    jump glassRug

                "Go to the door":
                    reader "I'm done looking around."
                    reader "I should get out of here."
                    play sound "footsteps long.mp3"
                    jump introduction

        "Rug":
            jump glassRug
        
        "Go to the door":
            reader "I'm done looking around."
            reader "I should get out of here."
            play sound "footsteps-long.mp3"
            jump introduction

label glassRug:
    play sound "footsteps short.mp3"
    "You look around the rug."
    reader "{i}Huh? What's this?{i}"

    "There is a glass shard under the rug."
    show cg glass with dissolve
    galleryunlock cg0

    menu:
        reader "{i}Should I take that? It looks really sharp.{i}"

        "Take it":
            reader "{i}Well, no harm if I just leave it in my pocket.{i}"
            reader "{i}I just have to remember it's there so I don't cut myself.{i}"
            play sound "glass shard.mp3"
            hide cg glass with dissolve
            "You took the glass shard and put it carefully into your pocket."
            $ glassClue = True
            scene bg reader room
        
        "Leave it":
            reader "{i}Nah, I don't want to accidentally cut myself.{i}"
            "You left the glass shard alone."
            hide cg glass with dissolve

    if checkSofa == False and checkLight == False:
        menu:
            "What should you look at next?"
            
            "Sofa":
                play sound "footsteps short.mp3"
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
                        play sound "footsteps long.mp3"
                        jump introduction
                
            "Light":
                $ checkLight = True
                "You look at the light."
                "It isn't very bright and looks like it'll fall apart at any second. It's best to stay cautious."

                menu:
                    "What should you look at next?"

                    "Sofa":
                        play sound "footsteps short.mp3"
                        $ checkSofa = True
                        "You look around the sofa."
                        "You find nothing and there is a lot of dust on it."
                        reader "ACHOO!" with vpunch

                    "Go to the door":
                        reader "I'm done looking around."
                        reader "I should get out of here."
                        play sound "footsteps short.mp3"
                        jump introduction

            "Go to the door":
                reader "I'm done looking around."
                reader "I should get out of here."
                play sound "footsteps long.mp3"
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
                play sound "footsteps long.mp3"
                jump introduction       

    elif checkSofa == False and checkLight == True:
        menu:
            "What should you look at next?"

            "Sofa":
                play sound "footsteps short.mp3"
                $ checkSofa = True
                "You look around the sofa."
                "You find nothing and there is a lot of dust on it."
                reader "ACHOO!" with vpunch

            "Go to the door":
                reader "I'm done looking around."
                reader "I should get out of here."
                play sound "footsteps long.mp3"
                jump introduction
    
    reader "{i}I think that's all.{i}"
    reader "{i}It's so dusty in here too, I don't want to spend another minute in here.{i}"

    play sound "footsteps long.mp3"
    "You start walking to the door."

    jump introduction


label introduction:
    play sound "door open.mp3"
    scene bg reader hallway with fade

    play sound "door slam 1.mp3"
    "{i}{b}SLAM{b}{i}" with vpunch
    "!!!"
    reader "{i}Oh... the door just closed all of a sudden.{i}"
    
    menu:
        reader "{i}What should I do now?{i}"

        "Try to open the door":
            $ checkedDoor = True
            play sound "rattling door.mp3"
            "The door doesn't budge."

            reader "Ugh, whatever."

            "You give up and start to walk down the hallway."

        "Continue to walk down the hallway":
            "You start to walk down the hallway."

    play sound "footsteps long.mp3"

    scene bg hallways with fade
    "You hear some voices. It sounds like there's an argument."

    show bg hallways rai with dissolve
    show hali blur at five
    show vyn blur at eightseven
    show lucy blur at three
    with dissolve

    ha "Ugh, whatever. I'm not going to listen to an insane person like you."

    v "Hah! Jokes on you, I take that as a compliment."

    ha "I'm saying it as an insult!"

    reader "{i}Oh god..{i}"

    menu:
        reader "{i}Should I approach them?{i}"

        "Go up to them and introduce yourself":
            "You start making your way to the group of people."
            "One of them turns around and meets your eyes."

            reader "Um.. Hello?"
            reader "Sorry to interrupt.."

            show lucy thinking
            with dissolve
            l "Oh! Hello there!"
            show lucy
        
        "Wait a bit":
            "You wait a bit further away from them but one of them spots you."

            show lucy excited
            with dissolve
            l "Hey! Another person over there!"
            show lucy smile
            
    show hali shocked with dissolve 
    ha "Holy shit!"
    show hali annoyed
    ha "Great, another person because that's just what we needed."
    ha "A creepy cabin that we're all probably going to be killed in and more strangers."
    show hali rbf

    show vyn happy with dissolve
    v "Hahahaha, don't mind her."
    show vyn smile

    show hali annoyed
    ha "You don't even know me?"
    ha "Stop acting like we're friends."
    show hali rbf

    show vyn happy
    v "She's so silly."
    show vyn hand
    v "Anyways, sup bro!"

    menu:
        "The person raises his hand for a high five from you."

        "High five the stranger":
            play sound "high five.mp3"
            "You high fived the stranger."
            
            show bar 2
            show trust unknown
            show up
            with dissolve

            show vyn silly
            v "Hell yea man."

            hide bar 2
            hide trust unknown
            hide up
            with dissolve
            $ vynTrust += 1
        
        "Do nothing":
            "You stared at the stranger."
            show vyn thinking
            v "Awh, but all good bro."
            show vyn silly

    $ vynName = "Vyn"
    v "Anyways, my name is Vyn."
    v "Nice to meet cha!"
    show vyn smile

    reader "{i}Oh right, names.{i}"
    $ readerName = renpy.input("{i}What was my name again?{i}")
    $ readerName = readerName.strip()
    while readerName == "Lucy" or readerName == "lucy" or readerName == "Hali" or readerName == "hali" or readerName == "Hacku" or readerName == "hacku" or readerName == "Vyn" or readerName == "vyn" or readerName == "Rai" or readerName == "rai" or readerName == "Shugo" or readerName == "shugo":
        "Hmm.."
        $ readerName = renpy.input("That doesn't seem right, lets think about it again.")
        $ readerName = readerName.strip()

    reader "My name is [readerName], nice to meet you Vyn."

    show lucy wave at threefour
    with move
    l "Hi hi friend!"
    $ lucyName = "Lucy"
    l "My name is Lucy! I hope we can be good friends!"
    show lucy smile

    show bg hallways empty 
    show rai annoyed at one
    with dissolve
    r "Why the hell would you want to be friends with people who might be the reason why we're even trapped here."
    r "You're also insane for wearing shorts in this type of weather."
    show rai rbf

    show lucy happy at three
    with move
    l "Because I love making friends! The more the merrier!"
    show lucy thinking
    l "Also, it isn't cold outside."
    show lucy neutral

    show rai annoyed
    r "You're insane."
    r "Forty degrees is cold as fuck."
    r "And even if it is, it's not weather to be wearing shorts in."
    show rai rbf

    show vyn silly
    v "I think our bro is just sensitive to the cold."
    v "Don't be mean to gramps."

    show rai annoyed
    r "Dude? You're literally wearing-"
    r "Ugh, forget it."
    show rai erm
    $ raiName = "Rai"
    r "I'm Rai or whatever. I don't trust any of you."
    show rai neutral

    show hali disgusted 
    ha "No one asked for your opinion."

    reader "If it makes you feel better, I think it's a bit cold outside."

    show rai happy
    r "Thanks dude."
    show rai neutral

    show hali annoyed
    ha "No it's not, idiot."
    show hali disgusted
    ha "God, I'm surrounded by morons."
    show hali thinking
    $ haliName = "Hali"
    ha "Hi there, I'm Hali and I hope you aren't as annoying as the other people here."
    show hali neutral

    show lucy thinking
    l "Am I annoying too?"

    show hali shocked
    show lucy smile
    ha "You're not as bad as that bitch with the stupid heart glasses."
    show hali neutral

    show vyn happy
    v "She loves me chat, don't worry."
    show vyn smile

    show hali enraged
    ha "UGH!"
    ha "I can't with this. I'm going to the other room already."
    play sound "stomping.mp3"
    show hali pissed at offright
    with move
    hide hali pissed 
 
    reader "There are other rooms?"

    show rai thinking
    r "Yea, we were about to go into it but then those two started to fight."
    show rai neutral

    reader "Oh, do you all know each other?"

    show lucy thinking
    l "Nope! We don't know each other, but I think they're all nice."
    show lucy excited
    l "So we should all be friends!"
    show lucy smile

    show rai annoyed
    r "Shut it pipsqueak."
    show rai thinking
    r "Vyn, Hali and I woke up in the same room, but the door locked behind us when we want out."
    r "I think that Vyn and Hali knew of each other before though. I'm not too sure, you'll have to ask them."
    show rai neutral

    reader "Oh, I see."
    reader "{i}Wait, woke up?{i}"
    reader "{i}So that means what happened to me also happened to them."
    reader "Wait, what about Lucy?"

    show rai thinking
    r "She was already out here and I don't know her at all."
    show rai neutral
    
    show lucy thinking
    l "I woke up here in the hallway!"
    show lucy neutral

    show rai annoyed
    r "Yea sure, I totally trust you."
    r "Ugh, I just wanna get out of here. I can already tell that some weird shit is going on here."

    show rai scared
    show lucy scared 
    show vyn neutral
    "KAAAHHHHHHHHHHHHHH!!!" with vpunch
    
    reader "!!!"
    reader "Who was that??"

    r "It might have been Hali."
    r "Come on, let's hurry to the other room."

    hide lucy scared
    hide vyn neutral
    hide rai scared
    with dissolve

    scene black with fade
    play sound "running.mps"

    "You run to the open door where Rai and Lucy were standing."

    scene cg body found with dissolve
    reader "Oh my.."
    
    l "!!!!"

    ha "Oh my god oh my god, this can't be happening."

    r "Fuck, I was suposes to see my girl, why did I have to get roped into this."

    show cg body found vyn with dissolve
    v "Hey guys, move! What are we even looking at?"

    reader "{i}?!{i}"
    reader "{i}Oh, it's just Vyn.{i}"

    ha "The- THE DEAD FUCKING BODIES????"
    ha "Oh my god, I'm going to throw up."

    show cg body found vyn smile

    v "Jeeez, looks like someone didn't have a good day."

    r "What the hell are you doing??"

    show cg body found vyn
    v "I wasn't gonnna do anything! Trust bro."

    reader "{i}Wow, he doesn't have a serious bone in his body.{i}"

    ha "ARGH!"
    ha "DO YOU NOT REALIZE HOW SERIOUS THIS IS??"

    v "Well I mean-"

    l "Wait! One of them is still alive!"

    r "How the hell can you tell?"

    l "Their nose moved and they're still breathing."

    r "What the fuck.."

    galleryunlock cg1
    scene cg hacku uncon with fade

    "You follow Lucy and go up to the supposed dead body."

    reader "{i}They are still breathing!{i}"

    "Looking at their clothes, you see traces of dirt and like it's been dragged or been through something."

    menu:
        reader "{i}Should I try to wake them up?{i}"

        "Shake them awake":
            show cg hacku uncon hand with dissolve    
            "You shake them a bit."
            galleryunlock cg3
        
        "Do nothing":
            "You stare at the person."

            r "What the hell are you doing [readerName]?"

            show bar 0
            show trust rai
            show down
            with dissolve
            r "Move over, I'll wake them up."

            hide bar
            hide trust
            hide down
            with dissolve  
            $ raiTrust -= 1

    galleryunlock cg2

    scene bg main body
    show rai scared at three
    show hacku hurt  at four
    show vyn neutral at seven
    show lucy scared at eight
    show hali scared at one
    with dissolve
    
    play sound "get up.mp3"
    "The stranger stood up."
    "They looked like they got into a fight, but they had no blood on them."
    "Aside from some smeered blood on their hand when they got up."

    show hacku strained
    hk "Ugh.."
    hk "What..?"
    hk "Where am I?"
    hk "Who are you people?"
    show hacku hurt

    show rai annoyed
    r "That's what we should be askin' you."
    r "What the hell are you doing next to a dead body?"
    show rai rbf

    show hacku strained
    hk "Huh? A body?"
    show hacku hurt
    hk "..."
    show hacku strained
    hk "Woah, what the.."
    show hacku hurt

    show lucy wave at seveneight
    with move
    l "Hi! Nice to meet you stranger!"
    l "My name is Lucy and I hope we can be friends!"
    show lucy smile

    show rai annoyed
    r "What the hell?"
    r "Now is not the time to befriend murderers!"
    show rai rbf

    show lucy neutral at eight
    with move

    show hacku strained
    hk "But do you have any other evidence other than that?"
    show hacku hurt

    show rai annoyed
    r "The fuck? Bruh, who else other than the murderer would say that?"
    show rai rbf

    show vyn silly
    v "Ey, bro don't mind that dude."
    v "He doesn't trust anyone here LOL."

    show hali enraged
    ha "What the fuck? Did you just say LOL out loud?"
    show hali pissed

    show vyn happy
    v "What's wrong with that?"
    show vyn smile

    show hali disgusted
    ha "I can't do this anymore."

    reader "Uh.. Hey.."
    reader "So, what's your name?"

    show hacku strained
    $ hackuName = "Hacku"
    hk "My name is Hacku."
    show hacku hurt

    show lucy excited
    l "Oooooooh cool!"
    show lucy smile
    show rai annoyed

    menu:
        r "Are we still not going to like, tie them up or anything?"

        "Suggest to tie them up":
            if raiTrust == 0:
                show bar 1
                show trust rai
                show up
                with dissolve
            else:
                show bar 0
                show trust rai
                show up
                with dissolve
            $ raiTrust += 1
            
            show rai rbf
            reader "I agree with Rai, we need to make sure they can't do anything."
            
            hide up
            show bar 0
            show trust hacku
            show down
            with dissolve

            show hacku guarded
            hk "Hey! I didn't get to defend myself or anything."

            hide bar 0 
            hide trust hacku
            hide down
            with dissolve
            $ hackuTrust -= 1

            hk "You guys are just making accusations and that isn't good for situations like this."
            show hacku hurt

            show rai annoyed
            r "So, you've been in situations like this?"
            show rai rbf

            show hali annoyed
            ha "No, they're just not stupid."
            show hali rbf

            show vyn thinking
            v "Ey, let's calm down."
            show vyn neutral

            show hali annoyed
            ha "Shut up, I don't want to hear anything from you."
            show hali rbf

        "Suggest to not be hasty":
            show rai rbf
            reader "Hey now.. let's not be hasty."

            show bar 1
            show trust hacku
            show up
            with dissolve

            show hacku grateful
            hk "Thank you... uh what's your name again?"
            show hacku hurt

            hide bar 1
            hide trust hacku
            hide up
            with dissolve
            $ hackuTrust += 1

            reader "It's [readerName]."
            reader "Are you ok?"

            show hacku grateful
            hk "My everything hurts a bit, but I'll manage. Thank you."
            show hacku hurt

            play sound "clean clothes.mp3"
            "You patted some dust off of their shoulder."

            show hacku grateful
            hk "Thanks."
            show hacku hurt

            reader "Yea, no problem."

        "Do nothing":
            r "Well?"
            show rai rbf

            show vyn happy
            v "Nah, I think bro is cool."
            show vyn smile

            show rai erm
            r "..."
            r "Ugh, whatever."
            show rai annoyed
            r "I'm watching you Chachu."
            show rai rbf

            show hacku strained
            hk "It's Hacku."
            show hacku hurt

            show rai annoyed
            r "Whatever."
            show rai rbf
    
    show vyn thinking
    v "So the dead guy.."
    v "What do we do?"
    show vyn neutral

    show hali annoyed
    ha "What??" 
    ha "We call the police, duh."
    show hali rbf

    show vyn thinking
    v "I don't have my phone though."
    show vyn neutral

    show hali enraged
    ha "WHAT!!"
    show hali huh
    "Hali frantically checks her pockets."
    show hali shocked
    ha "Holy shit, mines gone too."
    show hali huh

    show hacku strained
    hk "Same."
    show hacku hurt

    show rai thinking
    r "Don't got mine either."
    show rai neutral

    reader "..."
    "You feel around in your pocket."
    if glassClue == True:
        "You only feel the glass shard you got from your room."
    else:
        "You have nothing in your pocket."
    reader "I got nothing too."

    show lucy thinking
    l "I think I left my phone in my house."
    show lucy neutral

    show hali thinking
    ha "Speaking of houses, do you guys happen to know where we are?"
    show hali neutral

    show vyn thinking
    v "My vacation house obviously."
    show vyn neutral

    show hali annoyed
    ha "Ugh, can you take this seriously for once?"
    show hali rbf

    show vyn thinking
    v "Ok fine."
    show vyn happy
    v "We're at your mom's house."
    show vyn smile

    show hali enraged
    ha "I'm so done. There is a literal dead body in the middle of thie goddamn room."
    show hali pissed

    show vyn thinking
    v "Hey! I am taking this seriously. I even have my serious face on."
    show vyn neutral

    show hali enraged
    ha "THAT'S IT!"
    show hali pissed at seven
    with move

    scene cg halivsvyn with vpunch
    ha "If you don't have any fucking serious bones in your body, then they may as well be broken because they're useless."
    ha "JUST."
    ha "LIKE."
    ha "YOU."

    v "Woah chill dude!"
    v "You can't hit someone with glasses, that's attempted murder maybe you're the murderer!"

    ha "I'm about to be a murderer if you don't shut the hell up!"

    hk "Hey! Chill out!"

    galleryunlock cg4

    scene bg main body 
    show rai erm at left
    show hali pissed at two
    show hacku smile at four
    show hacku neutral
    show vyn silly at seven
    show lucy neutral at eight
    with fade

    reader "Hacku's right, guys stop fighting!"

    show hali enraged
    ha "If he is not taking this shit seriously, he may as well be knocked out."
    show hali pissed

    show lucy happy
    l "I'm sure he's taking this seriously! In his own way!"
    show lucy smile

    show vyn happy
    v "Yea! In my own way Haliey!"
    show vyn smile

    show hali annoyed
    ha "Don't call me that."
    show hali rbf

    show rai thinking
    r "Ok, shut up."
    show rai neutral

    reader "Guys..."

    show hacku thinking
    hk "Are there other rooms here?"
    show hacku neutral

    show rai thinking
    r "Probably?"
    show rai annoyed
    r "Why, you can't be considering we split up. This is not a horror film."
    show rai rbf

    show hacku happy
    hk "I thought you didn't trust any of us, hm?"
    show hacku smile

    show rai annoyed
    r "I don't, but that doesn't mean I want to stay alone in this murder house."
    show rai rbf

    show lucy excited
    l "Don't worry! I'll follow you so we can have like a buddy system!"
    show lucy smile

    show rai annoyed
    r "The hell?"
    r "What are you, twelve?"
    show rai rbf

    show lucy happy
    l "Seventeen!"
    show lucy smile

    show vyn silly
    v "Damn! You're a baby!"

    show lucy annoyed
    l "Am not!"

    show hali happy
    ha "Awhhh, baby."
    show hali smile

    show rai annoyed
    r "Ugh, enough of that."
    show lucy neutral
    show rai rbf

    reader "Should we look for clues around the house then?"

    show hacku thinking
    hk "Yes, we should."
    show hacku neutral

    show hali annoyed
    ha "As long as I'm not in a room with this bastard."
    show hali rbf

    show vyn dramatic
    v "You hurt my heart Halili!"
    v "ARGHHHH MY HEART!"

    show hali enraged
    ha "FUCK OFF! GO HAVE A HEART ATTACK AND DIE!"
    show hali pissed at offright
    with move
    hide hali pissed

    play sound "stomping.mp3"
    show vyn silly
    "Hali storms off into one of the other rooms."

    show hacku thinking
    hk "Let's split the rooms then."
    show hacku neutral

    show rai annoyed
    r "What?? If one of us is the murderer then-"
    show rai rbf

    show hacku thinking
    hk "It's best to trust for now and be betrayed later."
    hk "Because right now, we need to get out of this cabin and find a phone or something."
    show hacku neutral

    reader "What about the body?"

    show hacku thinking
    hk "I have some experience with handling them."
    show hacku neutral

    show rai scared
    r "HUH?"
    r "What the fuck do you do with them??"


    hk "..."
    show hacku thinking
    hk "I work at a mortuary, so I deal with them a lot."
    show hacku neutral

    show lucy excited
    l "Ooooh! So you get to make a lot of dead friends!"
    show lucy smile

    show rai thinking
    r "Dude."
    show rai annoyed
    r "I will never trust her if she says weird shit like that."
    show rai rbf

    reader "Well there are three other rooms so we could split up."

    show rai thinking
    r "I'm going alone."
    show rai neutral at offright
    with move
    play sound "footsteps short.mp3"

    show vyn thinking
    v "Welp, who wants the other two."
    show vyn neutral 

    show hacku thinking
    hk "I think that you and Lucy should take the other rooms."
    show hacku neutral

    show lucy happy 
    l "Oki!"
    play sound "footsteps short.mp3"
    show lucy smile at offleft
    with move
    hide lucy smile

    show vyn silly
    v "Gotcha brother."
    play sound "footsteps short.mp3"
    show vyn silly at offright
    with move
    hide vyn silly

    show hacku thinking
    hk "[readerName], you should go to all of them and make sure that none of them are doing anything weird."
    hk "Since you seem the most level headed."
    show hacku wink
    "Hacku winks at you."
    
    reader "{i}???{i}"
    reader "Huh? Well alright."

    scene bg main hacku with fade

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
            
            "You go up to Hacku who is looking at the body."
            show bg main body 
            show hacku neutral 
            with dissolve 

            reader "Find anything about the dude?"

            show hacku thinking
            hk "Naw."
            hk "I also don't want to disturb him too much or move too many things around."
            show hacku neutral

            reader "Oh, why?"
            
            show hacku thinking
            hk "Never good to move too many things from the crime scene."
            show hacku neutral

            reader "I see..."
            reader "Wait, how do you know all of this?"

            show hacku happy
            hk "Haha, I work with bodies a lot remember?"
            show hacku thinking
            hk "Technically, this isn't my first crime scene so.."
            show hacku neutral

            reader "Technically?"

            hk "..."
            show hacku happy
            hk "A story for another time."
            show hacku thinking
            hk "So, how did you get to this cabin?"
            hk "From what I can tell from the status of this place, it isn't really a place where people would like to visit."
            show hacku neutral

            reader "Oh, I actually don't remember."
            reader "When I woke up, I was in a room from the hallway we all came from."
            reader "Jeez, that makes me sound so ."

            show hacku happy
            hk "Haha, no worries [readerName]."
            hk "I don't have too much memory as to how I ended up here either."
            show hacku smile

            reader "Really?"

            show hacku happy
            hk "Yep."
            hk "So, that makes us equally as suspicious."
            show hacku smile

            reader "Haha, I guess so."
            reader "{i}Whew, I mean at least they're nicer and not creepy crazy like the others.{i}"

            show hacku thinking
            hk "Do you remember anything about the room you came from though?"
            show hacku neutral

            reader "Oh yea. It was a little bit away from where the others came from."
            reader "Also when I left the door closed behind me."

            if checkedDoor:
                reader "I tried to open it but it wouldn't open again."

            show hacku thinking
            hk "Hmm, I see."
            show hacku neutral

            reader "Yea, and I have a small feeling that we shouldn't break anything in this house."

            show hacku thinking
            hk "True, this place gives off very creepy vibes. Example A."
            show hacku neutral

            "Hacku slowly looks at the body that they were inspecting."

            reader "Yea..."

            if hackuTrust == 0:
                show bar 3
                show trust hacku
                show up
                with dissolve
            elif hackuTrust == 1:
                show bar 4
                show trust hacku
                show up
                with dissolve

            show hacku happy
            hk "Alright! C'mon [readerName], let's look for more clues and when we get our memories back let's talk more."
            show hacku smile

            hide bar
            hide trust
            hide up
            with dissolve
            $ hackuTrust += 3

            reader "Ok!"
            hide hacku smile
            show bg main hacku 
            with dissolve

        "Look around":
            reader "{i}I should look around first.{i}"

    while hackuClues != 5:
        menu:
            reader "{i}What should you look at?{i}"

            "Fireplace" if firePlace:
                $ hackuClues += 1
                $ firePlace = False

                play sound "footsteps short.mp3"
                "You walk over to the fireplace."

                reader "{i}This is a really fancy fireplace.{i}"
                reader "{i}Something you could only see in movies probably.{i}"
                reader "{i}Nothing related to the situation though.{i}"

            "Open vent" if vent:
                $ hackuClues += 1
                $ vent = False

                play sound "footsteps short.mp3"
                "You walk over to the open vent on the wall near the floor."

                reader "{i}What the..?{i}"
                reader "{i}Why is the vent open?{i}"
                reader "{i}There seems to be some sort of clear liquid leaking out from it.{i}"

                menu:
                    "How should you inspect it?"

                    "Taste it":
                        $ ventClue = True
                        $ numClues = numClues + 1
                        $ taste = True
                        "You reach your hand to touch the clear liquid and bring it to your mouth."
                        
                        reader "{i}Huh.. it's kind of sweet but it's very faint.{i}"
                        reader "{i}...{i}"
                        reader "{i}Why the hell did i just taste that, I'm so not surviving the apocalypse.{i}"
                        reader "{i}Wait..{i}" 
                        reader "{i}We were all unconscious at around the smae time, so we must have all been affected by the same thing.{i}" 
                        reader "{i}The murderer probably let a chemical in gas form go through the vents.{i}"
                        reader "{i}Then it became liquid because of the cold.{i}"
                        reader "{i}...{i}"
                        reader "{i}I feel so smart.{i}"

                    "Sniff it":
                        $ ventClue = True
                        $ numClues = numClues + 1
                        $ sniff = True
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
                show cg weird painting with dissolve
                menu:
                    "You look at the painting."

                    "What a weird painting":
                        reader "{i}Why would you even put this here, it's an eyesore.{i}"
                        $ cabinUgly = True

                    "Pretty painting":
                        reader "{i}I kind of want to take it to put back in my room.{i}"
                        reader "{i}When I find my phone, I have to take a picture of it.{i}"

                reader "{i}I doubt it has anything to do with anything here though.{i}"
                galleryunlock cg5
                hide cg weird painting with dissolve

            "The body" if body:
                $ hackuClues += 1
                $ body = False
                $ deathClue = True
                $ numClues += 1
                
                play sound "footsteps short.mp3"
                "You walk over to the body."
                "Hacku is sitting on the ground near the body. They look deep in thought."

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
                hide hacku neutral
                jump investigation

label investigation:
    if roomHali or roomVyn or roomLucy or roomRai:
        scene bg main hacku with fade
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

    reader "{i}I think that's all of the rooms.{i}"
    reader "{i}I should check back in with Hacku{i}"

    scene bg main body with fade
    "You walk back to the main room."
    "You look around but Hacku is no where in sight."

    reader "{i}Huh? They said they were investigating the body though.{i}"

    play sound "door slam 1.mp3"
    show hali neutral with dissolve

    reader "{i}Huh?{i}"
    reader "{i}Oh it's Hali. I guess she's done investigating her room.{i}"

    menu:
        "Should you talk to her?"

        "Talk with Hali":
            reader "Hey Hali."
                
            show hali shocked
            ha "Oh, hey [readerName]."

            if haliAngry:
                show hali thinking
                ha "By the way [readerName], I'm sorry for snapping at you eariler. I was just super pissed off because of a certain bitch."
                show hali huh
                reader "Oh! No worries I unnderstand."

            show hali thinking
            ha "So what's going on now?"
            show hali neutral

            reader "I'm not sure actually. I came back here to see Hacku but they aren't here."
            reader "They said that they were investigating the body a while ago."

            show hali thinking
            ha "Huh.. weird."
            show hali neutral

            reader "Maybe they just went to check up on Rai or Lucy."

            show hali thinking
            ha "Probably."
            ha "Say [readerName], how did you get here?"
            show hali neutral

            reader "Oh, I actually don't remember. I think I was maybe passing by the cabin? I don't know."
            reader "Ok, I know that makes me sound super suspicious, but I really don't remember."

            show hali happy
            ha "Hahaha! I understand, I don't really remember how I got here either."
            ha "I was just asking in case your story could jog my memory."
            show hali smile

            reader "Oh, I see."

            show hali happy
            ha "Yea.."
            show hali thinking
            ha "The only thing I really remember is that I saw a stray cat heading into the forest."
            ha "I volunteer at an animal shelter so I didn't want the poor thing to go into this creepy-ass forest alone."
            show hali happy
            ha "All cats deserves a home."
            show hali smile

            reader "That's really cool!"

            show hali happy
            menu:
                ha "Yea! Do you have a cat by chance?"

                "No, I'm allergic.":
                    show hali smile
                    reader "No, I'm actually allergic to them sadly."
                    reader "Doesn't stop me from petting them though, I just have to take medicine after."

                    show hali happy
                    ha "You are so real for that."

                "No, I don't.":
                    show hali smile
                    reader "No, I don't have a cat sadly."
                    
                    show hali thinking
                    ha "Awh, you should consider getting one."
                    show hali neutral

                "Yes, I do!":
                    reader "I do have a cat!"
                    
                    if haliTrust == -1:
                        show bar 0
                        show trust hali
                        show up
                        with dissolve

                    elif haliTrust == 0:
                        show bar 1
                        show trust hali
                        show up
                        with dissolve

                    elif haliTrust == 1:
                        show bar 2
                        show trust hali
                        show up
                        with dissolve

                    ha "Oh my GOD! What is the name?!"
                    show hali smile
                    hide bar
                    hide trust
                    hide up
                    with dissolve
                    $ haliTrust += 1

                    default catName = "Cat name"
                    $ catName = renpy.input("{i}What is your cat's name?{i}")
                    $ catName = catName.strip()

                    reader "It's [catName]."

                    if catName == "Vyn" or catName == "vyn":
                        show hali shocked
                        ha "Oh... why would you name your cat that?"
                        show hali annoyed
                        ha "Well, I bet that cat Vyn is more considerate and cuter than the idiot."
                        show hali neutral

                    elif catName == "Hali" or catName == "hali":
                        show hali happy
                        ha "Oh my god, I'm so honored to have the same name as your cat!"
                        show hali smile

                    elif catName == "Lucy" or catName == "lucy":
                        show hali happy
                        ha "Awh, your kitty has the same name as the little kid! How cute!"
                        show hali smile

                    elif catName == "Rai" or catName == "rai":
                        show hali shocked
                        ha "Ooh, your cat has the same name as that gloomy dude."
                        show hali annoyed
                        ha "I swear, he wouldn't stop talking about his girlfriend when we first woke up."
                        show hali rbf

                        if raiTrust >= 3:
                            reader "Yea, but that just means he's a good boyfriend."
                            
                            show hali thinking
                            ha "Looks like he ranted to you too about how much he misses her."
                            show hali neutral

                            reader "Haha, yea."

                            show hali thinking
                            ha "God, you have so much more patience than me."
                            show hali neutral

                        else:
                            reader "I see."

                            show hali annoyed
                            ha "Yea, I guarantee you that he will bring her up if you talk to him."
                            ha "It makes me feel single and like shit because girl, shut up."
                            show hali neutral

                    elif catName == "Hacku" or catName == "hacku":
                        show hali shocked
                        ha "Same name as the unconscious dude!"
                        show hali thinking
                        ha "I think they're kind of weird, but they seem smarter than the others so it's not that bad."
                        show hali neutral

                    elif catName == readerName or catName == readerName:
                        show hali happy
                        ha "Hahah! You guys are twins then!"
                        show hali smile

                    elif catName == "Juno" or catName == "juno":
                        show hali shocked
                        ha "WAIT! That's the name of my friend's cat!"
                        show hali happy
                        ha "Man, I miss her so much."
                        show hali smile

                        reader "Awh, you should show me a picture of her sometime."

                        show hali happy
                        ha "Yes of course!"
                        ha "I have a bunch of photos of her I stole from my friend."
                        ha "When I meet up with them.."
                        show hali enraged
                        ha "I'm totally going to kidnap Juno."
                        show hali happy
                        ha "Out of love!"
                        show hali smile

                        reader "{i}I feel uneasy for some reason..{i}"
                        reader "{i}I'm sure it's nothing.{i}"

                    elif catName == "Pickle" or catName == "pickle":
                        show hali shocked
                        ha "WAIT! That's the name of my friend's cat!"
                        show hali happy
                        ha "Man, I miss him so much."
                        show hali enraged
                        ha "But, my friend lives so fucking far away from me."
                        ha "When we meet up, I'm actually going to kill him."
                        show hali happy
                        ha "Then steal Pickle."
                        show hali smile

                        reader "{i}I feel uneasy for some reason..{i}"
                        reader "{i}I'm sure it's nothing.{i}"

                    elif catName == "Nezuko" or catName == "nezuko":
                        show hali happy
                        ha "Awh, that's the name of my cousin's cat."
                        ha "I miss her so much.."
                        show hali smile

                    elif catName == "Crespo" or catName == "crespo":
                        show hali shocked
                        ha "WAIT! That's the name of my friend's cat!"
                        show hali happy
                        ha "Man I miss her so much."
                        ha "She lives far away from me too."
                        show hali enraged
                        ha "When I meet up with this fucker, I'm going to eat her face."
                        show hali happy
                        ha "Then, of course, run away with her cat."        
                        show hali smile            
                    
                        reader "{i}I feel uneasy for some reason..{i}"
                        reader "{i}I'm sure it's nothing.{i}"

                    else:
                        show hali happy
                        ha "Cute!"
                        show hali smile

                "Yes, I have multiply.":
                    reader "Yes, I have a few cats."

                    show hali happy
                    ha "Oh my GOD! You have to tell me all the names and give me pictures when we get out of here."
                    show hali smile

                    if haliTrust == -1:
                        show bar 0
                        show trust hali
                        show up
                        with dissolve

                    elif haliTrust == 0:
                        show bar 1
                        show trust hali
                        show up
                        with dissolve

                    elif haliTrust == 1:
                        show bar 2
                        show trust hali
                        show up
                        with dissolve
                    $ haliTrust += 1

                    reader "Haha! Of course."

                    hide bar
                    hide trust
                    hide up
                    with dissolve

            show hali happy
            ha "Man, I wish I had a cat."
            show hali smile

            reader "You don't?"

            show hali thinking
            ha "Nah, but being at the shelter is really nice. I hope to get a cat soon though."
            ha "Wondering if I should actually adopt one from the shelter I volunteer at."
            show hali smile    

            reader "That seems like a good idea. You hould go for it."

            show hali happy
            ha "Yea! Once we get out of here though."
            show hali disgusted
            ha "Gah!! I really want to get out of here."
            show hali neutral

            reader "I'm sure we'll get out of here soon."
            reader "If we find a phone or something."
            
            show hali happy
            ha "True."
            ha "You're a good person, [readerName]."
            ha "You should come to the animal shelter sometime!"
            show hali smile

            if haliTrust == -1:
                show bar 1
                show trust hali
                show up
                with dissolve
            elif haliTrust == 0:
                show bar 2
                show trust hali
                show up
                with dissolve
            elif haliTrust == 1:
                show bar 3
                show trust hali
                show up
                with dissolve
            elif haliTrust == 2:
                show bar 4
                show trust hali
                show up
                with dissolve
                
            reader "Sure! I'd love to."

            hide bar
            hide trust
            hide up
            with dissolve
            $ haliTrust += 2

            show hali shocked
            ha "Ah! We should probably look for Hacku or someone to go over everything we found."
            show hali huh

            reader "Oh yea."
            reader "I came here to look for Hacku, but they weren't here."

            show hali shocked
            ha "Huh.. weird."
            show hali thinking
            ha "Well we should-"

        "Wait in silence.":
            "You wait in silence for a bit."

            reader "..."
            ha "..."
            reader "..."
            ha "..."
            reader "..."
            ha "..."
            reader "..."
            ha "..."
    jump argument


label checkLucy:
    $ roomLucy = False
    default lucyClues = 0
    default plant = True
    default trash = True
    default tool = True

    play sound "open door.mp3"
    scene black with fade
    "You go inside the garage and see Lucy squatting down next to a potted plant."
    "She seems a bit sad."

    menu:
        "What should you do?"

        "Talk to Lucy":
            show lucy neutral with dissolve
            reader "Hi Lucy."

            show lucy wave
            l "Hi [readerName]!!"

            reader "Have you found anything interesting?"

            show lucy thinking
            l "No.. I've been looking at these plants though!"
            l "They're really pretty, like the ones that are at my home."
            show lucy neutral 

            reader "You grow plants?"

            show lucy happy
            l "No, my big brother does!"
            show lucy sad
            l "I hope he isn't worried about where I am right now."
            l "Though he might not.."
            show lucy frown

            reader "Why not?"
            reader "He's your big brother."

            show lucy sad
            l "I had a small fight with him eariler today."
            l "I made a mistake and he was really angry."
            show lucy frown

            reader "Do you mind if I ask what you did?"

            show lucy thinking
            l "I don't! I just accidentally knocked over one of his potted plants."
            show lucy neutral
            "Lucy pointed at the pot that she was looking at."
            show cg flower with dissolve

            show lucy happy
            l "It actually looked kind of like this one."
            l "He really likes these kinds of flowers, even though he says they take a lot of care."
            show lucy smile
            galleryunlock cg6
            hide cg flower with dissolve

            reader "Awh, I'm sure that he knows you didn't mean to knock the pot over."

            show lucy thinking
            l "I didn't at all! I just felt really bad."
            show lucy sad
            l "When I feel like I messed up, I go out to the forest near my house."
            l "Because the person I upset would probably want some space."
            show lucy frown

            reader "Oh, is that how you ended up here?"

            show lucy thinking
            l "I think so? I'm not so sure."
            l "Is that how you got here too?"
            show lucy neutral

            reader "Ah, I actually don't remember how I got here."
            reader "I know it makes me sound suspicious, but it's true."

            show lucy happy
            l "I believe you!"
            l "My mom always said that strangers are friends you haven't met yet."
            show lucy excited
            l "And since I trust all my friends, I trust you!"
            show lucy smile

            reader "That's really idealistic."

            show lucy annoyed
            l "That's what my big brother says! He always says that I'm too naive and that I should be more careful."

            reader "Well, I would agree with your brother there. There's a lot of evil people in the world."

            show lucy thinking
            l "But, you're nice!"
            l "Everyone I meet is nice!"
            l "Well, almost everyone. I don't think Rai likes me too much."
            show lucy neutral
            
            reader "I think that is just how he is. From the time that I've talked to him."

            show lucy thinking
            l "Maybe.."
            show lucy sad
            l "I just didn't have many friends growing up so I like making them."
            show lucy frown

            reader "{i}She's just a lonely child..{i}"
            reader "I see."
            reader "Still you should be more careful with who you trust."

            show lucy annoyed
            l "Uehh! Everyone says that. I understand though.."
            show lucy sad
            l "My brother is probably right."
            show lucy frown

            reader "He's looking out for you because he doesn't want you to get hurt."

            show lucy happy
            l "I think so too! Well I hope so.."
            show lucy smile

            reader "You should call him when we get out of here."

            show lucy happy
            l "I will! I just hope he isn't still mad at me."
            show lucy neutral

            reader "Nah, he wouldn't be. I'm sure that he is just worried of where you are right now."

            show lucy happy
            l "Ok! I trust you."
            l "You and Rai remind me of my big brother!"
            l "Very stern but also very nice."
            show lucy smile

            reader "Awh, I'm flattered."

            show lucy happy
            l "Yea! Blah! I promised my mama I wouldn't be too sad for too long."
            l "[readerName]! What type of flowers do you like?"
            l "I really like sunflowers!"
            show lucy smile

            default flowers = "Flowers"
            $ flowers = renpy.input("{i}What is your favorite flower?{i}")
            $ flowers = flowers.strip()

            reader "I really like [flowers]!"

            if flowers == "Hyacinth" or flowers == "hyacinth" or flowers == "Hyacinths" or flowers == "hyacinths":
                show bar 1
                show trust lucy
                show up
                with dissolve

                show lucy happy
                l "My brother loves planting those!"
                
                hide bar 1
                hide trust lucy
                hide up
                with dissolve
                $ lucyTrust += 1

                l "He says that they're easy to care for."
                show lucy smile

            elif flowers == "Rose" or flowers == "Roses" or flowers == "rose" or flowers == "roses":
                show bar 1
                show trust lucy
                show up
                with dissolve

                show lucy thinking
                l "Oooh, my brother says that those are the most asked for flowers at his shop."
                
                hide bar
                hide trust
                hide up
                with dissolve
                $ lucyTrust += 1

                show lucy neutral

                reader "Oh, your brother owns a flower shop too?"

                show lucy happy
                l "A very small shop. He mainly works at a clock shop though!"
                show lucy smile

            elif flowers == "Forget me nots" or flowers == "Forget me not" or flowers == "forget me not" or flowers == "forget me nots":
                show lucy thinking
                l "Oooh, for some reason I think that suits you!"
                show lucy neutral

            elif flowers == "Lilacs" or flowers == "Lilac" or flowers == "lilacs" or flowers == "lilac":
                show bar 1
                show trust lucy
                show up
                with dissolve
                $ lucyTrust += 1
                
                show lucy thinking
                l "Oh! I know those flowers!"
                hide bar
                hide trust
                hide up
                with dissolve

                l "I mentioned it to Hali and she said her friend really likes them."
                show lucy neutral

                reader "Oh cute!"
                reader "How'd the topic of flowers come up though."

                show lucy happy
                l "I was just trying to make conversation like my brother does sometimes."
                l "He always talks about flowers whenever he can."
                show lucy smile

                reader "I see!"

            elif flowers == "Sunflowers" or flowers == "Sunflower" or flowers == "sunflowers" or flowers == "sunflower":
                show bar 1
                show trust lucy
                show up
                with dissolve
                $ lucyTrust += 1

                show lucy excited
                l "Yay! They're always facing towards the brightside so I want to do the same too!"
                hide bar
                hide trust
                hide up
                with dissolve
                show lucy smile

            else:
                show lucy thinking
                l "Oooh! That's a cute flower!"
                show lucy neutral

            show lucy thinking
            l "Oh wait! Hacku said to look around right?"
            l "We should do that!"
            show lucy neutral

            reader "Oh, you're right."
            
            show lucy happy
            l "But lets talk more later!"
            l "It was really fun! And this means we're friends now right?"
            show lucy smile

            reader "Sure! But yea, we should start looking around."
            
            if lucyTrust == 0:
                show bar 3
                show trust lucy
                show up
                with dissolve
            elif lucyTrust >= 1:
                show bar 4
                show trust lucy
                show up
                with dissolve

            show lucy happy 
            l "Got it!!"

            hide bar
            hide trust
            hide up
            with dissolve
            $ lucyTrust += 3

            hide lucy happy with dissolve

        "Look around":
            reader "{i}Woah, those are a lot of flowers.{i}"
            reader "{i}Well, I guess it is a garden. Or a garage..?{i}"
            reader "{i}Whatever.{i}"

    while lucyClues != 4:
        menu:
            "What should you look at?"

            "Potted plants" if plant:
                $ lucyClues += 1
                $ plant = False

                play sound "footsteps short.mp3"
                "You walk over to the potted plants that Lucy are near."
                "It's an assortment of diffently colored flowers."

                reader "{i}Huh, they all look well kept.{i}"
                reader "{i}I wonder if there is anyone taking care of them.{i}"

            "Trashcan" if trash:
                $ lucyClues += 1
                $ trash = False

                play sound "footsteps short.mp3"
                "You walk over to the trashcan near the corner."

                reader "{i}Ew... I hope there's nothing gross in here.{i}"

                menu:
                    "Go through the trash?"

                    "Yes":
                        $ numClues = numClues + 1
                        $ cameraClue = True
                        reader "{i}There might be something important here though. I guess I got no choice.{i}"

                        "You stick your hand in the trashcan."
                        
                        play sound "looking trash.mp3"
                        reader "{i}Grossgrossgrossgrossgrossgrossgrossgrossgrossgrossgrossgross.{i}"
                        reader "{i}Wait what?{i}"

                        play sound "glass shard.mp3"
                        "You pull out some broken glass pieces."

                        if clockClue:
                            reader "{i}Huh? More glass?"
                            reader "{i}No, I don't think that it's related to the clock. These pieces are too small.{i}"
                        else:
                            reader "{i}What the hell?{i}"
                            reader "{i}Ack, my hand almost got scratched.{i}"

                        reader "{i}There must be more in here then.{i}"

                        play sound "looking trash.mp3"
                        "You dig more into the trashcan and find a broken camera."
                        #show cg broken camera with dissolve

                        reader "{i}Woah, this look like a really good quailty camera too.{i}"

                        "You look at the camera. It's signed as \"Vyn's Property\"."

                        reader "{i}Eh? It says it belongs to Vyn.{i}"
                        reader "{i}If the sim card is still here, then maybe we could get a hint of what happened in the cabin!{i}"
                        reader "{i}Or it might just be full of weird stuff..{i}"
                        reader "{i}But then.. why would someone go out of their way to shatter it and try and hide it in the trashcan.{i}"
                        reader "{i}Hmmm..{i}"

                        play sound "sweeping.mp3"
                        galleryunlock cg8
                        #hide cg broken camera with dissolve
                        "You leave the camera on the table near by and make sure that none of the glass is on the floor."

                        reader "{i}I should just leave this here for now and bring it to him later.{i}"

                    "No":
                        reader "{i}I don't think I want to go through this.{i}"

            "Gardening tool shed" if tool:
                $ lucyClues += 1
                $ tool = False

                play sound "footsteps short.mp3"
                "You walk over to the tool shed."

                reader "{i}These look like they're used regularly.{i}"
                reader "{i}I don't think that this could have been used for any murdering though.{i}"
                reader "{i}Which is a good thing.{i}"
            
            "Finished looking around":
                reader "{i}I think I'm done look around.{i}"
                
                if roomHali or roomVyn or roomLucy or roomRai:
                    reader "{i}I guess I should check the other rooms.{i}"
                else:
                    reader "{i}This should have been the last room. I should go check back with Hacku.{i}"
                jump investigation

label checkRai:
    $ roomRai = False
    default raiClues = 0
    default boxes = True
    default clock = True
    default table = True

    play sound "open door.mp3"
    scene bg living glass with fade
    "You go inside the living room and see Rai looking at one of the bookshelves."

    menu:
        "What should you do?"

        "Talk to Rai":
            
            show rai neutral
            show bg living rai
            with dissolve

            reader "Hey Rai."

            show rai thinking
            r "Oh, it's you."
            show rai neutral

            reader "Find anything yet?"

            show rai thinking
            r "Nah."
            r "It's just a bunch of old books about.."
            show rai annoyed
            r "I can't even read this."
            show rai rbf

            play sound "flipping pages.mp3"
            "You look over Rai's shoulder. He is flipping through a dusty book."
            "It contains a bunch of unrecognizable characters and words that looked like it was just someone's bad handwriting."

            show rai thinking
            r "I mean I could probably try to understand it."
            r "It looks like english, but the handwriting is so bad."
            show rai neutral

            reader "Yea.."

            play sound "close book.mp3"
            "Rai shuts the book and puts it back on the shelf."

            show rai erm
            r "Ugh.."
            r "I was supposed to meet up with my girl you know."
            show rai neutral

            reader "How'd you end up here then?"

            show rai thinking
            r "All I remember is I took a shortcut throguh these creepy ass woods."
            show rai neutral

            reader "Why would you do that...?"

            show rai thinking
            r "Ok well, if you knew my girlfriend then you'd know she's the most beautiful girl ever."
            r "If I ever kept her waiting, I wouldn't be able to call myself her boyfriend."
            show rai neutral

            reader "..."
            reader "{i}This dude is a simp.{i}"
            reader "I see.."

            show rai annoyed
            r "Oi!"
            r "The hell's up with that face?"
            r "She had to move and I was trying to find the place so Moogle Maps told me to go through the forest."
            show rai rbf

            reader "The forest?"

            show rai thinking
            r "I don't know why either, but I was borderline running late so I had to get there quick."
            show rai neutral

            reader "I mean, I'm sure your girlfriend would have understood if you were a bit late."

            show rai thinking
            r "She would have but.."
            show rai erm
            r "I don't want her to wait."
            r "Because I promised her."
            r "Man.."
            show rai neutral

            play sound "photo.ogg"
            menu:
                "Rai pulls out a picture from inside the pocket of his jacket."

                "Can I see?":
                    reader "Mind if I take a look?"
                    
                    show rai happy
                    r "Sure bro."

                    if raiTrust == -1:
                        show bar 0
                        show trust rai
                        show up
                        with dissolve
                    elif raiTrust == 0:
                        show bar 1
                        show trust rai
                        show up
                        with dissolve
                    elif raiTrust == 1:
                        show bar 2
                        show trust rai
                        show up
                        with dissolve

                    #show tiffany with dissolve
                    r "I love her so much."

                    hide bar
                    hide trust
                    hide up
                    with dissolve
                    $ raiTrust += 1

                    r "She's so pretty and kind and nice."
                    show rai smile
                    
                    reader "She's pretty."
                    
                    show rai happy
                    r "Yep."
                    r "That's my girlfriend."
                    r "And I'm damn proud to have pulled her."
                    show rai smile
                    #hide tiffany with dissolve

                "Say nothing.":
                    "Rai puts away the photo."

            show rai thinking
            r "Bah, anyways."
            play sound "photo.ogg"
            show rai happy
            r "Thanks for listening [readerName]."
            show rai smile

            reader "No problem!"

            if raiTrust == -1:
                show bar 1
                show trust rai
                show up
                with dissolve
            elif raiTrust == 0:
                show bar 2
                show trust rai
                show up
                with dissolve
            elif raiTrust == 1:
                show bar 3
                show trust rai
                show up
                with dissolve
            elif raiTrust == 2:
                show bar 4
                show trust rai
                show up
                with dissolve

            show rai thinking
            r "Aight, let's look around now."

            hide rai thinking
            show bg living glass
            with dissolve

            hide bar
            hide trust
            hide up
            with dissolve
            $ raiTrust += 2
        
        "Look around":
            "You start looking around."
            reader "{i}Hmm...{i}"
            reader "{i}This place is really well furnished.{i}"
            reader "{i}Hoping that there isn't a lot of dust though.{i}"
    
    while raiClues != 4:
        menu:
            "What should you look at?"

            "Boxes" if boxes:
                $ raiClues += 1
                $ boxes = False
                
                play sound "footsteps short.mp3"
                "You walk over to the box next to the grandfather clock."

                if cabinUgly:
                    reader "..."
                    reader "{i}This place is such a dump. They just leave empty boxes around like it's nothing!{i}"
                else:
                    reader "{i}Huh, an empty box.{i}"
                    reader "{i}Looks like there's anotehr one on that table that Rai is sitting next to.{i}"
                
                if clockClue:
                    reader "{i}There's only the glass I put in there.{i}"
                    reader "{i}Other than that, there isn't anything worth noting.{i}"
                else:
                    reader "{i}I don't think that there is anything worth noting in them though.{i}"

            "Grandfather clock" if clock:
                $ raiClues += 1
                $ clock = False

                play sound "footsteps short.mp3"
                "You walk over to the grandfather clock."
                "The clock is broken and there is glass on the ground."

                reader "{i}Woah! There is so much glass on the ground.{i}"

                menu:
                    "What should you do?"

                    "Clean up the glass":
                        $ numClues += 1
                        $ clockClue = True

                        reader "{i}I should clean this up.{i}"

                        play sound "sweeping.mp3"
                        show bg living clean with dissolve

                        "You start moving the glass shards in a box nearby."

                        reader "{i}I feel like there are some pieces missing because this amount of glass.{i}"
                        reader "{i}I have a feeling that I should keep an eye out on where it went.{i}"

                    "Leave it alone":
                        reader "{i}I should just warn Rai about the glass.{i}"
                        reader "Rai! Be careful there's a lot of glass over here."

                        r "Oh shit. Bruh, who the fuck just leaves glass on the ground."

                        reader "Yea.."

            "Table" if table:
                $ raiClues += 1
                $ table = False
                
                play sound "footsteps short.mp3"
                "You walk over to the table. It's full of dust."
                reader "{i}I'm so done with all of these dust filled rooms.{i}"
            
            "Finished looking around":
                reader "{i}I think I'm done look around.{i}"
                
                if roomHali or roomVyn or roomLucy or roomRai:
                    reader "{i}I guess I should check the other rooms.{i}"
                else:
                    reader "{i}This should have been the last room. I should go check back with Hacku.{i}"
                jump investigation

label checkHali:
    $ roomHali = False
    default haliClues = 0
    default counter = True
    default door = True
    default floor = True

    play sound "open door.mp3"
    scene bg kitchen hali with fade
    "You go inside the kitchen and see Hali fiddling with something near the countertop."
    "As you walk closer, you see she is still very angry."

    menu:
        "What should you do?"

        "Talk to Hali":
            $ haliAngry = True
            show bg kitchen
            show hali rbf
            with dissolve
            reader "Hey Hali."

            show bar 0
            show trust hali
            show down
            with dissolve

            show hali annoyed
            ha "What do you want?"
            
            hide bar
            hide trust
            hide up
            with dissolve
            $ haliTrust -= 1

            ha "I'm pissed off as is so just leave me alone."
            ha "It's not like I even found anything in this stupid room anyways."
            show hali rbf

            reader "Ah.. Ok."

            hide hali rbf 
            show bg kitchen hali 
            with dissolve
            reader "{i}I should just look around.{i}"

        "Leaver her alone and look around":
            $ haliAngry = False
            play sound "footsteps short.mp3"
            "You start to walk quietly around."
            hide hali rbf with dissolve
            reader "{i}It looks like Hali hasn't notice me yet. It was a good idea to have left her alone.{i}"

    while haliClues != 4:
        menu:
            "What should you look at?"

            "Counter tops" if counter:
                $ counter = False
                $ haliClues += 1
                
                play sound "footsteps short.mp3"
                "You walk over to the counters. It's all full of dust."
                
                reader "{i}I need to be careful to not sneeze to not disturb Hali."

                menu:
                    "What should you do?"

                    "Look closer":
                        "You try to inspext the counter top more."
                        "You see hand prints and signs of some sort of fighting."

                        reader "{i}Crap, I'm going to sneeze.{i}"
                        reader "ACHOO!" with vpunch

                        play sound "running.mp3"
                        show hali shocked at left
                        show bg kitchen
                        with dissolve
                        ha "!!!"

                        if haliAngry:
                            show hali shock at five
                            with move
                            ha "Are you okay [readerName]??"
                            show hali huh

                            reader "Yea, It's just some dust."

                            show hali thinking
                            ha "I see."
                            show hali neutral at offright
                            with move

                            reader "{i}Ack, I need to be more careful.{i}"
                            hide hali neutral
                            show bg kitchen hali 
                            with dissolve
                        
                        else:
                            show hali annoyed 
                            ha "What the hell? When did you get in here?"
                            show hali rbf

                            reader "Oh.. a while ago. I didn't want to disturb you, sorry."
                        
                            show hali shocked
                            ha "..."
                            show hali happy
                            
                            show bar 1 with dissolve
                            show trust hali with dissolve
                            show up with dissolve

                            ha "Awh.. Thank you."

                            hide hali happy 
                            show bg kitchen hali 
                            with dissolve

                            hide bar
                            hide trust
                            hide up
                            with dissolve
                            $ haliTrust += 1

                            reader "{i}At least she doesn't seem angry any more.{i}"

                    "Do nothing":
                        reader "{i}I am not sneezing again.{i}"

            "Locked door" if door:
                $ door = False
                $ haliClues += 1
                
                "You looked at the door. It has no handle and is boarded up with planks of wood."
                
                reader "{i}This seems to be the door to the outside. Maybe.{i}"
                reader "{i}I wonder if we could just break it down, but it might not even go outside."

                "You put your ear near the door but hear nothing."

                reader "{i}It probably doesn't go outside then if I hear nothing.{i}"

            "The floor" if floor:
                $ floor = False
                $ haliClues += 1
                $ numClues += 1
                $ footPrintClue = True                

                "You look at the floor." 
                "There are a lot of footprints going in different directions."
                
                reader "{i}Huh? There are so many footprints here.{i}"
                reader "{i}Wait, what's this?{i}"
                reader "{i}Oh god, there's dirt and more dust. It also looks like something was dragged through here.{i}"
                reader "{i}The only things that would make this kind of big mark in this cabin would have been… a body..{i}"
                reader "{i}I should keep this in mind.{i}"

            "Finished looking around":
                reader "{i}I think I'm done look around.{i}"
                
                if roomHali or roomVyn or roomLucy or roomRai:
                    reader "{i}I guess I should check the other rooms.{i}"
                else:
                    reader "{i}This should have been the last room. I should go check back with Hacku.{i}"
                jump investigation

label checkVyn:
    $ roomVyn = False
    default vynClues = 0
    default diningTable = True
    default diningRug = True
    default plates = True

    play sound "open door.mp3"
    scene bg dining vyn with fade
    "You walk into the dining hall and see Vyn sitting on the dining table with his legs crossed."

    reader "{i}Wow, he looks really comfy.{i}"
    reader "{i}Oh and there's only two chairs..?{i}"

    menu:
        "What should you do?"

        "Talk to Vyn":
            show bg dining
            show vyn neutral 
            with dissolve

            reader "Sup Vyn!"

            show vyn happy
            v "Eyy, what's up dude?"
            show vyn smile

            reader "Did you find anything yet?"

            show vyn thinking
            v "Nope."
            v "TBH, I have no idea what I'm supposed to be looking for."
            show vyn neutral

            reader "Me either, don't worry."

            show vyn happy
            v "Ey, thanks bro."
            v "By the way, how'd you even get here?"
            show vyn smile

            reader "Oh, I actually don't remember."

            show vyn happy
            v "Ay, all good bro. I'm sure you'll get your memory back!"
            show vyn smile

            reader "{i}Wow, he's really nice.{i}"
            reader "How did you get here? If you don't mind me asking."

            show vyn silly
            v "All good, I don't mind."
            show vyn thinking
            v "I was actually filming a video near a forest as a dare."
            v "Also for content for my show."
            v "I didn't want to dance so I opted to do something else."
            show vyn happy
            v "This is actually more fun for me so win-win!"
            show vyn smile

            reader "Oh, I see."

            show vyn happy
            v "Yea bro. It look me a bit to remember of why I came into the forest, but I remembered so I'm sure you will too."
            show vyn smile

            reader "Haha, thanks."

            show vyn thinking
            v "Yuh."
            v "But also I don't know where my camera is."
            v "When I got up in that room, I was looking in my pockets or just around for it."
            v "It was hella expensive too so I hope nothing happened to it."
            show vyn neutral

            if cameraClue:
                reader "..."
                reader "{i}I should tell him later.{i}"
            reader "I hope you find it too!"

            show vyn happy
            v "Thanks!"
            v "You're actually so nice dude. A lot nicer than the others."
            show vyn smile

            reader "Ahh, thanks."
            reader "Oh also, why do you annoy Hali so much? If you don't know each other."

            show vyn silly
            v "Oh, that? I have met her before actually."
            v "Dunno if she actually remembers though."

            reader "Oh, wait if you know each other, why'd she blow up at you like that?"

            show vyn thinking
            v "I mean, I don't know her that well."
            v "She's just that type that gets super annoyed easily and it's so funny."
            show vyn smile

            reader "{i}Oh, he's that type of person.{i}"

            show vyn happy
            v "After all of this though, I think she's a cool person to hang out with!"
            v "I just like annoying people though LOL."
            show vyn smile

            reader "Haha, I see."

            show vyn thinking
            v "Oh shit, I rambled a lot."

            if vynTrust == 1:
                show bar 3
                show trust vyn
                show up
                with dissolve
            elif vynTrust == 2:
                show bar 4
                show trust vyn
                show up
                with dissolve

            v "C'mon [readerName]! We gotta lock in!"
            hide vyn thinking
            show bg dining vyn
            with dissolve

            hide bar
            hide trust
            hide up
            hide dissolve
            $ vynTrust += 2

        "Look around":
            reader "{i}I wonder if people actually used this room. It looks like it hasn't been used in years.{i}"
            reader "{i}Who would invite someone over to this dining hall in the middle of no where.{i}"

    while vynClues != 4:
        menu:
            "What should you look at?"

            "Dining table" if diningTable:
                $ vynClues += 1
                $ diningTable = False
                $ numClues = numClues + 1
                $ hairClue = True
                
                play sound "footsteps short.mp3"
                "You walk over to the dinning table that Vyn is sitting on."
                "The table looks like it was moved from it's original spot. The carpet being disturbed a bit too."

                reader "{i}Eh? What's this?{i}"

                "Under the table you see some strands of long white and black hair with some blood staining the carpet."
                "It looks like there was a fight here."

                reader "{i}Who would be fighting in the dining room?{i}"
                reader "{i}It must have been a serious fight if there was hair ripped out.{i}"
                reader "{i}Didn't the body have some bruises? When I go back I should check.{i}"

            "Broken chair" if diningRug:
                $ vynClues += 1
                $ diningRug = False

                play sound "footsteps short.mp3"
                "You walk over to the broken chair."

                reader "{i}Why would they just leave the broken chair here and not get rid of it?{i}"
                
                menu:
                    reader "{i}Should I ask Vyn if he knows anything?{i}"

                    "Ask Vyn":
                        reader "Hey Vyn?"

                        show bg dining
                        show vyn thinking 
                        with dissolve

                        v "Sup bro."
                        show vyn neutral

                        reader "When you came in here, was the chair broken already?"

                        show vyn thinking
                        v "Oh shit yea. Thought that was so weird because it was like put there normally."
                        show vyn happy
                        v "I mean that would a really good prank, you sit down and the chair like fails on you."
                        show vyn thinking
                        v "But, I moved it so it would be on the ground."
                        show vyn neutral

                        reader "Mhm, I see."

                        hide vyn neutral 
                        show bg dining vyn
                        with dissolve

                        reader "{i}Maybe it was used to hurt someone in some way.{i}"
                        reader "{i}I should ask Hacku later if they found anything about the body that could connect to this.{i}"

                    "Leave it alone":
                        reader "{i}I probably shouldn't bother him.{i}"
                        reader "{i}I doubt it was anything important other than just a broken chair.{i}"

            "Fancy place sets" if plates:
                $ vynClues += 1
                $ plates = False

                play sound "footsteps short.mp3"
                "You walk over to the cupboards holding some fancy looking plates."

                reader "{i}Woah, these plates are really fancy.{i}"
                reader "{i}I wonder why someone left these here.{i}"
                reader "{i}Wait, what if we're trespassing into someone's house?{i}"
                reader "{i}Well it's not like any of us asked to be here.{i}"

            "Finished looking around":
                reader "{i}I think I'm done look around.{i}"
                
                if roomHali or roomVyn or roomLucy or roomRai:
                    reader "{i}I guess I should check the other rooms.{i}"
                else:
                    reader "{i}This should have been the last room. I should go check back with Hacku.{i}"
                jump investigation

label argument:
    "{i}SLAM{i}" with vpunch

    show hali shocked at sixseven
    with move

    show rai enraged at fourthree
    show lucy scared at two
    with moveinleft

    r "I CAN'T FUCKING BELIEVE THIS!"
    show rai pissed

    reader "!?"

    show hali annoyed
    ha "The hell?"
    show hali rbf

    show rai enraged
    r "What the hell? You knew his name and you never said anything!"
    show rai pissed

    reader "What's going on?"

    show rai enraged
    r "Lucy knows who this dude is! The dead dude!"
    show rai pissed

    scene black with fade
    #scene rai mad cg with fade
    r "I can't believe you knew the entire time!"
    r "Why didn't you tell us or did you not even care because you're the one who doesn't want anyone to find out."

    menu:
        "What should you do?"

        "Calm him down":
            reader "Hey, calm down a bit-"

            r "I never asked for your damn opinion [readerName]!"
            
            if raiTrust == -1:
                show bar 0
                show trust rai
                show down
                with dissolve
            elif raiTrust <= 0:
                show bar 1
                show trust rai
                show down
                with dissolve
            elif raiTrust == 1:
                show bar 0
                show trust rai
                show down
                with dissolve
            elif raiTrust == 2:
                show bar 1
                show trust rai
                show down
                with dissolve
            elif raiTrust == 3:
                show bar 2
                show trust rai
                show down
                with dissolve

            r "Don't defend her when she is obviously the murder."

            hide bar
            hide trust
            hide down
            with dissolve
            $ raiTrust -= 1
                        
        "Stay quiet":
            r "Ugh, this is so annoying."

    l "I'm sorry..."
    l "I didn't tell you guys because I didn't think it was that important."

    r "Not that important??"
    r "That's one of the most important things ever that we need to know!"
    r "I can't tell if you're actually stupid or some sort of mastermind that planned all of this."

    play sound "open door"
    hk "Huh? What's going on with the yelling?"

    scene bg main body
    play sound "footsteps short.mp3"
    show hali huh at sixseven
    show rai at fourthree
    show lucy scared at two
    with dissolve

    show rai annoyed
    r "Oh my god, where have you been?"
    show rai rbf

    show hacku thinking at eightseven
    with moveinright
    hk "Just checking the other hallway, why?"
    show hacku neutral

    show rai enraged
    r "Lucy knows who the fucking dead dude is! His name is Shugo apparently."
    r "We have to like lock her in one of the rooms or something. We are not safe if she can move freely."
    show rai pissed

    #show hacku shocked
    hk "Shugo..?"

    reader "Something wrong?"

    show hacku thinking
    hk "No, nothing."
    hk "Anyways. his name doesn't matter right now."
    hk "Lucy, how do you know him?"
    show hacku neutral

    show lucy thinking
    l "Umm... he's a family friend of mine.."
    l "I guess not really like a friend but friends with the people who live around me."
    show lucy neutral

    show rai annoyed
    r "Hah! What a load of bullshit."
    r "Anyone could tell that you probably just betrayed him, killed him and then set up this whole murder house."
    show rai rbf

    show lucy sad
    l "I wouldn't do that to my friends though!"
    show lucy scared

    show rai enraged
    r "I AM NOT YOUR FUCKING FRIEND!"
    show rai pissed

    play sound "open door"
    show vyn thinking at one
    with moveinleft

    v "Hey dude, chill!"
    show vyn neutral

    show rai enraged
    r "Where the fuck did you come from? And don't \"dude\" me!"
    r "You haven't been taking this seriously since the beginning!"
    show rai erm
    r "Fuck man, I just want to get out of here."

    show hacku thinking
    hk "Even if you get out, you'll be on the suspects list and will have to remain in custody until the case is clear."
    show hacku neutral

    show rai annoyed
    r "Ugh, fine."
    r "Just keep me away from America Psycho over there."
    show rai rbf
    
    show vyn neutral at two
    show lucy frown at one
    with move

    reader "So, Hacku, what did you find about the body?"

    show hacku thinking
    hk "He seems to have died from blood loss."
    hk "There is a big gash on his neck, but I couldn't find anything sharp in the vicinity so I could be wrong."
    show hacku neutral

    show hali annoyed
    ha "I thought you said you worked with dead bodies?"
    show hali rbf

    show hacku happy
    hk "I don't perform autopsies, Hali."
    show hacku smile

    show hali annoyed
    ha "The hell do you do then?"
    show hali rbf

    reader "That doesn't matter right now."

    show hali annoyed
    ha "Ugh, whatever."
    show hali rbf

    show lucy thinking
    l "What did you guys find in the other rooms?"
    show hali neutral

    if numClues == 0:
        reader "To be honest, I didn't really find anything.."

        show hacku thinking
        hk "Oh, don't worry. I think I found enough things to piece together what happened."
        show hacku neutral

        show rai erm
        r "What? Really?"

        jump bad_ending_1
    
    else:
        default brokenGlass = False
        $ brokenGlass = clockClue

        default foot = False
        $ foot = footPrintClue

        default camera = False
        $ camera = cameraClue

        default death = False
        $ death = deathClue

        default hair = False
        $ hair = hairClue

        default liquid = False
        $ liquid = ventClue

        default clues = 0

        while clues != numClues:
            menu:
                "What evidence should you present?"

                "Grandfather clock" if brokenGlass:
                    $ clues += 1
                    $ brokenGlass = False
                    
                    reader "In the living room, I found a grandfather clock."

                    show hali thinking
                    ha "What's so great about a clock?"
                    show hali neutral

                    reader "Well nothing really but it was broken."

                    show lucy thinking
                    l "Broken? Like it fell?"
                    show lucy neutral

                    reader "No, the glass was broken. And it was all over the floor but here's the weird part."
                    reader "I tried to clean up the glass so that no one would step on it."

                    show rai happy
                    r "A model citizen. I like this guy."
                    show rai neutral

                    reader "Pfft sure. Anyways, when I cleaned it up and there seemed to be some glass missing."
                    reader "I also looked around and it seemed to just not be in the room."
                    reader "So, I don't know where it went."

                    if glassClue:
                        show hacku thinking
                        hk "Huh, you think it could be related to the murder?"
                        show hacku neutral

                        reader "I don't see what else could have.. uh..."

                        show rai thinking
                        r "Killed him?"
                        show rai neutral

                        reader "Well yea."

                        show rai annoyed
                        r "You're way too soft bruh."
                        show rai rbf

                        reader "Haha..."

                    else:
                        #show hacku shocked
                        hk "..."

                        v "What's up Hacku bro?"
                        v "You look like you need to, like, take a shit."

                        show hali disgusted
                        ha "What the fuck."

                        show hacku thinking
                        hk "Ah, don't worry. Contiune with the discussion."
                        show hacku neutral

                    reader "But yea, that is the only thing of interest in the living room."

                "Footprints" if foot:
                    $ clues += 1
                    $ foot = False
                    
                    reader "In the kitchen, I found a bunch of footprints."
                    reader "But also, there were a bunch of marks. Like something was dragging through the kitchen."

                    show hali shocked
                    ha "Oh shit, I didn't even notice. I thought that whoever owned this place is just doesn't clean."
                    show hali neutral

                    reader "Fair enough."

                    show rai thinking
                    r "I wouldn't be surprised though, if it's just regular dirt and not cleaning."
                    r "This place is a fucking dump."
                    show rai neutral

                    reader "I was thinking that the only thing that is big enough to make dragging marks like that was someone dragging a body."

                    show vyn silly
                    v "On god, bro." 
                    show vyn smile

                    show hali disgusted
                    show lucy thinking
                    l "I did wake up with a few leaves in my hair!"
                    show lucy neutral

                    show hacku thinking
                    hk "Huh.. good eye [readerName]."
                    hk "I did notice that almost everyone had some dirt on them."
                    hk "That means where we woke up doesn't really mean that is where you were knocked out."
                    show hacku smile

                    "Hacku gives Rai a side-eye."

                    show rai erm
                    r "..."
                    r "..Sorry."
                    show rai neutral

                    #show hacku laugh
                    hk "Haha! All good."
                    show hacku thinking
                    hk "Was there anything else in the kitchen?"
                    hk "Like a weapon or.."
                    show hacku neutral

                    reader "Nah, I didn't find any knifes or anything that could have killed Shugo."

                    show hacku thinking
                    hk "Hmm... I see."
                    show hacku neutral

                "Camera Clue" if camera:
                    $ clues += 1
                    $ camera = False

                    reader "In the garage, I found something in the trashcan."

                    show lucy thinking
                    l "Ouh, did you go through the trash? I did hear some russling behind me."
                    show lucy neutral

                    show vyn happy
                    v "You totally did, didn't you!"
                    v "Hahahaha!"
                    show vyn smile

                    show hali disgusted
                    ha "Please tell me you washed your hands or something after."
                    
                    reader "Ok well! There was only some crumpled pieces of paper and shattered glass in there."
                    reader "Probably some dirt too and the camera."
                    show hali neutral

                    show vyn thinking
                    v "Oh shit, did you say camera?"
                    show vyn neutral

                    reader "Yea! It actually said your name on it."

                    play sound "footsteps short.mp3"
                    "You walk to the garage to get the camera you left on the table."
                    reader "It's this right?"

                    show vyn happy
                    v "Yea dude!"
                    show vyn smile

                    "You give Vyn the camera."

                    show vyn thinking
                    v "Wait! I remember how I ended up here!"
                    v "I was filming something for a video and a buddy of mine dared me to go into the creepy forest."
                    show vyn neutral

                    show hali enraged
                    v "And you fucking listened?"
                    show hali pissed

                    show vyn happy
                    v "Duh, my buddy dared me too!"
                    show vyn smile

                    show rai thinking
                    r "Idiot."
                    show rai neutral

                    show lucy happy
                    l "So cool!"
                    show lucy smile

                    show vyn happy
                    v "But yea, I was filming then I found like this cabin in the middle of the woods."
                    v "Probably this one bro."
                    v "Of course I had my camera filming everything."
                    show vyn thinking
                    v "Then uh...."
                    show vyn neutral

                    show hali annoyed
                    ha "Well? Spit it out!"
                    show hali rbf

                    show vyn happy
                    v "Well, I dont remember anything after LOL."
                    show vyn smile

                    show hali annoyed
                    ha "Dumbass bruh, what the fuck."
                    show hali rbf

                    show vyn thinking
                    v "Hey! But if we get the sim card out and play it then we'll see what happened before we all knocked out."
                    show vyn neutral

                    show rai erm
                    r "..."
                    r "He just said something smart."

                    show hali shocked
                    ha "Holy shit."
                    show hali huh

                    show vyn happy
                    v "Hah! I meant to do that all along."
                    show vyn smile

                    show hacku thinking
                    hk "Is the sim card damaged at all?"
                    show hacku neutral

                    show vyn thinking
                    v "Naw, I make sure to make it extra protected in my cameras because I sometimes break them."
                    v "The camera might have turned to shit but the sim card should be good."
                    v "But this clears me right?"
                    show vyn neutral

                    show hali annoyed                    
                    ha "Ugh."
                    show hali rbf

                    show hacku thinking
                    hk "Well, I guess so. It checks out."
                    show hacku neutral
            
                "Cause of death" if death:
                    $ clues += 1
                    $ death = False

                    reader "I checked the body with Hacku and I'm pretty sure that he died by something sharp to the neck."
                    reader "Also, I'm pretty sure he was still alive when bleeding out."

                    show hali disgusted
                    ha "Ugh, spare me the details of that."

                    show lucy thinking
                    l "I don't think it's that bad."
                    l "My big brother always watches those kind of scary shows." 
                    show lucy neutral

                    show rai thinking
                    r "I don't even want to know."
                    show rai neutral

                    show lucy happy
                    l "My big brother is kinda of like you Rai!"
                    l "I think you two would get along."
                    show lucy smile

                    show rai enraged
                    r "Fuck no! If he's anything like you."
                    show rai pissed

                    show hacku happy
                    hk "Ahaha.. anyways."
                    show hacku thinking
                    hk "Shugo looked like he had a few bruises but nothing that caused anything life threatening."
                    show hacku neutral

                    show rai thinking
                    r "Did you find anything sharp that could kill the dude then?"
                    show rai neutral

                    reader "Um.. well I didn't."

                    show hacku thinking
                    hk "At least we know how he died and what we should be looking for for the murder weapon."
                    show hacku neutral

                    show lucy thinking
                    l "What if the weapon wasn't something like in the movies?"
                    show lucy neutral

                    show hacku thinking
                    hk "It's usually best to assume the more common things. Like how it could have been a knife or something similar."
                    show hacku neutral

                    show rai thinking
                    r "And if it is one of those rare cases?"
                    show rai neutral

                    show hacku happy
                    hk "Well, we'll deal with it if it happens!"
                    show hacku smile

                    show rai thinking
                    r "Bruh. Ok fine."
                    show rai neutral

                    show hacku happy
                    hk "I'm sure that we haven't uncovered everything in this house."
                    show hacku smile

                "White hair" if hair:
                    $ clues += 1
                    $ hair = False
                    
                    reader "In the dining room-"

                    show vyn happy
                    v "DAWG! There were a bunch of cool plates like a bunch of them."
                    show vyn smile

                    show lucy happy
                    l "Ooooh! Did any of them have any pretty patterns?"
                    show lucy smile

                    show vyn happy
                    v "Yea dude! There were-"
                    show vyn smile
                    
                    show hali annoyed
                    ha "Oh my fucking god, let [readerName] speak!"
                    show hali rbf

                    reader "Aha.."
                    reader "No worries."
                    reader "In the dining room, there were a lot of traces of a fight or someone at least resisted."

                    show hali shocked
                    ha "A fight?"
                    show hali thinking
                    ha "Shugo is also like bruised up."
                    show hali neutral

                "Liquid from vents" if liquid:
                    $ clues += 1
                    $ liquid = False

                    reader "I found something that was really weird in this room."

                    show hali annoyed
                    ha "Couldn't be more weird than the sunglasses bitch."
                    show hali rbf

                    reader "There's a vent in this room that was unscrewed so I looked at it and there was something leaking out of it."
                    reader "It was like a clear liquid but it wasn't water."

                    show rai thinking
                    r "How could you be so sure?"
                    r "This place is probably going to croak any minute."
                    show rai neutral

                    if taste:
                        reader "Well, I sorta tasted it."

                        show hali shocked
                        ha "What?!"
                        ha "Why would you do that?"
                        ha "What if it was poisen??"
                        show hali huh

                        reader "Yea yea I know! I just wasn't thinking."
                        reader "I don't feel any different though so I think it was safe?"

                        show vyn happy
                        v "My bro's stomach is strong as hell!"
                        show vyn smile

                        reader "It was slightly sweet."

                    elif sniff:
                        reader "Well.."

                        show hacku happy
                        hk "Oh wait! Is that the thing you were sniffing on the ground?"
                        show hacku smile

                        reader "!!"
                        reader "{i}Gah, I forget they were there to see that.{i}"
                        reader "Yea..."

                        #show hacku laugh
                        hk "Hahahahahah! God, that was so funny."

                        reader "Blahh!! Enough!"
                        
                        show hacku happy
                        hk "Hahaha! Sorry sorry, you can continue."
                        show hacku smile

                        reader "Well, it smelled kinda sweet."

                    show rai erm
                    r "Eh? Sweet?"

                    reader "Yea."
                    reader "I think that it was some sort of chemical that put us all to sleep."
                    reader "Or at least knocked us out for a while."       

                    show hacku thinking
                    hk "Chloroform."
                    hk "It's a chemical that can be used to knock people out."
                    show hacku neutral

                    show rai thinking
                    r "Bruh, how do you know this?"
                    show rai neutral

                    show hacku thinking
                    hk "Uhhh.."
                    show hacku neutral

                    show lucy thinking
                    l "Wait! I have a question."
                    show lucy neutral

                    reader "Yea?"

                    show lucy thinking
                    l "If it's a liquid then how did we get affected by it?"
                    show lucy neutral

                    reader "Because it was a gas.. that traveled through the vents but turned back into liquid because of the cold weather."

                    show rai annoyed
                    r "And you said it wasn't cold!"
                    show rai rbf

                    show lucy happy
                    l "Heheh! It isn't though!"
                    show lucy smile

                    show rai annoyed
                    r "Bruh-"
                    r "Ok, whatever"
                    show rai rbf

                    show hacku thinking
                    hk "It's good to know how we all got knocked out."
                    hk "And the fact that the culprit didn't have to be in the room to knock people out."
                    show hacku neutral

                    reader "Mhm."

    show hacku thinking
    hk "Is that everything you found?"
    show hacku neutral

    reader "Yea."

    #checking trust
    default trust = 0

    if lucyTrust >= 3:
        $ trust += 1

    if hackuTrust >= 3:
        $ trust += 1

    if raiTrust >= 3:
        $ trust += 1

    if haliTrust >= 3:
        $ trust += 1

    if vynTrust >= 3:
        $ trust += 1

    # you need 4-6 clues
    if numClues < 4:
        jump bad_ending_1
    
    # you need 4-5 people's trust
    elif trust < 4:
        jump bad_ending_2
    
    else:
        jump murderer
        

label bad_ending_1:
    show rai annoyed
    r "Dude, you found like nothing."
    show rai rbf

    show hali annoyed
    ha "Yea, what the hell [readerName]?"
    show hali rbf

    reader "..Sorry."

    show lucy annoyed
    l "Don't be mean to [readerName]!"
    show lucy neutral

    show hacku thinking
    hk "It's alright actually."
    show hacku neutral

    "?"

    reader "What do you mean Hacku?"

    show hacku happy
    hk "I found all the evidence needed from the rooms."
    show hacku smile

    show vyn happy
    v "Ayy bro you were holding out on us then!"
    v "What'dya find?"
    show vyn smile

    show hacku happy
    hk "Hahah, thanks Vyn."
    show hacku smile
    
    if ventClue == False:
        show hacku thinking
        hk "Well, there's traces of chloroform being spread throughout the vents."
        show hacku neutral

        show lucy thinking
        l "Ouh, what's chloroform?"
        show lucy neutral

        show hacku thinking
        hk "It's something that can make someone go to sleep by force basically."
        hk "It's what made us all pass out and be dragged into this cabin."
        show hacku neutral

        show rai annoyed
        r "Bruh, so you're telling me some sicko drugged us and dragged us into this shitty house."
        show rai rbf

        show hacku thinking
        hk "Essentially, yes."
        show hacku neutral

        show rai annoyed
        r "What the fuck."
        show rai rbf

    if cameraClue == False:
        show hacku thinking
        hk "Oh also, Vyn."
        show hacku neutral

        show vyn happy
        v "Yuh."
        show vyn smile

        "Hacku pulled out something from their pocket."
        #show cg camera with dissolve

        show hacku thinking
        hk "I'm assuming that this is yours? Since it had your name on it."
        show hacku neutral

        #hide cg camera with dissolve
        show vyn happy
        v "Yea! Dude, how'd you find it?"
        show vyn smile

        show hacku thinking
        hk "It was in a trashcan actually. I'm pretty sure that someone was trying to get rid of it."
        show hacku neutral

        show vyn thinking
        v "Ehh? But why? I legit just have a recording of me in the woods because I emptied the sim card before I went out."
        show vyn neutral

        show rai erm
        show hali shocked
        #show hacku shocked
        r "..."

        ha "..."

        hk "..."

        reader "..."

        show hali enraged
        show rai pissed
        ha "I am going to kill you."
        show hali pissed

        #show hacku laugh
        hk "Pft- Don't, it's ok."

        show hali enraged
        ha "YOU COULDN'T HAVE TOLD US EARILER?"
        show hali pissed

        show vyn thinking
        v "Eh? Is it that important LOL?"
        show vyn neutral

        show hacku happy
        hk "Well, it clears you for being the murderer."
        hk "Since why would the killer take a video of the crime scene and then throw it away later."
        show hacku smile

        show vyn silly
        v "I mean like, what if they weren't thinking."

        show rai enraged
        r "Not everyone is as stupid as you."
        show rai pissed

        show vyn dramatic
        v "ARGH! So mean!"

        show hacku happy
        hk "This is good to know though!"
        show hacku smile

        show vyn silly
        v "Let's go! I'm hashtag innocent!"

    if footPrintClue == False:
        show hacku thinking
        hk "Also!"
        hk "In the kitchen there were marks that indicated something was dragged along the floor."
        hk "Along with a lot of footprints."
        show hacku neutral

        show lucy thinking
        l "What does that mean then?"
        show lucy neutral

        show hacku thinking
        hk "It means that where we woke up wasn't necessarily where we fainted."
        show hacku smile

        "Hacku gives Rai a side-eye."
        
        show rai erm
        r "..."
        r "..Sorry."
        show rai neutral

        #show hacku laugh
        hk "Haha! All good."
        show hacku happy
        hk "Just wanted to let you know."
        show hacku smile

    if hairClue == False:
        show vyn thinking
        v "Oh yea, in the dining room there was like this broken chair."
        show vyn neutral

        show hacku thinking
        hk "Ah! You reminded me."
        hk "In the dining room, there was traces of a fight."
        show hacku neutral

        show hali thinking
        ha "A fight?"
        show hali neutral

        show hacku thinking
        hk "Yea."
        hk "I'm pretty sure that broken chair was hit as some sort of defence or offence."
        show hacku neutral
        
        show vyn silly
        v "That's such a sick fight."

        show hali shocked
        ha "Jeez, I wouldn't expect someone to be conscious after being hit by that."
        show hali huh

        show hacku thinking
        hk "That isn't all."
        hk "There was also some strands of black and white hair and some blood there too."
        show hacku neutral

        show vyn thinking
        v "Damn!"
        show vyn neutral

        show hali annoyed
        ha "How the hell did you miss this?!"
        show hali rbf

        show vyn silly
        v "I was just chilling man."

        show hali annoyed
        ha "I swear..."
        show hali rbf

    if deathClue == False:
        show rai thinking
        r "What about how Shugo died?"
        r "He didn't just like drop dead right?"
        show rai neutral

        show hacku thinking
        hk "No, of course."
        hk "When I looked at the body, he look really beaten up."
        hk "But not enough to be killed."
        show hacku neutral
        
        show rai thinking
        r "Then what killed him?"
        show rai neutral

        show hacku thinking
        hk "He had a really big gash on his neck."
        hk "There was some cloth on his neck but it looked like enough blood so that he would bleed out."
        show hacku neutral

        show rai erm
        r "Jeez..."
        
    show rai thinking
    r "Ok, if you found all this then how did Shugo get killed?"
    show rai neutral

    show hacku thinking
    hk "I'm still not sure."
    hk "But I have enough evidence to make a conclusion."
    show hacku neutral

    show hali shocked
    ha "Shit really?"
    show hali huh

    show hacku happy
    hk "Yep."
    hk "It's [readerName]."
    show hacku smile

    show rai scared
    show lucy scared
    show hali scared
    "?!"

    reader "Huh?!"

    show lucy thinking
    l "Wait, why [readerName]?"
    show lucy neutral

    show hacku happy
    hk "Hmm, well."
    hk "You didn't really find that much evidence correct?"
    show hacku smile

    reader "Well-"

    show rai annoyed
    r "Dude, even Vyn found something."
    show rai rbf

    show hali neutral
    ha "Rai does have a point."
    show hali annoyed
    ha "Honestly, you're pretty calm for someone who could be killed by the murderer."
    ha "Unless you were the murderer then of course you would be safe."
    show hali neutral

    show hacku thinking
    hk "You weren't really interested in looking for evidence to find anything about the murder."
    show hacku smile

    reader "I really couldn't find anything!"

    show vyn thinking
    v "Uh..."
    v "I mean, are you sure you did?"
    v "You need to see with your eyes."
    show vyn neutral

    show hali enraged
    ha "Can you shut up for a minute?!"
    show hali pissed

    show rai annoyed 
    r "Well? [readerName]?"
    show rai rbf

    reader "..."

    show hacku thinking
    hk "Well, based on that answer-"
    show hacku neutral

    reader "I didn't say anything."

    show hacku happy
    hk "Silence is also an answer for these types of situations."
    hk "If you can't give us a clear answer that you aren't then well.."
    show hacku smile

    reader "..."

    show hali annoyed
    ha "Hah! Well it's settled."
    ha "You disgust me [readerName]."
    show hali rbf

    show lucy sad
    l "It's not true.. right.. [readerName]?"
    l "We're friends though.. right?"
    show lucy frown
    
    show rai annoyed
    r "Ugh, use your brain Lucy. [readerName] is not your friend."
    r "Stay back."
    show rai rbf

    "You instinctively take a step back as Rai moves towards you."

    show rai enraged
    r "Where the hell do you think you're going, murderer!"

    play sound "running.mp3" volume 1.0
    scene black with fade
    play sound "punch.mp3" volume 1.0
    play music "ringing.mp3" loop

    "Ah crap...."

    v "Damn! You pack a punch!"

    ha "How barbaric."

    r "Hey! I knocked the murderer. So I just saved your sorry asses."

    hk "Ahaha! Thank you Rai."
    hk "Now, let's...."

    "..."

    "Well.."
    "That wasn't suposes to happen."
    "{b}Bad Ending 1{/b}."
    #scene cg bad ending 1
    return


label bad_ending_2:

    reader "So, uh, I was thinking-"

    show rai annoyed
    r "Ok, but how can we take your word for it huh?"
    r "I don't trust you at all!"
    show rai rbf

    show hali annoyed
    ha "True, honestly you're the most suspicious out of all of us, [readerName]."
    show hali rbf

    reader "Oh.."

    show lucy thinking
    l "Awh, guys don't say that!"
    show lucy scared

    show rai enraged
    r "Oh my god, can you shut up?"
    r "You can't just be trusting random people!"
    r "Especially in situations where your life is involved."
    show rai pissed

    show lucy sad
    l "But-"
    show lucy frown

    show hacku thinking
    hk "I'm afraid to say that Rai has a point."
    show hacku neutral

    reader "But, I found a lot of evidence!"
    reader "Why would I try to solve a murder that I caused?"

    show rai thinking
    r "And? You could have tried to tamper with the evidence!"
    show rai neutral

    reader "But-"

    show rai enraged
    r "Nah, I don't want to hear it!"
    show rai pissed

    show hali annoyed
    ha "You are the most suspicious."
    show hali rbf

    reader "And Hacku isn't?"

    show vyn happy
    v "Ay, Hacku is cool!"
    v "I think at least."
    show vyn smile

    show hali thinking
    ha "Better than [readerName]."
    ha "To be honest, I do trust Hacku more."
    show hali neutral

    show hacku happy
    hk "Oh, thank you Hali!"
    show hacku smile

    show hali happy
    ha "Of course!"
    show hali smile

    reader "..."

    show rai annoyed
    r "Do you have anything to say for yourself, [readerName]?"
    show rai rbf

    reader "Well.. there's evidence that it could be Hacku too."

    show lucy sad
    l "But... Hacku is really nice..."
    l "They listened to me when I was talking about flowers!"
    show lucy frown

    "When was that?!"

    show rai thinking
    r "Getting the trust of Lucy isn't that much."
    r "Getting Hali's trust though, is probably hard."
    show rai neutral

    show hali annoyed
    ha "What the hell do you mean by that?"
    show hali rbf

    show rai thinking
    r "That you have trust issues."
    r "Duh."
    show rai neutral

    show hali enraged
    ha "This fucking- ugh."
    show hali pissed

    show vyn happy
    v "Nah! I see what you mean Rairai."
    show vyn smile

    show rai annoyed
    r "Don't call me that."
    r "Also we're getting off topic!"
    show rai enraged
    r "[readerName], honestly none of us trust you enough to trust your judgement."
    show rai pissed

    reader "Eh? But-"

    show lucy thinking
    l "But what if it isn't [readerName]?"
    show lucy neutral

    show rai enraged
    r "I don't care, I'm going to knock em' out before they can kill another person!"
    show rai pissed

    "You instinctively take a step back as Rai moves towards you."

    show rai enraged
    r "Where the hell do you think you're going, murderer!"
    show rai pissed

    play sound "running.mp3" volume 1.0
    scene black with fade
    play sound "punch.mp3" volume 1.0
    play music "ringing.mp3" loop

    "Ah crap...."

    v "Damn! You pack a punch!"

    ha "How barbaric."

    r "Hey! I knocked the murderer. So I just saved your sorry asses."

    hk "Ahaha! Thank you Rai."
    hk "Now, let's...."

    "..."

    "Well.."
    "That wasn't suposes to happen."
    "{b}Bad Ending 2{/b}."
    #scene cg bad ending 2
    return

label murderer:
    show rai erm
    r "Wait, doesn't that only point to one person?"

    show lucy thinking
    l "Who?"
    show lucy neutral

    show rai annoyed
    r "Are you fucking dumb? It's Hacku!"
    show rai rbf

    show hacku thinking
    hk "What makes you think that?"
    show hacku neutral

    show rai annoyed
    r "You're the only one who could have had access to all of the things that happened!"
    r "Since you were in the main room."
    show rai rbf

    show hacku thinking
    hk "I thought we established that it didn't matter where we woke up?"
    show hacku neutral

    show rai annoyed
    r "It doesn't make it any better though."
    show rai rbf

    show hali annoyed
    ha "True, you're the only one other than Lucy that didn't wake up in a room."
    show hali rbf

    reader "Hey, let's not jump to conclusions."

    show rai annoyed
    r "Dude, you're way too nice."
    show rai rbf

    show lucy happy
    l "I think that's cool though!"
    show lucy smile

    show rai annoyed
    r "Ok, no one asked for your opinion."
    show rai rbf

    show hali annoyed
    ha "Hey! Don't be mean to her! She's just a child."
    show hali rbf

    show lucy annoyed
    l "I'm seventeen!"
    show lucy neutral

    show rai thinking
    r "Ok enough of that."
    show rai neutral

    reader "We're getting off topic guys.."

    show hali shocked
    ha "Ah shit!"
    show hali thinking
    ha "My bad"
    show hali neutral

    show vyn thinking
    v "Ok, so we think it's Hacku."
    show vyn neutral

    #show hacku annoyed
    hk "Ok, wait. Let's not-"
    #show hacku neutral

    show rai enraged
    r "Nah, I don't need to hear out a murderer."
    r "Unless anyone else has anything to say, I say we just tie this bitch up."
    show rai pissed

    reader "{i}Wait.. I have another piece of evidence I never told anyone.{i}"
    reader "{i}But if I bring it up now, it might sway the vote to something I won't like.{i}"

    if glassClue:
        menu:
            "Bring up the glass shard?"

            "Yes":
                jump bad_ending_3
        
            "No":
                jump good_ending

    else:
        jump true_ending


label bad_ending_3:
    #turn yourself over
    reader "Wait, I think that I have another piece of evidence."

    show rai erm
    r "Eh? Are you trying to save Hacku's ass right now or what."

    reader "Well, I just want to make sure that we're one hunderd percent on this."

    show hali enraged
    ha "Ok well, spit it out!"
    show hali pissed

    play sound "glass shard.mp3"
    "You pull out the glass shard you found when you first woke up."

    reader "I found this when I first woke up. It has no blood on it but someone might have washed it off."

    show hali shocked
    show lucy scared
    show vyn neutral
    show rai scared
    #show hacku shocked
    "..."

    r "What."

    ha "Wait..."

    reader "Wait, please it isn't me though."

    show rai enraged
    r "Bruh, you literally just outed yourself!"
    r "I can't believe I trusted you."
    show rai pissed

    show hali enraged
    ha "Yea! What the hell is wrong with you!"
    show hali pissed
    
    show rai annoyed
    r "Ah fuck, it isn't Hacku then?"
    r "Ugh, this is so annoyed."
    show rai rbf

    show lucy thinking
    l "Wait! What if they didn't mean to."
    show lucy scared

    show rai enraged
    r "SHUT UP ALREADY! Stop trying to defend them!"
    show rai pissed

    show hali annoyed
    ha "Stop yelling at her! She isn't the murderer, it's [readerName]!"
    show hali rbf

    show rai enraged
    r "Oh don't you start now!"
    show rai pissed

    #show hacku annoyed
    hk "Calm down! All this yelling isn't going to get us anywhere."
    #show hacku neutral

    show rai enraged
    r "Oh my god! Are you defending [readerName] too?"
    r "Are you two in kahoots or something?"
    show rai pissed

    #show hacku annoyed
    hk "What? No!"
    hk "I need you to calm down!"
    #show hacku neutral

    r "..."
    show rai annoyed
    r "Fine."
    show rai rbf

    show hacku thinking
    hk "[readerName]."
    show hacku neutral

    reader "Yea..?"

    show hacku thinking
    hk "Ok, where did you find this glass shard?"
    show hacku neutral

    reader "The first room where I woke up."

    #show hacku shocked
    hk "..."
    hk "Then.."
    hk "The only person it could have been is you."
    #show hacku netural

    reader "What? That's not-"

    show vyn thinking
    v "Not gonna lie dude, you kinda cooked yourself."
    show vyn neutral

    show hali annoyed
    ha "For once I agree with the himbo."
    show hali rbf

    show vyn thinking
    v "Himbo? What's that?"
    show vyn neutral

    show hali disgusted
    ha "Point proven."

    show rai enraged
    r "I don't care, I'm going to knock em' out before they can kill another person!"
    show rai pissed

    "You instinctively take a step back as Rai moves towards you."

    show rai enraged
    r "Where the hell do you think you're going, murderer!"

    play sound "running.mp3" volume 1.0
    scene black
    play sound "punch.mp3" volume 1.0
    play music "ringing.mp3" loop

    v "Damn! Bro packs a punch!"

    ha "Ugh, how barbaric."

    r "Bruh, I just saved your asses."
    r "[readerName] was literally holding the murder weapon."

    hk "True."
    hk "Alright now..."

    reader "..."
    "...
    "
    "{cps=5}Wait..{/cps}"
    "{cps=5}But it really isn't me..{/cps}"

    "{b}Bad Ending 3{/b}."
    return

label good_ending:

    "You keep quiet about the glass shard."

    show rai annoyed
    r "Well, looks like there is only one option here."
    show rai rbf

    hk "..."

    show hali annoyed
    ha "Got anything to say, murderer?"
    show hali rbf

    "Hacku stood there for a minute."
    "They started to pull something out of their pocket."

    show hacku thinking
    hk "If you allow me-"

    #show hacku shocked
    show rai enraged
    r "Nope, I'm not doing this."

    show rai pissed at eightseven
    with move 

    play sound "running.mp3"
    play sound "punch.mp3"
    hide hacku thinking with dissolve

    show hali shocked
    ha "Jeez! You didn't even let them finish their sentence!"
    show hali annoyed
    ha "How barbaric."
    show hali rbf

    show rai annoyed
    r "They were probably pulling out a knife so you're welcome."
    show rai rbf

    show vyn thinking
    v "So... what now?"
    show vyn neutral

    reader "Should we look for a way out now?"
    reader "Now that we found the murderer."

    show rai thinking
    r "Right."
    r "Ugh... If only there was like an emergency phone or something."
    show rai neutral

    show lucy thinking
    l "Oh, there is an emergency phone!"
    show lucy neutral

    show rai scared
    show hali shocked

    r "..."

    ha "..."

    reader "..."

    show rai pissed
    show hali enraged
    ha "RAI, stay where you are!"

    show rai enraged
    r "UGH! I'm so fucking done with kids."
    show rai pissed

    show vyn silly
    v "Awh, don't be like that gramps."

    show rai enraged
    r "I am not old! How old are you?! You're probably also a fetus!"
    show rai pissed

    show vyn happy
    v "I'm as young as the sun!"
    show vyn smile

    show hali disgusted
    ha "I'm so done with men."
    show hali happy
    ha "Hey, Lucy?"
    show hali smile

    show lucy thinking
    l "Mhm..?"
    show lucy neutral

    show hali happy
    ha "Can you show me where the emergency phone is?"
    show hali smile

    show lucy happy
    l "Yea!"
    show lucy smile

    #bg main halu
    hide hali
    hide lucy
    with dissolve
    "Lucy started to lead Hali to the fireplace."
    "She pushed one of the rocks and it clicked open, revealing an old wired phone."

    show vyn happy
    v "Damn! That thing is ancient!"
    show vyn silly
    v "Almost as much as unc' over here."

    show rai annoyed
    r "I will actualy knock you out."
    show rai rbf

    show vyn dramatic
    v "So forward!"

    ha "Just leave it Rai. If you try to argue with an idiot."
    ha "He'll just drag you down to his level and beat you with experience."

    show vyn thinking
    v "Hey! I got into grad school, so I'm at least smart in that department."
    show vyn neutral

    ha "Yea, ok. I do not give two shits."

    "Hali punched in 911 in the wired phone."

    ha "Hello?"
    ha "Yes."
    ha "Ah! Location?"
    ha "Lucy, can you tell me the address?"

    l "Yea! It's..."

    "Five minutes later, you could hear police sirens coming from outside of the house."
    scene black with fade #outside
    
    show vyn neutral at one
    show rai neutral at two
    show hali neutral at fourthree
    show lucy neutral at six
    with dissolve

    "\Police" "From what I've heard from the young lady, you were trapped in this house with a murderer, correct?"

    show vyn silly
    v "Yessir!"

    "/Police" "It must have been hard to get through this. Don't worry, we will take it from here."
    "/Police" "Although, you will need to go through some screening before we can let you go."
    "/Police" "We hope that you understand since this is a serious case."

    reader "Oh, have there been recent cases like this before?"

    "\Police" "Yes. But we may have caught the murderer now, thanks to you five!"
    "\Police" "The questioning will not take that long, so please do not be worried."

    show vyn hand
    v "Lit bro!"

    "The police man looked at Vyn confused."

    show hali happy
    ha "BWHAHAHAHA!"
    show hali smile
    
    show rai thinking
    r "Deserved."
    show rai neutral

    show lucy wave
    l "Awh! I'll high-five you Vyn!"

    show vyn dramatic
    v "Sniffles. Thank you Luc."

    "Police's assistant" "Excuse me! Is it [readerName]?"

    reader "Oh, yes? That's me."

    "The assistant came outside of the door that they sawed down with an unconscious Hacku."

    "Police's assistant" "This is the person you said that was the murderer?"

    show rai thinking
    r "Yep."
    show rai neutral

    show vyn silly
    v "This guy knocked them out with his big boy strength!"

    show rai enraged
    r "I will-"
    show rai pissed
    "Rai took a very deep breathe."
    show rai thinking
    r "They were going to pull something out of thier pocket so I knocked them out in self defence."
    show neutral

    "Police's assistant" "I see. I am glad that you are all safe!"

    "The police's assistant struggled to drag Hacku down the stairs, almost falling down."

    show hali shocked
    ha "Oh no! Wait, please let me help you."
    hide hali shocked with dissolve

    "Hali ran over to help the assistant."

    scene black with fade
    #scene cg outside
    "The other's voices faded as you fixated your gaze on Hacku."
    "You watched as they put handcuffs on them and lifted them into the police car."

    #show cg outside smile
    "You smile."
    "That was easier than it should have been."
    "You fiddle with the glass shard in your pocket."
    "..."
    "Good job."

    #scene good ending
    "{b}Good Ending?{/b}."
    return


label true_ending:

    show hacku thinking
    hk "Wait. I have another thing to mention."
    show hacku neutral

    show rai annoyed
    r "Ok? Spit it out then."
    show rai rbf

    show hacku thinking
    hk "[readerName]."
    show hacku neutral

    reader "?"
    reader "Yea?"

    show hacku thinking
    hk "You came from the room at the end of the long hallway, correct?"
    show hacku neutral

    reader "Um.. yea."

    show hacku thinking
    hk "Why did you lie when you said that the door closed?"
    show hacku neutral

    reader "!?"
    reader "Wait, what do you mean?"

    show hacku thinking
    hk "Before this, I went to investigate the hallways. Where you guys came from."
    hk "The doors to those rooms you were in were open."
    show neutral

    show hali shocked
    ha "Wait, but when we left the doors were shut!"
    show hali huh

    show rai thinking
    r "Yea, I even tried to open it again."
    show rai neutral

    show hacku happy
    hk "Well, to be honest I kind of broke the handles of the door with a screwdriver."
    "Hacku reached into their pocket and show everyone a screwdriver."
    hk "It's not like this is an escape room where you can't break anything."
    show hacku smile

    show vyn silly
    v "That's so metel."
    show vyn thinking
    v "Where'd you get it though?"
    show vyn neutral

    show hacku thinking
    hk "Oh, I usually keep a toolkit in my pocket."
    show hacku neutral

    show rai annoyed
    r "Then, couldn't you have killed Shugo too?"
    show rai rbf

    show hacku thinking
    hk "Hmm.. I supposed."
    hk "But, this only has a screwdriver function, something for my ID and a very dull small army knife."
    show hacku neutral

    show lucy excited
    l "Oooh! That's so cool1"
    show lucy smile

    show hacku thinking
    hk "It's something that everyone should have, in my opinion."
    hk "Especially the ID part."
    show hacku neutral

    show hali annoyed
    ha "Where are you getting at?"
    show hali rbf

    show hacku thinking
    hk "I found something interesting in the room that [readerName] came from."
    show hacku neutral

    "Hacku pulls something from out of thier pocket."

    show cg glass with dissolve
    play sound "glass shard.mp3"

    show rai thinking
    r "Is that a glass shard?"
    show rai neutral

    show hacku thinking
    hk "Yea."
    show hacku neutral

    "..."

    show vyn thinking
    v "Wait, I'm not following."
    show vyn neutral

    show rai scared
    r "!!"
    show rai erm
    r "A dull army knife can't make a cut that big but.."

    show hacku thinking
    hk "A sharp piece of glass can."
    show hacku neutral
    
    show vyn thinking
    v "Ohhh!"
    v "Then where's like, the blood."
    show vyn neutral

    show hacku thinking
    hk "Without special equiment, you probably wouldn't be able to see it if it were just simplely washed."
    hk "The only place where you could have found the murder weapon is the room where [readerName] came from."
    show hacku neutral

    reader "{i}!!{i}"

    show hacku happy
    hk "Haha! What's with that expression [readerName]?"
    show hacku smile

    reader "What are you saying, Hacku?"

    show hacku thinking
    hk "It's you [readerName]."
    show hali shocked
    show lucy scared
    show vyn neutral
    show rai shocked
    hk "You killed Shugo."
    show hacku neutral

    reader "What? Are you crazy?"
    reader "What's your reasoning?"

    show hali annoyed
    ha "Yea, aren't you just trying to shift the blame to [readerName]?"
    show hali rbf

    show hacku thinking
    hk "Well, I could be. I could be lying about all of this."
    hk "We are both equally suspicious."
    show hacku happy
    hk "However, you can't exactly rule out [readerName] either."
    hk "What do you have to say to this then, [readerName]?"
    
    scene black with fade
    #scene cg reader with fade
    reader "Hah."
    reader "Ahahah."
    reader "HAHAHAHAHA!"

    l "Huh..?"

    r "What the fuck? [readerName]?"

    reader "Well, nothing of it really."
    reader "I knew we had a tail on us, I just didn't expect for them to send a little birdie into the lion's den."

    hk "..."
    hk "Did you really lose your memory, [readerName]?"

    reader "And why would I tell you that?"
    reader "You're the detective, figure it out yourself."

    v "Wait, what?"
    v "Did I miss something? Since when was Hacku a detective."

    r "Hey, Hacku! What the hell is going on?"

    hk "..."
    hk "I wasn't lying when I said that I worked with corpses."
    hk "Just the name of my job."

    v "Oh shit!"
    v "You're like an underground hero!"

    reader "Hahahah!"
    reader "You're hilarious Vyn, I hope you know that."

    v "Eyy, thanks buddy!"

    ha "HUH?"
    ha "A murderer just complimented you and YOU'RE HAPPY?"

    v "Ok, damn."
    v "Also since when was [readerName] the murderer?"
    
    ha "Maybe if you paid attention you would know."

    l "Wait so.. [readerName]."
    l "You know Shugo..?"
    l "And.. killed him?"

    #show cg reader closer
    reader "Hmm.."
    reader "Maybe Hacku could answer you, little Lucy."

    hk "{i}!!{i}"
    hk "{i}What are they planning?{i}"
    hk "{i}I caught them already but it's as if there is still more to understand.{i}"
    hk "[readerName] is the only one who could have killed Shugo."

    l "But, why?!"
    l "Friends shouldn't kill friends!"

    reader "Well, he had it coming. Just another loose end that I had to tie up."

    ha "Hacku! Were you investigating [readerName]?"

    reader "Oh yea! Let's introduce each other again."
    reader "I insist you go first, Hacku."

    hk "{i}This guy is so annoyed.{i}"
    hk "Ugh.."
    hk "My name is Hacku. I'm a detective in training who used to work as a crime scene cleaner."
    hk "I was tasked with following a series of murders that led me to a cabin in the woods."

    reader "There you go."

    v "Goddamn! I'm just a dude."

    r "Guys, we can't let them free right now."

    reader "Oh, I'm well aware that I've lost. I also don't harm anyone I don't have to."

    hk "Yet, you killed your partner."

    reader "Another loose tie."

    hk "{i}Ugh, they make me sick.{i}"

    ha "What the hell is wrong with you?"
    ha "Were you actually just lying this entire time?"

    reader "Haha."
    reader "Go on, Hacku."

    hk "..."
    hk "The person in front of us right now is the murderer of the last seven cases we had."
    hk "They were calculating and cunning so they asked rookies to help the higher-ups."
    
    r "How did we get into this then?"

    reader "Ugh, don't even get me started with that."
    reader "I'm still surpised that they allowed rookies to take on such a case!"

    hacku "[readerName], if we can even call you that, what do you want?"

    reader ""




    
    #reader arrested
    reader "Hah, I'm glad to have had so much fun with you Hacku."
    reader "Sad to say though, you won't see the last of me."

    hk "!!!"
    hk "{i}No, this is too easy.{i}"

    "You turn back to the cabin and start sprinting."

    hk "{i}I must have missed something!{i}"

    v "Eh? Wait, where's bro going?"

    ha "Hacku! Ugh, why do people just start running out of no where?!"

    scene bg main with fade
    hk "CRAP! Ugh, they got me good."

    show rai neutral at five
    with moveinright
    r "Jesus fuck, why the hell do you run so fast?"
    r "Also, I don't know if you saw, but there are bunch of knocked out people in the kit-"
    show rai scared
    r "What the fuck?!"

    show hali thinking at sizeseven
    with moveinright
    ha "Ugh, I hate running."
    show hali shocked
    ha "Holy shit! Where is the body?"
    show hali huh

    hk "Ugh, there's probably a lot more to this case than we've witnessed."
    hk "I'm sorry that you guys got roped into all of this."

    show vyn silly
    v "No sweat bro! It was kinda fun."

    show hali annoyed
    ha "If fun you mean I lost 10 years off my life, then yes."
    show hali rbf

    hk "Hahahah!"
    hk "Ahem, well if you guys don't mind, you'll have to go through some questioning before you go back home."
    hk "Oh and here's my card if anything comes up."

    show vyn dramatic
    v "So forward!"

    show hali thinking
    ha "Bruh."
    show hali neutral

    show rai thinking
    r "How long have you been bitchless, Vyn."
    show rai neutral

    show vyn thinking
    v "AY! Uncalled for man."
    show vyn neutral

    show hali happy
    ha "HAHAHAHAH! Nice one Rai."
    show hali smile

    hk "Hahaha! Let's go back outside then. I'll have to ask for extra back up because of this."

    scene black with fade


    "Hacku's colleague" "Hak! Why'd you go back in there?"

    hk "The inpectors were knocked out and the body is gone."

    "Hacku's colleague" "Huh?!"

    hk "Yea."

    "Hacku's colleague" "Jeez, why do you always get the cool cases."

    hk "Hah! I wouldn't really call them cool. They're just more complex."

    "Hacku's colleague" "Same thing."
    "Hacku's colleague" "Anyways, Hali, Vyn and Rai, if you would follow me please."

    show vyn thinking
    v "Wait! Hacku, what's going to happen to Lucy?"
    show vyn neutral

    hk "She has to go through extra screening because of the bigger role she had to play in this."
    hk "But, because she is still a minor, she won't be punished too badly."
    hk "In a way, she's a victim for being manipulated by [readerName] and Shugo."

    show rai annoyed
    r "Ugh, deserved."
    show rai rbf

    show hali annoyed
    ha "Hey! She's just a kid."
    show hali rbf

    show rai annoyed
    r "Ok well I was never great with kids."
    show rai thinking
    r "Hey! Mister investigator, do you mind if I quickly call my girl so she isn't worried."
    show rai neutral at offleft
    with move

    "Rai runs after your colleague."
    hide rai neutral

    show hali happy
    ha "Well, I'll see you around Hacku!"
    ha "Don't be a stranger!"
    show hali smile

    show vyn happy
    v "Yea! You're cool. Let's hang out sometime!"
    show vyn smile

    show hali rbf
    "Hali rolls her eyes."

    show hali annoyed
    ha "We can hang out and not invite this dude."
    show hali rbf

    show vyn dramatic
    v "Hey! My feelings ARGH. They're wounded I say, WOUNDED!!"

    show hali enraged
    ha "ARGH, MISTER INVESTIGATOR PLEASE PUT ME IN A DIFFERENT ROOM THAN THIS BITCH!"
    show hali pissed at offleft
    show vyn silly at offleft
    with move

    "Hali runs off following Rai while Vyn follows her."
    hide hali pissed
    "You sigh."

    hk "{i}It seems over now but...{i}"
    hk "{i}There has to be a deeper meaning.{i}"
    hk "{i}I'll just have to keep working.{i}"

    scene black with fade
    "..."
    "{b}True Ending {/b}."

    menu:
        "Would you like to see the end credits?"

        "Yes":
            jump endCredits

        "No":
            return


label endCredits:
    #scene my room
    #show happy me
    "Thank you for playing my game!"

    #show me talk ig
    "This is the first time I ever made my own game."
    "I'd like to thank my friends for testing my game."
    "Y'all are the best."
    #show bow me
    return

label faint:
    reader "I feel so dizzy right now.."

    "My body swayed as a I heard something fall onto the ground."
    "If it wasn't clear enough, I was the thing that fell onto the ground."
    #play sound body falling

    reader "Shit.. my head hurts so bad.."
    scene black with eyesclose

    "Well.."
    "That wasn't suposes to happen."
    "{b}Bad Ending 0{/b}."
    #achievement : Help! I've fallen and I can't get up!
    #bonus cg of you dead if i have time
    return