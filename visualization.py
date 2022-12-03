from random import random
from typing import Any, List

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

import solution
from noise import NoiseHandler
from matplotlib.widgets import Button

from solution_bfs import BFS_Handler
from solution_dfs import DFS_Handler


class Visualizer:
    X = Y = Z = None
    x_data = y_data = None
    start = end = None
    noise = None
    axis = button_ter = button_bfs = button_dfs = None
    bfs_handler, dfs_handler = BFS_Handler(), DFS_Handler()

    def __init__(self, x_data=None, y_data=None):
        self.axis = plt.axes(projection="3d")

        self.X = x_data
        self.Y = y_data

    def set_data(self, noise_handler: NoiseHandler) -> None:
        x_data, y_data, Z = noise_handler.convert_matplotlib()
        size = len(noise_handler.getTer())
        self.start = (int(random() * size), int(random() * size))
        self.end = (int(random() * size), int(random() * size))

        self.noise = noise_handler
        self.Z = np.array(Z)

        self.X, self.Y = np.meshgrid(x_data, y_data)
        self.x_data = x_data
        self.y_data = y_data

    def set_buttons(self) -> None:
        self.button_ter = Button(plt.axes([0.01, 0.01, 0.1, 0.1]), "Generate Terrain")
        self.button_bfs = Button(plt.axes([0.11, 0.01, 0.1, 0.1]), "Generate Path via BFS")
        self.button_dfs = Button(plt.axes([0.21, 0.01, 0.1, 0.1]), "Generate Path via DFS")

        self.button_ter.on_clicked(self.get_new_terrain)
        self.button_bfs.on_clicked(self.get_path_bfs)
        self.button_dfs.on_clicked(self.get_path_dfs)

    def get_new_terrain(self, event) -> None:
        self.axis.cla()

        self.noise.genTerAgain()

        self.set_data(self.noise)
        self.plot_graph()

        plt.draw()

    def get_path_bfs(self, event) -> None:
        head = self.bfs_handler.calculate_path(self.start, self.end, self.noise.getTer())
        self.plot_line('blue', *self.bfs_handler.break_down_linked_list(head, self.noise.getTer()))

    def get_path_dfs(self, event) -> None:
        head = self.dfs_handler.calculate_path(self.start, self.end, self.noise.getTer())
        self.plot_line('green', *self.dfs_handler.break_down_linked_list(head, self.noise.getTer()))

    def plot_graph(self) -> None:
        self.axis.set_title("Terrain Map")
        self.axis.set_xlabel("X Position")
        self.axis.set_ylabel("Y Position")
        self.axis.set_zlabel("Elevation")

        self.axis.plot_surface(self.X, self.Y, self.Z, cmap="cividis", zorder=0, alpha=0.3, antialiased=True)
        # self.axis.plot_wireframe(self.X, self.Y, self.Z, rstride=5, cstride=5, cmap="cividis", zorder=0)
        # print(self.X)
        # self.axis.plot_trisurf(self.X.flatten(), self.Y.flatten(), self.Z.flatten(), cmap="cividis", edgecolor='none')

        self.axis.scatter(self.start[1], self.start[0], self.noise.getTer()[self.start[0]][self.start[1]],
                          c='green', s=100, zorder=10)
        self.axis.scatter(self.end[1], self.end[0], self.noise.getTer()[self.end[0]][self.end[1]], c='red', s=100,
                          zorder=10)

        plt.show()

    def plot_line(self, color: str, x_data: List[int], y_data: List[int], z_data: List[int]) -> None:
        self.axis.plot3D(y_data, x_data, z_data, color)

# Visualization of Line
# axis = plt.axes(projection="3d")
# x_data = np.arange(0, 5, (0.1))
# y_data = np.arange(0, 5, (0.1))
# z_data = x_data * y_data
#
# axis.plot(x_data, y_data, z_data)
# plt.show()
