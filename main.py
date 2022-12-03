import matplotlib as mpl
import platform

from noise import NoiseHandler
from visualization import Visualizer

if __name__ == '__main__':
    if platform.system() != "Windows":
        mpl.use('macosx')

    noise_handler = NoiseHandler()
    noise_handler.genTer(100, (1.0, 3), (0.5, 5))

    visualizer = Visualizer()
    visualizer.set_data(noise_handler)
    visualizer.set_buttons()
    visualizer.plot_graph()

