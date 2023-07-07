class Car: 
    brand = 'Mazda' 
    max_speed = 100 
    color = 'Black' 
 
    def __init__(self, b, ms): 
        self.brand = b 
        self.max_speed = ms 
     
    def upgrate(self): 
        self.max_speed += 25 
 
class Truck(Car): 
    num_trailers = 0 
    max_load = 0 
 
    def __init__(self, b, ms, nt, ml): 
        super().__init__(b, ms) 
        self.num_trailers = nt 
        self.max_load = ml 
 
    def __str__(self): 
        return f"Марка грузовика: {self.brand}\nМаксимальная скорость: {self.max_speed}\nЦвет: {self.color}\nКоличество прицепов: {self.num_trailers}\nГрузоподъемность: {self.max_load}"