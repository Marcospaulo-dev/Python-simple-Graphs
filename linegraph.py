import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [3, 5, 2, 4, 7, 5, 8]

plt.plot(x, y, color='red', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='black', markersize=8)

plt.ylim(0, 10)
plt.xlim(0, 10)

plt.xlabel('X - Data Label')
plt.ylabel('Y - Data Label')
plt.title('Title')
plt.grid(linestyle='dotted', axis='y')
plt.grid(linestyle='dotted', axis='x')
plt.show()
