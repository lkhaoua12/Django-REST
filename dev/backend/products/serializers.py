"""
Serializers for Product objects in the REST API.
"""

from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.
    """

    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='products-update', lookup_field='pk'
        )

    class Meta:
        model = Product
        fields = ['url', 'edit_url', 'title', 'price', 'content', 'sale_price', 'get_discount']

    def get_url(self, obj):
        """
        Get the URL of the product.
        """
        request = self.context.get('request')
        return reverse('products-detail', kwargs={'pk': obj.id}, request=request)
    
    def validate_title(self, value):
        """
        Validate the title field.
        """
        if len(value) > 100:
            raise serializers.ValidationError('Title is too long')
        if Product.objects.filter(title__exact=value).exists():
            raise serializers.ValidationError('Title already exists')
        if 'review' in value.lower():
            raise serializers.ValidationError('Title cannot contain "review"')
        return value

