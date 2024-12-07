# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster
FROM mcr.microsoft.com/playwright:v1.49.0-noble
# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
# (including run.py, filmpertutti.py, and requirements.txt)
ADD . /app
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
#RUN playwright install
#RUN playwright install-deps
#EXPOSE the port, for now default is 8080 cause it's the only one really allowed by HuggingFace
EXPOSE 8080

# Run run.py when the container launches
CMD ["python", "run.py"]