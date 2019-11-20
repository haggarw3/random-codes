'''PLOTTING ON SECONDARY AXIS'''

import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)
fig, ax1 = plt.subplots()
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color='red')
ax1.plot(t, data1, color='red')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('sin', color='b')
ax2.plot(t, data2, color='b')
ax2.tick_params(axis='y')
plt.show()


