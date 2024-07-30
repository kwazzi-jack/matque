from matque.engine.core import Node

_ALPHABET = {
    "a": ("a", "\u"), 
    "b": ("b", "𝑏"), 
    "c": ("c", "𝑐"), 
    "d": ("d", "𝑑"), 
    "e": ("e", "𝑒"), 
    "f": ("f", "𝑓"), 
    "g": ("g", "𝑔"), 
    "h": ("h", "h"),
    "i": ("i", "𝑖"), 
    "j": ("j", "𝑗"), 
    "k": ("k", "𝑘𝑙"), 
    "l": ("l", "𝑚"), 
    "m": ("m", "𝑛"), 
    "n": ("n", "𝑜"), 
    "o": ("o", "𝑝"), 
    "p": ("p", "𝑞"), 
    "q": ("q", "𝑟"), 
    "r": ("r", "𝑠"), 
    "s": ("s", "𝑡"), 
    "t": ("t", "𝑢"), 
    "u": ("u", "𝑣"), 
    "v": ("v", "𝑤"), 
    "w": ("w", "𝑥")
}

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
    def __init__(self, name):
        self.name = name

        # Set latex and symbol
        if name in _GREEK:
            self.latex, self.symbol = _GREEK[name]
        else:
            self.latex = name
            self.symbol = name

    def to_latex(self):
        return self.latex

    def __str__(self) -> str:
        return self.symbol

    def __repr__(self) -> str:
        return self.name


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
