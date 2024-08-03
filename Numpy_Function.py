from numpy import *

arr = array([1, 2, 3, 4, 5])
print(arr, "\n")

arg = arange(1, 11, 2)
print(arg, "\n")

zero = zeros((2, 2), dtype=int)
print(zero, "\n")

one = ones(5, dtype=int)
print(one, "\n")

ran = random.random((3, 3))
print(ran, "\n")

ranint = random.randint(1, 10, (2, 2))
print(ranint, "\n")

ful = full((2, 3), 5)
print(ful, "\n")

eye = eye(3, dtype=int)
print(eye, "\n")

lin = linspace(1, 10, 5)
print(lin, "\n")

log = logspace(1, 10, 5)
print(log, "\n")

til = tile([1, 2, 3], (2, 3))
print(til)
