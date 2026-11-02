# Converted from tasks.ipynb
import matplotlib.pyplot as plt
import numpy as np

# ---------- Task 1 ----------
x = np.linspace(-10, 10, 100)
y = x**2 - 4*x + 4
plt.plot(x,y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Basic parabola")
plt.grid()
plt.show()
plt.close("all")


# ---------- Task 2 ----------
x = np.linspace(0, 2*np.pi, 100)

plt.plot(x, np.sin(x), 'r--3', label="sin(x)")
plt.plot(x, np.cos(x), 'b-.p' , label="cos(x)")

plt.title('Sine and Cosine Plot')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
plt.close("all")


# ---------- Task 3 ----------
x = np.linspace(-10,10, 1000)

plt.subplot(2,2,1)
plt.plot(x**3, 'g-.h', label='x^3')
plt.grid()
plt.legend()
plt.title("1")

plt.subplot(2,2,2)
plt.plot(np.sin(x), 'r-*', label='sin(x)')
plt.legend()
plt.grid()
plt.title("2")


plt.subplot(2,2,3)
plt.plot(np.exp(x), 'b--s', label='e^2')
plt.legend()
plt.grid()
plt.title("3")


plt.subplot(2,2,4)
plt.plot(np.log(x+1), 'y:p', label='log(x+1)')
plt.legend()
plt.grid()
plt.title("4")

plt.show()
plt.close("all")


# ---------- Task 4 ----------
x = np.random.uniform(0, 10, size=(100))
y = np.random.uniform(0, 10, size=(100))
c = np.random.randint(0, 100, 100)
s = 10 * np.random.randint(100, size=(100))


plt.scatter(x, y, s=s, c=c, cmap='nipy_spectral', alpha=0.5)
plt.colorbar()
plt.title("Random points")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
plt.close("all")


# ---------- Task 5 ----------
x = np.random.normal(0, 1, 1000)
plt.hist(x, bins=30, label='histogram', alpha=0.5, edgecolor='b')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Random data of histogram with mean and standard deviation")

plt.show()
plt.close("all")


# ---------- Task 6 ----------
fig = plt.figure()
ax = plt.axes(projection="3d")

x = np.linspace(-5,5, 300)
y = np.linspace(-5,5, 300)
xx, yy = np.meshgrid(x, y)

z = np.cos(xx**2 + yy**2)
surf = ax.plot_surface(xx,yy,z, cmap='viridis', rstride=1, cstride=1)
fig.colorbar(surf, shrink=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title("$f(x, y) = cos(x² + y²)$")

plt.show()
plt.close("all")


# ---------- Task 7 ----------
categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = np.array([200, 150, 250, 175, 225])
colors = ['red', 'blue', 'green', 'black', 'yellow']

plt.barh(categories, values, label='data', color=colors)
plt.title("Product data")
plt.legend()
plt.xlabel('values')
plt.ylabel('categories')

plt.show()
plt.close("all")


# ---------- Task 8 ----------
periods = ['T1', 'T2', 'T3', 'T4']
values1 = np.random.randint(5, 30, 4)
values2 = np.random.randint(5, 30, 4)
values3 = np.random.randint(5, 30, 4)

plt.bar(periods, values1, label='Category A', color='blue',)
plt.bar(periods, values2, bottom=values1, label='Category B', color='red')
plt.bar(periods, values3, bottom=values1+values2, label='Category C', color='green')

plt.title('Stacked Bar Chart')
plt.xlabel('Time Periods')
plt.ylabel('Values')
plt.legend()
plt.show()
plt.close("all")