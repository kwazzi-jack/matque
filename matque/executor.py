from abc import ABC, abstractmethod


class MatqueObject(ABC):
    def __init__(self, symbol, name=None) -> None:
        self.symbol = symbol
        if name is not None:
            self.name = name
        else:
            self.name = symbol
        super().__init__()

    def wrap(self):
        return Expression(LPAREN, self, RPAREN)

    def __str__(self):
        return str(self.symbol)

    def convert(obj):
        if isinstance(obj, (int, float)):
            return Number(obj)
        elif isinstance(obj, str):
            return Variable(obj)
        else:
            raise NotImplementedError(
                f"Unknown term '{obj}'. Not supported or not implemented."
            )

    def __add__(self, other):
        if not isinstance(other, MatqueObject):
            other = MatqueObject.convert(other)

        return Expression(self, ADD, other)

    def __radd__(self, other):
        if not isinstance(other, MatqueObject):
            other = MatqueObject.convert(other)

        return Expression(other, ADD, self)

    def __sub__(self, other):
        if not isinstance(other, MatqueObject):
            other = MatqueObject.convert(other)

        return Expression(self, SUB, other.wrap())

    def __rsub__(self, other):
        if not isinstance(other, MatqueObject):
            other = MatqueObject.convert(other)

        return Expression(other, SUB, self.wrap())

    def __mul__(self, other):
        if not isinstance(other, MatqueObject):
            other = MatqueObject.convert(other)

        return Expression(self.wrap(), MUL, other.wrap())

    def __rmul__(self, other):
        if not isinstance(other, MatqueObject):
            other = MatqueObject.convert(other)

        return Expression(other.wrap(), MUL, self.wrap())

    def __truediv__(self, other):
        if not isinstance(other, MatqueObject):
            other = MatqueObject.convert(other)

        return Expression(self.wrap(), DIV, other.wrap())

    def __rtruediv__(self, other):
        if not isinstance(other, MatqueObject):
            other = MatqueObject.convert(other)

        return Expression(other.wrap(), DIV, self.wrap())


class Variable(MatqueObject):
    def __init__(self, symbol, name=None) -> None:
        super().__init__(symbol, name)


class Operator(MatqueObject):
    def __init__(self, symbol, name=None) -> None:
        super().__init__(symbol, name)


class Function(Operator):
    def __init__(self, func, name=None) -> None:
        self.func = func
        super().__init__(func, name)

    def __call__(self, arg):
        if not isinstance(arg, MatqueObject):
            arg = MatqueObject.convert(arg)

        return Expression(self, arg.wrap())


class Number(MatqueObject):
    def __init__(self, value, name=None) -> None:
        self.value = value
        super().__init__(value, name)

    def __str__(self):
        return f"{self.value}"


class Expression(MatqueObject):
    def __init__(self, *expression, name=None) -> None:
        new_expression = []
        for expr in expression:
            if isinstance(expr, Expression):
                new_expression += expr.expression
            else:
                new_expression.append(expr)

        self.expression = new_expression
        super().__init__(new_expression, name)

    def __str__(self):
        return " ".join(map(str, self.expression))


class Statement:
    def __init__(self, left, right, rel_op) -> None:
        self.left = left
        self.right = right
        self.rel_op = rel_op

    def to_latex(self) -> str:
        return f"{self.left} {self.rel_op} {self.right}"

    def __str__(self) -> str:
        return f"Statement('{self.left}', '{self.rel_op}', '{self.right}')"


class Equality(Statement):
    def __init__(self, left, right) -> None:
        super().__init__(left, right, "=")


class Inequality(Statement):
    def __init__(self, left, sign, right) -> None:
        super().__init__(left, right, sign)


ADD = Operator("+")
SUB = Operator("-")
MUL = Operator("", name="MUL")
DIV = Operator("÷")
LPAREN = Operator("(")
RPAREN = Operator(")")

if __name__ == "__main__":
    x = Variable("x")
    one = Number("1")
    f = Function("f")
    g = Function("g")
    y = Variable("y")
    eq1 = Equality(g(y), (f("x") + 1.0) / "y")

    print(eq1.right)
    print(eq1.to_latex())
