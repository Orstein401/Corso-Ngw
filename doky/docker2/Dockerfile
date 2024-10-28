# Utilizza un'immagine base di Python
FROM python:3.9-slim

MAINTAINER Alessandro

# Imposta il working directory
WORKDIR /app

# Copia i file necessari nella directory dell'app
COPY /python_lez/esercizio.py /app
COPY /python_lez/commedia.txt /app
COPY /python_lez/requirements.txt /app
COPY /python_lez/risultati_count.json /app
COPY /python_lez/.env_lez /app/.env_lez


# Installa le dipendenze necessarie
RUN pip install flask python-dotenv

# Espone la porta specificata nel file .env
# EXPOSE $PORT

# Comando per avviare l'applicazione
CMD ["python", "esercizio.py"]