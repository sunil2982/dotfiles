class Character:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.max_health = 100
        self.health = 100
        self.max_mana = 50
        self.mana = 50
        self.strength =10
        self.intelligence =10
        self.agility = 10
        self.defense = 5 
        self.abilities = []
        
        # TODO: Initialize empty abilities list as self.abilities
    
    
    def level_up(self):
        self.level =self.level +1
        self.max_health = self.max_health +10
        self.health = self.max_health
        self.max_mana  =  self.max_mana + 5 
        self.mana = self.max_mana 
        self.strength = self.strength +1 
        self.intelligence = self.intelligence +1 
        self.agility = self.agility + 1 
        self.defense = self.defense + 1 
        return  f"{self.name} leveled up to level {self.level}!" 


         # TODO: Increment self.level by 1 TODO: Increase max_health by 10
        # TODO: Set health to max_health (full heal on level up)
        # TODO: Increase max_mana by 5
        # TODO: Increase max_health by 10

        # TODO: Set mana to max_mana (full mana restore on level up)
        # TODO: Increase strength, intelligence, agility, and defense by 1 each
        # TODO: Return f"{self.name} leveled up to level {self.level}!" 
        
    
    def attack(self, target):
        damage = self.strength * 0.8
        damage_dealt= target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")
        return damage_dealt
        # TODO: Calculate damage as self.strength * 0.8
        # TODO: Call target.take_damage(damage) and store result as damage_dealt
        # TODO: Print f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage"
        # TODO: Return damage_dealt
        
    
    def take_damage(self, amount):
        effective_damage = max(1,amount - self.defense * 0.5)
        self.health = max(0,self.health - effective_damage
        # TODO: Calculate effective_damage as max(1, amount - self.defense * 0.5)
        # TODO: Reduce self.health by effective_damage, but not below 0
        # TODO: Use max(0, self.health - effective_damage)
        # TODO: Return effective_damage
        return effective_damage
        
    
    def is_alive(self):
        if self.health >0 :
            return True
        else:
            return False
                          # TODO: Return True if health > 0, False otherwise       

    
    def learn_ability(self, ability):
        # TODO: Append ability to self.abilities list
        self.abilities.append(ability)
    
    def use_ability(self, ability_index, target):
        # TODO: Check if ability_index is valid (>= 0 and < len(self.abilities))
        # TODO: If invalid, return 0
        # TODO: Get ability from self.abilities[ability_index]
        # TODO: Call ability.use(self, target) and return the result
        if ability_index >=0 and len(self.abilities):
            ability = self.abilities[ability_index]
            result= ability.use(self,target)
                return result
        return 0
        
