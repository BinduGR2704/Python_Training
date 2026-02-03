import csv
import io

csv_data = """Year, Industry, Value,  
2014, Manufacturing, 769400
2014, Manufacturing, 48000
2014, Manufacturing, 12
"""
# """ represents multiple lines of text

csvFile = io.StringIO(csv_data)
csvReader = csv.reader(csvFile)
for row in csvReader:
    print(row)