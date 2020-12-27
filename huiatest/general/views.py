from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import pagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Client,
    QualityLot,
    Product,
    Order
)
from .serializers import (
    SellerSerializer,
    ClientSerializer,
    QualityLotSerializer,
    ProductSerializer,
    OrderSerializer,
    OrderListSerializer,
)

# Create your views here.
# https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
# https://www.django-rest-framework.org/api-guide/pagination/
# https://www.django-rest-framework.org/api-guide/filtering/
# https://django-rest-auth.readthedocs.io/en/latest/installation.html
# https://www.django-rest-framework.org/api-guide/authentication/


#plus (optional)
class ClientCrud(viewsets.ModelViewSet):

    queryset = Client.objects.filter(inactive=False)
    serializer_class = ClientSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


#plus (optional)
class QualityLotCrud(viewsets.ModelViewSet):

    queryset = QualityLot.objects.filter(inactive=False)
    serializer_class = QualityLotSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]



class ProductCrud(viewsets.ModelViewSet):

    queryset = Product.objects.filter(inactive=False)
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]       



class OrderCrud(viewsets.ModelViewSet):

    queryset = Order.objects.filter(inactive=False)
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]



class OrderPagination(pagination.PageNumberPagination):       
       page_size = 4



class OrderView(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    pagination_class = OrderPagination
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['total_value', 'purchase_date']
    filterset_fields = ['inactive']
