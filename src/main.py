import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(
    title="Person Similarity Calculator",
    description="This is a simple API to calculate the similarity "
                "between two persons based on their names and dates of birth.",
    version="0.1.0"
)

from src.person_scoring import calculate_person_similarity


class Person(BaseModel):
    name: str
    birth_date: str


class PersonSimilarityRequest(BaseModel):
    person1: Person
    person2: Person


class PersonSimilarityResponse(BaseModel):
    score: float
    name_score: float
    year_score: float
    month_score: float
    day_score: float


@app.get("/", include_in_schema=False)
def read_root():
    return HTMLResponse(content=open(os.path.join(os.getcwd(), 'src', 'templates', 'index.html'), 'r').read())


@app.post("/api/compare", response_model=PersonSimilarityResponse)
def calculate(person1: Person, person2: Person):
    try:
        score, name_score, bd_scores = calculate_person_similarity((person1.name, person1.birth_date),
                                                                   (person2.name, person2.birth_date))

        return {
            'score': score,
            'name_score': name_score,
            'year_score': bd_scores[0],
            'month_score': bd_scores[1],
            'day_score': bd_scores[2]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('src.main:app', host="127.0.0.1", port=3000, reload=True)
