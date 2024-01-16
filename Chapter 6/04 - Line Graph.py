#Exercise 4 - Line Graph 
import matplotlib.pyplot as plt
plt.title('Solid & Dotted Line')

#Draw a line in a diagram from position (1, 2) to position (6, 8)
solid_x = [1, 6]
solid_y = [2, 8]
plt.plot(solid_x, solid_y, label='Solid Line')

#Draw a dotted line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10)
dotted_x = [1, 2, 6, 8]
dotted_y = [3, 8, 1, 10]
plt.plot(dotted_x, dotted_y, 'r--', label='Dotted Line')

plt.legend()
plt.show()