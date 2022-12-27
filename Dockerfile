FROM python:3.10.5
RUN apt update && apt install -y \
    curl
ENV DISPLAY host.docker.internal:0
WORKDIR project
ENV PYTHONPATH "${PYTHONPATH}:/project"
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src ./src
ENTRYPOINT ["python", "src/main.py"]
