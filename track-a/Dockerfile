# Build context: track-a/ (Railway Root Directory = track-a)
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY server/requirements.txt /app/server/requirements.txt
RUN pip install --no-cache-dir -r /app/server/requirements.txt

COPY server /app/server
COPY data /app/data

WORKDIR /app/server
ENV TRACK_A_DATA_DIR=/app/data

EXPOSE 8787

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8787}"]
