N = int(input())
set_country = set()
for _ in range(N):
    country_name = input()
    set_country.add(country_name)
print(len(set_country))
