from rest_framework import serializers

from myapp.models import Quote,QuoteCategory



class QuoteSerializers(serializers.Serializer):
    class Meta:
        model =Quote
        fields=["quote","author"]

class QuoteCategorySerializers(serializers.Serializer):
    class Meta:
        model = QuoteCategory
        fields="__all__"