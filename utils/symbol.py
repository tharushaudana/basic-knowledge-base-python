class Symbol:
    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name