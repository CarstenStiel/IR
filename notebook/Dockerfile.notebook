# Basisimage
FROM webis/tira-ir-starter-pyterrier:0.0.1-base

# Setzen der Arbeitsverzeichnis
WORKDIR /app

COPY ./ ./

# Aktualisieren von pip und Installation von Jupyter Notebook
RUN apt-get update && apt-get install -y python3-pip \
    && pip3 install jupyter pyterrier \
    && pip3 install tira

EXPOSE 8888

# Starten von Jupyter Notebook
CMD ["jupyter", "notebook", "--allow-root", "--ip", "0.0.0.0"]