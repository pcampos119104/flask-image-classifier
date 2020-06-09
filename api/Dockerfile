FROM python:3.8-slim

WORKDIR /app
RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv install --system

COPY ./code ./
CMD ["python", "app.py"] 
