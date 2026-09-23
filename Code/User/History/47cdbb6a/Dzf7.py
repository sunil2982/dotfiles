from character import Character

class Warrior(Character):
    def __init__(self, name, level=1):
        super().__init__(name,level)
        self.max_health,self.health =(150,150)
        self.max_mana,self.mana = (30,30)
        self.strength = 15 
        self.intelligence = 5
        self.defense = 8
        # Warriors have more health and strength, less mana and intelligence
        # TODO: Set max_health to 150 and health to 150
        # TODO: Set max_mana to 30 and mana to 30
        # TODO: Set strength to 15
        # TODO: Set intelligence to 5
        # TODO: Set defense to 8
  
    def level_up(self):
        result =super().level_up()
        self.strength = self.strength +2
        self.max_health =self.max_health +10 
        self.health =self.max_health
        return result
        # rent level_up method and store result
        # Extra stre#gth bonus for warriors
        # TODO: Increase strength by additional 2 points
        # TODO: Increase max_health by additional 10 points (extra health for warriors)
        # TODO: Set health to max_health (full heal)
        # TODO: Return the result from parent level_up
    
    def attack(self, target):
        damage = self.strength *1.2
        damage_dealt= target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")
        return damage_dealt
        # Warriors have a stronger basic attack
        # TODO: Calculate damage as self.strength * 1.2
        # TODO: Call target.take_damage(damage) and store result as damage_dealt
        # TODO: Print f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage"
        # TODO: Return damage_dealt
        
