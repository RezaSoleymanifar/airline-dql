#This code simulates a conventional hub and spoke network

import numpy as np


n_nodes = 4
n_legs = 4
n_jrnys = 16
arrival_probs = []
cancel_probs = []
no_show_probs = []

leg_caps = []

jrny_fares = []
no_show_sum = []
cancel_sum = []

state = np.zeros(n_jrnys)

def gen_event(arrival_probs, cancel_probs):
    no_vent_prob = 1 - (np.sum(arrival_probs), np.sum(cancel_probs))
    probs = []
    # make a matix of event indices and change to state
    elements = [1.1, 2.2, 3.3]
    probabilities = [0.2, 0.5, 0.3]
    event = np.random.choice(elements, 10, p=probabilities)
    return event
