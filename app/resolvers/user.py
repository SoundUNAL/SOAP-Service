import requests
from server import urlServer

def check_artist(username: str) -> bool:
    # Api gateway
    api_gateway = f"http://{urlServer}/graphql"

    # Query GraphQL con parámetros
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
        
        # Verificar si el microservicio envio información
        if graphql_data["data"]:
            
            # Verificar que el rol del usuario sea de artista 
            response = check_role(graphql_data["data"]["getId"])
            
            if response:
                return True
            
            print("El usuario no tiene rol de artista")
            return False

        # Hubo error en la petición al microservicio
        print ("Error de conexión")
        return False

    except requests.exceptions.RequestException as e:
        # Capturar y manejar cualquier error de solicitud
        print(f"Error al hacer la petición getId: {{}}".format(str(e)))
        return False
    
def check_role(id: int) -> bool:
    
    # Api gateway
    api_gateway = f"http://{urlServer}/graphql"
    
    # Query GraphQL con parámetros
    query  = f"""
        query {{
            getInfo(id: {id}) {{
                role
            }}
        }}
    """

    data = {"query": query}

    try:
        response = requests.post(api_gateway, json=data)
        response.raise_for_status()

        # Obtener los datos de la respuesta JSON
        graphql_data = response.json()
        print (graphql_data)
        
        # Verificar si el microservicio envio información
        if graphql_data["data"]:
            if graphql_data["data"]["getInfo"]["role"] == "2":
                return True
            
            else:
                return False

        # Hubo error en la petición al microservicio
        print ("Error de conexión")
        return False

    except requests.exceptions.RequestException as e:
        # Capturar y manejar cualquier error de solicitud
        print(f"Error al hacer la petición getInfo: {{}}".format(str(e)))
        return False