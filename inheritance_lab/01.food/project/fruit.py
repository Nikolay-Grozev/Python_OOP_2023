from project.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)  # This is a correct way
        self.name = name
