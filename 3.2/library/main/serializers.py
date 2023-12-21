from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    # реализуйте сериализацию объектов модели Book
    ...

    #доп задание
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['orders_count'] = ...
    #     return representation


class OrderSerializer(serializers.ModelSerializer):
    # добавьте поля модели Order
    ...

    #доп задание
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['books'] = ...
    #     return representation
