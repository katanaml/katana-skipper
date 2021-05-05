python dataservice.py

python -m grpc_tools.protoc -I ../protobufs --python_out=. \
   --grpc_python_out=. ../protobufs/dataservice.proto

pip install grpcio
pip install grpcio-tools