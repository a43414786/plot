import pickle
import matplotlib.pyplot as plt
with open("losschange.pickle", 'rb') as f:
    data = pickle.load(f)
for i in data:
    print(i)