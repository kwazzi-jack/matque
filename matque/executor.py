from abc import ABC, abstractmethod


class MatqueObject(ABC):
    def __init__(self, symbol, name=None) -> None:
        self.symbol = symbol
        if name is not None:
            self.name = name
        else:
            self.name = symbol
        super().__init__()

    def __str__(self):
        return str(self.symbol)


class Variable(MatqueObject):
    def __init__(self, symbol, name=None) -> None:
        super().__init__(symbol, name)


class Operator(MatqueObject):
    def __init__(self, symbol, name=None) -> None:
        super().__init__(symbol, name)


class Function(Operator):
    def __init__(self, func, arg, name=None) -> None:
        self.arg = arg
        self.func = func
        super().__init__(func, name)

    def __str__(self):
        return f"{self.func}({self.arg})"


class Number(MatqueObject):
    def __init__(self, value, name=None) -> None:
        self.value = value
        super().__init__(value, name)

    def __str__(self):
        return f"{self.value}"


class Expression(MatqueObject):
    def __init__(self, *expression, name=None) -> None:
        self.expression = expression
        super().__init__(expression, name)

    def __str__(self):
        return " ".join(map(str, self.expression))


class Statement:
    def __init__(self, left, right, rel_op="=") -> None:
        self.left = left
        self.right = right
        self.rel_op = rel_op

    def to_latex(self) -> str:
        return f"{self.left} {self.rel_op} {self.right}"

    def __str__(self) -> str:
        return f"Statement('{self.left}', '{self.rel_op}', '{self.right}')"


if __name__ == "__main__":
    x = Variable("x")
    one = Number("1")
    print(x)
    f = Function("f", x)
    plus = Operator("+")
    y = Variable("y")
    eq1 = Statement(y, Expression(f, plus, one), rel_op=">")
    print(eq1)
    print(eq1.to_latex())
