from random import choice


cave_numbers = range(1,21)
wumpus_Location = choice(cave_numbers)
player_Location = choice(cave_numbers)
while player_Location == wumpus_Location:
    player_Location = choice(cave_numbers)

print("welcome to Hunt the wupus!")
print("You can see",len(cave_numbers),"caves")
print("To play,just type the number")
print("of the cave you wish to enter next")

while True:
    print("You are in cave",player_Location)
    if(player_Location == wumpus_Location-1 or player_Location == wumpus_Location+1):
        print("I smell a wumpus!")
        print("Which cave next?")
    layer_input = input(">")
    if(not player_input.isdigit() or int(player_Location) not in cave_numbers):
         print(player_input,"is not a cave")
   
    else:
         player_Location=int(player_input)
    if player_Location==wumpus_Location:
        print(" Aargh! You got eaten by a wumpus!")
        break