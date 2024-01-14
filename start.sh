#!/bin/bash

# Check if the venv directory exists
if [ ! -d "venv" ]; then
    echo "venv directory not found, creating a new one..."
    # If it doesn't exist, create it
    python -m venv venv
    echo "venv directory created."

    # Activate the virtual environment
    echo "Activating the virtual environment..."
    source venv/bin/activate
    echo "Virtual environment activated."

    # Install the requirements
    echo "Installing requirements from requirements.txt..."
    pip install -r requirements.txt
    echo "Requirements installed."
else
    echo "venv directory found."
    echo "Activating the virtual environment..."
    source venv/bin/activate
    echo "Virtual environment activated."
fi

cd src

# Run the FastAPI server using uvicorn
echo "Starting the FastAPI server."
uvicorn main:app --reload