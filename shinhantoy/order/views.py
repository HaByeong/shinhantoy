from rest_framework import generics, mixins
from .serializers import OrderSerializer, CommentSerializer, CommentCreateSerializer
from .models import Order, Comment

# Create your views here.

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class OrderDetailView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentSerializer

    def get_queryset(self):
        ord_no = self.kwargs.get('ord_no')
        return Order.objects.filter(ord_no=ord_no)

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
