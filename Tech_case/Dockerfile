# pull official base image
FROM python:3.9

SHELL ["/bin/bash", "-c"]
# set work directory

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim


RUN useradd -rms /bin/bash tc && chmod 777 /opt /run

WORKDIR /tc

RUN mkdir /tc/static && mkdir /tc/media && chown -R tc:tc /tc && chmod 755 /tc

COPY --chown=tc:tc . .

RUN pip install -r requirements.txt

USER tc

CMD ["gunicorn","-b","0.0.0.0:8001","Tech_case.wsgi:application"]

