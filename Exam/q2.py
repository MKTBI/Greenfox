'''The rainiest city
Write a method that can read and parse a file containing information about the weather in various cities(in the format: date;city;rain quantity in millimeters). The method should take the name of the file as an input and return the name of the rainiest city (where the highest overall quantity of rain was measured). If there are more cities with the same amount of rainfall, you can decide which one to return.

The function should handle possible exceptions by printing messages to the standard output.



Example
You should use an example .txt file with the following content:



2021-01-30;Budapest;0
2021-01-30;Amsterdam;10
2021-01-30;Regensburg;2
2021-01-31;Budapest;1
2021-01-31;Amsterdam;9
2021-01-31;Regensburg;4
2021-02-01;Budapest;2
2021-02-01;Amsterdam;7
2021-02-01;Regensburg;6
2021-02-02;Budapest;0
2021-02-02;Amsterdam;9
2021-02-02;Regensburg;3
2021-02-03;Budapest;0
2021-02-03;Amsterdam;12
2021-02-03;Regensburg;0
2021-02-04;Budapest;1
2021-02-04;Amsterdam;7
2021-02-04;Regensburg;2
2021-02-05;Budapest;1
2021-02-05;Amsterdam;8
2021-02-05;Regensburg;6
2021-02-06;Budapest;0
2021-02-06;Amsterdam;10
2021-02-06;Regensburg;1
2021-02-07;Budapest;1
2021-02-07;Amsterdam;9
2021-02-07;Regensburg;2
2021-02-08;Budapest;0
2021-02-08;Amsterdam;15
2021-02-08;Regensburg;2


Output:
Amsterdam'''

def rainiest_city(file_name):

    try:
        city_rain_data = {}

        with open(file_name, 'r') as file:
            for line in file:
                date, city, rain = line.strip().split(';')

                if city in city_rain_data:
                    city_rain_data[city] += int(rain)
                else:
                    city_rain_data[city] = int(rain)

        max_rain = 0
        rainiest_city = None
        for city, rain in city_rain_data.items():
            if rain > max_rain:
                max_rain = rain
                rainiest_city = city

        return rainiest_city
    
    except FileNotFoundError:
        print("File not found")
        
    except:
        print("An error occured while reading the file")

print(rainiest_city('q2.txt'))