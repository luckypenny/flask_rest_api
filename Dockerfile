FROM python:3.7.7

LABEL Author="YoungHo Kim"
LABEL E-mail="luckypenny79@gmail.com"
LABEL version="1.0.0"

ENV FLASK_APP "api.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /app
RUN echo "alias ll='ls -al'" >> ~/.bashrc
WORKDIR /app

COPY Pip* /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

COPY src /app

EXPOSE 5000

CMD flask run --host=0.0.0.0