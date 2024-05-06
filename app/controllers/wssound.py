from pydantic_xml import element
from fastapi_soap import SoapRouter, XMLBody, SoapResponse
from fastapi_soap.models import BodyContent
from resolvers.song import upload_song

# soap web service route
soap_router = SoapRouter(name='WSSound', prefix='/wssound')

""" Data operaciones """

# Parametros de entrada de la operación CheckArtist
class ArtistData(BodyContent, tag="DataArtist"):
    userUsername: int = element(tag="Username")

# Parametros de salida de la operación CheckArtist
class ArtistResponse(BodyContent, tag="Response"):
    value: bool

# Parametros de entrada de la operación UploadSong
class SongData(BodyContent, tag="DataSong"):
    title: str = element(tag="Title")
    publicationDate: str = element(tag="PublicationDate")
    lyrics: str = element(tag="Lyrics")
    version: int = element(tag="Version")
    userid: int = element(tag="Userid")
    audioid: str = element(tag="Audioid")
    albumid: int = element(tag="Albumid")

# Parametros de salida de la operación UploadSong
class SongResponse(BodyContent, tag="Response"):
    value: bool
    
""" Operaciones """

# Definir operación para validar un artista
@soap_router.operation(
    name="CheckArtist",
    request_model=ArtistData,
    response_model=ArtistResponse
)

def checkArtist_operation(body: ArtistData = XMLBody(ArtistData)):
    """ Operación para validar un artista """
    
    result = sum(body.operands)
    
    return SoapResponse(
        ArtistResponse(value=result)
    )

# Definir operación para subir una canción
@soap_router.operation(
    name="UploadSong",
    request_model=SongData,
    response_model=SongResponse
)

def uploadSong_operation(body: SongData = XMLBody(SongData)):
    """ Operación para subir una canción """
    
    result = upload_song(
                body.albumid,
                body.audioid,
                body.lyrics,
                body.publicationDate,
                body.title,
                body.userid,
                body.version
            )
    
    return SoapResponse(
        SongResponse(value=result)
    )

