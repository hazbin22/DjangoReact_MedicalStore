from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer

# API view for listing products (GET) and creating new ones (POST)
class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

# API view for retrieving (GET), updating (PUT/PATCH), or deleting (DELETE) a single product
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # Use 'pk' (primary key) for retrieving single products by default
    permission_classes = [IsAuthenticated]