class Punto:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    def get_coordinate(self):
        value_x=input("If you want to add a coordinate for x, please enter the coordinate. If not, enter 'N'. \n---> ")
        if value_x!="N" or value_x!="n":
            while True:
                try:
                    value_x=int(value_x)
                    break
                except:
                    value_x=input("Invalid input, please enter the coordinate for x: ")
            self.x=value_x
        value_y=input("If you want to add a coordinate for y, please enter the coordinate. If not, enter 'N'. \n---> ")
        if value_y!="N" or value_y!="n":
            while True:
                try:
                    value_y=int(value_y)
                    break
                except:
                    value_y=input("Invalid input, please enter the coordinate for y: ")
            self.y=value_y
    def print_punto(self):
        print(f"({self.x}, {self.y})")
    def get_quadrant(self):
        if self.x==0 and self.y==0:
            print("The point entered is the origin.")
        elif self.x==0 and self.y!=0:
            print("The point entered is located on the Y axis.")
        elif self.x!=0 and self.y==0:
            print("The point entered is located on the X axis.")
        else:
            if self.x>0 and self.y>0:
                print("The point entered is located on the I quadrant.")
            elif self.x<0 and self.y>0:
                print("The point entered is located on the II quadrant.")
            elif self.x<0 and self.y<0:
                print("The point entered is located on the III quadrant.")
            else:
                print("The point entered is located on the IV quadrant.")
    def vector(self, punto, punto_2):
        vector_x=punto.x + punto_2.x
        vector_y=punto.y + punto_2.y
        print(f"The vector is ({vector_x}, {vector_y}).")