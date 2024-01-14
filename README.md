# Mistral 7b API (MLX)

This project uses Apples's MLX framework to run inference on a Mistral 7b instruct model for text generation over a simple API. 

## Setup

1. Clone the repository.
2. Run `download_model.sh` to download the Mistral MLX model and setup the virtual environment.
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
