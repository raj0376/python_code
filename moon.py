import numpy as np
import matplotlib.pyplot as plt
theta_degrees=np.linspace(0, 113*360, 10000)
theta_radians = np.deg2rad(theta_degrees)
z=np.exp(theta_radians * 1j) + np.exp(np.pi*theta_radians * 1j)
x=np.real(z)
y=np.imag(z)

plt.figure(figsize = (10,10))
plt.plot(x,y,color = 'white', linewidth = 0.5)
plt.gca().set_facecolor('black')
plt.gca().set_aspect('equal')
plt.grid(False)
plt.xlim(-2.5,2.5)
plt.ylim(-2.5,2.5)

plt.show()