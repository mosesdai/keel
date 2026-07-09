# Build context: repository root (when Railway Root Directory is empty or /)
# Recommended: Service Settings → Root Directory = track-a (uses track-a/Dockerfile instead).
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY track-a/server/requirements.txt /app/server/requirements.txt
RUN pip install --no-cache-dir -r /app/server/requirements.txt

COPY track-a/server /app/server
COPY track-a/data /app/data

WORKDIR /app/server
ENV TRACK_A_DATA_DIR=/app/data

EXPOSE 8787

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8787}"]
