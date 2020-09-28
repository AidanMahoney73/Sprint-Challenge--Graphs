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











memory = dict()
travel_log = []
start_loc = player.current_room.id
memory[start_loc] = ["Start", "Gray"]

def get_connected():
    global player
    exits = player.current_room.get_exits()
    exit_ids = [player.current_room.get_room_in_direction(direction).id for direction in player.current_room.get_exits()]
    num_exits = len(exits)
    return num_exits, exit_ids, exits

num_exits, exit_ids, exits = get_connected()
print(num_exits, exit_ids, exits)

def travel(travel_log):
    # if node 0 is not black then 
    if memory[0][1] != "Black":
        # then
        print("Next Movement iteration")
        # then check which nodes are connected to the current node
        num_exits, exit_ids, exits = get_connected()
        print(f"Currently in {player.current_room.id} connected to {exit_ids}")
        # if any nodes are unexplored
        unexplored = [node for node in exit_ids if node not in memory]
        if len(unexplored) > 0:
            print(f"unexplored nodes: {unexplored}")
            # Then make the current node gray
            memory[player.current_room.id][1] = "Gray"
            print(f"set current node {player.current_room.id} to Gray")
            # Get the first Unexplored node
            next_node = unexplored[0]
            # add the new node to memory using [node_leaving, White]
            memory[next_node] = [player.current_room.id, "White"]
            print(memory)
            # travel to the first unexplored node in the list
            for num in range(num_exits):
                if exit_ids[num] == next_node:
                    dir_next_node = exits[num]
            print(f"traveling {dir_next_node} to {next_node}")
            player.travel(dir_next_node)
            print(f"now in {player.current_room.id}")
            # append the direction be travled to the travel log
            travel_log.append(dir_next_node)
            print(travel_log)
            # Recursion
            return travel(travel_log)
        # else
        else:
            print("No unexplored nodes here")
            # Then Current node is marked black
            memory[player.current_room.id][1] = "Black"
            print(f"set current node {player.current_room.id} to Black")
            if memory[0][1] != "Black":
                # travel to this nodes parent node
                next_node = memory[player.current_room.id][0]
                for num in range(num_exits):
                    if exit_ids[num] == next_node:
                        dir_next_node = exits[num]
                print(f"traveling {dir_next_node} to {next_node}")
                player.travel(dir_next_node)
                print(f"now in {player.current_room.id}")
                # Append the direction of travel to list
                travel_log.append(dir_next_node)
                print(travel_log)
                # Recursion
                return travel(travel_log)
            else:
                # print(travel_log)
                return travel_log
    # Else
    else:
        # Return travel log
        # print(travel_log)
        return travel_log

traversal_path = travel(travel_log)













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
