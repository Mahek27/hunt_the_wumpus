import random


def print_cave():
    print('''                                       ______18_______
                                      /      |        \\
                                     /      _9__       \ 
                                    /      /    \       \\
                                   /      /      \       \ 
                                  17     8        10     19
                                  | \   / \      /  \   / |
                                  |  \ /   \    /    \ /  |
                                  |   7     1---2     11  |   
                                  |   |    /     \    |   |
                                  |   6----5     3---12   |
                                  |   |     \   /     |   |
                                  |   \       4      /    |
                                  |    \      |     /     |
                                  \     15---14---13     /
                                   \   /            \   /
                                    \ /              \ /
                                    16---------------20''')  # when input is P printing the map of cave


def directions():
    print('''Hunt the Wumpus:
            The Wumpus lives in a completely dark cave of 20 rooms. Each
            room has 3 tunnels leading to other rooms.
            Hazards:
            1. Two rooms have bottomless pits in them.  If you go there you fall and die.
            2. Two other rooms have super-bats.  If you go there, the bats grab you and
               fly you to some random room, which could be troublesome.  Then those bats go
               to a new room different from where they came from and from the other bats.
            3. The Wumpus is not bothered by the pits or bats, as he has sucker feet and
               is too heavy for bats to lift.  Usually he is asleep.  Two things wake
               him up: Anytime you shoot an arrow, or you entering his room.  The Wumpus
               will move into the lowest-numbered adjacent room anytime you shoot an arrow.
               When you move into the Wumpus' room, then he wakes and moves if he is in an
               odd-numbered room, but stays still otherwise.  After that, if he is in your
               room, he snaps your neck and you die!
            Moves:
            On each move you can do the following, where input can be upper or lower-case:
            1. Move into an adjacent room.  To move enter 'M' followed by a space and
               then a room number.
            2. Shoot your guided arrow through a list of up to three adjacent rooms, which
               you specify.  Your arrow ends up in the final room.
               To shoot enter 'S' followed by the number of rooms (1..3), and then the
               list of the desired number (up to 3) of adjacent room numbers, separated
               by spaces. If an arrow can't go a direction because there is no connecting
               tunnel, it ricochets and moves to the lowest-numbered adjacent room and
               continues doing this until it has traveled the designated number of rooms.
               If the arrow hits the Wumpus, you win! If the arrow hits you, you lose. You
               automatically pick up the arrow if you go through a room with the arrow in
               it.
            3. Enter 'R' to reset the person and hazard locations, useful for testing.
            4. Enter 'C' to cheat and display current board positions.
            5. Enter 'D' to display this set of instructions.
            6. Enter 'P' to print the maze room layout.
            7. Enter 'X' to exit the game. ''')  # wen input is D printing directions


cave = {1: [5, 2, 8], 2: [10, 1, 3], 3: [2, 4, 12], 4: [14, 5, 3], 5: [4, 6, 1], 6: [7, 15, 5],
        7: [8, 6, 17], 8: [1, 9, 7], 9: [18, 8, 10], 10: [2, 9, 11], 11: [10, 12, 19], 12: [13, 11, 3],
        13: [12, 14, 20], 14: [4, 13, 15], 15: [14, 16, 6], 16: [17, 15, 20], 17: [7, 16, 18], 18: [17, 19, 9],
        19: [18, 11, 20], 20: [16, 13, 19]}  # cave's dictionary


class game:
    # self, wumpus, pit1, pit2, bat1, bat2, chest1, chest2, chest3, chest4, chest5
    def __init__(self, wumpus, pit1, pit2, bat1, bat2, chest1, chest2, chest3, chest4, chest5):
        self.wumpus = wumpus
        self.pit1 = pit1
        self.pit2 = pit2
        self.bat1 = bat1
        self.bat2 = bat2
        self.player_pos = 13
        self.arrow = -1  # arrow is with player
        self.gold_collected = 0
        self.chest1_location = chest1
        self.chest2_location = chest2
        self.chest3_location = chest3
        self.chest4_location = chest4
        self.chest5_location = chest5
        # wumpus, pit1, pit2, bat1, bat2, chest1, chest2, chest3, chest4, chest5
        self.pos = [wumpus, pit1, pit2, bat1, bat2, chest1, chest2, chest3, chest4, chest5]  # list of locations of hazards and chests
        self.chest1_value = 40
        self.chest2_value = 40
        self.chest3_value = 40
        self.chest4_value = 40
        self.chest5_value = 40

    def randomize_initially(self):
        self.pos = []
        self.wumpus = random.randint(1, 20)  # randomising location of wumpus(0)
        while self.wumpus == 13 or self.wumpus in self.pos:  # position should != to player pos or hazards pos
            self.wumpus = random.randint(1, 20)  # keep randomising till any other number comes
        self.pos.append(self.wumpus)  # adding to list of location of hazards

        # randomize pit1(1)
        self.pit1 = random.randint(1, 20)
        while self.pit1 == 13 or self.pit1 in self.pos:
            self.pit1 = random.randint(1, 20)
        self.pos.append(self.pit1)

        # randomize pit2(2)
        self.pit2 = random.randint(1, 20)
        while self.pit2 == 13 or self.pit2 in self.pos:
            self.pit2 = random.randint(1, 20)
        self.pos.append(self.pit2)

        # randomize bat1(3)
        self.bat1 = random.randint(1, 20)
        while self.bat1 == 13 or self.bat1 in self.pos:
            self.bat1 = random.randint(1, 20)
        self.pos.append(self.bat1)

        # randomize bat2(4)
        self.bat2 = random.randint(1, 20)
        while self.bat2 == 13 or self.bat2 in self.pos:
            self.bat2 = random.randint(1, 20)
        self.pos.append(self.bat2)

        # randomize chest1
        self.chest1_location = random.randint(1,20)
        while self.chest1_location == 13 or self.chest1_location in self.pos:
            self.chest1_location = random.randint(1,20)
        self.pos.append(self.chest1_location)

        # randomize chest2
        self.chest2_location = random.randint(1, 20)
        while self.chest2_location == 13 or self.chest2_location in self.pos:
            self.chest2_location = random.randint(1, 20)
        self.pos.append(self.chest2_location)

        # randomize chest3
        self.chest3_location = random.randint(1, 20)
        while self.chest3_location == 13 or self.chest3_location in self.pos:
            self.chest3_location = random.randint(1, 20)
        self.pos.append(self.chest3_location)

        # randomize chest4
        self.chest4_location = random.randint(1, 20)
        while self.chest4_location == 13 or self.chest4_location in self.pos:
            self.chest4_location = random.randint(1, 20)
        self.pos.append(self.chest4_location)

        # randomize chest5
        self.chest5_location = random.randint(1, 20)
        while self.chest5_location == 13 or self.chest5_location in self.pos:
            self.chest5_location = random.randint(1, 20)
        self.pos.append(self.chest5_location)

    def cheat(self):
        print("Cheating! Game elements are in the following rooms: ")
        print('''Wumpus    Pit1   Pit2    Bat1    Bat2    Chest1    Chest2    Chest3    Chest4    Chest5    Player    Arrow
  {0}       {1}     {2}       {3}       {4}       {5}        {6}        {7}        {8}        {9}        {10}       {11} '''.format(self.pos[0], self.pos[1], self.pos[2],self.pos[3], self.pos[4], self.pos[5], self.pos[6], self.pos[7], self.pos[8], self.pos[9], self.player_pos, self.arrow))

    def reset(self):
        self.player_pos = 13
        self.gold_collected = 0
        self.randomize_initially()
        

    def randomize_bat1(self):  # wen player_pos == self.bat1, use this function
        self.pos[3] = -1
        self.bat1 = random.randint(1, 20)
        while self.bat1 == self.player_pos or self.bat1 in self.pos:  # Make sure bat1 != other hazards
            self.bat1 = random.randint(1, 20)
        self.pos[3] = self.bat1  # pos[3] is position of bat1 in the list pos

    # when player_pos == self.bat2.
    def randomize_bat2(self):
        self.pos[4] = -1
        self.bat2 = random.randint(1, 20)
        while self.bat2 == self.player_pos or self.bat2 in self.pos:  # make sure bat2 != other hazards
            self.bat2 = random.randint(1, 20)
        self.pos[4] = self.bat2  # pos[4] is position of bat2 in the list pos

    # when bats fly the player into new room, the player position is randomised
    def randomize_person(self):
        self.player_pos = random.randint(1, 20)
        while self.player_pos == self.pos[3] or self.player_pos == self.pos[4]:
            # randomised player position can match other hazards but not bat1 or bat2
            self.player_pos = random.randint(1, 20)  # we don't have to add to list since its separately defined

    def randomize_wumpus(self):
        adjacent_rooms = cave.get(self.player_pos, "none")
        list1 = adjacent_rooms
        self.wumpus = random.choice(list1)
        self.pos[0] = self.wumpus

    def play_again(self):
        what = input("Do u want to play again? (Y/N): ")  # wants to play again?
        if what == 'Y' or what == 'y':
            self.reset()  # if yes, resets the game
        elif what == 'N' or what == 'n':
            exit()  # if no, exits the game

    def choice_to_buy_out_wumpus(self):
        what = input("Do you want to pay 80 gold to get out of this room? (Y/N): ")  # wants to play again?
        if what == 'Y' or what =='y':
            if self.gold_collected >= 80:
                self.gold_collected -= 80
                print("You will be transported into a random room")
                self.randomize_person()
            else:
                print("You do not have enough golds to buy the wumpus")
        else:
            return

    def choice_to_buy_out_pit(self):
        what = input("Do you want to pay 40 gold to get out of this room? (Y/N): ")  # wants to play again?
        if what == 'Y' or what =='y':
            if self.gold_collected >= 20:
                self.gold_collected -= 20
                print("You will be transported into a random room")
                self.randomize_person()
            else:
                print("You do not have enough golds to buy the pit")
        else:
            return

    def death_by_pos(self):
        if self.player_pos == self.pos[0]:  # checking if player_pos = wumpus location
            if (self.player_pos % 2) == 0:  # check even or odd
                # checking if player has enough gold to potentially buy their way out
                if self.gold_collected > 79:
                    print("Oh no! You've discovered the wumpus and it has its slimy tentacle arm around you...")
                    self.choice_to_buy_out_wumpus()
                else:
                    print('''You briefly feel a slimy tentacled arm as your neck is snapped.
                             It is over.''')
                    print("Game over")  # even kills
                    self.play_again()
            elif (self.player_pos % 2) != 0:  # odd, the wumpus goes away.
                self.randomize_wumpus()  # change location of wumpus
                print('''You hear a slithering sound, as the Wumpus slips away.
                         Whew, that was close!''')

        # checks if the player hit landed in the pit
        if self.player_pos == self.pos[1] or self.player_pos == self.pos[2]:
            if self.gold_collected > 19:
                print("You are falling down a pit!")
                self.choice_to_buy_out_pit()
            else:
                print('''Aaaaaaaaahhhhhh....
                            You fall into a pit and die.''')  # player falls into pit
                self.play_again()

    def hints(self, cave):
        self.w = ['wumpus', 'pit1', 'pit2', 'bat1', 'bat2', 'chest1', 'chest2', 'chest3', 'chest4', 'chest5']  # list of threat names
        self.x = cave.get(self.player_pos,
                          "none")  # referring to the values from the cave dict acc to key, i.e.,player_pos
        for rooms in self.x:  # rooms = value numbers from dict
            for locations in self.pos:  # locations = values of hazards randomised numbers
                if rooms == locations:  # checking if any common number to see if any hazards in adjacent rooms
                    self.y = self.pos.index(rooms)  # index of that matching room
                    for hazards in self.w:
                        if self.w.index(hazards) == self.y:  # matching the index number to give a str value to threat
                            self.threat = self.w[self.w.index(hazards)]
                            if self.threat == 'bat1':
                                print("You hear a rustling.")
                            elif self.threat == 'bat2':
                                print("You hear a rustling.")
                            elif self.threat == 'pit1':
                                print("You feel a draft.")
                            elif self.threat == 'pit2':
                                print("You feel a draft.")
                            elif self.threat == 'wumpus':
                                print("You smell a stench.")  # printing warning acc to the threat detected
                            elif self.threat == 'chest1':
                                print("You see a beaming yellow light from nearby room")
                            elif self.threat == 'chest2':
                                print("You see a beaming yellow light from nearby room")
                            elif self.threat == 'chest3':
                                print("You see a beaming yellow light from nearby room")
                            elif self.threat == 'chest4':
                                print("You see a beaming yellow light from nearby room")
                            elif self.threat == 'chest5':
                                print("You see a beaming yellow light from nearby room")

    def move(self, cave):
        validMove = False
        self.adj_rooms = cave.get(self.player_pos, "none")
        while not validMove:
            self.room_num = int(input("Enter the room number you want to enter: "))
            if (self.room_num > 20 or self.room_num < 0):
                print("Invalid room number! Please enter a room number above 0 and below 21")
            elif (self.room_num not in self.adj_rooms):
                print("PLease enter one the adjacent numbers {0}".format(self.adj_rooms))
            else:
                validMove = True
                self.player_pos = self.room_num  # changing the player position to a new room
                self.adj_rooms = cave.get(self.player_pos, "none") # adjacent rooms should updated once player moves
                if self.player_pos == self.arrow:
                    self.arrow = -1
                    print("Congratulations, you found the arrow and can once again shoot.")
        
    

    def death_by_arrow(self):
        if self.arrow == self.pos[0]:
            print('''Wumpus has just been pierced by your deadly arrow!
Congratulations on your victory, you awesome hunter you.''')
            print()
            print()
            print("Exiting Program ...")
            self.play_again()
        elif self.arrow == self.player_pos:
            print('''You just shot yourself.
        Maybe Darwin was right.  You're dead.''')
            print()
            print()
            print("Exiting Program ...")
            self.play_again()

    def death_by_ricochet(self):
        if self.arrow == self.pos[0]:
            print('''Your arrow ricochet killed the Wumpus, you lucky dog!
Accidental victory, but still you win!''')
            print()
            print()
            print("Exiting Program ...")
            self.play_again()
        elif self.arrow == self.player_pos:
            print('''You just shot yourself, and are dying.
It didn't take long, you're dead.''')
            print()
            print()
            print("Exiting Program ...")
            self.play_again()

    def check_adj1(self):
        if self.room in self.adj_rooms: # if room in adjacent rooms, shoot arrow to the target room
            self.arrow = self.room
        else: # else arrow move to the smallest adjacent room
            print("Room {} is not adjacent.  Arrow ricochets...".format(self.room))
            self.arrow = min(self.adj_rooms)  # it ricochets to the smallest adjacent room
        self.death_by_arrow()


    def check_adj2(self):
        if self.list[0] in self.adj_rooms: # if room in adjacent rooms shoot arrow  to the target room
            if self.list[1] in cave.get(self.list[0], "none"):
                self.arrow = self.list[1]
            else:
                print("Room {} is not adjacent.  Arrow ricochets...".format(self.list[1]))
                self.arrow = min(cave.get(self.list[0], "none"))  # it ricochets to the smallest adjacent room
        else: # it ricochets to the smallest adjacent room
            print("Room {} is not adjacent.  Arrow ricochets...".format(self.list[0]))
            firstRoom = min(self.adj_rooms)
            if self.list[1] in cave.get(firstRoom, "none"):
                self.arrow = self.list[1]
            else:
                print("Room {} is not adjacent.  Arrow ricochets...".format(self.list[1]))
                self.arrow = min(cave.get(firstRoom, "none"))  # it ricochets to the smallest adjacent room
        self.death_by_arrow()


    def check_adj3(self):
        if self.list[0] in self.adj_rooms: # if room in adjacent rooms shoot arrow  to the target room
            if self.list[1] in cave.get(self.list[0], "none"):
                if self.list[2] in cave.get(self.list[1], "none"):
                    self.arrow = self.list[2]
                else:
                    print("Room {} is not adjacent.  Arrow ricochets...".format(self.list[2]))
                    self.arrow = min(cave.get(self.list[1], "none"))  # it ricochets to the smallest adjacent room
            else:
                print("Room {} is not adjacent.  Arrow ricochets...".format(self.list[1]))
                secondRoom = min(cave.get(self.list[0], "none"))  # it ricochets to the smallest adjacent room
                if self.list[2] in cave.get(secondRoom, "none"):
                    self.arrow = self.list[2]
                else:
                    print("Room {} is not adjacent.  Arrow ricochets...".format(self.list[2]))
                    self.arrow = min(cave.get(secondRoom, "none"))  # it ricochets to the smallest adjacent room

        else: # it ricochets to the smallest adjacent room
            print("Room {} is not adjacent.  Arrow ricochets...".format(self.list[0]))
            firstRoom = min(self.adj_rooms)
            if self.list[1] in cave.get(firstRoom, "none"):
                if self.list[2] in cave.get(self.list[1], "none"):
                    self.arrow = self.list[2]
                else:
                    print("Room {} is not adjacent.  Arrow ricochets...".format(self.list[2]))
                    self.arrow = min(cave.get(self.list[1], "none"))  # it ricochets to the smallest adjacent room
            else:
                print("Room {} is not adjacent.  Arrow ricochets...".format(self.list[1]))
                secondRoom = min(cave.get(firstRoom, "none"))  # it ricochets to the smallest adjacent room
                if self.list[2] in cave.get(secondRoom, "none"):
                    self.arrow = self.list[2]
                else:
                    print("Room {} is not adjacent.  Arrow ricochets...".format(self.list[2]))
                    self.arrow = min(cave.get(secondRoom, "none"))  # it ricochets to the smallest adjacent room
        self.death_by_arrow()
       

    def shoot(self):
        self.arrow = self.player_pos
        self.room_distance = -1
        while self.room_distance > 3 or self.room_distance < 1:
            self.room_distance = int(input("Enter the number of rooms (1..3) into which you want to shoot: "))
        counter = 0
        self.list = []
        if self.room_distance > 1:
            while counter < self.room_distance:
                self.room = int(input("Enter the room numbers you want to shoot through: "))
                counter += 1
                self.list.append(self.room)
        if self.room_distance == 1:
            self.check_adj1()
        elif self.room_distance == 2:
            self.check_adj2()
        elif self.room_distance == 3:
            self.check_adj3()

    def chest_questions(self):

        questions = {'Question: Which of the following computer generation uses concept of artificial intelligence?\n 1. First Generation\n 2. Second Generation\n 3. Third generation\n 4. Forth Generation\n':4, 
        'Question: The list of coded instructions is called?\n 1. Computer Program\n 2. Algorithm\n 3. Flowchart\n 4. Utility Program\n':1, 
        'Question: The brain of any computer system is?\n 1. ALU\n 2. CPU\n 3. Memory Unit\n 4. Control Unit\n':2,
        'Question: ALU stands for?\n 1. Arithmetic Logic Unit\n 2. Application Logic Unit\n 3. Array Logic Unit\n 4. None of the above\n': 1,
        'Question: Who is the father of Computers?\n 1. James Gosling\n 2. Charles Babbage\n 3. Dennis Ritchie\n 4. Bjarne Stroustrup\n':2,
        'Question: Which of the following language does the computer understand?\n 1. C Language\n 2. Assembly Language\n 3. Binary Language\n 4. BASIC\n':3,
        'Question: Which methodology is used to performed Maintenance testing?\n 1. Breadth test and depth test\n 2. Confirmation testing\n 3. Retesting\n 4. Sanity testing\n':1,
        'Question: Which of the following is not part of the Test document?\n 1. Test Case\n 2. Requirements Traceability Matrix [RTM]\n 3. Test strategy\n 4. Project Initiation Note [PIN]\n':4,
        'Question: Which term is used to define testing?\n 1. Evaluating deliverable to find errors\n 2. Finding broken code\n 3. A stage of all projects\n 4. None of the above\n':1,
        'Question: Which of the following is not a valid phase of SDLC (Software Development Life Cycle)?\n 1. Testing Phase\n 2. Requirement Phase\n 3. Deployment phase\n 4. Testing closure\n':4,
        'Question: Which of the following testing is also known as white-box testing?\n 1. Structural testing\n 2. Error guessing technique\n 3. Design based testing\n 4. None of the above\n':1,
        'Question: Functional testing is a?\n 1. Test design technique\n 2. Test level\n 3. SDLC Model\n 4. Test type\n':4,
        'Question: Testing the end to end functionality of the system as a whole is defined as?\n 1. Unit Testing\n 2. Functional Testing\n 3. Stress Testing\n 4. Load Testing\n':2}

        questions_list = ['Question: Which of the following computer generation uses concept of artificial intelligence?\n 1. First Generation\n 2. Second Generation\n 3. Third generation\n 4. Forth Generation\n', 
        'Question: The list of coded instructions is called?\n 1. Computer Program\n 2. Algorithm\n 3. Flowchart\n 4. Utility Program\n',
        'Question: The brain of any computer system is?\n 1. ALU\n 2. CPU\n 3. Memory Unit\n 4. Control Unit\n',
        'Question: ALU stands for?\n 1. Arithmetic Logic Unit\n 2. Application Logic Unit\n 3. Array Logic Unit\n 4. None of the above\n'
        'Question: Who is the father of Computers?\n 1. James Gosling\n 2. Charles Babbage\n 3. Dennis Ritchie\n 4. Bjarne Stroustrup\n',
        'Question: Which of the following language does the computer understand?\n 1. C Language\n 2. Assembly Language\n 3. Binary Language\n 4. BASIC\n',
        'Question: Which methodology is used to performed Maintenance testing?\n 1. Breadth test and depth test\n 2. Confirmation testing\n 3. Retesting\n 4. Sanity testing\n',
        'Question: Which of the following is not part of the Test document?\n 1. Test Case\n 2. Requirements Traceability Matrix [RTM]\n 3. Test strategy\n 4. Project Initiation Note [PIN]\n',
        'Question: Which term is used to define testing?\n 1. Evaluating deliverable to find errors\n 2. Finding broken code\n 3. A stage of all projects\n 4. None of the above\n',
        'Question: Which of the following is not a valid phase of SDLC (Software Development Life Cycle)?\n 1. Testing Phase\n 2. Requirement Phase\n 3. Deployment phase\n 4. Testing closure\n',
        'Question: Which of the following testing is also known as white-box testing?\n 1. Structural testing\n 2. Error guessing technique\n 3. Design based testing\n 4. None of the above\n',
        'Question: Functional testing is a?\n 1. Test design technique\n 2. Test level\n 3. SDLC Model\n 4. Test type\n',
        'Question: Testing the end to end functionality of the system as a whole is defined as?\n 1. Unit Testing\n 2. Functional Testing\n 3. Stress Testing\n 4. Load Testing\n']

        questions_asked = {}
        qnum = random.randint(0,12)
        while questions_list[qnum] in questions_asked:
            qnum = random.randint(0,12)

        questions_asked[questions_list[qnum]] = 1
        print(questions_list[qnum])
        user_answer = int(input("Please enter the answer by choosing the option number (1, 2, 3, or 4):"))
        return user_answer == questions[questions_list[qnum]]


    def collect_chest(self):
        if self.player_pos == self.chest1_location:
            self.gold_collected += self.chest1_value
            self.chest1_value = 0
            print("Congrats! You collected chest1 containing 40 gold.")

        if self.player_pos == self.chest2_location:
            self.gold_collected += self.chest2_value
            self.chest2_value = 0
            print("Congrats! You collected chest2 containing 40 gold.")

        if self.player_pos == self.chest3_location:
            self.gold_collected += self.chest3_value
            self.chest3_value = 0
            print("Congrats! You collected chest3 containing 40 gold.")

        if self.player_pos == self.chest4_location:
            self.gold_collected += self.chest4_value
            self.chest4_value = 0
            print("Congrats! You collected chest4 containing 40 gold.")

        if self.player_pos == self.chest5_location:
            self.gold_collected += self.chest5_value
            self.chest5_value = 0
            print("Congrats! You collected chest5 containing 40 gold.")

    def chest_unlock_questions_5(self, player):
        print("Right Answer!\n")
        deci = int(input("Enter the decimal Value of 1010 for unlocking the chest:"))
        if deci == 10:
            player.collect_chest()
        else:
            print('Wrong Passcode! Better luck next time!')
            #randomize chest location
            new_chest_loc = player.chest1_location
            while new_chest_loc in player.pos:
                new_chest_loc = random.randint(1,20)
            self.chest1_location = new_chest_loc
            self.pos[5] = new_chest_loc

    def chest_unlock_questions_6(self, player):
        print("Right Answer!\n")
        deci = int(input("Enter the decimal Value of 1111 for unlocking the chest:"))
        if deci == 15:
            player.collect_chest()
        else:
            print('Wrong Passcode! Better luck next time!')
            #randomize chest location
            new_chest_loc = player.chest2_location
            while new_chest_loc in player.pos:
                new_chest_loc = random.randint(1,20)
            player.chest2_location = new_chest_loc
            player.pos[6] = new_chest_loc

    def chest_unlock_questions_7(self, player):
        print("Right Answer!\n")
        deci = input("Enter the decimal Value of 0001.1100 (unsigned) for unlocking the chest:")
        if deci == 1.75:
            player.collect_chest()
        else:
            print('Wrong Passcode! Better luck next time!')
            #randomize chest location
            new_chest_loc = player.chest3_location
            while new_chest_loc in player.pos:
                new_chest_loc = random.randint(1,20)
            player.chest3_location = new_chest_loc
            player.pos[7] = new_chest_loc

    def chest_unlock_questions_8(self, player):
        print("Right Answer!\n")
        deci = int(input("Enter the decimal Value of 1010+0101 for unlocking the chest:"))
        if deci == 15:
            player.collect_chest()
        else:
            print('Wrong Passcode! Better luck next time!')
            #randomize chest location
            new_chest_loc = player.chest4_location
            while new_chest_loc in player.pos:
                new_chest_loc = random.randint(1,20)
            player.chest4_location = new_chest_loc
            player.pos[8] = new_chest_loc

    def chest_unlock_questions_9(self, player):
        print("Right Answer!\n")
        deci = int(input("Enter the decimal Value of 1000 for unlocking the chest:"))
        if deci == 8:
            player.collect_chest()
        else:
            print('Wrong Passcode! Better luck next time!')
            #randomize chest location
            new_chest_loc = player.chest5_location
            while new_chest_loc in player.pos:
                new_chest_loc = random.randint(1,20)
            player.chest5_location = new_chest_loc
            player.pos[9] = new_chest_loc
    



# while (game is running):
# print the threat message
# take the move from the user (First, they take a character.. if character is P or D, R, C then you just have to call the function)
# if the user enters M, then you need take the room number
# Check to see if the room number is valid
# Make the move happen, check if the player dies or gets carried by bats. If carried by bats... randomize both bats location and player location


def play():
    print('''Hunt the Wumpus:
            The Wumpus lives in a completely dark cave of 20 rooms. Each
            room has 3 tunnels leading to other rooms.
            Hazards:
            1. Two rooms have bottomless pits in them.  If you go there you fall and die.
            2. Two other rooms have super-bats.  If you go there, the bats grab you and
               fly you to some random room, which could be troublesome.  Then those bats go
               to a new room different from where they came from and from the other bats.
            3. The Wumpus is not bothered by the pits or bats, as he has sucker feet and
               is too heavy for bats to lift.  Usually he is asleep.  Two things wake
               him up: Anytime you shoot an arrow, or you entering his room.  The Wumpus
               will move into the lowest-numbered adjacent room anytime you shoot an arrow.
               When you move into the Wumpus' room, then he wakes and moves if he is in an
               odd-numbered room, but stays still otherwise.  After that, if he is in your
               room, he snaps your neck and you die!
            Moves:
            On each move you can do the following, where input can be upper or lower-case:
            1. Move into an adjacent room.  To move enter 'M' followed by a space and
               then a room number.
            2. Shoot your guided arrow through a list of up to three adjacent rooms, which
               you specify.  Your arrow ends up in the final room.
               To shoot enter 'S' followed by the number of rooms (1..3), and then the
               list of the desired number (up to 3) of adjacent room numbers, separated
               by spaces. If an arrow can't go a direction because there is no connecting
               tunnel, it ricochets and moves to the lowest-numbered adjacent room and
               continues doing this until it has traveled the designated number of rooms.
               If the arrow hits the Wumpus, you win! If the arrow hits you, you lose. You
               automatically pick up the arrow if you go through a room with the arrow in
               it.
            3. Enter 'R' to reset the person and hazard locations, useful for testing.
            4. Enter 'C' to cheat and display current board positions.
            5. Enter 'D' to display this set of instructions.
            6. Enter 'P' to print the maze room layout.
            7. Enter 'X' to exit the game.
            Good luck!''')  # initial printing of directions and rules of game
    print('''                                       ______18_______
                                        /      |        \\
                                        /      _9__       \ 
                                        /      /    \       \\
                                    /      /      \       \ 
                                    17     8        10     19
                                    | \   / \      /  \   / |
                                    |  \ /   \    /    \ /  |
                                    |   7     1___2     11  |   
                                    |   |    /     \    |   |
                                    |   6____5     3___12   |
                                    |   |     \   /     |   |
                                    |   \       4      /    |
                                    |    \      |     /     |
                                    \     15___14___13      /
                                    \   /            \    /
                                        \ /              \  /
                                        16________________20''')  # initial printing of the map
    #player = game()
    player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
    # player.randomize_initially()
    # print(player.cheat())
    while 1:
        print("Hey! You are in room {0}.".format(player.player_pos), end=' '), player.hints(cave)
        print("So far, you've collected", player.gold_collected, "gold")
        print()
        # taking input from the user
        answer = input("Enter X for exit, P for map print, D for directions, R for reset, C for cheat, M for move (and hit enter) and S"
                    " for shoot: ")
        if answer == 'P' or answer == 'p':  # print design of cave
            print_cave()
        elif answer == 'D' or answer == 'd':  # prints the rules of game
            directions()
        elif answer == 'R' or answer == 'r':  # resets the game to initial
            player.reset()  # Put it inside the class
        elif answer == 'C' or answer == 'c':  # it shows where all hazards r present
            player.cheat()
        elif answer == 'S' or answer == 's':  # allows u to shoot an arrow
            if player.arrow != -1:
                print("Sorry, you can't shoot an arrow you don't have.  Go find it.")
            else:
                player.shoot()
        elif answer == 'M' or answer == 'm':  # allows u to move to another room
            player.move(cave)
            player.death_by_pos()

            # checks to see if player has encountered a chest
            if player.player_pos == player.pos[5]:
                if player.chest_questions():
                    player.chest_unlock_questions_5(player)

                else:
                    print("No treasure, wrong answer!") 
                    #randomize the chest location different value
                    new_chest_loc = player.chest1_location
                    while new_chest_loc in player.pos:
                        new_chest_loc = random.randint(1,20)
                    player.chest1_location = new_chest_loc
                    player.pos[5] = new_chest_loc
                    

            elif player.player_pos == player.pos[6]:
                if player.chest_questions():
                    player.chest_unlock_questions_6(player)
                    
                else:
                    print("No treasure, wrong answer!") 
                    #randomize the chest location different value
                    new_chest_loc = player.chest2_location
                    while new_chest_loc in player.pos:
                        new_chest_loc = random.randint(1,20)
                    player.chest2_location = new_chest_loc
                    player.pos[6] = new_chest_loc

            elif player.player_pos == player.pos[7]:
                if player.chest_questions():
                    player.chest_unlock_questions_7(player)

                else:
                    print("No treasure, wrong answer!") 
                    #randomize the chest location different value
                    new_chest_loc = player.chest3_location
                    while new_chest_loc in player.pos:
                        new_chest_loc = random.randint(1,20)
                    player.chest3_location = new_chest_loc
                    player.pos[7] = new_chest_loc

            elif player.player_pos == player.pos[8]:
                if player.chest_questions():
                    player.chest_unlock_questions_8(player)

                else:
                    print("No treasure, wrong answer!") 
                    #randomize the chest location different value
                    new_chest_loc = player.chest4_location
                    while new_chest_loc in player.pos:
                        new_chest_loc = random.randint(1,20)
                    player.chest4_location = new_chest_loc
                    player.pos[8] = new_chest_loc

            elif player.player_pos == player.pos[9]:
                if player.chest_questions():
                    player.chest_unlock_questions_9(player)

                else:
                    print("No treasure, wrong answer!") 
                    #randomize the chest location different value
                    new_chest_loc = player.chest5_location
                    while new_chest_loc in player.pos:
                        new_chest_loc = random.randint(1,20)
                    player.chest5_location = new_chest_loc
                    player.pos[9] = new_chest_loc

            elif player.player_pos == player.pos[3]:  # check if in same room at bat1.
                player.randomize_person()  # bat will fly the player to random room
                player.randomize_bat1()  # bat will then fly to random room
                print('''Woah... you're flying!
                        You've just been transported by bats to room {0}'''.format(player.player_pos))
                player.death_by_pos()
                # we also have to check, after the player lands in random room via bats, does that room have wumpus or pit

            elif player.player_pos == player.pos[4]:  # check if in same room as bat2
                player.randomize_person()
                player.randomize_bat2()
                print('''Woah... you're flying!
                        You've just been transported by bats to room {0}'''.format(player.player_pos))
                player.death_by_pos()
                # we also have to check, after the player lands in random room via bats, does that room have wumpus or pit
                
        elif answer == 'X' or answer == 'x':
            exit()

play()
