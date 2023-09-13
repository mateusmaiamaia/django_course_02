from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import cpf_valido, nome_valido, rg_valido, celular_valido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "Número do CPF inválido"})
        if not nome_valido(data['nome']):
           raise serializers.ValidationError({'nome': "Não inclua números neste campo!"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O rg deve conter 9 dígitos!"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve seguir este modelo: 11 91234-1234."})
        return data

    

    # def validate_cpf(self, cpf):
    #     if len(cpf) != 11:
    #             raise serializers.ValidationError("O cpf deve conter 11 dígitos!")
    #     return cpf
    
    # def validate_nome(self, nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError("Não inclua números neste campo!")
    #     return nome
         
    # def validate_rg(self, rg):
    #     if len(rg) != 9:
    #         raise serializers.ValidationError("O cpf deve conter 9 dígitos!")
    #     return rg
    
    # def validate_celular(self, celular):
    #     if len(celular) < 11 or len(celular) > 14:
    #         raise serializers.ValidationError("O número de celular deve conter 11!")
    #     return celular