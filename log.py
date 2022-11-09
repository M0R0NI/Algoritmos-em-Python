# logging.debug DEBUG – Informação detalhada, tipicamente de interesse apenas quando diagnosticando problemas.
# logging.info INFO – Confirmação de que as coisas estão funcionando como esperado.
# logging.warning WARNING – Uma indicação que algo inesperado aconteceu, ou um indicativo que algum problema em um futuro próximo (ex.: ‘pouco espaço em disco’). O software está ainda funcionando como esperado.
# logging.error ERROR – Por conta de um problema mais grave, o software não conseguiu executar alguma função.
# logging.critical CRITICAL – Um erro grave, indicando que o programa pode não conseguir continuar rodando.

import logging
logging.basicConfig(level=logging.INFO, filename="program.log", format="%(asctime)s - %(levelname)s - %(message)s") 
# Caso opte por usar logging INFO, ele não dara as devidas informações a não ser que você declare o nivel, como feito na 
# função acima. Veja esse formato na documentação do Python, pois no início é difícil de decorar.

mylist = ["Mercedes-Benz", "BMW", "Audi", "Lamborghini", "Ferrari", "Porsche"]
logging.info(mylist)