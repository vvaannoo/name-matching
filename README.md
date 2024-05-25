# Person Similarity

This is a simple API to calculate the similarity between
two persons based on their names and dates of birth.

## How to run

To run the API, you need to have Python 3.* installed. Then, you can run the following commands:

```shell
pip install -r requirements.txt
python src/main.py
```

## How to use

The API has only one endpoint, which is `/api/compare`. You can send a POST request to this endpoint with the following JSON body:

```json
{
  "person1": {
    "name": "John Doe",
    "date_of_birth": "1990-01-01"
  },
  "person2": {
    "name": "John Doe",
    "date_of_birth": "1990-01-01"
  }
}
```

The response will be a JSON object with the similarity between the two persons:

```json
{
  "score": 1,
  "name_score": 1,
  "year_score": 1,
  "month_score": 1,
  "day_score": 1
}
```

The `score` is the overall similarity between the two persons.

## Demo

You can access a demo at http://localhost:3000).