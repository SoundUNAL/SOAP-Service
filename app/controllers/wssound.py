from pydantic_xml import element
from fastapi_soap import SoapRouter, XMLBody, SoapResponse
from fastapi_soap.models import BodyContent

# soap web service route
soap_router = SoapRouter(name='WSSound', prefix='/wssound')

