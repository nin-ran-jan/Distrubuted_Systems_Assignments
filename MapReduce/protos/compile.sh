#! /bin/bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mapper.proto  
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. reducer.proto  

mv -f *.py ../


