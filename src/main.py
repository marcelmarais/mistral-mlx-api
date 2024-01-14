from datetime import datetime
from typing import List

from fastapi import FastAPI

from config.constants import MODEL_PATH
from data_models import (
    ChatCompletionResponse,
    CreateChatCompletionRequest,
    Message,
    Role,
)
from mistral_mlx.mistral import generate_text, load_model

model, tokenizer = load_model(MODEL_PATH)

app = FastAPI()


def convert_messages_to_prompt(messages: List[Message]):
    prompt = ""
    for msg in messages:
        if msg.role == Role.assistant:
            prompt += f"<s>[INST] {msg.content} [/INST] "
        else:
            prompt += f"{msg.content} </s> "
    return prompt


@app.post("/chat/completions", response_model=ChatCompletionResponse)
async def create_chat_completion(request: CreateChatCompletionRequest):
    prompt = convert_messages_to_prompt(messages=request.messages)

    generated_message = generate_text(
        prompt=prompt,
        model=model,
        tokenizer=tokenizer,
        max_tokens=request.max_tokens,
        temp=request.temperature,
        tokens_per_eval=10,
        seed=1,
    )

    request.messages.append(generated_message)

    response = ChatCompletionResponse(
        model="Mistral-7B-Instruct-v0.2",
        created=int(datetime.now().timestamp()),
        messages=request.messages,
    )

    return response
