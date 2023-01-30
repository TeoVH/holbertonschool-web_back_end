#!/usr/bin/env python3
"""
function make_multiplier that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier
    """

    def fn(n: float):
        return n * multiplier

    return fn
