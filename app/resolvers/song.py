import requests
from server import url, apigateway_port

def upload_song(albumid: int, audioid: str, lyrics: str, publication_date: str, title: str, userid: str, version: int):
    # Api gateway
    api_gateway = f"http://{url}:{apigateway_port}/graphql"

    # Mutation GraphQL con parámetros
    mutation  = f"""
        mutation {{
            createSong(
                albumid: {albumid}
                audioid: "{audioid}"
                lyrics: "{lyrics}"
                publicationDate: "{publication_date}"
                title: "{title}"
                userid: "{userid}"
                version: {version}
            )
        }}
    """

    data = {"query": mutation}

    try:
        response = requests.post(api_gateway, json=data)
        response.raise_for_status()

        # Obtener los datos de la respuesta JSON
        graphql_data = response.json()
        print (graphql_data)
        
        # Verificar si se envio información a la cola del api-gateway
        if graphql_data["data"]:
            return True

        # Hubo error en la cola de subida de la canción
        print ("Error en la cola de rabbitMQ al subir la canción")
        return False

    except requests.exceptions.RequestException as e:
        # Capturar y manejar cualquier error de solicitud
        print(f"Error al hacer la mutación createSong: {{}}".format(str(e)))
        return False
