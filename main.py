x = 0
y = 0

total_population = 25520468
main_data = ((6, 5663322, 39.92077, 32.85411), (34, 15462452, 41.00527, 28.97696 ), (35, 4394694, 38.41885, 27.12872))

for i in range(3):
    x += (main_data[i][1] * main_data[i][2] / total_population)

print ("Latitude:", x)
#for loop above, multiplies population and latitude of each city and divides it to total population of Turkey 

for e in range(3):
    y += (main_data[e][1] * main_data[e][3] / total_population )

print ("Longitude:", y)

#for loop above, multiplies population and longitude of each city and divides it to total population of Turkey 