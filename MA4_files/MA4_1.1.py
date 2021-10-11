# MA4_1
# Niklas Eckert Elfving

import random
import matplotlib.pyplot as plt
from math import pi

n = input('Give number of points: ')
circle = [] 
square = []

for i in range(int(n)):
        coordinate = [random.uniform(-1, 1), random.uniform(-1, 1)]
        if coordinate[0]**2 + coordinate[1]**2 <= 1:
            circle.append(coordinate)
        else:
            square.append(coordinate)

pi_approx = 4*len(circle)/(len(circle)+len(square))

print(f'Number of points in cirlce : {len(circle)}')
print(f'Pi exact                   : {pi}')
print(f'Pi approx                  : {pi_approx}')

x_circle = []
y_circle = []
for n in circle:
    x_circle.append(n[0])
    y_circle.append(n[1])
plt.plot(x_circle, y_circle, 'o', color = 'red')

x_square = []
y_square = []
for n in square:
    x_square.append(n[0])
    y_square.append(n[1])
plt.plot(x_square, y_square, 'o', color = 'blue')

plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.title('Coordinates')
plt.legend(['in_circle', 'in_square'], loc = 'upper right')
#plt.savefig('100000.png')
plt.show() 