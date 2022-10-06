from grpc import ssl_channel_credentials, secure_channel

from src.gajou_api.grpc import BaseStub

# unfortunately there is no public gRPC to demonstrate real working example

# there should be imports from codegen files
from .generated import example_pb2 as pb2
from .generated import example_pb2_grpc as pb2_grpc


# API describer class should be inherited from BaseStub
class ExampleClient(BaseStub):
    def __init__(self, channel):
        super().__init__(channel, pb2_grpc.ExampleStub)

    def example_request(self, some_param):
        request = pb2.ExampleRequest(some_param=some_param)
        return self.stub.CountOrdersByClientID(request)


# need to create channel and pass it to gRPC client
channel = secure_channel('some-host.com:443', ssl_channel_credentials())
example_grpc = ExampleClient(channel)

response = example_grpc.example_request('bazinga')
