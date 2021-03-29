#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt



# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:

     return np.linspace(start=-1.3, stop=2.5, num=64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:

    return np.array([(np.sqrt(coord[0]**2 + coord[1]**2), np.arctan2(coord[1], coord[0])) for coord in cartesian_coordinates])

    # coord_polaire = []
    # for coord in cartesian_coordinates:
    #     x = coord[0]
    #     y = coord[1]
    #     rayon = np.sqrt(x**2 + y**2)
    #     angle = np.arctan2(y, x)
    #     coord_polaire.append((rayon, angle))
    #
    # return np.array(coord_polaire)


def find_closest_index(values: np.ndarray, number: float) -> int:

    return np.abs(values - number).argmin()


def creat_plot():
    x = np.linspace(start=-1, stop=1, num=250)
    y = x**2 * np.sin(1 / x**2) + x

    plt.scatter(x, y, label="Ca represente y")
    plt.xlabel("axe des x")
    plt.ylabel("axe des y")
    plt.title("exercice chap 10")
    plt.xlim((-2, 2))
    plt.legend()
    plt.show()


def estimation_pi(iteration: int=5000):
    x_inside_circle = []
    x_outside_circle = []
    y_inside_circle = []
    y_outside_circle = []

    for i in range(iteration):
        x = np.random.random()
        y = np.random.random()

        if np.sqrt(x**2 + y**2) <= 1.0:
            x_inside_circle.append(x)
            y_inside_circle.append(y)
        else:
            x_outside_circle.append(x)
            y_outside_circle.append(y)

    plt.scatter(x_inside_circle, y_inside_circle, label="inside circle")
    plt.scatter(x_outside_circle, y_outside_circle, label="outside circle")
    plt.xlabel("axe des x")
    plt.ylabel("axe des y")
    plt.title("estimation valeur de pi")
    plt.legend()
    plt.show()

    return len(x_inside_circle) / iteration * 4


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    # print(linear_values())
    # print(coordinate_conversion(cartesian_coordinates=np.array([(15, 30), (-7, 10)])))
    # print(find_closest_index(np.array([10, 15, 20, 12, 13]), 11.1))
    # creat_plot()
    # print(estimation_pi(100000))
