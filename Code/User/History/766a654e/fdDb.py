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
    
mycoffee =Coffee()

print(f"{mycoffee.description()}: ${mycoffee.cost()}")

mycoffee =MilkDecorator(mycoffee)
print(f"{mycoffee.description()}: ${mycoffee.cost()}")

mycoffee =SugarDecorator(mycoffee)
print(f"{mycoffee.description()}: ${mycoffee.cost()}")


class Text:
    def __init__(self, content):
        self.content = content
    
    def render(self):
        return self.content

class BoldDecorator:
    def __init__(self, text):
        self.text = text
    
    def render(self):
        return f"<b>{self.text.render()}</b>"

class ItalicDecorator:
    def __init__(self, text):
        self.text = text
    
    def render(self):
        return f"<i>{self.text.render()}</i>"

# Build formatted text step by step
message = Text("Hello World")
message = BoldDecorator(message)
message = ItalicDecorator(message)

print(message.render())

class Chocaklate:
    def __init__(self,kitkat):
        self.kitkat = kitkat

    def display():
        return print("{self.kitkat.title()}")

