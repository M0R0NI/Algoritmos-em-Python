# Nada mais é do que um formato de um arquivo, exemplo .txt, jpeg...
# No Python essencialemente um dicionário.

# AwesomeAPI - API de cotações de moedas. Faremos uma REQUISIÇÃO para a API disponibilizar dados do link abaixo.
# Um dicionário onde dentro dele tem uma chave, e um dicionário de informações sobre a chave.

import requests #Essa biblioteca permite fazer requisições para a API, solicitar e enviar informações para a internet.

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()
print(requisicao)
print(requisicao['USDBRL']['varBid'])


