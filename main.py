import fases as fases_func
import data

life = 100

print('You just robbed a bank, you are now the most wanted person in US! SURVIVE')
input("Press enter to start the game.")
i = 1
for fase in data.fases:
    chosen_action, life = fases_func.dofase(i, data.fases, data.enemies, life, data.actions)
    data.actions.pop(chosen_action)
    i += 1
