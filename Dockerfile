FROM python:3.11-slim
WORKDIR /usr/src/app

# Evitar prompts interactivos y cache innecesaria
ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Carpeta de trabajo montada desde el host
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token="]
