from __future__ import annotations

from typing import Optional, List, Annotated
from uuid import UUID, uuid4
from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr, StringConstraints

from .mistake import MistakeBase

Username = Annotated[str, StringConstraints(pattern=r"^[a-z0-9_]{3,20}$")]
GradeLevel = Literal["K-5", "6-8", "9-12", "Undergrad", "Graduate", "Adult", "Other"]

class PersonBase(BaseModel):
    first_name: str = Field(
        ...,
        description="Given name."
        json_schema_extra={"example": "Ada"},
    )
    last_name: str = Field(
        ...,
        description="Family name.",
        json_schema_extra={"example": "Smith"},
    )
    email: EmailStr = Field(
        ...,
        description="Primary email address.",
        json_schema_extra={"example": "ada@example.com"},
    )
    birth_date: Optional[date] = Field(
        None,
        description="Date of birth (YYYY-MM-DD).",
        json_schema_extra={"example": "1815-12-10"},
    )
    grade_level: Optional[GradeLevel] = Field(
        None, 
        description="Educational stage.",
        json_schema_extra={"example": "9-12"},
    )

    mistake: List[MistakeBase] = Field(
        default_factory=list,
        description="Mistakes linekd to this person (each carries a persistent Mistake ID).",
        json_schema_extra={
            "example": [
                {
                    "id":"550e8400-e29b-41d4-a716-446655440000",
                    "subject":"lsat",
                    "key_concept":"Logical Reasoning",
                    "prompt":"Political scientist: As a political system, democracy does not promote political freedom. There are historical examples of democracies that ultimately resulted in some of the most oppressive societies. Likewise, there have been enlightened despotisms and oligarchies that have provided a remarkable level of political freedom to their subjects. The reasoning in the political scientist’s argument is flawed because it",
                    "correct_answer":"D. overlooks the possibility that democracy promotes political freedom without being necessary or sufficient by itself to produce it",
                    "wrong_answer":"A. confuses the conditions necessary for political freedom with the conditions sufficient to bring it about",
                    "reflection":"A is incorrect. The political scientist’s argument does not indicate that any particular conditions are necessary for political freedom, nor does it indicate that any particular conditions are sufficient to bring about political freedom. Thus the argument could not be said to confuse these two sorts of conditions. Rather, the political scientist’s argument attempts to demonstrate that democracy does not promote political freedom on the grounds that democracy is neither necessary nor sufficient for bringing about political freedom.",
                }
            ]
        }
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "Ada",
                    "last_name": "Smith",
                    "email": "Aada@exmaple.com",
                    "birth_date": "2004-12-10",
                    "grade_level": "9-12",
                    "mistake": [
                        {
                            "id":"550e8400-e29b-41d4-a716-446655440000",
                            "subject":"lsat",
                            "key_concept":"Logical Reasoning",
                            "prompt":"Political scientist: As a political system, democracy does not promote political freedom. There are historical examples of democracies that ultimately resulted in some of the most oppressive societies. Likewise, there have been enlightened despotisms and oligarchies that have provided a remarkable level of political freedom to their subjects. The reasoning in the political scientist’s argument is flawed because it",
                            "correct_answer":"D. overlooks the possibility that democracy promotes political freedom without being necessary or sufficient by itself to produce it",
                            "wrong_answer":"A. confuses the conditions necessary for political freedom with the conditions sufficient to bring it about",
                            "reflection":"A is incorrect. The political scientist’s argument does not indicate that any particular conditions are necessary for political freedom, nor does it indicate that any particular conditions are sufficient to bring about political freedom. Thus the argument could not be said to confuse these two sorts of conditions. Rather, the political scientist’s argument attempts to demonstrate that democracy does not promote political freedom on the grounds that democracy is neither necessary nor sufficient for bringing about political freedom.",
                        }
                    ],
                }
            ]
        }
    }

class PersonCreate(PersonBase):
    """Creation payload for a Person."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "Susan",
                    "last_name": "Lee",
                    "email": "susanlee@gmail.com",
                    "birth_date": "1998-06-10",
                    "grade_level": "undergraduate",
                    "mistake": [
                        {
                            "id":"550e8400-e29b-41d4-a716-aaaaaaaaaaaa",
                            "subject":"lsat",
                            "key_concept":"Logical Reasoning",
                            "prompt":"Several critics have claimed that any contemporary poet who writes formal poetry—poetry that is rhymed and metered—is performing a politically conservative act. This is plainly false. Consider Molly Peacock and Marilyn Hacker, two contemporary poets whose poetry is almost exclusively formal and yet who are themselves politically progressive feminists. The conclusion drawn above follows logically if which one of the following is assumed?",
                            "correct_answer":"C. No one who is politically progressive is capable of performing a politically conservative act.",
                            "wrong_answer":"D.Anyone who sometimes writes poetry that is not politically conservative never writes poetry that is politically conservative.",
                            "reflection":"D says that anyone who sometimes writes poetry that is not politically conservative never writes poetry that is politically conservative. However, to make the conclusion of the argument follow logically, one must show that some contemporary poets who write formal poetry are sometimes not performing a politically conservative act. The information in (D) is not applicable to this question.",
                        }
                    ],
                }
            ]
        }
    }

class PersonUpdate(BaseModel):
    """Partial update for a Person; supply only fields to change."""
    first_name: Optional[str] = Field(None, json_schema_extra={"example": "Augusta"})
    last_name: Optional[str] = Field(None, json_schema_extra={"example": "King"})
    email: Optional[EmailStr] = Field(None, json_schema_extra={"example": "ada@newmail.com"})
    birth_date: Optional[date] = Field(None, json_schema_extra={"example": "1815-12-10"})
    grade_level: Optional[str] = Field(None, json_schema_extra={"example": "+44 20 7946 0958"})

    mistake: Optional[List[MistakeBase]] = Field(
        None, 
        description="Replace the entire set of mistakes with this list.",
        json_schema_extra={
            "examples": [
                {
                    "id":"550e8400-e29b-41d4-a716-446655440000",
                    "subject":"lsat",
                    "key_concept":"Logical Reasoning",
                    "prompt":"Political scientist: As a political system, democracy does not promote political freedom. There are historical examples of democracies that ultimately resulted in some of the most oppressive societies. Likewise, there have been enlightened despotisms and oligarchies that have provided a remarkable level of political freedom to their subjects. The reasoning in the political scientist’s argument is flawed because it",
                    "correct_answer":"D. overlooks the possibility that democracy promotes political freedom without being necessary or sufficient by itself to produce it",
                    "wrong_answer":"A. confuses the conditions necessary for political freedom with the conditions sufficient to bring it about",
                    "reflection":"A is incorrect. The political scientist’s argument does not indicate that any particular conditions are necessary for political freedom, nor does it indicate that any particular conditions are sufficient to bring about political freedom. Thus the argument could not be said to confuse these two sorts of conditions. Rather, the political scientist’s argument attempts to demonstrate that democracy does not promote political freedom on the grounds that democracy is neither necessary nor sufficient for bringing about political freedom.",
                }
            ]
        },
    )

class PersonRead(PersonBase):
    """Server representation returned to clients."""
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Person ID.",
        json_schema_extra={"example": "99999999-9999-4999-8999-999999999999"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-01-16T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "Susan",
                    "last_name": "Lee",
                    "email": "susanlee@gmail.com",
                    "birth_date": "1998-06-10",
                    "grade_level": "undergraduate",
                    "mistake": [
                        {
                            "id":"550e8400-e29b-41d4-a716-aaaaaaaaaaaa",
                            "subject":"lsat",
                            "key_concept":"Logical Reasoning",
                            "prompt":"Several critics have claimed that any contemporary poet who writes formal poetry—poetry that is rhymed and metered—is performing a politically conservative act. This is plainly false. Consider Molly Peacock and Marilyn Hacker, two contemporary poets whose poetry is almost exclusively formal and yet who are themselves politically progressive feminists. The conclusion drawn above follows logically if which one of the following is assumed?",
                            "correctanswer":"C. No one who is politically progressive is capable of performing a politically conservative act.",
                            "wrong answer":"D.Anyone who sometimes writes poetry that is not politically conservative never writes poetry that is politically conservative.",
                            "reflection":"D says that anyone who sometimes writes poetry that is not politically conservative never writes poetry that is politically conservative. However, to make the conclusion of the argument follow logically, one must show that some contemporary poets who write formal poetry are sometimes not performing a politically conservative act. The information in (D) is not applicable to this question.",
                        }
                    ],
                    "created_at": "2025-09-15T10:20:30Z",
                    "updated_at": "2025-09-16T12:00:00Z",
                }
            ]
        }
    }
