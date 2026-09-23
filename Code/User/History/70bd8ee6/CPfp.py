from abc import ABC, abstractmethod

class Beverage(ABC):
    "Abstract base calss for all beverages"
    def __init__(self):
        self.description = "Unknown Beverage"

    def get_description(self):
        return self.description
    @abstractmethod
    def cost(self):
        # TODO: Abstract method that must be implemented by concrete beverage classes
        # TODO: Should return the cost of the beverage as a float
        pass

class Espresso(Beverage):
    """
    A concrete beverage implementation - Espresso.
    """
    def __init__(self):
        # TODO: Call parent constructor using super()
        # TODO: Set description to "Espresso"
        
    
    def cost(self):
        # TODO: Return the cost of Espresso (1.99)
        pass


class HouseBlend(Beverage):
    """
    A concrete beverage implementation - House Blend Coffee.
    """
    def __init__(self):
        # TODO: Call parent constructor using super()
        # TODO: Set description to "House Blend Coffee"
        pass
    
    def cost(self):
        # TODO: Return the cost of House Blend Coffee (0.89)
        pass


class DarkRoast(Beverage):
    """
    A concrete beverage implementation - Dark Roast Coffee.
    """
    def __init__(self):
        # TODO: Call parent constructor using super()
        # TODO: Set description to "Dark Roast Coffee"
        pass
    
    def cost(self):
        # TODO: Return the cost of Dark Roast Coffee (0.99)
        pass


class Decaf(Beverage):
    """
    A concrete beverage implementation - Decaf Coffee.
    """
    def __init__(self):
        # TODO: Call parent constructor using super()
        # TODO: Set description to "Decaf Coffee"
        pass
    
    def cost(self):
        # TODO: Return the cost of Decaf Coffee (1.05)
        pass