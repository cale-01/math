import matplotlib.pyplot as plt
import numpy as np

# 1. Mandelbrot Set
def mandelbrot_set(real_min, real_max, imag_min, imag_max, width, height, max_iter):
    real_vals = np.linspace(real_min, real_max, width)
    imag_vals = np.linspace(imag_min, imag_max, height)
    mandelbrot = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            c = complex(real_vals[i], imag_vals[j])
            z = complex(0, 0)
            iteration = 0

            while abs(z) <= 2 and iteration < max_iter:
                z = z * z + c
                iteration += 1

            mandelbrot[i, j] = iteration

    plt.figure(figsize=(10, 10))
    plt.imshow(mandelbrot.T, cmap='hot', extent=[real_min, real_max, imag_min, imag_max])
    plt.title("Mandelbrot Set")
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    plt.show()


# 2. Julia Set
def julia_set(real_min, real_max, imag_min, imag_max, width, height, max_iter, c):
    real_vals = np.linspace(real_min, real_max, width)
    imag_vals = np.linspace(imag_min, imag_max, height)
    julia = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            z = complex(real_vals[i], imag_vals[j])
            iteration = 0

            while abs(z) <= 2 and iteration < max_iter:
                z = z * z + c
                iteration += 1

            julia[i, j] = iteration

    plt.figure(figsize=(10, 10))
    plt.imshow(julia.T, cmap='hot', extent=[real_min, real_max, imag_min, imag_max])
    plt.title("Julia Set")
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    plt.show()


# 3. Sierpinski Triangle
def sierpinski_triangle(x, y, size, depth):
    if depth == 0:
        triangle = plt.Polygon([[x, y], [x + size, y], [x + size / 2, y + size]], fc='b')
        plt.gca().add_patch(triangle)
    else:
        sierpinski_triangle(x, y, size / 2, depth - 1)
        sierpinski_triangle(x + size / 2, y, size / 2, depth - 1)
        sierpinski_triangle(x + size / 4, y + size / 2, size / 2, depth - 1)


def plot_sierpinski_triangle(size, depth):
    plt.figure(figsize=(10, 10))
    sierpinski_triangle(0, 0, size, depth)
    plt.title("Sierpinski Triangle")
    plt.axis('equal')
    plt.show()


# 4. Koch Snowflake
def koch_snowflake(x, y, size, depth):
    if depth == 0:
        x_end = x + size * np.cos(0)
        y_end = y + size * np.sin(0)
        plt.plot([x, x_end], [y, y_end], 'b')
    else:
        size /= 3
        x1 = x + size * np.cos(0)
        y1 = y + size * np.sin(0)
        x2 = x1 + size * np.cos(-np.pi / 3)
        y2 = y1 + size * np.sin(-np.pi / 3)
        x3 = x2 + size * np.cos(np.pi / 3)
        y3 = y2 + size * np.sin(np.pi / 3)
        koch_snowflake(x, y, size, depth - 1)
        koch_snowflake(x1, y1, size, depth - 1)
        koch_snowflake(x2, y2, size, depth - 1)
        koch_snowflake(x3, y3, size, depth - 1)


def plot_koch_snowflake(size, depth):
    plt.figure(figsize=(10, 10))
    koch_snowflake(-size / 2, 0, size, depth)
    plt.title("Koch Snowflake")
    plt.axis('equal')
    plt.show()


# 5. Dragon Curve
def dragon_curve(x, y, length, angle, depth):
    if depth == 0:
        x_end = x + length * np.cos(angle)
        y_end = y + length * np.sin(angle)
        plt.plot([x, x_end], [y, y_end], 'b')
    else:
        x_mid = x + length / 2 * np.cos(angle)
        y_mid = y + length / 2 * np.sin(angle)
        angle += np.pi / 4
        dragon_curve(x, y, length / np.sqrt(2), angle, depth - 1)
        dragon_curve(x_mid, y_mid, length / np.sqrt(2), angle - np.pi / 2, depth - 1)


def plot_dragon_curve(length, depth):
    plt.figure(figsize=(10, 10))
    dragon_curve(0, 0, length, 0, depth)
    plt.title("Dragon Curve")
    plt.axis('equal')
    plt.show()


# 6. Sierpinski Carpet
def sierpinski_carpet(x, y, size, depth):
    if depth == 0:
        rectangle = plt.Rectangle((x, y), size, size, fc='b')
        plt.gca().add_patch(rectangle)
    else:
        size /= 3
        sierpinski_carpet(x, y, size, depth - 1)
        sierpinski_carpet(x + size, y, size, depth - 1)
        sierpinski_carpet(x + 2 * size, y, size, depth - 1)
        sierpinski_carpet(x, y + size, size, depth - 1)
        sierpinski_carpet(x + 2 * size, y + size, size, depth - 1)
        sierpinski_carpet(x, y + 2 * size, size, depth - 1)
        sierpinski_carpet(x + size, y + 2 * size, size, depth - 1)
        sierpinski_carpet(x + 2 * size, y + 2 * size, size, depth - 1)


def plot_sierpinski_carpet(size, depth):
    plt.figure(figsize=(10, 10))
    sierpinski_carpet(0, 0, size, depth)
    plt.title("Sierpinski Carpet")
    plt.axis('equal')
    plt.show()


# 7. Barnsley Fern
# 7. Barnsley Fern
def barnsley_fern(iterations):
    x = 0
    y = 0
    x_coords = [x]
    y_coords = [y]
    for _ in range(iterations):
        r = np.random.uniform()
        if r <= 0.01:
            x = 0
            y = 0.16 * y
        elif r <= 0.86:
            new_x = 0.85 * x + 0.04 * y
            new_y = -0.04 * x + 0.85 * y + 1.6
            x = new_x
            y = new_y
        elif r <= 0.93:
            new_x = 0.20 * x - 0.26 * y
            new_y = 0.23 * x + 0.22 * y + 1.6
            x = new_x
            y = new_y
        else:
            new_x = -0.15 * x + 0.28 * y
            new_y = 0.26 * x + 0.24 * y + 0.44
            x = new_x
            y = new_y

        x_coords.append(x)
        y_coords.append(y)

    plt.figure(figsize=(10, 10))
    plt.scatter(x_coords, y_coords, s=0.2, c='green')
    plt.title("Barnsley Fern")
    plt.axis('off')
    plt.show()



# 8. Tree Fractal
def tree_fractal(x, y, length, angle, depth):
    if depth == 0:
        x_end = x + length * np.sin(angle)
        y_end = y + length * np.cos(angle)
        plt.plot([x, x_end], [y, y_end], 'b')
    else:
        x_end = x + length * np.sin(angle)
        y_end = y + length * np.cos(angle)
        plt.plot([x, x_end], [y, y_end], 'b')
        tree_fractal(x_end, y_end, length * 0.8, angle + np.pi / 6, depth - 1)
        tree_fractal(x_end, y_end, length * 0.8, angle - np.pi / 4, depth - 1)


def plot_tree_fractal(length, angle, depth):
    plt.figure(figsize=(10, 10))
    tree_fractal(0, 0, length, angle, depth)
    plt.title("Tree Fractal")
    plt.axis('equal')
    plt.show()


# 9. Levy C Curve
def levy_c_curve(x, y, length, angle, depth):
    if depth == 0:
        x_end = x + length * np.cos(angle)
        y_end = y + length * np.sin(angle)
        plt.plot([x, x_end], [y, y_end], 'b')
    else:
        angle -= np.pi / 4
        length /= np.sqrt(2)
        levy_c_curve(x, y, length, angle, depth - 1)
        x = x + length * np.cos(angle)
        y = y + length * np.sin(angle)
        angle += np.pi / 2
        levy_c_curve(x, y, length, angle, depth - 1)


def plot_levy_c_curve(length, angle, depth):
    plt.figure(figsize=(10, 10))
    levy_c_curve(0, 0, length, angle, depth)
    plt.title("Levy C Curve")
    plt.axis('equal')
    plt.show()


# 10. Peano Curve
def peano_curve(x, y, length, angle, depth):
    if depth == 0:
        x_end = x + length * np.cos(angle)
        y_end = y + length * np.sin(angle)
        plt.plot([x, x_end], [y, y_end], 'b')
    else:
        length /= 3
        peano_curve(x, y, length, angle, depth - 1)
        x = x + length * np.cos(angle)
        y = y + length * np.sin(angle)
        angle -= np.pi / 2
        peano_curve(x, y, length, angle, depth - 1)
        x = x + length * np.cos(angle)
        y = y + length * np.sin(angle)
        angle += np.pi / 2
        peano_curve(x, y, length, angle, depth - 1)
        x = x + length * np.cos(angle)
        y = y + length * np.sin(angle)
        peano_curve(x, y, length, angle, depth - 1)


def plot_peano_curve(length, depth):
    plt.figure(figsize=(10, 10))
    peano_curve(0, 0, length, 0, depth)
    plt.title("Peano Curve")
    plt.axis('equal')
    plt.show()


# Generate fractals
mandelbrot_set(-2.5, 1, -1.5, 1.5, 800, 800, 256)
julia_set(-1.5, 1.5, -1.5, 1.5, 800, 800, 256, -0.8 + 0.156j)
plot_sierpinski_triangle(600, 5)
plot_koch_snowflake(600, 5)
plot_dragon_curve(600, 10)
plot_sierpinski_carpet(600, 4)
barnsley_fern(50000)
plot_tree_fractal(400, -np.pi / 2, 10)
plot_levy_c_curve(600, 0, 10)
plot_peano_curve(600, 3)
