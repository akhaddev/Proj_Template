# import grpc
# from concurrent import futures
# import example_pb2
# import example_pb2_grpc
# from grpc_reflection.v1alpha import reflection


# # Implement the gRPC service
# class ExampleServiceServicer(example_pb2_grpc.ExampleServiceServicer):
#     def SayHello(self, request, context):
#         return example_pb2.HelloResponse(message=f'Hello, {request.name}!')

# # Start the gRPC server
# def serve():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
#     # Add your service to the server
#     example_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleServiceServicer(), server)
    
#     # Add reflection for the service
#     SERVICE_NAMES = (
#         example_pb2.DESCRIPTOR.services_by_name['ExampleService'].full_name,
#         reflection.SERVICE_NAME,
#     )
#     reflection.enable_server_reflection(SERVICE_NAMES, server)

#     server.add_insecure_port('[::]:50051')
#     server.start()
#     print("gRPC server running on port 50051 with reflection enabled...")
#     server.wait_for_termination()


# if __name__ == "__main__":
#     serve()




import grpc
from concurrent import futures
import product_pb2
import product_pb2_grpc
from grpc_reflection.v1alpha import reflection

# Connect to the gRPC server
channel = grpc.insecure_channel('localhost:50051')
stub = product_pb2_grpc.ProductServiceStub(channel)

# Helper function to print product details
def print_product(response):
    print(f"Product ID: {response.id}")
    print(f"Title: {response.title}")
    print(f"Price: {response.price}")
    print(f"Image: {response.image}")
    print(f"Description: {response.description}")
    print(f"Category ID: {response.category_id}")

# 1. Test CreateProduct
def create_product():
    try:
        response = stub.CreateProduct(product_pb2.CreateProductRequest(
            title="Sample Product",
            price=19.99,
            image="sample_image.png",
            description="This is a sample product description",
            category_id=1  # Ensure you have a category with ID 1 in your database
        ))
        print("Product created:")
        print_product(response)
    except grpc.RpcError as e:
        print(f"CreateProduct failed: {e.details()}")

# 2. Test GetProduct
def get_product(product_id):
    try:
        response = stub.GetProduct(product_pb2.GetProductRequest(id=product_id))
        print("Product retrieved:")
        print_product(response)
    except grpc.RpcError as e:
        print(f"GetProduct failed: {e.details()}")

# 3. Test UpdateProduct
def update_product(product_id):
    try:
        response = stub.UpdateProduct(product_pb2.UpdateProductRequest(
            id=product_id,
            title="Updated Product Title",
            price=29.99,
            image="updated_image.png",
            description="This is an updated product description",
            category_id=1  # Ensure this category exists
        ))
        print("Product updated:")
        print_product(response)
    except grpc.RpcError as e:
        print(f"UpdateProduct failed: {e.details()}")

# 4. Test DeleteProduct
def delete_product(product_id):
    try:
        response = stub.DeleteProduct(product_pb2.DeleteProductRequest(id=product_id))
        print(f"Product with ID {product_id} deleted successfully.")
    except grpc.RpcError as e:
        print(f"DeleteProduct failed: {e.details()}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServiceServicer_to_server(product_pb2_grpc.ProductService(), server)

    # Enable gRPC reflection
    SERVICE_NAMES = (
        product_pb2.DESCRIPTOR.services_by_name['ProductService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')  # Bind to all interfaces
    server.start()
    print("gRPC server running on port 50051 with reflection enabled...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
