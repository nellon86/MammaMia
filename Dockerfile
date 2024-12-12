FROM debian:bullseye

# Install basic dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    fonts-liberation \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Add Google Chrome repository
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/bin/chromium-browser.gpg

# Install Google Chrome
RUN apt-get update && apt-get install -y \
    google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

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