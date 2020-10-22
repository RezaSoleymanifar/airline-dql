#This code simulates a conventional hub and spoke network

import numpy as np


n_nodes = 4
n_legs = 4
arrival_probs = []
cancel_probs = []
no_show_probs = []
leg_caps = []
n_jrnys = 16
jrny_fares = []
no_show_sum = []
cancel_sum = []

state = np.zeros(n_jrnys)

