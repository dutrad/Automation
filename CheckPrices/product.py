
class Product:
    def __init__(self, name, last_price, lowest_price, link, price_element):
        self.name = name
        self.last_price = last_price
        self.lowest_price = lowest_price
        self.link = link
        self.price_element = price_element
    
    def serialize(self):
        return {
            "name" : self.name,
            "last_price" : self.last_price,
            "lowest_price" : self.lowest_price,
            "link" : self.link,
            "price_element" : self.price_element
        }
    
    def from_json(self, json_):
        self.name = json_["name"]
        self.last_price = json_["last_price"]
        self.lowest_price = json_["lowest_price"]
        self.link = json_["link"]
        self.price_element = json_["price_element"]