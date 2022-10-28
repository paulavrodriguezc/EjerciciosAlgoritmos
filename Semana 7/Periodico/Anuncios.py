class Advertisement:
    def __init__(self, name_requester, id_requester, section, title, body):
        self.name_requester=name_requester
        self.id_requester=id_requester
        self.section=section
        self.title=title
        self.body=body
class Classified(Advertisement):
    def __init__(self, name_requester, id_requester, section, title, body, price, publish_date, days_avaliable, type_article):
        super().__init__(name_requester, id_requester, section, title, body)
        self.price=price
        self.publish_date=publish_date
        self.days_available=days_avaliable
        self.type_article=type_article
class State(Classified):
    def __init__(self, name_requester, id_requester, section, title, body, price, publish_date, days_avaliable, type_article, size, num_rooms, num_bathrooms, num_parkplaces, law_applied):
        super().__init__(name_requester, id_requester, section, title, body, price, publish_date, days_avaliable, type_article)
        self.size=size
        self.num_rooms=num_rooms 
        self.num_bathrooms=num_bathrooms
        self.num_parkplaces=num_parkplaces
        self.law_applied=law_applied
class Car(Classified):
    def __init__(self, name_requester, id_requester, section, title, body, price, publish_date, days_avaliable, type_article, brand, model, year, color, mileage):
        super().__init__(name_requester, id_requester, section, title, body, price, publish_date, days_avaliable, type_article)
        self.brand=brand
        self.model=model
        self.year=year
        self.color=color
        self.mileage=mileage