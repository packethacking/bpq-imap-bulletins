FROM python:3.12

ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

CMD ["pipenv", "run", "python", "bpqmail.py"]
