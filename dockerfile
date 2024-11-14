# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /embeddings_llm_bootcamp

# Copy requirements file
COPY requirements.toml .
COPY .model/bin/ ./model/bin

# Install dependencies
RUN poetry install

# Copy Python script
COPY ./scripts ./scripts
COPY .main.py .


# Make port available
EXPOSE 8000

# Run command
CMD ["python", "main.py"]
