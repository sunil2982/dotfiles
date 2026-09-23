class Coffee:
    def cost(self):
        return 5
    def description(self):
        return "Simple coffee"
class MilkDecorator:
    def __init__(self,coffee):
        self.coffee =coffee
    def cost(self):
        return self.coffee.cost() + 2
    def description(self):
        return self.coffee.description() + " + Milk" 
    
class SugarDecorator:
    def __init__(self,coffee):
        self.coffee = coffee
    def cost(self):
        return self.coffee.cost() +1 
    def description(self):
        return self.coffee.description() + " + Sugar"
