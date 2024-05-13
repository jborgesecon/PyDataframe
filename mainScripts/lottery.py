import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Image size (pixels)
width, height = (600, 400)

# Plot window
re_min, re_max = -2, 2
im_min, im_max = -1, 1

image = np.zeros((width, height))

for x in range(width):
    for y in range(height):
        # Convert pixel coordinate to complex number
        c = complex(re_min + (x / width) * (re_max - re_min),
                    im_min + (y / height) * (im_max - im_min))
        # Compute the number of iterations
        m = mandelbrot(c, 256)
        # The color depends on the number of iterations
        color = 255 - int(m * 255 / 256)
        # Plot the point
        image[x, y] = color

plt.imshow(image.T, cmap='hot', extent=(re_min, re_max, im_min, im_max))
plt.title('Mandelbrot Set')
plt.xlabel('Re')
plt.ylabel('Im')
plt.show()
