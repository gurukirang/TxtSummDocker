FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir flask spacy \
 && python -m spacy download en_core_web_sm
EXPOSE 5000
CMD ["python", "app.py"]
