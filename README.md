# sm-esp-tcc
<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge"/>
</p>

<h1 align="center"> SmartMotors com ESP8266 usando Micropython </h1>

Código para ESP8266 utilizando Firmware de Micropython

Detalhes do projeto podem ser localizados no site:
https://sites.google.com/view/smartmotors/in%C3%ADcio

Menus: 
  - Paramêtros e Gráficos são atualizados em tempo real de acordo com a inclusão de dados na planilha (seja através da placa ou manualmente).
  - Tutoriais contém o passo a passo da configuração, da gravação do Firmware à integração com o IFTTT, Apps Script, Sheetsu, criação da shield e código (aqui presente).

<b> PRIMEIRO USO:</b></br>

1) Edite o secrets.py inserindo o ssid (nome da rede) e em senha (a senha da rede) na qual deseja se conectar. A placa possui compatibilidade com redes 2.4 GHz. Para dúvidas sobre a conexão consulte o passo 6: "Conexão a outras redes", presente no tutorial <a href = "https://fab.poalab.net.br/#!/projects/esp8266-com-micropython-webrepl"> "ESP8266 COM MICROPYTHON WEBREPL" </a>.

ATENÇÃO! Sempre após edição do **secrets.py** é preciso reiniciar a placa para que a mesma identifique as novas modificações realizadas nesse arquivo. Esse processo pode ser realizado via "Ctrl + D" ou simplesmente desconectando e conectando novamente a placa de sua fonte de energia.

2) Através da IDE de sua preferência, importe e configure o WebREPL da seguinte maneira:

$ import webrepl_setup

Siga as instruções de habilitar ou não sua execução na inicialização da placa e da configuração de uma senha. Enfim, reinicie a placa novamente.

PERSONALIZAÇÕES:</br>
Caso queira fazer uso de uma planilha diferente da utilizada aqui (a qual tenha total gestão sobre), é necessário modificar a variável "api_key", presente também no secrets.py.

# :hammer: Funcionalidades do projeto

- `Executar o SmartMotors`: roda o SM, permitindo que o usuário treine a placa para o comportamento esperado de acordo com quantidade de luminosidade e posição do motor. Após a conclusão do treinamento, envia os parâmetros para a planilha.
- `Inserir manualmente um treinamento`: permite inserir manualmente na interface do WebREPL valores para o motor e o sensor (um conjunto de treinamento)
- `Escolher um treinamento anterior`: exibe todos os treinamentos presentes na planilha e permite executar uma combinação de treinamentos
