from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    pass


class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    pass


class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    pass
