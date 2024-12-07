# Stage 1: Usa l'immagine di Python come base per installare Python e le dipendenze
FROM python:3.10-slim-buster AS python-base

# Installa Playwright e le dipendenze necessarie
RUN pip install --no-cache-dir playwright

# Stage 2: Usa l'immagine di Playwright
FROM mcr.microsoft.com/playwright:v1.49.0-noble

# Copia Python e i file relativi da python-base
COPY --from=python-base /usr/local /usr/local
COPY --from=python-base /usr/lib/python3.10 /usr/lib/python3.10
COPY --from=python-base /usr/bin/python3 /usr/bin/python3
COPY --from=python-base /usr/bin/pip3 /usr/bin/pip3

# Configura Python come eseguibile predefinito
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
