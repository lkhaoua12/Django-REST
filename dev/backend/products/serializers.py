from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='products-update', lookup_field='pk'
        )
    class Meta:
        model = Product
        fields = ['url', 'edit_url', 'title', 'price', 'content', 'sale_price', 'get_discount']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse('products-detail', kwargs={'pk': obj.id}, request=request)

