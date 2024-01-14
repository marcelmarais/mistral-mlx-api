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
from mistral_mlx.mistral import generate_text_from_tokens, load_model
import mlx.core as mx

model, tokenizer = load_model(MODEL_PATH)

app = FastAPI()


def convert_messages_to_prompt_tokens(messages: List[Message]) -> mx.array:
    prompt = []
    for msg in messages:
        if msg.role == Role.user:
            prompt.extend(tokenizer.encode(f"[INST] {msg.content} [/INST]"))
        else:
            prompt.extend(tokenizer.encode(msg.content))
            prompt.append(tokenizer.eos_id)
    
    return mx.array(prompt)


@app.post("/chat/completions", response_model=ChatCompletionResponse)
async def create_chat_completion(request: CreateChatCompletionRequest):
    prompt_tokens = convert_messages_to_prompt_tokens(messages=request.messages)

    generated_message = generate_text_from_tokens(
        prompt_tokens=prompt_tokens,
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
