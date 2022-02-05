from main.training.training import Q_learning
import pprint

q_learning = Q_learning(5)
q_learning.start(10000)
table = q_learning.Q_table
pprint.pprint({ state: table[state] for state in table if '[1. 1. 1. 1. 1.]' in state })