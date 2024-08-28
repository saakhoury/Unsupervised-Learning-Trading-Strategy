import pandas as pd 

# Load CSV file
df = pd.read_csv('NGen project snapshot .csv')

# Convert to JSON
json_data = df.to_json(orient='records')

# Save JSON data to file
with open('file.json', 'w') as json_file:
    json_file.write(json_data)
