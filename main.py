from random import shuffle

# printing the welcome message
print("\n" + "---------------------------------------------------" + "\n" +
      "Welcome! this is a script to practice phrasal verbs." + "\n" + "\n" +
      "You will be shown sentences with blank spaces inside," + "\n" +
      "try to fill them with the correct phrasal verb." "\n" + "\n" +
      "You can ask for a hint in any moment typing 'hint'" + "\n" +
      "instead of the requested solution, and you can see your" + "\n" +
      "current mark by typing 'mark'." + "\n" + "\n"
      "Let's start! Good luck! :)" + "\n"
      "---------------------------------------------------" + "\n" + "\n")

# declaring variables
marks = 0
total = 0
final_mark = 0
used_hints = 0

shuffled_list = [x for x in range(0, 31)]
shuffle(shuffled_list)


sentences = {0: "Brian finally was brave enough to _ Judy _ ",
            1: "The car was about to run over me when she shouted: _ _!",
            2: "We have _ _ of clinex again... I'll buy more tomorrow.",
            3: "You are too special, I can't __  on us.",
            4: "I'm in a hurry! I have to __  these exercises to my teacher by tomorrow morning!",
            5: "Only thing I disliked about the hotel was that we had to __ _ before 12am...",
            6: "My grandma always tells the same story where a bottle of gas __  in her face.",
            7: "I've been ____ __ about the topic, but nobody knows shit.",
            8: "My expenses in burgers this month _   $350... omg...",
            9: "Don't worry Gorra, we will __ you  on this! -told we before leaving him alone again-.",
            10: "I just ___ __ when I got the bad news: Gorra had died in horrible suffering.",
            11: "It was a well secured building, but we managed to ___ __ the room and steal the money.",
            12: "I'm so sad my grandpa ____ __ so soon.",
            13: "This new push-up jeans hurt me! I have to ___ them __",
            14: "I'm young, but not stupid. You have to stop _____ __ on me.",
            15: "He is secluded at home today. His parents forced him to __ _ his little sister.",
            16: "We were angry again this morning, but we __  fast because we had things to do.",
            17: "Yesterday I _ __ an old school-friend. It was scary, I think he's a drug dealer now.",
            18: "Hey, I'm sure you'll like arepas. C'mon, let's _ them _.",
            19: "I hate this kind of formal events. I really don't want to _  for them, I hate suits!",
            20: "It was sad they had to ___  because of the distance. They were a great couple.",
            21: "I will never fail you, you always can ___  me.",
            22: "You are still mad. You have to __ __ to drive the car, please.",
            23: "__  there, soon everything will be OK!",
            24: "Oh shit, I forgot my phone at the pub, __  here for a second, will be right back!",
            25: "If you __ this marks , you will pass the english exam easily.",
            26: "I'm sorry to ___ , but I have some information about Gorra that might help.",
            27: "Please, don't _ me __. I'm fed up of being sad.",
            28: "He only bought that fucking car to __ _ and prove he is richer than me.",
            29: "Don't worry, she always __ _ when she smokes these Holland joints.",
            30: "Everyone loves and _ _ with Gorra, but at the same time, everyone do bad to him..."}

solutions = {0: "ask out",
             1: "watch out",
             2: "run out",
             3: "give up",
             4: "hand in",
             5: "check out",
             6: "blew up",
             7: "asking around",
             8: "add up to",
             9: "back up",
             10: "broke down",
             11: "break into",
             12: "passed away",
             13: "break down",
             14: "look down",
             15: "look after",
             16: "made up",
             17: "ran into",
             18: "try out",
             19: "dress up",
             20: "break up",
             21: "count on",
             22: "calm down",
             23: "hang in",
             24: "hang on",
             25: "keep up",
             26: "break in",
             27: "let down",
             28: "show off",
             29: "pass out",
             30: "get along"}

hints = {0: "as_ _",
         1: "ten cuidado!",
         2: "r _",
         3: "g_ ",
         4: "h_ ",
         5: "esta te la sabes tia",
         6: "Explotar. b_ . Ojo al tiempo verbal.",
         7: "He estado informandome. I've been as__ aro___",
         8: "add  ",
         9: "Apoyar, estar ahi. Es igual que 'copia de seguridad'.",
         10: "Cuando no puedes mas, cuando te ROMPES",
         11: "Colarse: br___ ",
         12: "Palmarla. En pasado. pa__ __",
         13: "br_ something __, significa adecuar ropa a tu cuerpo... no se como se dice en espanol :P",
         14: "Menospreciar. lo___ __",
         15: "(secluded == recluido)   __ after",
         16: "tambien significa maquillaje",
         17: "Encontrarse a alguien inesperadamente. Tambien puede ser toparse con algo. r__ __",
         18: "Probar. t _",
         19: "Vestirse formal. dr_ ",
         20: "Cortar, romper con alguien. br_ ",
         21: "Contar con!",
         22: "Calmarse, tranquilizarse",
         23: "Uh, este era dificil. Significa mantenerse positivo, aguantar con buena onda. ha_ ",
         24: "h_ on",
         25: "Mantener algo. k___ up",
         26: "br___ ",
         27: "l d___",
         28: "Creo que es la traduccion mas cerca a FLIPARSE. s___ f",
         29: "ahhhh que recuerdos... p_ _",
         30: "Llevarse bien. g _"}


for x in range(0, len(shuffled_list)):

    print(sentences[shuffled_list[x]])

    sol = input()

    if sol == "hint":
        print(hints[shuffled_list[x]])
        used_hints += 1
        sol = input()

    if sol == solutions[shuffled_list[x]]:
        print("correct!")
        marks += 1
        total += 1

    else:
        print("wrong, the correct answer is: ", solutions[shuffled_list[x]])
        total += 1

