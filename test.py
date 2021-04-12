import math
import random

from compas.geometry import Pointcloud
from compas.geometry import Translation, Rotation
from compas.geometry import Box

cloud = Pointcloud.from_bounds(10, 5, 3, 100)
box = Box.from_width_height_depth(2, 2, 2)

T = Translation.from_vector([5, 2.5, 1.5])
R = Rotation.from_axis_and_angle([0, 0, 1], random.random() * math.pi)

box.transform(T * R)

colors = []
for point in cloud:
    if box.contains(point):
        color = 1, 0, 0
    else:
        color = 0, 0, 1
    colors.append(color)
