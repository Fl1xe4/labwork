tom = {"type": "cat", "owner": "Jim"}
rex = {"type": "dog", "owner": "Alex"}
kesha = {"type": "parrot", "owner": "Elena"}

pets = [tom, rex, kesha]

for pet in pets:
    print(pet["owner"] + " is the owner of a pet - a " + pet["type"] + ".")
    