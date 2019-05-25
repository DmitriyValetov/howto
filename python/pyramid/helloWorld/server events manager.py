            
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.events import NewRequest
from pyramid.events import NewResponse
from pyramid.events import subscriber
from pyramid.response import Response
from pyramid.view import view_config


@view_config(
    route_name='home',
)
def home(request):
    return Response('Welcome!')

# 1) 
# @subscriber(NewRequest, NewResponse)
# def mysubscriber(event):
#     print('event NewRequest/NewResponse ', event)

# 2)
@subscriber(NewRequest)
def mysubscriber1(event):
    print('event NewRequest ', event)

# 3)
@subscriber(NewResponse)
def mysubscriber2(event):
    print('event NewResponse ', event)

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()

          