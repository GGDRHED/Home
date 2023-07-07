class Soda:
    def __init__(self, ingredient=None):
        self.ingredient = ingredient
    
    def show_my_drink(self):
        if self.ingredient:
            print(f"Газировка и {self.ingredient}")
        else:
            print("Обычная газировка")