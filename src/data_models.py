from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class Role(str, Enum):
    user = "user"
    assistant = "assistant"


class Message(BaseModel):
    role: Role = Field(..., description="Role of the message")
    content: str


class CreateChatCompletionRequest(BaseModel):
    messages: List[Message]
    max_tokens: int = 256
    temperature: float = Field(default=0.5, ge=0, le=1)


class ChatCompletionResponse(BaseModel):
    model: str
    created: int
    messages: List[Message]
