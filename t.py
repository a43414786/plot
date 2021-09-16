import pickle
import matplotlib.pyplot as plt
with open("losschange.pickle", 'rb') as f:
    data = pickle.load(f)
epoch = []
trainLoss = []
valLoss = []
valerr = []
for i in data:
    epoch.append(i['epoch'])
    trainLoss.append(i['trainLoss'])
    valLoss.append(i['valLoss'])
    valerr.append(i['valerr'])
    print(i)

x = epoch     # Step 1
y = trainLoss     # Step 1
fig = plt.figure()            # Step 2
ax = fig.add_subplot(111)     # Step 3
plt.plot(x, y, color='blue', linewidth=2, marker='o') # Step 3&4
plt.xlim(1, 5.5)                   
plt.savefig('workflow.png')   # Step 5
plt.show() 

