# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

RUN apt-get update && apt-get install -y unzip && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libappindicator3-1 \
    libasound2 \
    libnspr4 \
    fonts-liberation \
    libappindicator3-1 \
    libxtst6 \
    lsb-release \
    wget \
    ca-certificates \
    libgbm1 \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
# (including run.py, filmpertutti.py, and requirements.txt)
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
#EXPOSE the port, for now default is 8080 cause it's the only one really allowed by HuggingFace
EXPOSE 8080

# Run run.py when the container launches
CMD ["python", "run.py"]