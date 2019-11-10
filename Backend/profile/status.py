from enum import IntEnum

# django-rest-framework.org/api-guide/status-codes/
class Code(IntEnum):
    HTTP_100_CONTINUE = 100
    HTTP_200_OK = 200
    HTTP_201_CREATED = 201
    HTTP_404_NOT_FOUND = 404