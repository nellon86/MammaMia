# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

RUN apk update && apk add --no-cache nmap && \
    echo @edge https://dl-cdn.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories && \
    echo @edge https://dl-cdn.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories && \
    apk update && \
    apk add --no-cache \
      chromium \
      harfbuzz \
      "freetype>2.8" \
      ttf-freefont \
      nss


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