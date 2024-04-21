
FROM python:3.12

# Ustawiamy zmienną środowiskową
ENV APP_HOME /app

# Ustawiamy katalog roboczy wewnątrz kontenera
WORKDIR $APP_HOME

# Kopiujemy inne pliki do katalogu roboczego kontenera
COPY . .

# Instalujemy zależności wewnątrz kontenera
RUN pip install -e .

# Oznaczamy port, na którym aplikacja działa wewnątrz kontenera
EXPOSE 8000

# Uruchomiamy naszą aplikację wewnątrz kontenera
ENTRYPOINT ["personal-assistant"]