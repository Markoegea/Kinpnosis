"""
A Neural Network is just a collection of layers.
It behaves a lot like a layer itself, although
we're not going to make it one.
"""

from typing import Sequence, Iterator, Tuple

from kinpnosis.tensor import Tensor
from kinpnosis.layers import Layer

class NeuralNet:
    def __init__(self, layers: Sequence[Layer]) -> None:
        self.layers = layers
    
    def forward(self, inputs: Tensor) -> Tensor:
        for layer in self.layers:
            inputs = layer.forward(inputs)
        return inputs

    def backward(self, grad: Tensor) -> Tensor:
        for layer in reversed(self.layers):
            grad = layer.backward(grad)
        return grad
    
    def params_and_grads(self) -> Iterator[Tuple[Tensor, Tensor]]:
        for layer in self.layers:
            for name, param in layer.params.items():
                grad = layer.grads[name]
                yield param, grad

    def zero_grad(self) -> None:
        for layer in self.layers:
            layer.zero_grad()