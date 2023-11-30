import urequests, secrets

def insere_treinamento():
    while True:
        print('\nPreparando para insercao manual...')

        try:
            motor_inserido = int(input('\nInforme o valor do motor: '))
            sensor_inserido = int(input('\nInforme o valor do sensor: '))
          
            dados = {'value1': motor_inserido, 'value2': sensor_inserido}
            print(dados)

            request_headers = {'Content-Type': 'application/json'}

            request = urequests.post(
                'http://maker.ifttt.com/trigger/inserir/with/key/' + secrets.api_key,
                json=dados,
                headers=request_headers
            )

            print(request.text)
            print('\nProcedimento concluido!\n')

        except OSError as e:
            print('Falha ao inserir os dados. Por favor, tente novamente mais tarde.')

        finally:
            if 'request' in locals():
                request.close()

        print('\n####################################\n')

        print('1. Inserir mais um treinamento')
        print('2. Voltar ao menu anterior')
        
        treinamento_manual = input("\nO que deseja fazer? ")
        
        if treinamento_manual != "1":
            print('\nVoltando ao menu principal...')
            break

        print('\nOk, vamos inserir um novo treinamento.')

# Chama a funcao
if __name__ == "__main__":
    insere_treinamento()
