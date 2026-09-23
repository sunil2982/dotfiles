# Import all necessary classes
from beverage import Espresso, HouseBlend, DarkRoast, Decaf
from condiment_decorator import Milk, Mocha, Soy, Whip

# Comprehensive test case handler
test_case = input()

if test_case == "basic_beverage_test":
    # Test basic beverage functionality
    espresso = Espresso()
    print(f"Description: {espresso.get_description()}")
    print(f"Cost: ${espresso.cost():.2f}")

elif test_case == "all_beverages_test":
    # Test all beverage types
    beverages = [Espresso(), HouseBlend(), DarkRoast(), Decaf()]
    for beverage in beverages:
        print(f"{beverage.get_description()}: ${beverage.cost():.2f}")

elif test_case == "single_condiment_test":
    # Test single condiment decoration
    espresso = Espresso()
    espresso_with_milk = Milk(espresso)
    print(f"Description: {espresso_with_milk.get_description()}")
    print(f"Cost: ${espresso_with_milk.cost():.2f}")

elif test_case == "multiple_condiments_test":
    # Test multiple condiment decorations
    house_blend = HouseBlend()
    decorated_coffee = Mocha(Soy(Whip(house_blend)))
    print(f"Description: {decorated_coffee.get_description()}")
    print(f"Cost: ${decorated_coffee.cost():.2f}")

elif test_case == "all_condiments_test":
    # Test all condiments on one beverage
    dark_roast = DarkRoast()
    fully_loaded = Milk(Mocha(Soy(Whip(dark_roast))))
    print(f"Description: {fully_loaded.get_description()}")
    print(f"Cost: ${fully_loaded.cost():.2f}")

elif test_case == "cost_calculation_test":
    # Test cost calculations for different combinations
    espresso = Espresso()
    
    # Single additions
    with_milk = Milk(espresso)
    with_mocha = Mocha(espresso)
    
    print(f"Espresso: ${espresso.cost():.2f}")
    print(f"Espresso + Milk: ${with_milk.cost():.2f}")
    print(f"Espresso + Mocha: ${with_mocha.cost():.2f}")

elif test_case == "decoration_order_test":
    # Test that decoration order doesn't affect final result
    decaf = Decaf()
    
    order1 = Milk(Mocha(decaf))
    order2 = Mocha(Milk(decaf))
    
    print(f"Order 1 - {order1.get_description()}: ${order1.cost():.2f}")
    print(f"Order 2 - {order2.get_description()}: ${order2.cost():.2f}")
    print(f"Same cost: {order1.cost() == order2.cost()}")

elif test_case == "complex_order_test":
    # Test complex beverage orders
    orders = [
        Mocha(Whip(Espresso())),
        Soy(Milk(HouseBlend())),
        Whip(Mocha(Soy(DarkRoast()))),
        Milk(Decaf())
    ]
    
    for i, order in enumerate(orders, 1):
        print(f"Order {i}: {order.get_description()}")
        print(f"Cost: ${order.cost():.2f}")
        print("---")

elif test_case == "double_condiment_test":
    # Test adding the same condiment multiple times
    espresso = Espresso()
    double_mocha = Mocha(Mocha(espresso))
    print(f"Description: {double_mocha.get_description()}")
    print(f"Cost: ${double_mocha.cost():.2f}")

elif test_case == "beverage_comparison_test":
    # Compare costs of different beverages with same condiments
    base_beverages = [Espresso(), HouseBlend(), DarkRoast(), Decaf()]
    
    print("All beverages with Milk + Mocha:")
    for beverage in base_beverages:
        decorated = Milk(Mocha(beverage))
        print(f"{decorated.get_description()}: ${decorated.cost():.2f}")

elif test_case == "condiment_cost_test":
    # Test individual condiment costs
    espresso = Espresso()
    base_cost = espresso.cost()
    
    condiments = [
        ("Milk", Milk(espresso)),
        ("Mocha", Mocha(espresso)),
        ("Soy", Soy(espresso)),
        ("Whip", Whip(espresso))
    ]
    
    for name, decorated in condiments:
        additional_cost = decorated.cost() - base_cost
        print(f"{name} adds: ${additional_cost:.2f}")

elif test_case == "cheapest_most_expensive_test":
    # Find cheapest and most expensive base beverages
    beverages = [
        ("Espresso", Espresso()),
        ("House Blend", HouseBlend()),
        ("Dark Roast", DarkRoast()),
        ("Decaf", Decaf())
    ]
    
    beverages.sort(key=lambda x: x[1].cost())
    print(f"Cheapest: {beverages[0][0]} - ${beverages[0][1].cost():.2f}")
    print(f"Most Expensive: {beverages[-1][0]} - ${beverages[-1][1].cost():.2f}")

elif test_case == "nested_decoration_test":
    # Test deeply nested decorations
    beverage = HouseBlend()
    # Add 5 layers of decorations
    decorated = Whip(Soy(Mocha(Milk(Whip(beverage)))))
    print(f"Description: {decorated.get_description()}")
    print(f"Cost: ${decorated.cost():.2f}")
    
    # Count number of condiments
    description = decorated.get_description()
    condiment_count = description.count(" + ")
    print(f"Number of condiments: {condiment_count}")

elif test_case == "cost_breakdown_test":
    # Detailed cost breakdown
    dark_roast = DarkRoast()
    print(f"Base Dark Roast: ${dark_roast.cost():.2f}")
    
    with_soy = Soy(dark_roast)
    print(f"+ Soy: ${with_soy.cost():.2f}")
    
    with_mocha = Mocha(with_soy)
    print(f"+ Mocha: ${with_mocha.cost():.2f}")
    
    with_whip = Whip(with_mocha)
    print(f"+ Whip: ${with_whip.cost():.2f}")
    
    final_cost = with_whip.cost()
    print(f"Final total: ${final_cost:.2f}")

elif test_case == "description_format_test":
    # Test description formatting consistency
    espresso = Espresso()
    test_combinations = [
        Milk(espresso),
        Mocha(Milk(espresso)),
        Whip(Mocha(Milk(espresso))),
        Soy(Whip(Mocha(Milk(espresso))))
    ]
    
    for combo in test_combinations:
        description = combo.get_description()
        print(f"Description: '{description}'")
        # Check if description starts with base beverage name
        starts_correctly = description.startswith("Espresso")
        print(f"Starts with base name: {starts_correctly}")
        print("---")