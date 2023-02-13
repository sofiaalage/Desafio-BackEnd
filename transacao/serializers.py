from .models import Transacao

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = [
            "id",
            "tipo",
            "data",
            "valor",
            "cartão",
            "hora",
        ]