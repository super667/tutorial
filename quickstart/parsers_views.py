from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView


class ExampleView(APIView):
    """
    A View that can accept POST requests with JSON content.
    """
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        return Response({"receive data": request.data})



from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser


@api_view(["post"])
@parser_classes([JSONParser])
def example(request, format=True):
    """
    A view than can accept POST requests with JSON content.
    """
    return Response({"receive data": request.data})


from rest_framework.parsers import FileUploadParser

class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        print(file_obj)
        return Response(status=204)


from rest_framework.parsers import BaseParser

class PlainTextParser(BaseParser):
    """
    Plain text parser.
    自定义实现一个解析器类
    """
    media_type = 'text/plain'


    def parse(self, stream, media_type=None, parser_context=None):
        return stream.read()


