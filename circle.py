# Created at 2022/02/19

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
from matplotlib.ticker import MultipleLocator


def create_eclipse(a: float, b: float, center: tuple[float, float]) -> patches.Ellipse:
    e = patches.Ellipse(center, a * 2, b * 2, fill=False, ec="black")
    return e


def create_rectangle(left_down_pos: tuple[float, float]) -> patches.Rectangle:
    return patches.Rectangle(left_down_pos, width=1, height=1,
                             ec="#981200", fc="pink", alpha=0.5)


def ax_setting(ax: plt.Axes, a: float, b: float, center: tuple[float, float]) -> None:
    ax.set_aspect('equal')
    t = 1.1
    ax.set_xlim(center[0] - a * t, center[0] + a * t)
    ax.set_ylim(center[1] - b * t, center[1] + b * t)
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.grid(True)
    return


def trial1(x_array, y_array) -> list[tuple[int, int]]:
    x_ = np.sign(x_array) * np.abs(x_array).astype(int)
    y_ = np.sign(y_array) * np.abs(y_array).astype(int)
    return sorted(set(zip(x_, y_)))


def main1():
    center = (0, 0)
    a, b = 3, 6
    fig: plt.Figure = plt.figure(figsize=(a * 2, b * 2))
    ax: plt.Axes = fig.add_subplot(1, 1, 1)
    ax.add_patch(create_eclipse(a, b, center))
    ax_setting(ax, a, b, center)

    theta = np.linspace(0, np.pi / 2, 1000)
    x, y = a * np.cos(theta) + center[0], b * np.sin(theta) + center[1]
    t1 = trial1(x, y)
    for t in t1:
        ax.add_patch(create_rectangle(t))

    plt.show()
    plt.close(fig)

    return


if __name__ == '__main__':
    main1()
