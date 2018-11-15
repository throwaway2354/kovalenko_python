city_to_country = {}

for _ in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        city_to_country[city] = country

for _ in range(int(input())):
    print(city_to_country[input()])
