class Product:
    def __init__(self, id, name, type, stock, colors):
        self.id=id
        self.name=name
        self.type=type
        self.stock=stock
        self.colors=colors
    def print_information(self):
        print(f"ID: {self.id} \nName: {self.name.title()} \nType: {self.type.title()} \nStock available: {self.stock}")
        print("Colors: ")
        for color in self.colors:
            print(f"\t*{color.title()}")