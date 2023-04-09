# This program is about Class and object Instantiation. More importantly, it makes use of inheritance by enabling the child to inherit properties from its parent



class Vehicle:

    def __init__(self, seating_capacity=50):
        self.seating_capacity = seating_capacity 
        print(f'The seating capacity of a bus is {seating_capacity} passengers')


        
# toyota = Vehicle(500)  


class bus(Vehicle):
    def __init__(self):
        print('Toyota is a nice and fantastic car!')
   

bus = Vehicle()
