<p align="center">
  <img src="https://user-images.githubusercontent.com/63745733/135949071-327c7732-c0f3-4bd3-838a-faf2180fb2ab.gif">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/63745733/135949996-f284cb7a-b5ac-4bfd-a5cc-717b8b4d674f.png">
</p>

<p align="center">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP-Brasil&metric=alert_status">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP-Brasil&metric=reliability_rating">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP-Brasil&metric=bugs">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP-Brasil&metric=coverage"/>
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP-Brasil&metric=security_rating">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP-Brasil&metric=sqale_rating">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP-Brasil&metric=code_smells">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP-Brasil&metric=vulnerabilities">
</p>

<h1>NLP Brasil</h1>

## Motivação

Cada vez mais tem se monstrado a necessidade de um modelo de processamento natural de linguagem, e principalmente na nossa linguagem que diga-se de passagem
é muito complexa, a ponto de que pequenas variações em sinais, virgulas, e até mesmo o possicionamento de determinadas palavras pode influenciar diretamente o sentido e a polarização da frase. Esse repositorio e API tem como motivação justamente solucionar de forma simples, prática, estratégica e com um modelo estatístico essa necessidade!

### Status: Em desenvolvimento ⚠

## Atenção!
Como o projeto está hospedado nos dynos gratuitos do heroku, após 30 minutos de inatividade ele é desiligado automáticamente, então ao acessar a api, ou client, é normal demorar para inicar, após no máximo 1 minuto (Nunca passou disso, pelo menos pra mim, o frontend deve demorar mais, pois, diferente do python ele é servido em Node) os servidores já estão de pé!

# Principais mudanças:

1. Framework
As últimas versões da API eram feitas no framework Flask, que é excelente, sem sombra de dúvidas, porém, após experimentar o framework FastAPI me apaixonei! O código particulamente falando fica muito mais sofisticado, não que no Flask seja impossível de fazer isso, mas no FastAPI isso vem de documentação! Sem contar que além da documentação
ser excelente ela tem uma ótima tradução para o português! Também vem com uma "documentação" provida pelo open api por default, então se acessarem o endpoint "/docs" na api
terão um schematic da api! Como uso um modelo de resposta customizado, ele não aparece bonitinho lá, mas é uma feature muito boa!


2. Retorno
  Na última versão, se não me engano, o último commit foi ajustando o retorno, pois, ao invés de retornar im json com os dados da frase, era apenas um objeto python entre      doble-quotes (aspas duplas) o que impedia de fazer seleções diretas como "phrase.polaridade", no último commit tínhamos uma estrutura json assim: 
    ```json
    {
    "polaridade": 0,
    "confidence": "33%",
    "numero de palavras": 3,
    "palavras desconhecidas": 2,
    "mensagem": "a frase 'chamada de api' e neutra", 
    }
    ```
    Atualmente visando organização e deixar a resposta mais sofisticada e com mais informações principalmente para quem for consumir apenas pelo terminal, a estrutura json está  assim: 

    ```json
    {
      "status": 200,
      "data": {
          "Polaridade": 0,
          "Confianca": "33%",
          "NumeroPalavras": 3,
          "PalavrasCon": 1,
          "PalavrasDesc": 2,
          "Mensagem": "A frase \"chamada de api\" é neutra",
          "Frase": "chamada de api"
      },
      "error": false
    }
    ```
    Nos dados do próprio processamento agora temos as palavras conhecidas ("PalavrasCon") e a frasae em sí ("Frase"). Também houve o acrésimo de informações acerca do status code da resposta, os dados se tiverem, e se houve algum error. 

3. Forma de contribuir. Agora é possível contríbuir de maneira "indireta", mais a frente explico, mas o "database" que tem os dados de polaridade de frases e tudo mais foi resetado, ele, como dito nas últimas versões, tinha muitas frases que estavam com a polaridade errada, muitas delas foram corrigidas por mim, mas como foi resetado as alterações foram perdidas, por isso, temos um novo recurso, no endpoint '/stack/review' fazendo um post com a frase e um comentário "Opcional" abrirá um issue nesse repo e eu vou conferir o resultado e tentar resolver.

4. Suporte para o Português(BR)
Parece até piada, mas, infelizmente não é! Como dito nas moticações do projeto, a nossa linguagem é cheia de nuances, que pequeníssimos detalhes mudam completamente o sentido da frase! Cometi, admito, o erro bobo de ao receber uma frase, a normalizar para os padrões ASCII que removem os acentos e os caracteres especiais como "ç", basicamente ele recebia o UTF-8 "ç" e "substituia" pelo equivalente ASCII "c", só que é precisamente esse tipo de abordagem que faz com que a premissa do projeto falhe, pois, suponhamos que uma empresa de metrô queira usar o serviço, na versão futura que detectará entidades nas frases, então, um cliente escreve o comentário: "Gostei muito do metrô da cidade", na antiga abordagem a frase seria normalizada em ASCII para: "gostei muito do metro da cidade", dependendo da autonomia do processamento, a resposta poderia vincular "metro" a unidade de medida, então o algorítmo "entenderia" que o cliente está satisfeito com a quantidade de m² da cidade! Que falta faz o acento! Não apenas isso, mas como o cristianismo é a religião predominante no nosso país, imagine alguém escreve um comentário do tipo "gostei muito do hamburguer, que Deus abençoe amém, mais molho da próxima vez não faz mal!" o processamento seria "gostei muito do hamburguer, que Deus abencoe amem, mais molho da próxima vez não faz mal!" ao tirar o acento de "amém" vira outra palavra "amem" amem mais molho??? Pode ser até um exemplo tosco, mas eu, na minha experiencia com seres humanos sou cétido a desacreditar que tal comentário não pudesse aparecer e até outros do mesmo tipo! Por esse motivo, resetei o "database" que é um arquivo json, coloquei as opções de encoding para utf-8 e o argumento ensure_ascii quando for fazer um dump de objeto python para json como False resolvendo assim esse problema!


# Como usar

🤓 Antes de colocar a mão na prática sugiro a leitura completa para o entendimento de como funciona e como as palavras são classificadas

Esse repositório está sendo hospedado pelo Heroku pelo link: https://nlp-brasil-api.herokuapp.com/, que é uma das formas de acesso nesse caso a API então não espere uma view friendly, para isso acesse o nosso client: https://nlp-brasil.herokuapp.com/ só digitar a frase no input e clicar em enviar, se o servidor da API estiver inativo aparecerá uma mensagem "processando..." e após uns 30 segundos a frase aparecerá processada, também tem as estatísticas para nerds, que se referem aos dados do retorno do json, invés só da frase processada, o frontend no momento ainda tá meio quebrado, não é o meu forte, mas está funcinal! Desculpa!! Estou trabalhando nisso

<p align=center>
  <img src="https://user-images.githubusercontent.com/63745733/135955141-a3e0971e-805b-4816-b979-8cf432c49ff3.gif">
</p>


Outra forma é consumir a api através de bibliotecas como requests (python) e programas como postman ou insominia atráves
dsse endpoint https://nlp-brasil-api.herokuapp.com/processing só aceita o método POST na forma de application/json e a estrutura do objeto json deve ser a seguinte:

```json
{
"phrase":"Chamada de api"
}
```

# Exemplos práticos:

* gif do inicio do rep (Usando o postman e mandando para o endpoint)

* Requests (biblioteca em python) 

<p align="center">
  <img src="https://user-images.githubusercontent.com/63745733/120118781-ab537680-c16a-11eb-8a61-d49681a8a93f.gif">
</p>

### Código:

```python
import requests
import json

data = {"phrase":"Chamada de api"}

h={"Content-Type":"application/json"}

resposta = requests.post('https://nlp-brasil-api.herokuapp.com/processing', data=json.dumps(data), headers=h,verify=True)

print(resposta.text)
```
O formato de saída da api é:

```json
{
  "status": 200,
  "data": {
      "Polaridade": 0,
      "Confianca": "33%",
      "NumeroPalavras": 3,
      "PalavrasCon": 1,
      "PalavrasDesc": 2,
      "Mensagem": "A frase \"chamada de api\" é neutra",
      "Frase": "chamada de api"
  },
  "error": false
}
```

A API também pode ser consumida por qualquer biblioteca que funcione de maneira análoga ao requests em python:

*  XMLHttpRequest (Javascript)
*  Axios (Javascript é usado no frontend para consumir a api)
*  JAXB (Java)
*  Entre outros

# Casos reais:

Em breve!

# Desafios enfrentados

Atualmente o maior desafio se dá pelo léxico que muitas vezes classifica uma palavra positiva como negativa ou neutra e vice e versa, o que quando acontece faz com que 
o indice de confiança saia baixo e ou a polaridade da frase venha errada, um método para atualizar o léxico já está em desenvolvimento

Atualmente não há uma forma de classificar quantas palavras estão classificadas erroneamente.


# Como funciona

A classe NLP consome um léxico que foi transformado num json gigantesco (22463 linhas) que contém a palavra e a polaridade dela Ex:

```json
"pesaroso": {
        "polaridade": -1
    },
```
Então para cada palavra na frase o algoritmo soma a polaridade (-1 negativa, 0 neutra ou 1 positiva) e atribui a uma variável de polaridade que é então modificada pelo 
contexto, um bom exemplo de como o contexto pode mudar completamente a polaridade de uma frase é justamente quando encontramos a palavra "gostei" que a primeira 
vista é uma palavra "1" positiva, porém, se eu disser "eu não gostei muito desse pão" a palvra "gostei" se torna na verdade um amplificador para o não que é (nesse contexto)
negativo.
Depois de passar por essa atribuição de contexto o algoritmo calcula o indice de confiança, que é semelhante a notação erro relativo estatistico
básicamente para se ter uma porcentagem do quão certo o modelo está nós temos a seguinte notação:

C (Confiança) = PC (Palavras conhecidas) / PD (Palavras desconhecidas) * 100

Já que nós estamos dividindo o nosso espaço amostral pelas palavras que o algoritmo não entendende (que pode no máximo ser todas e retornar 0) sempre teremos
um numero que corresponderá a porcentagem, por isso multiplicamos por 100 para poder obter a porcentagem

### Código:

```python
if know_words > 0: #O algorimo só processerá se houver alguma palavra conhecida caso o contrário receberemos 0 (0/1)

            total_words = len(phrase_list.split()) #Onde total_words = PC, cf = C e know_words = PC 
            cf =  f'{round(know_words / total_words *100)}%'

        else:
            cf = 'Baseado nos dados já coletados não posso chegar numa conclusão precisa' #Caso não haja palavras conhecidas

        return cf
```
Então uma vez que temos todos os dados o nosso objeto json é criado onde conterá todos os dados da frase como palavras desconhecidas e etc. Porém, apenas
a mensagem de resumo "A frase 'frase' é 'polaridade'

O formato final do json é:

```json
{
  "status": 200,
  "data": {
      "Polaridade": 0,
      "Confianca": "33%",
      "NumeroPalavras": 3,
      "PalavrasCon": 1,
      "PalavrasDesc": 2,
      "Mensagem": "A frase \"chamada de api\" é neutra",
      "Frase": "chamada de api"
  },
  "error": false
}
```
