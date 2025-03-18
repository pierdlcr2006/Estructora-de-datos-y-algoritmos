import matplotlib.pyplot as plt

data = {10:0.3,100:0.5,1000:0.8}
plt.scatter(x=data.keys(),y=data.values(), color="Blue")
plt.title("Loops")
plt.xlabel("Iteractions")
plt.ylabel("Time(s)")
plt.show()