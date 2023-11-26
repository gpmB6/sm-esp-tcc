import urequests, secrets

try:
  motor_inserido = int(input('\nInforme o valor do motor: '))
  sensor_inserido = int(input('\nInforme o valor do sensor: '))
  
  dados = {'value1':motor_inserido, 'value2':sensor_inserido}
  print(dados)
  request_headers = {'Content-Type': 'application/json'}

  #print('Temperature: ', motor_inserido)
  #print('Humidity: ', sensor_inserido)

  request = urequests.post(
    'http://maker.ifttt.com/trigger/inserir/with/key/' + secrets.api_key,
    json=dados,
    headers=request_headers)

  print(request.text)
  request.close()

except OSError as e:
  print('Falha ao inserir os dados. Por favor, tente novamente mais tarde.')

