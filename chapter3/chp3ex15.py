'''
Write a program that prints out the sine and cosine of the angles ranging from 0 to 345° in 15° increments. 
Each result should be rounded to 4 decimal places. Sample output is shown below:
0 --- 0.0 1.0
15 --- 0.2588 0.9659
30 --- 0.5 0.866
...
345 --- -0.2588 0.9659
'''
# import modules
from math import pi, sin, cos

# Loop from 0 to 360
for i in range(0, 360, 15):
    # Calculate the angle in radian
    radian = i * pi / 180

    # Print result
    print(f"{i} --- {round(sin(radian),4)} {round(cos(radian),4)}")
    