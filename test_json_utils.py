import test_data

import sys
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    game1 = json_data["Game 1"]
    #print(game1["Year"])
    game2 = json_data["Game 2"]
    game3 = json_data["Game 3"]

    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    game_name1 = game1["title"]
    game_year1 = game1["Year"]
    platform1 = game1["platform"]
    for elem in platform1:
        platform_name1 = elem["name"]
        platform_year1 = elem["launch year"]

    game_name2 = game2["title"]
    game_year2 = game2["Year"]
    platform2 = game2["platform"]
    for elem in platform2:
        platform_name2 = elem["name"]
        platform_year2 = elem["launch year"]

    game_name3 = game3["title"]
    game_year3 = game3["Year"]
    platform3 = game3["platform"]

    for elem in platform3:
        platform_name3 = elem["name"]
        platform_year3 = elem["launch year"]

    game1_platform = test_data.Platform(platform_name1, platform_year1)
    game1_data = test_data.Game(game_name1, game1_platform, game_year1)
    game2_platform = test_data.Platform(platform_name2, platform_year2)
    game2_data = test_data.Game(game_name2, game2_platform, game_year2)
    game3_platform = test_data.Platform(platform_name3, platform_year3)
    game3_data = test_data.Game(game_name3, game3_platform, game_year3)
    game_library.add_game(game1_data)
    game_library.add_game(game2_data)
    game_library.add_game(game3_data)



    #Return the completed game_library
    return game_library

# Handling command line arguments
#  Note: sys.argv is a list of strings that contains each command line argument
#        The first element in the list is always the name of the python file being run
# Command line format: <input json filename>

default_input_json_file = "test_data.json"

if len(sys.argv) == 2:
    input_json_file = sys.argv[1]
    print("Using command line args:", input_json_file)
else:
    print("Unknown command line options. Using default values:", default_input_json_file)
    input_json_file = default_input_json_file

#Load the json data from the input file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print_game_library(game_library_data) in test_data.py
with open("test_data.json", 'r') as reader:
    json_data = json.load(reader)

mygamelib = make_game_library_from_json(json_data)

test_data.print_game_library(mygamelib)
