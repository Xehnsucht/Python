class Neuron:
    def __init__(self, w1, w2, b):
        self.w1 = w1
        self.w2 = w2
        self.b = b

    def act(self, x, y):
        return 1 if (x * self.w1 + y * self.w2 + self.b) > 0 else 0

n_and = Neuron(1,1,-1)
n_or = Neuron(1,1,-0.5)
n_notand = Neuron(-1,-1,2)

def xor(x,y):
    return n_and.act(
    n_or.act(x,y),
    n_notand.act(x,y)
)

print("x y xor")
[print(f"{x} {y} {xor(x, y)}") for x, y in [(1, 1), (0, 1), (1, 0), (0, 0)]]
