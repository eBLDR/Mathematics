def var(*var_names):
    return (Variable(name) for name in var())


class Proposition:
    def __init__(self):
        ...


class Variable(Proposition):
    def __init__(self, name):
        super().__init__()
        self.name = name
