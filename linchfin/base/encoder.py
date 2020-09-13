import numpy as np

from .dataclasses.value_types import Metric


class Encoder:
    @classmethod
    def encode(cls, data: Metric) -> Metric:
        raise NotImplementedError("Need to be implemented")


class EuclideanEncoder(Encoder):
    @classmethod
    def encode(cls, data: Metric) -> Metric:
        encoded_value = np.sqrt(np.divide((1 - data.value), 2))
        return Metric(name='dist', value=encoded_value)
