import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D figure
fig = plt.figure()

# Point
ax_point = fig.add_subplot(221, projection='3d')
point = np.array([1, 2, 3])
ax_point.scatter(point[0], point[1], point[2], color='red')
ax_point.set_xlabel('X')
ax_point.set_ylabel('Y')
ax_point.set_zlabel('Z')
ax_point.set_title('Point')

# Line Segment
ax_line = fig.add_subplot(222, projection='3d')
start = np.array([1, 1, 1])
end = np.array([4, 4, 4])
ax_line.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], color='green')
ax_line.set_xlabel('X')
ax_line.set_ylabel('Y')
ax_line.set_zlabel('Z')
ax_line.set_title('Line Segment')

# Plane
ax_plane = fig.add_subplot(223, projection='3d')
xx, yy = np.meshgrid(range(-5, 6), range(-5, 6))
zz = 2 * xx + 3 * yy - 4
ax_plane.plot_surface(xx, yy, zz, alpha=0.5, color='blue')
ax_plane.set_xlabel('X')
ax_plane.set_ylabel('Y')
ax_plane.set_zlabel('Z')
ax_plane.set_title('Plane')

# Sphere
ax_sphere = fig.add_subplot(224, projection='3d')
center = np.array([0, 0, 0])
radius = 3
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = radius * np.outer(np.cos(u), np.sin(v)) + center[0]
y = radius * np.outer(np.sin(u), np.sin(v)) + center[1]
z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
ax_sphere.plot_surface(x, y, z, alpha=0.5, color='orange')
ax_sphere.set_xlabel('X')
ax_sphere.set_ylabel('Y')
ax_sphere.set_zlabel('Z')
ax_sphere.set_title('Sphere')

# Adjust the layout
plt.tight_layout()

# Show the plots
plt.show()
