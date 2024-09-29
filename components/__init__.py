"""
O arquivo __init__.py tem as seguintes funções principais:

Tornar o diretório um pacote: Quando um diretório contém um arquivo __init__.py, ele é tratado como um pacote Python. Isso permite que você importe módulos desse diretório para outros arquivos.

Execução de código na inicialização do pacote: Qualquer código dentro do __init__.py é executado automaticamente quando o pacote é importado. Isso é útil para configurar pacotes, definir variáveis ou importar submódulos de maneira conveniente.

Controlar as importações do pacote: No __init__.py, você pode definir quais submódulos serão acessíveis ao importar o pacote, utilizando a variável __all__. Isso organiza e limita o que será exportado.

"""
