# Step 1: Use a lightweight Python base image
FROM python:3.11-slim

# Step 2: Set up a non-root user for security (Required by HF Spaces)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Step 3: Set the working directory
WORKDIR $HOME/app

# Step 4: Install system dependencies needed for spaCy/NLP
# We use 'root' briefly to install packages, then switch back
USER root
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*
USER user

# Step 5: Copy requirements and install them
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Step 6: Download the spaCy model
RUN python -m spacy download en_core_web_sm

# Step 7: Copy the rest of your application code
COPY --chown=user . .

# Step 8: Start the application on Port 7860 (HF Default)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]