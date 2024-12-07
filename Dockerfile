# Usa l'immagine Playwright ufficiale basata su Python
FROM mcr.microsoft.com/playwright:v1.49.0-noble

# Aggiorna i pacchetti di sistema e installa pip se non presente
RUN apt-get update && apt-get install -y python3-pip

# Imposta la directory di lavoro nel container
WORKDIR /app

# Copia il contenuto della directory corrente nel container
COPY . /app

# Installa le dipendenze Python
RUN pip install --no-cache-dir -r requirements.txt

# Installa Playwright e le dipendenze necessarie per i browser
RUN playwright install && playwright install-deps

# Espone la porta 8080 per il servizio
EXPOSE 8080

# Comando per avviare l'app
CMD ["python", "run.py"]
