import functions

def dofase(i, fases, enemies, life, actions):
    print(fases[i]["introduction_msg"])
    input("Click enter to start")
    life = functions.villons_challange(i, fases, enemies, life)
    print("Congratulations! You escaped them\n Chose your next move:")
    return functions.choose_action(actions), life
