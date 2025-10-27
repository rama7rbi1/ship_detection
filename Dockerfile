FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY . .
COPY web_interface/models/best.pt models/best.pt

RUN pip install --upgrade pip
RUN pip install -r web_interface/requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "web_interface/app.py"]
