PlanetNum = int(input())
SequenceOfPlanet = None

if PlanetNum == 1:
    SequenceOfPlanet = '수성'
elif PlanetNum == 2:
    SequenceOfPlanet = "금성"
elif PlanetNum == 3:
    SequenceOfPlanet = "지구"
elif PlanetNum == 4:
    SequenceOfPlanet = "화성"
elif PlanetNum == 5:
    SequenceOfPlanet = "목성"
elif PlanetNum == 6:
    SequenceOfPlanet = "토성"
elif PlanetNum == 7:
    SequenceOfPlanet = "천왕성"
elif PlanetNum == 8:
    SequenceOfPlanet = "해왕성"

print(SequenceOfPlanet)

planets = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']

n = int(input()) -1
print(planets[n])