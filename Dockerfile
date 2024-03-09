FROM python:3.12-bookworm
ENV DOMAIN_FILE=/app/domains.yaml
USER root
RUN groupadd -g 10000 python && useradd -u 10000 -g python -m -d /app python
USER python
WORKDIR /app
COPY --chown=python:python domains.yaml monitoring.py requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir --user
CMD [ "python", "monitoring.py" ]
