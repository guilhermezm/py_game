enemies = {
    "police": {
        "damage": 5,
        "sequence": "police",
        "time": 3.5
    },
    "cia": {
        "damage": 8,
        "sequence": "cia",
        "time": 3
    },
    "fbi": {
        "damage": 11,
        "sequence": "fbi",
        "time": 3
    },
    "swat": {
        "damage": 14,
        "sequence": "swat",
        "time": 2.8
    },
    "navy": {
        "damage": 17,
        "sequence": "Navy",
        "time": 2.8
    },
    "militar": {
        "damage": 20,
        "sequence": "@Militar",
        "time": 2.8
    },

}
fases = {
    1: {
        "map_graph": {},
        "enemies": ["police", "police", "police"],
        "introduction_msg": "You just got out of the bank, there are 3 cops shotting at you\nShow them who they are messing with!"
    },
    2: {
        "map_graph": {},
        "enemies": ["police", "police", "police", "cia", "cia", "cia"],
        "introduction_msg": "Oww no! They found you there\nNow you are messing up with professionals!"
    },
    3: {
        "map_graph": {},
        "enemies": ["police", "police", "fbi", "fbi", "fbi", "cia", "cia"],
        "introduction_msg": "Shit got federal! Now even the FBI is after you."
    },
    4: {
        "map_graph": {},
        "enemies": ["police", "police", "fbi", "fbi", "fbi", "cia", "cia", "swat", "swat", "swat"],
        "introduction_msg": "They called reforces, deal now also with SWAT"
    },
    5: {
        "map_graph": {},
        "enemies": ["police", "police", "fbi", "fbi", "fbi", "cia", "cia", "swat", "swat", "swat", "navy", "navy", "navy"],
        "introduction_msg": "The navy cornered you trough the river, let's see how good you are"
    },
    6: {
        "map_graph": {},
        "enemies": ["police", "police", "fbi", "fbi", "fbi", "cia", "cia", "swat", "swat", "swat", "navy", "navy", "navy", "militar", "militar", "militar"],
        "introduction_msg": "No one said it would be an easy task, beat the military"
    },
    7: {
        "map_graph": {},
        "enemies": ["police", "police", "police", "fbi", "fbi", "fbi", "fbi", "cia", "cia", "cia", "swat", "swat", "swat", "swat", "navy", "navy", "navy", "navy", "militar", "militar", "militar", "militar"],
        "introduction_msg": "You literally almost killed the whole regional forces, if you succed now, you can run away with all the money"
    },
}
actions = {
    "Run away": "You sprint into the nearest alley, hoping to lose your pursuers.",
    "Climb to the roof": "You look for a fire escape to get a height advantage.",
    "Run to the river": "You head towards the river, thinking you can use the water to your advantage.",
    "Run to the forest": "You dash towards the nearby woods, blending in with the foliage.",
    "Hide behind a tree": "You find a large oak, perfect for concealment.",
    "Hide behind a car": "You duck behind a parked car, keeping low.",
    "Take a hostage": "In desperation, you grab a bystander, using them as leverage."
}
