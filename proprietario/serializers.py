from .models import Proprietario

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietario
        fields = [
            "id",
            "nome",
            "cpf",
            "dono_da_loja",
        ]
        