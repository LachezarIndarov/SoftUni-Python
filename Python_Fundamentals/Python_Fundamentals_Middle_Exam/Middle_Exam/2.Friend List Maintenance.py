friends = input().split(", ")
commands_list = input().split(" ")
command = commands_list[0]

while command != "Report":

    if command == "Blacklist":
        name = commands_list[1]
        if name in friends:
            index = friends.index(name)
            friends.remove(name)
            friends.insert(index,"Blacklisted")
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
    if command == "Error":
        index = int(commands_list[1])
        if (0 <= index < len(friends)) and friends[index] != "Blacklisted" and friends[index] != "Lost":
            print(f"{friends[index]} was lost due to an error.")
            friends[index] = "Lost"
    if command == "Change":
        index = int(commands_list[1])
        new_name = commands_list[2]
        if (0 <= index < len(friends)):
            print(f"{friends[index]} changed his username to {new_name}.")
            friends[index] = new_name
    commands_list = input().split(" ")
    command = commands_list[0]

print(f"Blacklisted names: {friends.count('Blacklisted')}")
print(f"Lost names: {friends.count('Lost')}")
print(*friends,sep=" ")



