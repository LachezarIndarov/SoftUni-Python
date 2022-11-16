"""
Input1
3 Motes 5 stones 5 Shards
6 leathers 255 fragments 7 Shards

Output1
Valanyr obtained!
shards: 5
fragments: 5
motes: 3
stones: 5
leathers: 6

Input2
123 silver 6 shards 8 shards 5 motes
9 fangs 75 motes 103 MOTES 8 Shards
86 Motes 7 stones 19 silver

Output2
Dragonwrath obtained!
shards: 22
fragments: 0
motes: 19
silver: 123
fangs: 9

"""
key_materials = ["shards", "fragments", "motes"]

text = input().split(" ")
key_material = dict()
junk = dict()

legendary_material = False

while True:
    for i in range(0, len(text), 2):
        quantity = int(text[i])
        material = text[i + 1].lower()
        if material in key_materials:
            if material in key_material.keys():
                key_material[material] += quantity
            else:
                key_material[material] = quantity

            if key_material[material] >= 250:
                key_material[material] -= 250
                legendary_material = True
                if material == "shards":
                    print("Shadowmourne obtained!")
                elif material == "fragments":
                    print("Valanyr obtained!")
                elif material == "motes":
                    print("Dragonwrath obtained!")
        else:
            if material in junk.keys():
                junk[material] += quantity
            else:
                junk[material] = quantity
        if legendary_material:
            break
    if legendary_material:
        break
    text = input().split(" ")

if "shards" in key_material.keys():
    print(f"shards: {key_material['shards']}")
else:
    print(f"shards: 0")
if "fragments" in key_material.keys():
    print(f"fragments: {key_material['fragments']}")
else:
    print(f"fragments: 0")
if "motes" in key_material.keys():
    print(f"motes: {key_material['motes']}")
else:
    print("motes: 0")
for (key, value) in junk.items():
    print(f"{key}: {value}")

