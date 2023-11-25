api_key = 'fj6vQD1kaPXtjaLN1cutzdMTiYHFVelpoGRR-FKZDet'

try:
  #sensor = float(input("Escolha a luminosidade: "))
  #print('Sensor: %2.2f C' %sensor)

  #o IFTTT permite apenas uma edicao de célula por vez
  motor = float(input("Escolha a posicao do motor: "))
  print('Motor: %2.2f' %motor)
  sensor_readings = {'value1':motor}
  #sensor_readings = {'value1':motor, 'value2':sensor}

  request_headers = {'Content-Type': 'application/json'}

  request = urequests.post(
    'http://maker.ifttt.com/trigger/editar/with/key/' + api_key,
    json=sensor_readings,
    headers=request_headers)

  print(request.text)
  request.close()

except OSError as e:
  print('Failed to read/publish sensor readings.')







