from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from news.models import News, Comment, Category, Tag
from news.serializers import NewsListSerializer, NewsDetailSerializer, \
    CommentListSerializer, NewsValidateSerializer, CategorySerializer, TagSerializer


class TagViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', ]
    ordering_fields = ['name', 'id']
    # permission_classes = [IsAuthenticated]
    # pagination_class = None

    # def list(self, request, *args, **kwargs):
    #     serializer = TagSerializer(instance=self.get_queryset(), many=True)
    #     return Response(serializer.data)


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


@api_view(['GET'])
def hello_world(request):
    dct = {
        'message': 'Hello World!',
    }
    return Response(dct)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def news_list(request):
    if request.method == 'GET':
        print(request.user)
        search = request.GET.get('search', '')

        # Get all news
        news = News.objects.select_related('category').prefetch_related(
            'tags', 'comments').filter(title__icontains=search)
        # Serialize news
        serializer = NewsListSerializer(instance=news, many=True)
        print(serializer)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        serializer = NewsValidateSerializer(data=request.data)
        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=400)
        serializer.is_valid(raise_exception=True)
        news = serializer.save()
        data = NewsListSerializer(instance=news, many=False).data
        return Response(data, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
def news_detail(request, slug):
    try:
        news = News.objects.get(slug=slug)
    except News.DoesNotExist as e:
        return Response({'error': str(e)}, status=404)
    if request.method == 'GET':
        serializer = NewsDetailSerializer(instance=news, many=False)
        return Response(serializer.data, status=200)

    elif request.method == 'PUT':
        serializer = NewsValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_news = serializer.update(news, serializer.validated_data)

        data = NewsListSerializer(instance=updated_news, many=False).data
        return Response(data, status=200)

    elif request.method == 'DELETE':
        news.delete()
        return Response(status=204)


@api_view(['GET'])
def comments_list(request):
    comments = Comment.objects.all()
    data = CommentListSerializer(instance=comments, many=True).data
    return Response(data)
