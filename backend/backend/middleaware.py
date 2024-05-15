from django.http import HttpResponse

class CORSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Si es una solicitud OPTIONS (preflight), devuelve una respuesta vacía
        if request.method == 'OPTIONS':
            response = HttpResponse()
        else:
            # Pasa la solicitud al siguiente middleware
            response = self.get_response(request)

        # Configura los encabezados CORS para permitir cualquier origen
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
        response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Origin, Access-Control-Allow-Methods, Access-Control-Allow-Headers, Content-Type, Authorization"

        return response
