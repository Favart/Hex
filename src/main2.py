from main.training.q_learning import Q_learning
import pprint
import json

import matplotlib.pyplot as plt

q_learning = Q_learning(11)
q_learning.start(10)
with open('Q_table.txt', 'w') as json_file:
    json.dump(q_learning.Q_table, json_file)
#q_learning = Q_learning(11,epsilon=0.2,Q=q_learning.Q_table)
#q_learning.start(10000)
#wins, losts = q_learning.test(1000)
#print("Nombre de victoires: ",wins)
#print("Nombre de défaites: ",losts)
#print("Ratio de victoires: ",wins/(wins+losts))
# table = q_learning.Q_table
# pprint.pprint(table)
# pprint.pprint(table['[[0. 0. 0.]\n [0. 1. 0.]\n [0. 0. 0.]]'])
# print(sum(q_learning.all_penalties[500:])/len(q_learning.all_penalties[500:]))