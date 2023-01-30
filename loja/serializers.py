from .models import Loja

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = [
            "id",
            "nome",
            "saldo",
        ]
        