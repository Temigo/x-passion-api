from django.http import Http404

from rest_framework import viewsets, decorators
from rest_framework.response import Response

from xpassion_mag.models import Article, ArticleSerializer, Feature, FeatureSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    search_fields = ('title', 'subtitle', 'author_firstname', 'author_lastname', )

    @decorators.detail_route(methods=['put'])
    def remove(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404()

        article.deleted = True
        article.save()

        serializer = self.get_serializer_class()(article)
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def restore(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404()

        article.deleted = False
        article.save()

        serializer = self.get_serializer_class()(article)
        return Response(serializer.data)

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    search_fields = ('title', )

    @decorators.detail_route(methods=['put'])
    def remove(self, request, pk=None):
        try:
            feature = Feature.objects.get(pk=pk)
        except Feature.DoesNotExist:
            raise Http404()

        feature.deleted = True
        feature.save()

        serializer = self.get_serializer_class()(feature)
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def restore(self, request, pk=None):
        try:
            feature = Feature.objects.get(pk=pk)
        except Feature.DoesNotExist:
            raise Http404()

        feature.deleted = False
        feature.save()

        serializer = self.get_serializer_class()(feature)
        return Response(serializer.data)