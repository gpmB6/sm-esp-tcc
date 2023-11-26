# sm-esp-tcc
SmartMotors com ESP8266 usando Micropython

Código para ESP8266 utilizando Firmware de Micropython
Testado em versões 2.7 e superiores.

Detalhes do projeto podem ser localizados no site:
https://sites.google.com/view/smartmotors/in%C3%ADcio
Menus: 
  - Paramêtros e Gráficos são atualizados em tempo real de acordo com a inclusão de dados na planilha (seja através da placa ou manualmente).
  - Tutoriais contém o passo a passo da configuração, da gravação do Firmware à integração com o IFTTT, Apps Script, Sheetsu, criação da shield e código (aqui presente).

PRIMEIRO USO:</br>
Edite o secrets.py inserindo o ssid (nome da rede) e em password (a senha da rede) na qual deseja se conectar. A placa possui compatibilidade com redes 2.4 GHz. Para dúvidas sobre a conexão consulte o passo 6: "Conexão a outras redes", presente no tutorial "ESP8266 COM MICROPYTHON WEBREPL".

ATENÇÃO! Sempre após edição do **secrets.py** é preciso reiniciar a placa para que a mesma identifique as novas modificações realizadas.

PERSONALIZAÇÕES:</br>
Caso queira fazer uso de uma planilha diferente da utilizada aqui (a qual tenha total gestão sobre), é necessário modificar a variável "api_key", presente também no secrets.py.
