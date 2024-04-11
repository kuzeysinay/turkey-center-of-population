import csv

def read_csv_data(csv_file):
    
    data = []
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append({key: float(value) for key, value in row.items()})
    return data

def calculate_latitude(data, total_population):
   
    latitude = 0
    for row in data:
        latitude += (row['POPULATION'] * row['LATITUDE'] / total_population)
    return latitude

def calculate_longitude(data, total_population):
 
    longitude = 0
    for row in data:
        longitude += (row['POPULATION'] * row['LONGITUDE'] / total_population)
    return longitude

def main():
    input_csv_file = "data.csv"

    data = read_csv_data(input_csv_file)

    total_population = sum(row['POPULATION'] for row in data)

    longitude = calculate_longitude(data, total_population)
    print("Longitude:", longitude)
    latitude = calculate_latitude(data, total_population)
    print("Latitude:", latitude)

main()
