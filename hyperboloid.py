import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for the modified hyperboloid
a = 2  # Scaling along x-axis
b = 2  # Scaling along y-axis
c = 3  # Scaling along z-axis
thickness_factor = 30  # Controls the middle thickness effect

# Create a grid of points for the u (angle) and v (height) parameters
u = np.linspace(0, 2 * np.pi, 96)
v = np.linspace(-5, 5, 96)
u, v = np.meshgrid(u, v)

# Gaussian-like term for thickness modification
gaussian_thickness = 1 + thickness_factor * np.exp(-0.2 * v**2)

# Modified parametric equations for the hyperboloid of one sheet with thicker middle
x = a * gaussian_thickness * np.cosh(v) * np.cos(u)
y = b * gaussian_thickness * np.cosh(v) * np.sin(u)
z = c * np.sinh(v)
vertices = []
lines = []
colors = []
indices = []

# Adjust color gradients
redfirst = np.linspace(1, 0, 48)
#greenfirst = np.linspace(0, 1, 24)
#greenlast = np.linspace(1, 0, 24)
bluelast = np.linspace(0, 1, 48)
zeros = np.zeros(48)
green = np.zeros(96)
zeros24=np.zeros(24)
red = np.linspace(1, 0.5, 96)
#red = np.concatenate((redfirst, zeros))
blue = np.linspace(0.5, 1, 96)
#blue = np.concatenate((zeros, bluelast))
#green = np.concatenate((np.concatenate((zeros24, greenfirst)), np.concatenate((greenlast, zeros24))))



for i in range(95):
        for j in range(95):
            if j == 95:
                pointa = [x[i][j], y[i][j], z[i][j]]
                pointb = [x[i+1][j+1], y[i+1][j+1], z[i+1][j+1]]
                pointc = [x[i][0], y[i][0], z[i][0]]
                pointd = [x[i+1][0], y[i+1][0], z[i+1][0]]
            else:
                pointa = [x[i][j], y[i][j], z[i][j]]
                pointb = [x[i+1][j], y[i+1][j], z[i+1][j]]
                pointc = [x[i][j+1], y[i][j+1], z[i][j+1]]
                pointd = [x[i+1][j+1], y[i+1][j+1], z[i+1][j+1]]
            vertices.append([pointa, pointb, pointc])
            vertices.append([pointb, pointc, pointd])
            btmcol = [red[i], green[i], blue[i]]
            topcol = [red[i+1], green[i+1], blue[i+1]]
            colors.append([btmcol, topcol, btmcol])
            colors.append([topcol, btmcol, topcol])
            lines.append(tuple((pointa, pointb)))
            lines.append(tuple((pointb, pointc)))
            lines.append(tuple((pointa, pointc)))
            lines.append(tuple((pointb, pointd)))

for i in range(0, len(vertices)*3, 3):
    indices.append([i, i+1, i+2])
print("Total vertices:", len(vertices))
print("Total colors:", len(colors))
print("Total lines:", len(lines))
print("total indices:",len(indices))
print("First vertex:", vertices[0])
print("Last vertex:", vertices[-1])

with open("data.js", 'w') as file:
    file.write("var vertices = [\n")
    for i in vertices:
        for j in i:
            file.write(f'{j[0]}, {j[1]}, {j[2]},\n')
    file.write("];\n\nvar lines = [\n")
    for i in lines:
        for j in i:
            file.write(f'{j[0]}, {j[1]}, {j[2]},\n')
    file.write("];\n\nvar colors = [ \n")
    for i in colors:
        for j in i:
            file.write(f'{j[0]}, {j[1]}, {j[2]},\n')
    file.write("];\n\nvar indices = [\n")
    for i in indices:
        file.write(f'{i[0]}, {i[1]}, {i[2]},\n')
    file.write("];")



#print(len(vertices))
#for i in vertices:
    #print(len(i[0]))
    #for j in i:
    #    print(len(j))
    #print("\n")
"""







alright vertices are points on the thing. so basically each index on the collective
ganjil genap gak sih?
ITU VERTICES
print(f'{pointa[0]},{pointa[1]},{pointa[2]},\n{pointb[0]},{pointb[1]},{pointb[2]},\n{pointc[0]},{pointc[1]},{pointc[2]},\n\n')    
LINES


"""
# Plotting
u = np.linspace(0, 2 * np.pi, 24)
v = np.linspace(-5, 5, 24)
u, v = np.meshgrid(u, v)

# Parametric equations for the hyperboloid of one sheet
x = a * np.cosh(v) * np.cos(u)
y = b * np.cosh(v) * np.sin(u)
z = c * np.sinh(v)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Surface plot of the hyperboloid
ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)

# Add labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Hyperboloid of One Sheet')

# Set equal scaling for all axes
ax.set_xlim([-200, 200])
ax.set_ylim([-200, 200])
ax.set_zlim([-200, 200])

# Show the plot
#plt.show()
