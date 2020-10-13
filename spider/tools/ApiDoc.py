from drf_yasg import openapi


class APIDoc(object):
    openapi = openapi

    def __init__(self):
        self.GET_ARGS = []

    def add_GET_ARGS(self, arg, description, type=openapi.TYPE_STRING, required=False):
        self.GET_ARGS.append(
            openapi.Parameter(arg, openapi.IN_QUERY, description=description, type=type, required=required))

    def get_GET_ARGS(self):
        return self.GET_ARGS
