from character import Character

class Rogue(Character):
    def __init__(self, name, level=1):
        super().__init__(name,level)
        self.max_health,self.health =(100,100)
        self.max_mana,self.mana = (60,60)
        self.strength = 12
        self.intelligence = 8
        self.agility = 18
        self.defense = 4
        # TODO: Call parent constructor with name and level
        # Rogues have more agility, balanced other stats
        # TODO: Set max_health to 100 and health to 100
        # TODO: Set max_mana to 60 and mana to 60
        # TODO: Set strength to 12
        # TODO: Set intelligence to 8
        # TODO: Set agility to 18
        # TODO: Set defense to 4
        
    
    def level_up(self):
        result =super().level_up()
        self.agility = self.agility + 2
        
        return result
        # TODO: Call parent level_up method and store result
        # Extra agility bonus for rogues
        # TODO: Increase agility by additional 2 points
        # TODO: Return the result from parent level_up
        
    
    def attack(self, target):
        damage = self.strength * 0.5 + self.agility * 0.7
        damage_dealt= target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")
        return damage_dealt
        # Rogues use agility for stronger attacks
        # TODO: Calculate damage as self.strength * 0.5 + self.agility * 0.7
        # TODO: Call target.take_damage(damage) and store result as damage_dealt
        # TODO: Print f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage"
        # TODO: Return damage_dealt
        