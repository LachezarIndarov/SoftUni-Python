class Weapon:

    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return("shooting...")
        elif self.bullets == 0 or self.bullets < 0 :
            return("no bullets left")



    def __repr__(self):
        return (f"Remaining bullets: {self.bullets}")

# Test Code
weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)

# Output
"""
shooting...
shooting...
Remaining bullets: 3
shooting...
shooting...
shooting...
no bullets left
Remaining bullets: 0
"""