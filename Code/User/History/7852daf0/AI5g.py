from character import Character

class Mage(Character):
    def __init__(self, name, level=1):
        # TODO: Call parent constructor with name and level
        # Mages have more mana and intelligence, less health and strength
        # TODO: Set max_health to 80 and health to 80
        # TODO: Set max_mana to 150 and mana to 150
        # TODO: Set strength to 5
        # TODO: Set intelligence to 20
        # TODO: Set defense to 3
        pass
    
    def level_up(self):
        # TODO: Call parent level_up method and store result
        # Extra intelligence bonus for mages
        # TODO: Increase intelligence by additional 2 points
        # TODO: Increase max_mana by additional 15 points (extra mana for mages)
        # TODO: Set mana to max_mana (full mana restore)
        # TODO: Return the result from parent level_up
        pass
    
    def attack(self, target):
        # Mages use intelligence for basic attacks
        # TODO: Calculate damage as self.intelligence * 0.4
        # TODO: Call target.take_damage(damage) and store result as damage_dealt
        # TODO: Print f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage"
        
        # Mages regain some mana on basic attacks
        # TODO: Set mana_regen to 5
        # TODO: Increase self.mana by mana_regen, but don't exceed max_mana
        # TODO: Use min(self.max_mana, self.mana + mana_regen)
        
        # TODO: Return damage_dealt
        pass