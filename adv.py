from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)










def get_travel_order():
    #* init travel log and memory
    memory = dict()
    travel_log = []
    start_room = player.current_room.id
        #? Room Stutus Codes (White = Unvisited), (Grey = Visted but Uncompleted), (Black = Completely Vistited)
    memory[start_room] = ["Start", "Grey"] # [Descovered_by, Room_Status]

    while_loop_fail_safe = 0
    while memory[start_room][1] != "Black":
        while_loop_fail_safe += 1
        if (while_loop_fail_safe % 2000) == 0:
            memory[start_room][1] = "Black"
            print("You Failed")
            
    return travel_log

traversal_path = get_travel_order()




















# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = []
#'e', 'n', 'e', 'n', 'e', 'n', 'e', 'n', 'e', 'n', 'n', 'e', 'n', 'n', 'e', 'e', 'e', 'e'


#! ==================== DO NOT MODIFY ====================
# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
#! ==================== DO NOT MODIFY ====================



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
