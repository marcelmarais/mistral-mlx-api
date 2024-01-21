# Mistral 7b API (using MLX)

This project uses Apple's MLX framework to allow text generation on a Mistral 7b instruct model through a straightforward OpenAI style API. The code is modified from the version available [here](https://huggingface.co/mlx-community/Mistral-7B-Instruct-v0.2). 

## Setup

1. Clone the repository.
2. Run `download_model.sh` to download the Mistral-7B-Instruct-v0.2 weights and tokenizer (it also sets up the virtual environment)
3. Run the FastAPI server with `start.sh`
## API

The API has a single endpoint `/chat/completions` which accepts a POST request with a list of messages and returns a generated message from the Mistral-7b model. Here's an example request:

```bash
curl  -X POST \
  'http://localhost:8000/chat/completions' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "messages": [
    {
      "role": "assistant",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Who won the world series in 2020?"
    }
  ],
  "max_tokens": 60,
  "temperature": 0.5
}'
```

## Contributing

Contributions are welcome. Please submit a pull request or create an issue to discuss the changes.
