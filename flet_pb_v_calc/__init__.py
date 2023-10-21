"""Flet Progress Bar Value Calculator."""


from typing import Union


def calculate_value(current: Union[int, float], maximal: Union[int, float], minimal: Union[int, float]) -> float:
    """
    Calculate progress bar value.

    `current` - Current progress bar value.

    `maximal` - Maximal progress bar value.

    `minimal` - Minimal progress bar value.
    """
    current, maximal, minimal = float(current), float(maximal), float(minimal)

    if current > maximal: return maximal
    elif current < minimal: return minimal
    elif minimal >= maximal: return current
    elif current == 0.0: return current
    else: return current / maximal
