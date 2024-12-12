# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
    nmap \
    chromium \
    harfbuzz \
    libfreetype6 \
    fonts-freefont-ttf \
    libnss3 && \
    # Pulisci la cache di apt per ridurre le dimensioni dell'immagine
    rm -rf /var/lib/apt/lists/*

# Imposta la variabile di ambiente per il browser Chromium
ENV CHROME_BIN=/usr/bin/chromium


# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
# (including run.py, filmpertutti.py, and requirements.txt)
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps chromium
#EXPOSE the port, for now default is 8080 cause it's the only one really allowed by HuggingFace
EXPOSE 8080

# Run run.py when the container launches
CMD ["python", "run.py"]