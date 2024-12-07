# Stage 1: Usa Python per installare Python e le dipendenze
FROM python:3.10-slim-buster AS python-base

# Installa pip e Playwright
RUN apt-get update && apt-get install -y curl && \
    pip install --no-cache-dir playwright

# Stage 2: Usa Playwright come base
FROM mcr.microsoft.com/playwright:v1.49.0-noble

# Copia Python e pip dallo stage precedente
COPY --from=python-base /usr/local /usr/local
COPY --from=python-base /usr/bin/python3 /usr/bin/python3
COPY --from=python-base /usr/bin/pip3 /usr/bin/pip3

# Configura Python e pip come comandi predefiniti
RUN ln -s /usr/bin/python3 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file del progetto
COPY . /app

# Installa le dipendenze del progetto
RUN pip install --no-cache-dir -r requirements.txt

# Espone la porta 8080
EXPOSE 8080

# Comando per avviare il progetto
CMD ["python", "run.py"]
