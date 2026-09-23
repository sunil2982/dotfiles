class Ability:
    def __init__(self, name, mana_cost, damage):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        # TODO: Initialize ability with name, mana_cost, and damage
        # TODO: Store name as self.name
        # TODO: Store mana_cost as self.mana_cost
        # TODO: Store damage as self.damage
        
    
    def use(self, character, target):
        if character.mana <self.mana_cost:
            print( f"{character.name} doesn't have enough mana to use {self.name}")
            return 0
        character.mana =character.mana - self.mana_cost
        # TODO: Check if character has enough mana (character.mana < self.mana_cost)
        # TODO: If not enough mana, print f"{character.name} doesn't have enough mana to use {self.name}"
        # TODO: If not enough mana, return 0
        
        # TODO: Reduce character.mana by self.mana_cost
        if hasattr(character,'intelligence'):
            damage = self.damage + (character.intelligence * 0.5)
        else:
            damage =self.damage
        damage_dealt = target.take_damage(damage)
        print(f"{character.name} used {self.name} on {target.name} for {damage_dealt:.1f} damage!")
        # Calculate damage
        # TODO: Check if character has intelligence attribute using hasattr(character, 'intelligence')
        # TODO: If has intelligence, calculate damage as self.damage + (character.intelligence * 0.5)
        # TODO: If no intelligence, use self.damage as damage
        
        # TODO: Call target.take_damage(damage) and store result as damage_dealt
        # TODO: Print f"{character.name} used {self.name} on {target.name} for {damage_dealt:.1f} damage!"
        
        # TODO: Return damage_dealt
        return damage_dealt