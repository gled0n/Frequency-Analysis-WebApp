FROM ubuntu:rolling
USER root
RUN export DEBIAN_FRONTEND="noninteractive" \
  && apt-get update && apt-get install -y --no-install-recommends \
    python3-setuptools     \
    python3-wheel          \
    python3-pip            \
    less                  \
    nano                  \
    sudo                  \
    git                   \
    npm                   \
  && rm -rf /var/lib/apt/lists/*
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run PIN_Seminar.py
