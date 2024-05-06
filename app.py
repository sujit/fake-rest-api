import csv
import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

# Read the CSV file and store the data
data = []
with open('input.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

# Extract the column names from the first row
column_names = data[0]
# Remove the column names from the data
data = data[1:]

class RandomData(BaseModel):
    query: str

@app.get("/random/{query}")
async def get_random_data(query: str):
    # Select a random row from the data
    random_row = random.choice(data)

    # Create a dictionary to store the random values for each column
    random_values = {}
    for i, column_name in enumerate(column_names):
        random_values[column_name] = random_row[i]

    # Add the raw client query to the response data
    random_values['query'] = query

    return random_values

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)
