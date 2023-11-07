class Dog:
    def __init__(self, rozmer: str):
        self.rozmer = rozmer

    def bark(self):
        if self.rozmer == "velky":
            print("HAaAAAfffFF")
        elif self.rozmer == "maly":
            print("hiiiff")

fufik = Dog("velky")
alik = Dog("maly")

print(alik.rozmer)
fufik.bark()