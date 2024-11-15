from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status, generics, viewsets

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.pagination import PageNumberPagination
from .seriallizer import ProductSerializer, CollectionSerializer, CreateProductSerializer, CreateCollectionSerializer, \
    ReviewSerializer, CartSerializer
from .models import Products, Collection, Review, Cart


#localhost:8000/store/product
#localhost:8000/store/product/1


class ProductListAPIView(ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = CreateProductSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        elif self.request.method == 'POST':
            return CreateProductSerializer


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = CreateProductSerializer


class CollectionListAPIView(ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CreateCollectionSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CollectionSerializer
        elif self.request.method == 'POST':
            return CreateCollectionSerializer


class CollectionDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CreateCollectionSerializer


class CollectionFilter:
    pass


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterSet_class = CollectionFilter
    pagination_class = PageNumberPagination


class ProductFilter:
    pass


class ProductViewSet(ModelViewSet):
    queryset = Products.objects.select_related("collection").all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterSet_class = ProductFilter
    pagination_class = PageNumberPagination

    # def get_queryset(self):
    #     collection_id = self.request.query_params('collection_id')
    #     queryset = Products.objects.filter(collection_id=collection_id)
    #     return queryset


class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])


class CartViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
    queryset = Cart.objects.prefetch_related("items__product").all()
    serializer_class = CartSerializer

    # def get_queryset(self):
    #     product_pk = self.request.query_params.get('product_pk', )
    #     return Review.objects.get(product_id=product_pk)

# @api_view(['GET','POST'])
# def product_list(request):
#     if request.method == 'GET':
#         products = Products.objects.all()
#         serializer = ProductSerializer(products, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
#
#
# @api_view(['GET','PUT','DELETE','PATCH'])
# def product_detail(request, pk):
#     product = get_object_or_404(Products, pk=pk)
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method == 'PUT':
#         serializer=CreateProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method == 'DELETE':
#         product.delete()
#         return Response(data={"message": f"Product with id {pk} deleted."}, status=status)
#
#
#
# @api_view()
# def collection_list(request):
#     collections = Collection.objects.all()
#     serializer = CollectionSerializer(collections, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view()
# def collection_detail(request, pk):
#     collection = get_object_or_404(Collection, pk=pk)
#     serializer = CollectionSerializer(collection)
#     return Response(serializer.data, status=status.HTTP_200_OK)
