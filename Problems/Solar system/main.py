from os import linesep

# create the planets.txt
planets = open('planets.txt', 'w', encoding='utf-8')

items = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for item in items:
    planets.write(item + linesep)

planets.close()
