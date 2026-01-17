# Transcrevendo uma Imagem em Texto com AWS

### Processo de extração:
1. A etapa inicial é ler a imagem que contém o texto que desejamos extrair. Neste projeto usaremos uma lista de materiais escolares.
2. Lida a imagem como um objeto binário, podemos usar a API do Textract com a função detect_document_text, que processa a imagem e retorna um JSON contendo as informações de textos.
3. Recebida a resposta da API, o JSON contém toda a informação extraída. Processamos o arquivo JSON para extrair dados significativos, como itens da lista e suas quantidades.
4. 
