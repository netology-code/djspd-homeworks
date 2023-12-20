from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    pass


class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    pass


class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля
    pass
