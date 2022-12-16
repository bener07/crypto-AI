def getCsvsData(name):
    import csv
    with open(f'csvs/{name.upper()}/info.csv') as file:
        reader = csv.reader(file)
        data = [[i[0],i[1]] for i in reader]
        return data
