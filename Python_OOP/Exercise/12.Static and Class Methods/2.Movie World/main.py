from project.customer import Customer
from project.dvd import DVD
from project.movie_world import MovieWorld

c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)

"""
output
John should be at least 18 to rent this movie
Anna has successfully rented Black Widow
John has successfully rented The Croods 2
1: John of age 16 has 1 rented DVD's (The Croods 2)
2: Anna of age 55 has 1 rented DVD's (Black Widow)
1: Black Widow (April 2020) has age restriction 18. Status: rented
2: The Croods 2 (December 2020) has age restriction 3. Status: rented

"""
