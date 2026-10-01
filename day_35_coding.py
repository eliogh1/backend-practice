class Planet:

    def __init__(self,name,planet_type,star):
        self.name = name
        self.planet_type = planet_type
        self.star = star

        if not isinstance(name ,str) or not isinstance(planet_type,str) or not isinstance(star, str):
            raise TypeError("name, planet type, and star must be strings")       

        if name == "" or planet_type == "" or star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")     

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"



#planet_1 = (Planet("Earth", "terrestrial plant", "sun"))
#planet_2 = (Planet("Mars", "terrestrial planet", "sun"))
#planet_3 = (Planet("venus", "terrestiral planet", "sun"))

#print(str(planet_1))
#print(str(planet_2))
#print(str(planet_3))

#print(Planet.orbit(planet_1))
#print(Planet.orbit(planet_2))
#print(Planet.orbit(planet_3))