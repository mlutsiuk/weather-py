from typing import List

import numpy as np
from fastapi import Query


def predict(pressures: List[int]):
    sum_x = float(np.sum(np.arange(1, len(pressures) + 1)))
    sum_y = float(np.sum(pressures))
    sum_x2 = float(np.sum(np.arange(1, len(pressures) + 1) ** 2))
    sum_xy = float(np.sum(np.arange(1, len(pressures) + 1) * pressures))

    a = (sum_x * sum_y - len(pressures) * sum_xy) / (sum_x ** 2 - len(pressures) * sum_x2)
    b = (sum_y - a * sum_x) / len(pressures)

    delta = (a * len(pressures) + b) - (a + b)

    return delta
