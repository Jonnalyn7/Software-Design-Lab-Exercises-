class A:
    def __str__(self):
        pass

class B(A):
    def __init__(self, Age):
        self.Age = Age
    def __str__(self):
        return "Age: " + Age + ", parent: " +A.__str__