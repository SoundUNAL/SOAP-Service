# SOAP-Service
Servicio SOAP de SoUNd que cuenta con dos operaciones para verificar que un usuario exista, tenga rol de artista, y si es asi, suba una canción a la aplicación SoUNd.

# Correr el proyecto : 
- Crear ambiente : py -m venv .venv
- Entrar al ambiente virtual : .venv\Scripts\activate
- Descargar los paquetes de pip : pip install -r .\requirements.txt
- Ubicarse en el directorio app : cd app
- Desplegar el proyecto en carpeta app : uvicorn main:app --reload --port 9000
