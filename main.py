import csv

def read_csv_data(csv_file):
    
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
        data = list(csv_reader)
    return data

def calculate_latitude(data, total_population):
    
    latitude = 0
    for row in data:
        latitude += (row[1] * row[2] / total_population)
    return latitude

def calculate_longitude(data, total_population):
    
    longitude = 0
    for row in data:
        longitude += (row[1] * row[3] / total_population)
    return longitude

def main():
    input_csv_file = "data.csv"

    data = read_csv_data(input_csv_file)

    total_population = sum(row[1] for row in data)

    latitude = calculate_latitude(data, total_population)
    print("Latitude:", latitude)

    longitude = calculate_longitude(data, total_population)
    print("Longitude:", longitude)

main()
