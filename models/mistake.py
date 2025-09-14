from __future__ import annotations

from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class MistakeBase(BaseModel):
    id: UUID = Field(
        default_factory=uuid4,
        description="Persistent Address ID (server-generated).",
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"},
    )
    subject: str = Field(
        ...,
        description="subject name of test question",
        json_schema_extra={"example": "lsat"},
    )
    key_concept: str = Field(
        ...,
        description="concept/concept type in the specific question",
        json_schema_extra={"example": "Logical Reasoning"},
    )
    prompt: str = Field(
        ...,
        description="test question",
        json_schema_extra={"example": "Political scientist: As a political system, democracy does not promote political freedom. There are historical examples of democracies that ultimately resulted in some of the most oppressive societies. Likewise, there have been enlightened despotisms and oligarchies that have provided a remarkable level of political freedom to their subjects. The reasoning in the political scientist’s argument is flawed because it"},
    )
    correct_answer: str = Field(
        ...,
        description="correct answer for the question",
        json_schema_extra={"example": "D. overlooks the possibility that democracy promotes political freedom without being necessary or sufficient by itself to produce it"},
    )
    wrong_answer: str = Field(
        ...,
        description="wrong answer you chose for the question",
        json_schema_extra={"example": "A. confuses the conditions necessary for political freedom with the conditions sufficient to bring it about"},
    )
    reflection: str = Field(
        ...,
        description="explain why you chose the wrong answer, and why the correct answer is correct",
        json_schema_extra={"example": "A is incorrect. The political scientist’s argument does not indicate that any particular conditions are necessary for political freedom, nor does it indicate that any particular conditions are sufficient to bring about political freedom. Thus the argument could not be said to confuse these two sorts of conditions. Rather, the political scientist’s argument attempts to demonstrate that democracy does not promote political freedom on the grounds that democracy is neither necessary nor sufficient for bringing about political freedom."},
    )
    model_config = {
        "json_schema_extra": {
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
        }
    }

class MistakeCreate(MistakeBase):
    """Creation payload; ID is generated server-side but present in the base model."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id":"550e8400-e29b-41d4-a716-aaaaaaaaaaaa",
                    "subject":"lsat",
                    "key_concept":"Logical Reasoning",
                    "prompt":"Several critics have claimed that any contemporary poet who writes formal poetry—poetry that is rhymed and metered—is performing a politically conservative act. This is plainly false. Consider Molly Peacock and Marilyn Hacker, two contemporary poets whose poetry is almost exclusively formal and yet who are themselves politically progressive feminists. The conclusion drawn above follows logically if which one of the following is assumed?",
                    "correct_answer":"C. No one who is politically progressive is capable of performing a politically conservative act.",
                    "wrong_answer":"D.Anyone who sometimes writes poetry that is not politically conservative never writes poetry that is politically conservative.",
                    "reflection":"D says that anyone who sometimes writes poetry that is not politically conservative never writes poetry that is politically conservative. However, to make the conclusion of the argument follow logically, one must show that some contemporary poets who write formal poetry are sometimes not performing a politically conservative act. The information in (D) is not applicable to this question.",
                }
            ]
        }
    }

class MistakeUpdate(BaseModel):
    """Partial update; address ID is taken from the path, not the body."""
    subject: Optional[str] = Field(
        None, description="subject name of test question",
        json_schema_extra={"example": "lsat"}
    )
    key_concept: Optional[str] = Field(
        None, description="concept/concept type in the specific question",
        json_schema_extra={"example": "Logical Reasoning"}
    )
    prompt: Optional[str] = Field(
        None, description="test question",
        json_schema_extra={"example": "Political scientist: As a political system, democracy does not promote political freedom. There are historical examples of democracies that ultimately resulted in some of the most oppressive societies. Likewise, there have been enlightened despotisms and oligarchies that have provided a remarkable level of political freedom to their subjects. The reasoning in the political scientist’s argument is flawed because it"}
    )
    correct_answer: Optional[str] = Field(
        None, description="correct answer for the question",
        json_schema_extra={"example": "D. overlooks the possibility that democracy promotes political freedom without being necessary or sufficient by itself to produce it"}
    )
    wrong_answer: Optional[str] = Field(
        None, description="wrong answer you chose for the question",
        json_schema_extra={"example": "A. confuses the conditions necessary for political freedom with the conditions sufficient to bring it about"}
    )
    reflection: Optional[str] = Field(
        None, description="explain why you chose the wrong answer, and why the correct answer is correct",
        json_schema_extra={"example": "A is incorrect. The political scientist’s argument does not indicate that any particular conditions are necessary for political freedom, nor does it indicate that any particular conditions are sufficient to bring about political freedom. Thus the argument could not be said to confuse these two sorts of conditions. Rather, the political scientist’s argument attempts to demonstrate that democracy does not promote political freedom on the grounds that democracy is neither necessary nor sufficient for bringing about political freedom."}
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id":"550e8400-e29b-41d4-a716-aaaaaaaaaaaa",
                    "subject":"lsat",
                    "key_concept":"Logical Reasoning",
                    "prompt":"Several critics have claimed that any contemporary poet who writes formal poetry—poetry that is rhymed and metered—is performing a politically conservative act. This is plainly false. Consider Molly Peacock and Marilyn Hacker, two contemporary poets whose poetry is almost exclusively formal and yet who are themselves politically progressive feminists. The conclusion drawn above follows logically if which one of the following is assumed?",
                    "correct_answer":"C. No one who is politically progressive is capable of performing a politically conservative act.",
                    "wrong_answer":"D.Anyone who sometimes writes poetry that is not politically conservative never writes poetry that is politically conservative.",
                    "reflection":"D says that anyone who sometimes writes poetry that is not politically conservative never writes poetry that is politically conservative. However, to make the conclusion of the argument follow logically, one must show that some contemporary poets who write formal poetry are sometimes not performing a politically conservative act. The information in (D) is not applicable to this question.",
                },
                {"key_concept": "Reading Comprehension"},
            ]
        }
    }

class MistakeRead(MistakeBase):
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
                    "id":"550e8400-e29b-41d4-a716-446655440000",
                    "subject":"lsat",
                    "key_concept":"Logical Reasoning",
                    "prompt":"Several critics have claimed that any contemporary poet who writes formal poetry—poetry that is rhymed and metered—is performing a politically conservative act. This is plainly false. Consider Molly Peacock and Marilyn Hacker, two contemporary poets whose poetry is almost exclusively formal and yet who are themselves politically progressive feminists. The conclusion drawn above follows logically if which one of the following is assumed?",
                    "correct_answer":"C. No one who is politically progressive is capable of performing a politically conservative act.",
                    "wrong_answer":"D.Anyone who sometimes writes poetry that is not politically conservative never writes poetry that is politically conservative.",
                    "reflection":"D says that anyone who sometimes writes poetry that is not politically conservative never writes poetry that is politically conservative. However, to make the conclusion of the argument follow logically, one must show that some contemporary poets who write formal poetry are sometimes not performing a politically conservative act. The information in (D) is not applicable to this question.",
                    "created_at": "2025-01-15T10:20:30Z",
                    "updated_at": "2025-01-16T12:00:00Z",
                }
            ]
        }
    }
