class Soda:
    def __init__(self, addition = "nothing"):
        self.addition = addition 

    def show_my_drink(self):
        if (self.addition == "nothing"):
            print("Обычная газировка")
        else:
            print(f"Газировка и {self.addition}")

cola = Soda("something")
cola.show_my_drink()

justSoda = Soda()
justSoda.show_my_drink