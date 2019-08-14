from rest_framework import serializers
#from django.core.serializers import ModelSerializer
from django.db.models.fields.related import ManyToManyField
from .models import Catagory,Movie,Basket,BasketDetails

class CatagorySerializer(serializers.ModelSerializer):
      class Meta:
            model = Catagory
            fields = ('catagory',)

class MovieSerializer(serializers.ModelSerializer):
      catagory=CatagorySerializer(many=True)

      class Meta:
            model= Movie
            fields=('id','catagory','description','title','actors','director','language','sub_language','year','image','price',)

class MovieShortSerializer(serializers.ModelSerializer):
      catagory=CatagorySerializer()
      image_url = serializers.SerializerMethodField()
      class Meta:
            model= Movie
            fields=('id','image_url','catagory','title','actors','director','year','price',)

      def get_image_url(self, movie):
            request = self.context.get('request')
            image_url = movie.image.url
            return request.build_absolute_uri(image_url)


class BasketDetailsSerializer(serializers.ModelSerializer):
      movie=MovieShortSerializer()
      #basket=BasketSerializer()
      class Meta:
            model= BasketDetails
            fields=('movie','quantity',)

class BasketSerializer(serializers.ModelSerializer):
      #movie=MovieShortSerializer(many=True)
      basket_details=BasketDetailsSerializer(many=True)
      class Meta:
            model= Basket
            fields=('basket_details','total',)

