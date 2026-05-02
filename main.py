class TrafficLight :
    def __init__(self,location,color):
        self.location = location
        self.color = color
        color = 'Червоний'
    def change_c(self) :
        self.color = input('Введіть колір світлофора').lower
        if self.color not in ['зелений','жовтий','червоний']:
            print("Гад в такого кольору нема в списку")
        else:
            print(f"На {self.location} тепер колір: {self.color}")

Tl103 = TrafficLight('103','Зелений')#це в нас так в ківерцях сторони звуть де 103 маршрyтка їде і 107

Tl107 = TrafficLight('107','Зелений')

Tl103.change_c()
Tl103.change_c()