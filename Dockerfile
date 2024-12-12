# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y \
    nmap \
    chromium \
    fonts-freefont-ttf \
    libharfbuzz0b \
    libfreetype6 \
    libnss3 && \
    rm -rf /var/lib/apt/lists/

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
# (including run.py, filmpertutti.py, and requirements.txt)
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
#EXPOSE the port, for now default is 8080 cause it's the only one really allowed by HuggingFace
EXPOSE 8080

# Run run.py when the container launches
CMD ["python", "run.py"]