# RPC Server for CMPE273 lab2
# Add function is implemented

from concurrent import futures
import time
import grpc

import calc_pb2
import calc_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Calculator (calc_pb2_grpc.CalculatorServicer):
    def add(self, request, context):
        return calc_pb2.AddResult(result = request.num1 + request.num2)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calc_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()