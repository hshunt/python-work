class Motorcycle():

    def __init__(self, brand, model, **details):
        self.brand = brand.title()
        self.model = model.title()
        self.details = details
        
    def stats(self):
        moto_stats = [self.brand.title() + " " + self.model.title()]
        if len(self.details) > 0:
            moto_stats.append("Details:")
            for data, name in self.details["details"].items():
                moto_stats.append(f'{data} = {self.details["details"]}')
        return moto_stats
        
class MotoDB():
    motorcycles = []

    def add(self, *moto_models):
        for moto_model in moto_models:
            self.motorcycles.append(moto_model)

    def delete(self, *moto_models):
        for moto_model in moto_models:
            for self.motorcycle in self.motorcycles:
                if self.motorcycle.model == moto_model.title():
                    self.motorcycles.remove(self.motorcycle)
        
    def search(self, *moto_models, **get_details):
        for self.motorcycle in self.motorcycles:
            for moto_model in moto_models:
                if self.motorcycle.model == moto_model.title():
                    for get in get_details:
                        if get_details[get] == "model":
                            print(self.motorcycle.model)
                        elif get_details[get] == "brand":
                            print(self.motorcycle.brand)
                        elif get_details[get] == "all":
                            print(self.motorcycle.stats())

    # def update_moto(self, *moto_models, **moto_details):
    #     for moto_model in moto_models:
    #         for self.motorcycle in self.motorcycles:
    #             if self.motorcycle.model == moto_model.title():  
    #                 for key in moto_details:
    #                     if key == "displacement":
    #                         self.motorcycle.displacement = moto_details[key]
    #                     elif key == "model":
    #                         self.motorcycle.model = moto_details[key]
    #                     elif key == "brand":
    #                         self.motorcycle.brand = moto_details[key]

    def moto_print(self):
        for self.motorcycle in self.motorcycles:
            print(self.motorcycle.model)
        if len(self.motorcycles) == 0:
            print("You have no motorcycles in the DB!")

db = MotoDB()
scrambler_1200_xe=Motorcycle("Triumph", "Scrambler 1200 XE")
db.add(scrambler_1200_xe)



