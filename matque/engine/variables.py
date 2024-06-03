from matque.engine.core import Node

_GREEK = {
    "alpha": (r"\alpha", "α"),
    "beta": (r"\beta", "β"),
    "gamma": (r"\gamma", "γ"),
    "delta": (r"\delta", "δ"),
    "epsilon": (r"\epsilon", "ε"),
    "zeta": (r"\zeta", "ζ"),
    "eta": (r"\eta", "η"),
    "theta": (r"\theta", "θ"),
    "iota": (r"\iota", "ι"),
    "kappa": (r"\kappa", "κ"),
    "lambda": (r"\lambda", "λ"),
    "mu": (r"\mu", "μ"),
    "nu": (r"\nu", "ν"),
    "xi": (r"\xi", "ξ"),
    "omicron": (r"\omicron", "ο"),
    "pi": (r"\pi", "π"),
    "rho": (r"\rho", "ρ"),
    "sigma": (r"\sigma", "σ"),
    "tau": (r"\tau", "τ"),
    "upsilon": (r"\upsilon", "υ"),
    "phi": (r"\phi", "φ"),
    "chi": (r"\chi", "χ"),
    "psi": (r"\psi", "ψ"),
    "omega": (r"\omega", "ω"),
    "Alpha": (r"\Alpha", "Α"),
    "Beta": (r"\Beta", "Β"),
    "Gamma": (r"\Gamma", "Γ"),
    "Delta": (r"\Delta", "Δ"),
    "Epsilon": (r"\Epsilon", "Ε"),
    "Zeta": (r"\Zeta", "Ζ"),
    "Eta": (r"\Eta", "Η"),
    "Theta": (r"\Theta", "Θ"),
    "Iota": (r"\Iota", "Ι"),
    "Kappa": (r"\Kappa", "Κ"),
    "Lambda": (r"\Lambda", "Λ"),
    "Mu": (r"\Mu", "Μ"),
    "Nu": (r"\Nu", "Ν"),
    "Xi": (r"\Xi", "Ξ"),
    "Omicron": (r"\Omicron", "Ο"),
    "Pi": (r"\Pi", "Π"),
    "Rho": (r"\Rho", "Ρ"),
    "Sigma": (r"\Sigma", "Σ"),
    "Tau": (r"\Tau", "Τ"),
    "Upsilon": (r"\Upsilon", "Υ"),
    "Phi": (r"\Phi", "Φ"),
    "Chi": (r"\Chi", "Χ"),
    "Psi": (r"\Psi", "Ψ"),
    "Omega": (r"\Omega", "Ω"),
}


class Variable(Node):
    def __init__(self, name, latex=None, symbol=None):
        self.name = name

        # Set latex
        if latex:
            self.latex = latex
        else:
            self.latex = name

        # Set symbol
        if symbol:
            self.symbol = symbol
        else:
            self.symbol = name

    def to_latex(self):
        return self.name

    def __str__(self) -> str:
        return self.name

    @classmethod
    def create(symbol):
        if symbol in _GREEK:
            return Variable(symbol)

        return Variable(symbol)


if __name__ == "__main__":
    # Example usage
    x = Variable("x")
    print(x, x.to_latex())
    print(x, str(x))

    y = Variable("y")
    print(y, y.to_latex())
    print(y, str(y))

    mu = Variable("mu")
    print(mu, mu.to_latex())
    print(mu, str(mu))

    zeta = Variable("zeta")
    print(zeta, zeta.to_latex())
    print(zeta, str(zeta))
