import numpy as np

A = np.array([2.493, 0.911])
print("tehtävä 1.1:")
for i in A:
    print(np.degrees(i).round(1))

print("")

B = np.array([137.7, 62.3])
print("tehtävä 1.2:")
for i in B:
    print(np.radians(i).round(3))

print("")

C = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
print("tehtävä 1.3:")
for i in C:
    print(np.radians(i).round(3))

print("")

print("tehtävä 2.1:")

print(np.hypot(1.6, 2.3).round(2))