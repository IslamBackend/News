from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.models import News, Comment
from news.serializers import NewsListSerializer, NewsDetailSerializer, CommentListSerializer


@api_view(['GET'])
def hello_world(request):
    dct = {
        'message': 'Hello World!',
    }
    return Response(dct)


@api_view(['GET'])
def news_list(request):
    search = request.GET.get('search', '')

    # Get all news
    news = News.objects.select_related('category').prefetch_related(
            'tags', 'comments').filter(title__icontains=search)
    # Serialize news
    serializer = NewsListSerializer(instance=news, many=True)
    print(serializer)
    return Response(serializer.data)


@api_view(['GET'])
def news_detail(request, news_id):
    try:
        news = News.objects.get(id=news_id)
    except News.DoesNotExist as e:
        return Response({'error': str(e)}, status=404)
    serializer = NewsDetailSerializer(instance=news, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def comments_list(request):
    comments = Comment.objects.all()
    data = CommentListSerializer(instance=comments, many=True).data
    return Response(data)
