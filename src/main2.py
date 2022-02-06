from main.training.q_learning import Q_learning
import pprint

import matplotlib.pyplot as plt

q_learning = Q_learning(3)
q_learning.start(10000)
q_learning = Q_learning(3,epsilon=0.5,Q=q_learning.Q_table)
q_learning.start(1000)
table = q_learning.Q_table
pprint.pprint(table)
print(sum(q_learning.all_penalties[500:])/len(q_learning.all_penalties[500:]))