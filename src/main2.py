from main.training.q_learning import Q_learning
import pprint
import json

import matplotlib.pyplot as plt

q_learning = Q_learning(n=3)
q_learning.start(epochs=100000)
#q_learning = Q_learning(5,epsilon=0.2,Q=q_learning.Q_table)
#q_learning.start(50000)

wins, losts = q_learning.test(1000)
print("Nombre de victoires: ",wins)
print("Nombre de défaites: ",losts)
print("Ratio de victoires: ",wins/(wins+losts))

#with open('Q_table.txt', 'w') as json_file:
#    json.dump(q_learning.Q_table, json_file)
