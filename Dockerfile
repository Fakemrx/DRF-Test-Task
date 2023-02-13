FROM python:3.9

RUN mkdir -p /usr/src/docker/
WORKDIR /usr/src/docker/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Pipfile Pipfile.lock ./

RUN pip install -U pipenv
RUN pipenv install --system

COPY . .

EXPOSE 8000

ENTRYPOINT ["/usr/src/docker/entrypoint.sh"]