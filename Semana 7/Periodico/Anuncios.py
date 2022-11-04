class ComercialAdvertisement:
    def __init__(self, image, section):
        self.image=image
        self.section=section
class ClassifiedAdvertisement:
    def __init__(self, price, publish_date, days_avaliable, type_article):
        self.price=price
        self.publish_date=publish_date
        self.days_available=days_avaliable
        self.type_article=type_article
class State(ClassifiedAdvertisement):
    def __init__(self, price, publish_date, days_avaliable, size, num_rooms, num_bathrooms, num_parkplaces, law_applies):
        super().__init__(price, publish_date, days_avaliable, "State")
        self.size=size
        self.num_rooms=num_rooms 
        self.num_bathrooms=num_bathrooms
        self.num_parkplaces=num_parkplaces
        self.law_applies=law_applies
class Vehicle(ClassifiedAdvertisement):
    def __init__(self, price, publish_date, days_avaliable, brand, model, year, color, mileage):
        super().__init__(price, publish_date, days_avaliable, "Vehicle")
        self.brand=brand
        self.model=model
        self.year=year
        self.color=color
        self.mileage=mileage