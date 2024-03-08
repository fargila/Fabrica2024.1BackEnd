from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..models import ViaCepModel
from .serializers import CepSerializer
import requests

class ViaCapViewSet(ModelViewSet):
    queryset = ViaCepModel.object.all()
    serializer_class = CepSerializer

    def create(self, request):

        cep = request.get('cep', 'Não encontrado')
        site = f'https://viacep.com.br/ws/{cep}/json/'

        requisicao = requests.get(site)
        json = requisicao.json()

        cep = json.get('cep', '')
        logradouro = json.get('logradouro', '')
        complemento = json.get('complemento', '')
        bairro = json.get('bairro', '')
        localidade = json.get('localidade', '')
        uf = json.get('uf', '')

        dados_recenidos = {
            "cep": f'{cep}',
            "logradouro": f'{logradouro}',
            "complemento": f'{complemento}',
            "bairro": f'{bairro}',
            "localidade": f'{localidade}',
            "uf": f'{uf}'        
        }

        print(json)
        meuseri = CepSerializer(data=dados_recenidos)

        if meuseri.is_valid():

            cep_pesq = ViaCepModel.objects.filter(cep=cep)
            cep_pesqTrue = cep_pesq.exists()
            if cep_pesqTrue:
                return Response("Aviso: esse CEP já existe no banco")

            meuseri.save()
            return Response(meuseri.data)
        else:
            return Response("aviso: Ocorreu algum erro")
        # print(meuseri.is_valid())
        # return Response(f"Seu CEP é {cep}")