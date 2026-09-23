class Character:
    def __init__(self, name, level=1):
        # TODO: Initialize character with name and level (default 1)
        # TODO: Store name as self.name
        # TODO: Store level as self.level
        
        # Base stats - will be adjusted by subclasses
        # TODO: Set max_health to 100 and health to 100
        # TODO: Set max_mana to 50 and mana to 50
        # TODO: Set strength to 10
        # TODO: Set intelligence to 10
        # TODO: Set agility to 10
        # TODO: Set defense to 5
        
        # TODO: Initialize empty abilities list as self.abilities
        pass
    
    def level_up(self):
        # TODO: Increment self.level by 1
        # TODO: Increase max_health by 10
        # TODO: Set health to max_health (full heal on level up)
        # TODO: Increase max_mana by 5
        # TODO: Set mana to max_mana (full mana restore on level up)
        # TODO: Increase strength, intelligence, agility, and defense by 1 each
        # TODO: Return f"{self.name} leveled up to level {self.level}!"
        pass
    
    def attack(self, target):
        # TODO: Calculate damage as self.strength * 0.8
        # TODO: Call target.take_damage(damage) and store result as damage_dealt
        # TODO: Print f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage"
        # TODO: Return damage_dealt
        pass
    
    def take_damage(self, amount):
        # TODO: Calculate effective_damage as max(1, amount - self.defense * 0.5)
        # TODO: Reduce self.health by effective_damage, but not below 0
        # TODO: Use max(0, self.health - effective_damage)
        # TODO: Return effective_damage
        pass
    
    def is_alive(self):
        # TODO: Return True if health > 0, False otherwise
        pass
    
    def learn_ability(self, ability):
        # TODO: Append ability to self.abilities list
        pass
    
    def use_ability(self, ability_index, target):
        # TODO: Check if ability_index is valid (>= 0 and < len(self.abilities))
        # TODO: If invalid, return 0
        # TODO: Get ability from self.abilities[ability_index]
        # TODO: Call ability.use(self, target) and return the result
        pass