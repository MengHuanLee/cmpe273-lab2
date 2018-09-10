# RPC Client for CMPE273 lab2
# Add function is implemented

import grpc

import calc_pb2
import calc_pb2_grpc

def run(input_num1, input_num2):
    with grpc.insecure_channel('localhost:50050') as channel:
        stub = calc_pb2_grpc.CalculatorStub(channel)
        response = stub.add(calc_pb2.AddRequest(num1=input_num1, num2=input_num2))
        print(input_num1, " + ", input_num2, " = ", response.result)

if __name__ == '__main__':
    print("Welcome to simple adder!")
    input_num1 = float(input("Please input the first number: "))
    input_num2 = float(input("Please input the second number: "))
    run(input_num1,input_num2)