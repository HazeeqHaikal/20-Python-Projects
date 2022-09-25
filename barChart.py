import matplotlib.pyplot as plt

left = [1, 2, 3, 4, 5]
height = [10, 11, 23, 25, 15]

tickLabel = ['one', 'two', 'three', 'four', 'five']
plt.bar(left, height, tick_label = tickLabel, width = 0.8, color = ['grey', 'lightgrey'])


plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Bar Chart')

plt.show()