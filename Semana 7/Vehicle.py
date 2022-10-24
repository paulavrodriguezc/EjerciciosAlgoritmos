class Vehicle: 
    def __init__(self,brand,model,color,year):
        self.brand=brand 
        self.model=model 
        self.color=color 
        self.year=year
# para poner un atributo privado, se pone self.__ (dos guiones bajos) y el nombre
# es decir, solo se va a poder acceder a él si se define otra función dentro de la clase que devuelva ese valor privado