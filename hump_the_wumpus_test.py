import unittest
import sys
from unittest.mock import patch
from io import StringIO
from hunt_the_wumpus import game,cave


class TestGame(unittest.TestCase):

    # unit test for randomize initialization
    # Game wumpus, hazards and chest locations should be initialize to values in range 1-20
    # each location should be unique
    # each location should not be equal to player location which is 13
    def test_randomize_initially_test(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.randomize_initially()
        positions = player.pos

        for pos in positions:
            self.assertTrue(1 <= pos <=20,"Randomize Initialize Test Failed! positions are out of 1-20 range")
            self.assertNotEqual(13, pos, "Randomize Initialize Test Failed! hazards or chests in player position")
        
        self.assertTrue(len(positions) == len(set(positions)), "Randomize Initialize Test Failed! Hazards and chests positions duplicates")

    # unit test for reset
    # player position should be set to 13
    # gold collected should be set to 0
    # Game wumpus, hazards and chest locations should be initialize to values in range 1-20
    #   each above location should be unique
    #   each above location should not be equal to player location which is 13
    def test_reset(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.randomize_initially()
        player.gold_collected = 10 # set gold collected to 10 - later check if this reset to 0
        player.pos = 14 # set player location to 14 - later check this reset to 14

        player.reset()

        self.assertReset(player, "Reset Test")


    # unit test for randomize bat1
    # bat1 position should be initialize to values in range 1-20
    # bat1 location should be unique
    # bat1 location should not be equal to player location which is 13
    def test_randomize_bat1(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.randomize_bat1()

        self.assertEqual(player.bat1, player.pos[3], "Randomize Bat1 Test Failed! bat1 in position is not matched with map locations")
        self.assertTrue(1 <= player.pos[3] <=20,"Randomize Bat1 Test Failed! Bat1 position is out of 1-20 range")
        self.assertNotEqual(13, player.pos[3], "Randomize Bat1 Test Failed! bat1 in player position")
        bat1Position = player.bat1
        for i in range (len(player.pos)):
            if i != 3:
                self.assertFalse(player.pos[i]==bat1Position, "Randomize Initialize Bat1 Failed! Bat1 in initialized to already occupied location")

    # unit test for randomize bat2
    # bat2 position should be initialize to values in range 1-20
    # bat2 location should be unique
    # bat2 location should not be equal to player location which is 13
    def test_randomize_bat2(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.randomize_bat2()

        self.assertEqual(player.bat2, player.pos[4], "Randomize Bat2 Test Failed! bat2 in position is not matched with map locations")
        self.assertTrue(1 <= player.pos[4] <=20,"Randomize Bat2 Test Failed! Bat2 position is out of 1-20 range")
        self.assertNotEqual(13, player.pos[4], "Randomize Bat2 Test Failed! bat2 in player position")
        bat2Position = player.bat2
        for i in range (len(player.pos)):
            if i != 4:
                self.assertFalse(player.pos[i]==bat2Position, "Randomize Initialize Bat2 Failed! Bat1 in initialized to already occupied location")

    # unit test for randomize person
    # person position should be initialize to values in range 1-20
    # person position should not be equal to bat1 or bat2
    def test_randomize_person(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.randomize_person()

        self.assertTrue(1 <= player.player_pos <=20,"Randomize Person Test Failed! Person position is out of 1-20 range")
        self.assertNotEqual(player.player_pos, player.pos[3], "Randomize Person Test Failed! person in bat1 position")
        self.assertNotEqual(player.player_pos, player.pos[4], "Randomize Person Test Failed! person in bat2 position")

    # unit test for randomize wumpus
    # wumpus position should be initialize to values in range 1-20
    # person position should be adjacent to player position
    def test_randomize_wumpus(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.randomize_wumpus()

        self.assertTrue(1 <= player.wumpus <=20,"Randomize Wumpus Test Failed! Wumpus position is out of 1-20 range")
        self.assertEqual(player.wumpus, player.pos[0],"Randomize Wumpus Test Failed! Wumpus location mis match in map positions and self.wumpus")
        self.assertIn(player.wumpus, cave.get(player.player_pos, "none"), "Randomize Wumpus Test Failed! Wumpus not in adjacent position to player")

    # unit test for play agin
    # user enter "Y"
    # set gold collected to 15 and player_pos to 9
    # assert if gold collected reset to 0 and player_pos to 13
    def test_play_again_yes(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.gold_collected = 15 # set gold collected to 15 - later check if this reset to 0
        player.player_pos = 9 # set player location to 9 - later check this reset to 14
        userChoice = "Y"
        with unittest.mock.patch('builtins.input', return_value = userChoice):
            player.play_again()
            self.assertReset(player, "Play Again Test")

    # unit test for choice_to_buy_out_wumpus -1
    # user enter "Y"
    # set gold collected to 100 
    # assert if gold collected set to 20 (80 deducted)
    def test_choice_to_buy_out_wumpus_yes(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.gold_collected = 100 # set gold collected to 100 -
        userChoice = "Y"
        with unittest.mock.patch('builtins.input', return_value = userChoice):
            player.choice_to_buy_out_wumpus()
            self.assertEqual(player.gold_collected, 20, "Choice to buy out wumpus test failed! 80 Golds not deducted")

    # unit test for choice_to_buy_out_wumpus -2
    # user enter "Y"
    # set gold collected to 60 
    # assert if gold collected not changed
    def test_choice_to_buy_out_wumpus_yes_not_enough_golds(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.gold_collected = 60 # set gold collected to 60
        userChoice = "Y"
        with unittest.mock.patch('builtins.input', return_value = userChoice):
            player.choice_to_buy_out_wumpus()
            self.assertEqual(player.gold_collected, 60, "Choice to buy out wumpus test with not enough golds failed!")

    # unit test for choice_to_buy_out_wumpus -3
    # user enter "Y"
    # set gold collected to 100 
    # assert if gold collected not changed
    def test_choice_to_buy_out_wumpus_no(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.gold_collected = 100 # set gold collected to 100 -
        userChoice = "n"
        with unittest.mock.patch('builtins.input', return_value = userChoice):
            player.choice_to_buy_out_wumpus()
            self.assertEqual(player.gold_collected, 100, "Choice to buy out wumpus test with user enter no failed!")

    # unit test for choice_to_buy_out_pit -1
    # user enter "Y"
    # set gold collected to 100 
    # assert if gold collected set to 80 (20 deducted)
    def test_choice_to_buy_out_pit_yes(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.gold_collected = 100 # set gold collected to 100 -
        userChoice = "Y"
        with unittest.mock.patch('builtins.input', return_value = userChoice):
            player.choice_to_buy_out_pit()
            self.assertEqual(player.gold_collected, 80, "Choice to buy out pit test failed! 20 Golds not deducted")

    
    # unit test for choice_to_buy_out_pit -2
    # user enter "Y"
    # set gold collected to 10 
    # assert if gold collected not changed
    def test_choice_to_buy_out_pit_yes_not_enough_golds(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.gold_collected = 10 # set gold collected to 10
        userChoice = "Y"
        with unittest.mock.patch('builtins.input', return_value = userChoice):
            player.choice_to_buy_out_pit()
            self.assertEqual(player.gold_collected, 10, "Choice to buy out pit test with not enough golds failed!")

    # unit test for choice_to_buy_out_pit -3
    # user enter "Y"
    # set gold collected to 60 
    # assert if gold collected not changed
    def test_choice_to_buy_out_pit_no(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.gold_collected = 60 # set gold collected to 60
        userChoice = "n"
        with unittest.mock.patch('builtins.input', return_value = userChoice):
            player.choice_to_buy_out_pit()
            self.assertEqual(player.gold_collected, 60, "Choice to buy out pit test with user enter no failed!")


    # unit test for death_by_pos -1
    # player enter into wumpus room, room is even room and have gold to buy the wumpus
    # assert if gold deducted by 80 after buy the wumpus
    def test_death_by_pos_even_room(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.gold_collected = 100 # set gold collected to 100
        player.pos[0] = 12
        player.player_pos = player.pos[0]
        userChoice = "Y"
        with unittest.mock.patch('builtins.input', return_value = userChoice):
            player.death_by_pos()
            self.assertTrue(player.gold_collected <= 20, "death by pos test -1 failed!")
    
    # unit test for death_by_pos -2
    # player enter into wumpus room, room is odd room and have gold to buy the wumpus
    # assert if gold is not deducted by 80 after buy the wumpus
    def test_death_by_pos_odd_room(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.gold_collected = 100 # set gold collected to 100
        player.pos[0] = 11
        player.player_pos = player.pos[0]
        
        player.death_by_pos()
        self.assertEqual(player.gold_collected, 100, "death by pos test -2 failed!")

    # unit test for death_by_pos -3
    # player enter into wumpus room, room is even room and do not have gold to buy the wumpus
    # assert if gold is not deducted by 80 after buy the wumpus
    @unittest.mock.patch('builtins.input', return_value = "n")
    def test_death_by_pos_even_room_without_golds(self, mockInput):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.gold_collected = 50 # set gold collected to 50
        player.pos[0] = 12
        player.player_pos = player.pos[0]
        with self.assertRaises(SystemExit):
            player.death_by_pos()
            self.assertEqual(player.gold_collected, 50, "death by pos test -3 failed!")

    # unit test for death_by_pos -4
    # player enter into pit room, have gold to buy the pit
    # assert if gold deducted by 80 after buy the wumpus
    def test_death_by_pos_pit_room(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.gold_collected = 100 # set gold collected to 100
        player.player_pos = player.pos[1]
        userChoice = "Y"
        with unittest.mock.patch('builtins.input', return_value = userChoice):
            player.death_by_pos()
            self.assertTrue(player.gold_collected <=80, "death by pos test -4 failed!")
    
    # unit test for death_by_pos -5
    # player enter into pit room, have not enough gold to buy the pit
    # assert if gold not deducted by 80 after buy the wumpus
    @unittest.mock.patch('builtins.input', return_value = "n")
    def test_death_by_pos_pit_room_and_not_have_enough_golds(self, mockInput):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.gold_collected = 1 # set gold collected to 100
        player.player_pos = player.pos[2]
        with self.assertRaises(SystemExit):
            player.death_by_pos()
            self.assertEqual(player.gold_collected, 1, "death by pos test -5 failed!")

    # unit test for hints
    # Player room = 13 -> neigbour rooms (12,14,20)
    # bat1 locatrion set to 12 -> "You hear a rustling."
    # wumpus location set to 14 -> "You smell a stench."
    # chest1 location set to 20 -> "You see a beaming yellow light from nearby room"
    # above messages should display
    def  test_hints(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.pos = [14,1,2,12,3,20,4,5,6,7]
        expected = "You hear a rustling.\nYou smell a stench.\nYou see a beaming yellow light from nearby room\n"
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
           player.hints(cave)
           self.assertEqual(mock_stdout.getvalue(), expected, "hint test failed!")

            
    # unit test for move -1
    # player position is set to 13 hence adjacent rooms are 12,14,20
    # enter invalid number over range 1-20 first time as moving room
    # enter room number not adjacent to current room in second time as moving room
    # enter valid room to move in third time
    # validate for error messages and player final position
    @unittest.mock.patch('builtins.input', side_effect= [21,2,12])
    def move_test_op(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mo:
            player.move(cave)
            self.assertEqual(player.player_pos, 12, "move test failed!")
            self.assertEqual(player.adj_rooms, cave.get(player.player_pos), "move test failed!")
            return(mo.getvalue())

    # unit test for move -2
    # player position is set to 13 hence adjacent rooms are 12,14,20
    # arrow is place in 12
    # enter valid room to move - 12
    # validate prompt messages and player final position
    @unittest.mock.patch('builtins.input', return_value= 12)
    def move_test_get_arrow(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.arrow = 12
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mo:
            player.move(cave)
            self.assertEqual(player.player_pos, 12, "move test get arrow failed!")
            self.assertEqual(player.adj_rooms, cave.get(player.player_pos), "move test get arrow failed!")
            return(mo.getvalue())
    
    def test_move(self):
        expected = "Invalid room number! Please enter a room number above 0 and below 21\n" + "PLease enter one the adjacent numbers [12, 14, 20]\n"
        returned = self.move_test_op()
        self.assertEqual(expected, returned, "move test failed!")

        expected = "Congratulations, you found the arrow and can once again shoot.\n"
        returned = self.move_test_get_arrow()
        self.assertEqual(expected, returned, "move test failed!")

    # unit test for death by arrow - wumpus dead
    @unittest.mock.patch('builtins.input', return_value= "n")
    def test_death_by_arrow_wumpus_dead(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.arrow = player.wumpus
        with self.assertRaises(SystemExit):
            player.death_by_arrow()
    
    # unit test for death by arrow - player dead
    @unittest.mock.patch('builtins.input', return_value= "n")
    def test_death_by_arrow_wumpus_dead(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.arrow = player.player_pos
        with self.assertRaises(SystemExit):
            player.death_by_arrow()

    # unit test for death by richochet - wumpus dead
    @unittest.mock.patch('builtins.input', return_value= "n")
    def test_death_by_richochet_wumpus_dead(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.arrow = player.wumpus
        with self.assertRaises(SystemExit):
            player.death_by_ricochet()
    
    # unit test for death by arrow - player dead
    @unittest.mock.patch('builtins.input', return_value= "n")
    def test_death_by_ricochet_player_dead(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.arrow = player.player_pos
        with self.assertRaises(SystemExit):
            player.death_by_ricochet()

    # unit test for check adj1 -1
    # arrow shoots to player adjacent room -> no one deads
    # check arrow in correct room
    def test_check_adj1(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")
        player.room = player.adj_rooms[0]

        player.check_adj1()

        self.assertEqual(player.arrow, player.room, "check adj1 test failed!!")

    # unit test for check adj1 -2
    # arrow shoots to player  non adjacent room and no one deads
    # player in room 12 : adjacent rooms are [13, 11, 3]
    # arrow should be in lowest adj room -> i.e 3
    def test_check_adj1_non_adj_room(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")
        player.room = 20

        player.check_adj1()

        self.assertEqual(player.arrow, 3, "check adj1 non adj room test failed!!")

    # unit test for check adj2 -1
    # player in room 12 : adjacent rooms are [13, 11, 3]
    # arrow shoot to 2 rooms distances : two rooms are 11 and
    # arrow shoots to distance = 2_rooms
    #    room1 : adjacent room to player 1
    #    room2 : adjacent room to room1
    # check arrow in room2
    def test_check_adj2_success_both(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")
        player.list = [11, 10]

        player.check_adj2()

        self.assertEqual(player.arrow, 10, "check adj2 success both test failed!!")

    # unit test for check adj2 -2
    # player in room 12 : adjacent rooms are [13, 11, 3]
    # arrow shoot to 2 rooms distances : two rooms are 11 and 4
    # arrow shoots to distance = 2_rooms
    #    room1 : adjacent room to player 1
    #    room2 : not adjacent room to room1
    # check arrow in min of adjacent rooms to room1
    def test_check_adj2_one_success_one_ricochets(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")
        player.list = [11, 4]

        player.check_adj2()

        self.assertEqual(player.arrow, min(cave.get(11, "none")), "check adj2 one success one ricochetsh test failed!!")

    # unit test for check adj2 -3
    # player in room 12 : adjacent rooms are [13, 11, 3]
    # arrow shoot to 2 rooms distances : two rooms are 5 and 7
    # arrow shoots to distance = 2_rooms
    #    room1 : not adjacent room to player 1
    #    room2 : not adjacent room to room1
    # check arrow in min of adjacent rooms to room1
    def test_check_adj2_both_ricochets(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")
        player.list = [5, 7]

        player.check_adj2()

        self.assertEqual(player.arrow, min(cave.get(min(cave.get(5, "none")))), "check adj2 both ricochetsh test failed!!")

    # unit test for check adj2 -4
    # player in room 12 : adjacent rooms are [13, 11, 3]
    # arrow shoot to 2 rooms distances : two rooms are 5 and
    # arrow shoots to distance = 2_rooms
    #    room1 : not adjacent room to player 1
    #    room2 : not adjacent room to room1
    # check arrow in min of adjacent rooms to room1
    def test_check_adj2_one_ricochets_one_success(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")
        player.list = [5, 4]

        player.check_adj2()

        self.assertEqual(player.arrow, 4, "check adj2 one ricochets one success test failed!!")

    # unit test for check adj3 -1
    # player in room 12 : adjacent rooms are [13, 11, 3]
    # arrow shoot to 3 rooms distances : three rooms are 3,2 and 10
    # arrow shoots to distance = 3_rooms
    #    room1 : adjacent room to player 1
    #    room2 : adjacent room to room1
    #    room3 : adjacent room to room2
    # check arrow in room 10
    def test_check_adj3_all_success(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")
        player.list = [3, 2, 10]

        player.check_adj3()

        self.assertEqual(player.arrow, 10, "check adj3 all success test failed!!")

    # unit test for check adj3 -2
    # player in room 12 : adjacent rooms are [13, 11, 3]
    # arrow shoot to 3 rooms distances : three rooms are 3,2 and 19
    # arrow shoots to distance = 3_rooms
    #    room1 : adjacent room to player 1
    #    room2 : adjacent room to room1
    #    room3 : non adjacent room to room2
    # check arrow in room min of adjacent rooms to room 11
    def test_check_adj3_first_two_success_one_ricochets(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")
        player.list = [3, 2, 19]

        player.check_adj3()

        self.assertEqual(player.arrow, min(cave.get(2,"none")), "check adj3 first two success one ricochets test failed!!")

    # unit test for check adj3 -3
    # player in room 12 : adjacent rooms are [13, 11, 3]
    # arrow shoot to 3 rooms distances : three rooms are 3,19 and 10
    # arrow shoots to distance = 3_rooms
    #    room1 : adjacent room to player 1
    #    room2 : non adjacent room to room1
    #    room3 : adjacent room to room2
    # check arrow in room 10
    def test_check_adj3_one_success_two_ricochets_three_success(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")
        player.list = [3, 19, 10]

        player.check_adj3()

        self.assertEqual(player.arrow, 10, "check adj3 one success two ricochets three success test failed!!")
    
    # unit test for check adj3 -4
    # player in room 12 : adjacent rooms are [13, 11, 3]
    # arrow shoot to 3 rooms distances : three rooms are 3,19 and 1
    # arrow shoots to distance = 3_rooms
    #    room1 : adjacent room to player 1
    #    room2 : non adjacent room to room1
    #    room3 : non adjacent room to room2
    # check arrow in  min adjacent room
    def test_check_adj3_one_success_two_ricochets_three_ricochets(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")
        player.list = [3, 19, 1]

        player.check_adj3()

        self.assertEqual(player.arrow, min(cave.get(min(cave.get(3,'none')),'none')), "check adj3 one success two ricochets three ricochets test failed!!")

    # unit test for check adj3 -5
    # player in room 12 : adjacent rooms are [13, 11, 3]
    # arrow shoot to 3 rooms distances : three rooms are 19,12 and 11
    # arrow shoots to distance = 3_rooms
    #    room1 : non adjacent room to player 1
    #    room2 : adjacent room to room1
    #    room3 : adjacent room to room2
    # check arrow in room 11
    def test_check_adj3_one_ricochets_two_success_three_success(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")
        player.list = [19, 12, 11]

        player.check_adj3()

        self.assertEqual(player.arrow, 11, "check adj3 one ricochets two success three success test failed!!")

    # unit test for check adj3 -6
    # player in room 12 : adjacent rooms are [13, 11, 3]
    # arrow shoot to 3 rooms distances : three rooms are 19,12 and 1
    # arrow shoots to distance = 3_rooms
    #    room1 : non adjacent room to player 1
    #    room2 : adjacent room to room1
    #    room3 : non adjacent room to room2
    # check arrow in room 11
    def test_check_adj3_one_ricochets_two_success_three_ricochets(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")
        player.list = [19, 12, 1]

        player.check_adj3()

        self.assertEqual(player.arrow, min(cave.get(12)), "check adj3 one ricochets two success three ricochets test failed!!")

    # unit test for check adj3 -7
    # player in room 12 : adjacent rooms are [13, 11, 3]
    # arrow shoot to 3 rooms distances : three rooms are 19,14 and 10
    # arrow shoots to distance = 3_rooms
    #    room1 : non adjacent room to player 1
    #    room2 : non adjacent room to room1
    #    room3 : adjacent room to room2
    # check arrow in room 11
    def test_check_adj3_one_ricochets_two_ricochets_three_success(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")
        player.list = [19,14,10]

        player.check_adj3()

        self.assertEqual(player.arrow, 10, "check adj3 one ricochets two ricochets three success test failed!!")
    
    # unit test for check adj3 -8
    # player in room 12 : adjacent rooms are [13, 11, 3]
    # arrow shoot to 3 rooms distances : three rooms are 19,14 and 15
    # arrow shoots to distance = 3_rooms
    #    room1 : non adjacent room to player 1
    #    room2 : non adjacent room to room1
    #    room3 : non adjacent room to room2
    # check arrow in room 11
    def test_check_adj3_one_ricochets_two_ricochets_three_ricochets(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")
        player.list = [19,14,15]

        player.check_adj3()

        self.assertEqual(player.arrow, min(cave.get(min(cave.get(min(cave.get(12)))))), "check adj3 one ricochets two ricochets three ricochets test failed!!")

    # unit test for shoot - room distance 3
    # user input room_distance - 3
    # user input rooms to shoot as - 3,2,10
    @unittest.mock.patch('builtins.input', side_effect= [3,3,2,10])
    def test_shoot(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = 12
        player.adj_rooms = cave.get(player.player_pos, "none")

        player.shoot()

        self.assertListEqual(player.list, [3,2,10], "shoot test failed!")
        self.assertEqual(player.room_distance, 3, "shoot test failed!")

    # unit test for chest_questions
    # user input correct answer
    @unittest.mock.patch('builtins.input', return_value=1)
    def test_chest_question(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)

        with patch('random.randint', return_value = 1) as mock_random:
            result = player.chest_questions()
            self.assertEqual(True, result, "chest questions failed!")
    
    # unit test for chest_questions
    # user input in-correct answer
    @unittest.mock.patch('builtins.input', return_value=2)
    def test_chest_question(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)

        with patch('random.randint', return_value = 1) as mock_random:
            result = player.chest_questions()
            self.assertEqual(False, result, "chest questions failed!")
    
    # unit test for collection chest - chest1
    # player collected chest1
    def test_collect_chest1(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest1_location
        oldGold = player.gold_collected
        chestVal = player.chest1_value
        expectedGold = oldGold + chestVal

        player.collect_chest()
        self.assertEqual(player.gold_collected, expectedGold, "collect chest1 test failed!")
        self.assertEqual(player.chest1_value, 0, "collect chest1 test failed!")

    # unit test for collection chest - chest2
    # player collected chest2
    def test_collect_chest2(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest2_location
        oldGold = player.gold_collected
        chestVal = player.chest2_value
        expectedGold = oldGold + chestVal

        player.collect_chest()
        self.assertEqual(player.gold_collected, expectedGold, "collect chest2 test failed!")
        self.assertEqual(player.chest2_value, 0, "collect chest2 test failed!")

    # unit test for collection chest - chest3
    # player collected chest3
    def test_collect_chest3(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest3_location
        oldGold = player.gold_collected
        chestVal = player.chest3_value
        expectedGold = oldGold + chestVal

        player.collect_chest()
        self.assertEqual(player.gold_collected, expectedGold, "collect chest3 test failed!")
        self.assertEqual(player.chest3_value, 0, "collect chest3 test failed!")

    # unit test for collection chest - chest4
    # player collected chest4
    def test_collect_chest4(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest4_location
        oldGold = player.gold_collected
        chestVal = player.chest4_value
        expectedGold = oldGold + chestVal

        player.collect_chest()
        self.assertEqual(player.gold_collected, expectedGold, "collect chest4 test failed!")
        self.assertEqual(player.chest4_value, 0, "collect chest4 test failed!")
    
    # unit test for collection chest - chest5
    # player collected chest1
    def test_collect_chest5(self):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest5_location
        oldGold = player.gold_collected
        chestVal = player.chest5_value
        expectedGold = oldGold + chestVal

        player.collect_chest()
        self.assertEqual(player.gold_collected, expectedGold, "collect chest5 test failed!")
        self.assertEqual(player.chest5_value, 0, "collect chest5 test failed!")
    
    # unit test for chest unlock questions5 - correct passcode
    @unittest.mock.patch('builtins.input', return_value = 10)
    def test_chest_unlock_question5_correct_passcode(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest1_location
        oldGold = player.gold_collected
        chestVal = player.chest1_value
        expectedGold = oldGold + chestVal

        player.chest_unlock_questions_5(player)
        self.assertEqual(player.gold_collected, expectedGold, "chest unlock question5 correct passcode test failed!")
        self.assertEqual(player.chest1_value, 0, "chest unlock question5 correct passcode test failed!")
    
    # unit test for chest unlock questions5 - wrong passcode
    @unittest.mock.patch('builtins.input', return_value = 100)
    def test_chest_unlock_question5_wrong_passcode(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest1_location
        oldGold = player.gold_collected
        expectedGold = oldGold
        oldChestLocation = player.chest1_location

        player.chest_unlock_questions_5(player)
        self.assertEqual(player.gold_collected, expectedGold, "chest unlock question5 wrong passcode test failed!")
        self.assertNotEqual(player.chest1_value, oldChestLocation, "chest unlock question5 wrong passcode test failed!")

    # unit test for chest unlock questions6 - correct passcode
    @unittest.mock.patch('builtins.input', return_value = 15)
    def test_chest_unlock_question6_correct_passcode(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest2_location
        oldGold = player.gold_collected
        chestVal = player.chest2_value
        expectedGold = oldGold + chestVal

        player.chest_unlock_questions_6(player)
        self.assertEqual(player.gold_collected, expectedGold, "chest unlock question6 correct passcode test failed!")
        self.assertEqual(player.chest2_value, 0, "chest unlock question6 correct passcode test failed!")
    
    # unit test for chest unlock questions6 - wrong passcode
    @unittest.mock.patch('builtins.input', return_value = 100)
    def test_chest_unlock_question6_wrong_passcode(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest2_location
        oldGold = player.gold_collected
        expectedGold = oldGold
        oldChestLocation = player.chest2_location

        player.chest_unlock_questions_5(player)
        self.assertEqual(player.gold_collected, expectedGold, "chest unlock question6 wrong passcode test failed!")
        self.assertNotEqual(player.chest2_value, oldChestLocation, "chest unlock question6 wrong passcode test failed!")
    
    # unit test for chest unlock questions7 - correct passcode
    @unittest.mock.patch('builtins.input', return_value = 1.75)
    def test_chest_unlock_question7_correct_passcode(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest3_location
        oldGold = player.gold_collected
        chestVal = player.chest3_value
        expectedGold = oldGold + chestVal

        player.chest_unlock_questions_7(player)
        self.assertEqual(player.gold_collected, expectedGold, "chest unlock question7 correct passcode test failed!")
        self.assertEqual(player.chest3_value, 0, "chest unlock question7 correct passcode test failed!")
    
    # unit test for chest unlock questions7 - wrong passcode
    @unittest.mock.patch('builtins.input', return_value = 100)
    def test_chest_unlock_question7_wrong_passcode(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest3_location
        oldGold = player.gold_collected
        expectedGold = oldGold
        oldChestLocation = player.chest3_location

        player.chest_unlock_questions_7(player)
        self.assertEqual(player.gold_collected, expectedGold, "chest unlock question7 wrong passcode test failed!")
        self.assertNotEqual(player.chest3_value, oldChestLocation, "chest unlock question7 wrong passcode test failed!")
    
    # unit test for chest unlock questions8 - correct passcode
    @unittest.mock.patch('builtins.input', return_value = 15)
    def test_chest_unlock_question8_correct_passcode(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest4_location
        oldGold = player.gold_collected
        chestVal = player.chest4_value
        expectedGold = oldGold + chestVal

        player.chest_unlock_questions_8(player)
        self.assertEqual(player.gold_collected, expectedGold, "chest unlock question8 correct passcode test failed!")
        self.assertEqual(player.chest4_value, 0, "chest unlock question8 correct passcode test failed!")
    
    # unit test for chest unlock questions8 - wrong passcode
    @unittest.mock.patch('builtins.input', return_value = 100)
    def test_chest_unlock_question8_wrong_passcode(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest4_location
        oldGold = player.gold_collected
        expectedGold = oldGold
        oldChestLocation = player.chest4_location

        player.chest_unlock_questions_8(player)
        self.assertEqual(player.gold_collected, expectedGold, "chest unlock question8 wrong passcode test failed!")
        self.assertNotEqual(player.chest4_value, oldChestLocation, "chest unlock question8 wrong passcode test failed!")

    # unit test for chest unlock questions9 - correct passcode
    @unittest.mock.patch('builtins.input', return_value = 8)
    def test_chest_unlock_question9_correct_passcode(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest5_location
        oldGold = player.gold_collected
        chestVal = player.chest5_value
        expectedGold = oldGold + chestVal

        player.chest_unlock_questions_9(player)
        self.assertEqual(player.gold_collected, expectedGold, "chest unlock question9 correct passcode test failed!")
        self.assertEqual(player.chest5_value, 0, "chest unlock question9 correct passcode test failed!")
    
    # unit test for chest unlock questions9 - wrong passcode
    @unittest.mock.patch('builtins.input', return_value = 100)
    def test_chest_unlock_question9_wrong_passcode(self, mi):
        player = game(15, 18, 16, 4, 2, 20, 12, 10, 19, 17)
        player.player_pos = player.chest5_location
        oldGold = player.gold_collected
        expectedGold = oldGold
        oldChestLocation = player.chest5_location

        player.chest_unlock_questions_9(player)
        self.assertEqual(player.gold_collected, expectedGold, "chest unlock question9 wrong passcode test failed!")
        self.assertNotEqual(player.chest5_value, oldChestLocation, "chest unlock question9 wrong passcode test failed!")











    def assertReset(self, player, testName):
        self.assertEqual(0, player.gold_collected, testName +" Failed! Gold collected not reset to zero")
        self.assertEqual(13, player.player_pos,  testName +" Failed! Player position not resetted to 13")

        positions = player.pos
        for pos in positions:
            self.assertTrue(1 <= pos <=20, testName +" Failed! positions are out of 1-20 range")
            self.assertNotEqual(13, pos,  testName +" Failed! hazards or chests in player position")
        
        self.assertTrue(len(positions) == len(set(positions)),  testName +" Failed! Hazards and chests positions duplicates")


unittest.main()