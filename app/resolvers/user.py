import requests
from server import url, apigateway_port

def check_artist(username: str) -> bool:
    # Api gateway
    api_gateway = f"http://{url}:{apigateway_port}/graphql"

    # Mutation GraphQL con parámetros
    query  = f"""
        query {{
            getId(
                username: "{username}"
            )
        }}
    """

    data = {"query": query}

    try:
        response = requests.post(api_gateway, json=data)
        response.raise_for_status()

        # Obtener los datos de la respuesta JSON
        graphql_data = response.json()
        print (graphql_data)
        
        # Verificar si se envio información a la cola del api-gateway
        if graphql_data["data"]:
            return True

        # Hubo error en la petición al microservicio
        print ("Error de conexión")
        return False

    except requests.exceptions.RequestException as e:
        # Capturar y manejar cualquier error de solicitud
        print(f"Error al hacer la petición getId: {{}}".format(str(e)))
        return False