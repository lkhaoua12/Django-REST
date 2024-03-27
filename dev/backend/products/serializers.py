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
    
    def validate_title(self, value):
        if len(value) > 100:
            raise serializers.ValidationError('This is way too long')
        qs = Product.objects.filter(title__exact=value)
        if qs:
            raise serializers.ValidationError('title already exist in the database')
        return value

