from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single product instance.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    """
    List all products or create a new product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """
        Create a new product instance with validated data.
        If 'content' is not provided, set it to 'No content'.
        """
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or 'No content'
        serializer.save(title=title, content=content)


class ProductUpdateView(generics.UpdateAPIView):
    """
    Update an existing product instance.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        """
        Update an existing product instance with validated data.
        If 'content' is not provided, set it to 'No content'.
        """
        instance = serializer.save()
        if not instance.content:
            instance.content = 'No content'
            instance.save()


class ProductDeleteView(generics.DestroyAPIView):
    """
    Delete an existing product instance.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        """
        Perform deletion of a product instance.
        """
        return super().perform_destroy(instance)
