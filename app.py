import csv
import random
import json
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from optparse import OptionParser

app = FastAPI()

# Global variable to store the parsed data
parsed_data = []

def parse_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def render_json(data):
    # Extract the column names from the first row
    column_names = data[0]
    # Remove the column names from the data
    data = data[1:]

    # Select a random row from the data
    random_row = random.choice(data)

    # Create a dictionary to store the random values for each column
    random_values = {}
    for i, column_name in enumerate(column_names):
        random_values[column_name] = random_row[i]

    return random_values

class RandomData(BaseModel):
    query: str

@app.get("/random/{query}")
async def get_random_data(query: str, response_type: str = "JSON"):
    response_type = response_type.upper()  # Convert response_type to uppercase
    if response_type == 'JSON':
        random_values = render_json(parsed_data)
        # Add the query to the response data
        random_values['query'] = query
        return random_values
    elif response_type == 'CSV':
        # Select a random row from the parsed data
        random_row = random.choice(parsed_data)
        # Add the query to the random row
        random_row.append(query)
        # Convert the random row to a comma-separated string
        csv_string = ','.join(random_row)
        return Response(content=csv_string, media_type="text/csv")
    else:
        raise HTTPException(status_code=400, detail="Invalid response type. Supported types: JSON, CSV")

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="file_path", help="Path to the CSV file")
    parser.add_option("-t", "--type", dest="response_type", default="JSON", help="Response type (JSON or CSV)")
    (options, args) = parser.parse_args()

    if not options.file_path:
        parser.error("File path is required.")

    parsed_data = parse_csv(options.file_path)

    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)
