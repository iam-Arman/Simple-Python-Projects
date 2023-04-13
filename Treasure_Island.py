#Treasure Island 
print('''                                o
                            .-'"|
                            |-'"|
                                |   _.-'`.
                               _|-"'_.-'|.`.
                              |:^.-'_.-'`.;.`.
                              | `.'.   ,-'_.-'|
                              |   + '-'.-'   J
           __.            .d88|    `.-'      |
      _.--'_..`.    .d88888888|     |       J'b.
   +:" ,--'_.|`.`.d88888888888|-.   |    _-.|888b.
   | \ \-'_.--'_.-+888888888+'  _>F F +:'   `88888bo.
    L \ +'_.--'   |88888+"'  _.' J J J  `.    +8888888b.
    |  `+'        |8+"'  _.-'    | | |    +    `+8888888._-'.
  .d8L  L         J  _.-'        | | |     `.    `+888+^'.-|.`.
 d888|  |         J-'            F F F       `.  _.-"_.-'_.+.`.`.
d88888L  L     _.  L            J J J          `|. +'_.-'    `_+ `;
888888J  |  +-'  \ L         _.-+.|.+.          F `.`.     .-'_.-"J
8888888|  L L\    \|     _.-'     '   `.       J    `.`.,-'.-"    |
8888888PL | | \    `._.-'               `.     |      `..-"      J.b
8888888 |  L L `.    \     _.-+.          `.   L+`.     |        F88b
8888888  L | |   \   _..--'_.-|.`.          >-'    `., J        |8888b
8888888  |  L L   +:" _.--'_.-'.`.`.    _.-'     .-' | |       JY88888b
8888888   L | |   J \ \_.-'     `.`.`.-'     _.-'   J J        F Y88888b
Y888888    \ L L   L \ `.      _.-'_.-+  _.-'       | |       |   Y88888b
`888888b    \| |   |  `. \ _.-'_.-'   |-'          J J       J     Y88888b
 Y888888     +'\   J    \ '_.-'       F    ,-T"\   | |    .-'      )888888
  Y88888b.      \   L    +'          J    /  | J  J J  .-'        .d888888
   Y888888b      \  |    |           |    F  '.|.-'+|-'         .d88888888
    Y888888b      \ J    |           F   J    -.              .od88888888P
     Y888888b      \ L   |          J    | .' ` \d8888888888888888888888P
      Y888888b      \|   |          |  .-'`.  `\ `.88888888888888888888P
       Y888888b.     J   |          F-'     \\ ` \ \88888888888888888P'
        Y8888888b     L  |         J       d8`.`\  \`.8888888888888P'
         Y8888888b    |  |        .+      d8888\  ` .'  `Y888888P'
         `88888888b   J  |     .-'     .od888888\.-'
          Y88888888b   \ |  .-'     d888888888P'
          `888888888b   \|-'       d888888888P
           `Y88888888b            d8888888P'
             Y88888888bo.      .od88888888   hs
             `8888888888888888888888888888
              Y88888888888888888888888888P
               `Y8888888888888888888888P'
                 `Y8888888888888P'
                      `Y88888P'
''')
print("\t\t\t\t\t----------WELCOME TO TREASURE ISLAND-----------")
print("\t\t\t\t\t-------YOUR MISSION IS TO FIND THE TREASURE---------\n\n")

print("You are at a cross road,Where do you want to go left or right ........")
choice=input()
if(choice=="left"):
    print('you came to a lake. there is an island in the middle of the lake . type "wait" to wait for a both type "swim" to swim across......... ')
    choice=input()
    choice=choice.lower()
    if(choice=="wait"):
        print("You arrived at the island unharmed. There is a house with theree doors. One red oen yellow and one blue . Which color do you choose ........")
        choice=input()
        choice=choice.lower()
        if(choice == "blue"):
            print("You entered a room of beasts\n")
            print("................GAME OVER...................\n")
        elif(choice=="yellow"):
            print(">>>>>>>>>>>>>>>>>>YOU WIN<<<<<<<<<<<<<<<<<\n")
        elif(choice=="red") :
            print("..................GAME OVER................\n")
    else :
        print("........................GAME OVER.................... \n")

else :
    print("....................GAME OVER.................... \n")
