from __future__ import annotations

import os
import socket
from datetime import datetime

from typing import Dict, List
from uuid import UUID

from fastapi import FastAPI, HTTPException
from fastapi import Query, Path
from typing import Optional

from models.person import PersonCreate, PersonRead, PersonUpdate
from models.mistake import MistakeCreate, MistakeRead, MistakeUpdate
from models.health import Health

port = int(os.environ.get("FASTAPIPORT", 8000))

# Fake in-memory "databases"
persons: Dict[UUID, PersonRead] = {}
mistakes: Dict[UUID, MistakeRead] = {}

app = FastAPI(
    title="Person/Mistakes API",
    description="Demo FastAPI app using Pydantic v2 models for Person and Mistakes",
    version="0.1.0",
)

# Mistake endpoints
def make_health(echo: Optional[str], path_echo: Optional[str]=None) -> Health:
    return Health(
        status=200,
        status_message="OK",
        timestamp=datetime.utcnow().isoformat() + "Z",
        ip_address=socket.gethostbyname(socket.gethostname()),
        echo=echo,
        path_echo=path_echo
    )

@app.get("/health", response_model=Health)
def get_health_no_path(echo: str | None = Query(None, description="Optional echo string")):
    # Works because path_echo is optional in the model
    return make_health(echo=echo, path_echo=None)

@app.get("/health/{path_echo}", response_model=Health)
def get_health_with_path(
    path_echo: str = Path(..., description="Required echo in the URL path"),
    echo: str | None = Query(None, description="Optional echo string"),
):
    return make_health(echo=echo, path_echo=path_echo)

@app.post("/mistakes", response_model=MistakeRead, status_code=201)
def create_mistake(mistake: MistakeCreate):
    if mistake.id in mistakes:
        raise HTTPException(status_code=400, detail="Mistake with this ID already exists")
    mistakes[mistake.id] = MistakeRead(**mistake.model_dump())
    return mistakes[mistake.id]

@app.get("/mistakes", response_model=List[MistakeRead])
def list_mistakes(
    subject: Optional[str] = Query(None, description="Filter by subject"),
    key_concept: Optional[str] = Query(None, description="Filter by key_concept"),
    prompt: Optional[str] = Query(None, description="Filter by prompt"),
    correct_answer: Optional[str] = Query(None, description="Filter by correct_answer"),
    wrong_answer: Optional[str] = Query(None, description="Filter by wrong_answer"),
    reflection: Optional[str] = Query(None, description="Filter by reflection"),
):
    results = list(mistakes.values())

    if subject is not None:
        results = [a for a in results if a.subject == subject]
    if key_concept is not None:
        results = [a for a in results if a.key_concept == key_concept]
    if prompt is not None:
        results = [a for a in results if a.prompt == prompt]
    if correct_answer is not None:
        results = [a for a in results if a.correct_answer == correct_answer]
    if wrong_answer is not None:
        results = [a for a in results if a.wrong_answer == wrong_answer]
    if reflection is not None:
        results = [a for a in results if a.reflection == reflection]

    return results

@app.get("/mistakes/{mistakes_id}", response_model=MistakeRead)
def get_mistakes(mistakes_id: UUID):
    if mistakes_id not in mistakes:
        raise HTTPException(status_code=404, detail="Mistake not found")
    return mistakes[mistakes_id]

@app.patch("/mistakes/{mistakes_id}", response_model=MistakeRead)
def update_mistake(mistakes_id: UUID, update: MistakeUpdate):
    if mistakes_id not in mistakes:
        raise HTTPException(status_code=404, detail="Mistake not found")
    stored = mistakes[mistakes_id].model_dump()
    stored.update(update.model_dump(exclude_unset=True))
    mistakes[mistakes_id] = MistakeRead(**stored)
    return mistakes[mistakes_id]

@app.delete("/mistakes/{mistakes_id}", status_code=204)
def delete_mistake(mistakes_id: UUID):
    if mistakes_id not in mistakes:
        raise HTTPException(status_code=404, detail="Mistake not found")
    del mistakes[mistakes_id]
    return None


# Person endpoints
@app.post("/persons", response_model=PersonRead, status_code=201)
def create_person(person: PersonCreate):
    # Each person gets its own UUID; stored as PersonRead
    person_read = PersonRead(**person.model_dump())
    persons[person_read.id] = person_read
    return person_read


@app.get("/persons", response_model=List[PersonRead])
def list_persons(
    first_name: Optional[str] = Query(None, description="Filter by first name"),
    last_name: Optional[str] = Query(None, description="Filter by last name"),
    email: Optional[str] = Query(None, description="Filter by email"),
    birth_date: Optional[str] = Query(None, description="Filter by date of birth (YYYY-MM-DD)"),
    grade_level: Optional[str] = Query(None, description="Filter by grade level of at least one feature"),
    subject: Optional[str] = Query(None, description="Filter by subject of at least one feature"),
):
    results = list(persons.values())

    if first_name is not None:
        results = [p for p in results if p.first_name == first_name]
    if last_name is not None:
        results = [p for p in results if p.last_name == last_name]
    if email is not None:
        results = [p for p in results if p.email == email]
    if birth_date is not None:
        results = [p for p in results if str(p.birth_date) == birth_date]

    # nested mistake filtering
    if grade_level is not None:
        results = [p for p in results if any(mistake.grade_level == grade_level for mistake in p.mistakes)]
    if subject is not None:
        results = [p for p in results if any(mistake.subject == subject for mistake in p.mistakes)]
    return results

@app.get("/persons/{person_id}", response_model=PersonRead)
def get_person(person_id: UUID):
    if person_id not in persons:
        raise HTTPException(status_code=404, detail="Person not found")
    return persons[person_id]

@app.patch("/persons/{person_id}", response_model=PersonRead)
def update_person(person_id: UUID, update: PersonUpdate):
    if person_id not in persons:
        raise HTTPException(status_code=404, detail="Person not found")
    stored = persons[person_id].model_dump()
    stored.update(update.model_dump(exclude_unset=True))
    persons[person_id] = PersonRead(**stored)
    return persons[person_id]

@app.delete("/persons/{person_id}", status_code=204)
def delete_person(person_id: UUID):
    if person_id not in persons:
        raise HTTPException(status_code=404, detail="Person not found")
    del persons[person_id]
    return None

# Root
@app.get("/")
def root():
    return {"message": "Welcome to the Person/Mistake API. See /docs for OpenAPI UI."}

# Entrypoint for `python main.py`
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
