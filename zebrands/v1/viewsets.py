from rest_framework import filters
from rest_framework import viewsets
from django.contrib.auth.models import User

from catalog.settings.base import EMAIL_HOST_USER
from utils.email import send_email
from zebrands.models import Brand, Product, TrackProduct
from zebrands.serializers import BrandSerializer, ProductSerializer


class BrandViewSet(viewsets.ModelViewSet):
    """
    ViewSet for create,update and delete brand for product
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = '__all__'
    search_fields = ['title', 'description']


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD product
    perform_update(): send email for users admins(Update product)
    retrieve(): Tracking product by users
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = '__all__'
    search_fields = ['sku', 'name', 'brand_id__title']

    def perform_update(self, serializer):
        product = self.request.data
        users = User.objects.all()
        email_to = []
        for user in users:
            email_to.append(user.email)
        message = "Product modify %s " % product
        send_email(email_from=EMAIL_HOST_USER, email_to=email_to, message=['Product Update', message])
        super().perform_update(serializer)

    def retrieve(self, request, *args, **kwargs):
        user_name = str(request.user)
        product_id = kwargs['pk']
        TrackProduct.create_track(user=user_name, product_id=product_id)
        return super().retrieve(request, *args, **kwargs)
