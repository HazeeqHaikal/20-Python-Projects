import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 8]
y1 = [1, 2, 5, 6, 7]

plt.plot(x1, y1, color="blue", linestyle="dashed", linewidth=1.5, marker="o", markerfacecolor='black', markersize=8, label='First Line')
plt.ylim(1, 10)
plt.xlim(1, 10)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Graph Plotter')

plt.show()