# Imagen base con Python
FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios
COPY requirements.txt requirements.txt

# Instalar dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar el resto del código
COPY . .

# Exponer el puerto que usará Django
EXPOSE 8000

# Comando por defecto para iniciar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
