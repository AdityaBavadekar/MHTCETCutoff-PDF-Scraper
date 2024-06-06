import json

data = json.load(open('cleaned.json', 'r', encoding='utf-8'))

print("Enter cities (Delim : ','):")
c = str(input('Cities: ')).strip().split(',')

if not c: exit(0)
print()

city_colleges = {city:[] for city in c}

for college_name in data:
    for city in c:
        if city in college_name:
            city_colleges[city].append(college_name)
            break
        
for city in city_colleges:
    print()
    print('*'*40)
    print(city)
    print('*'*40)
    print('-','\n- '.join(city_colleges[city]))
