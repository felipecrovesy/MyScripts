<div align="center">
  <h1 align="center">Encontrar Imagens Repetidas</h1>

   <div align="center">
     É um script que procura através do seu input no terminal o local que deseja verificar as imagens duplicadas e cria um relatório em arquivo de texto.
    </div>
</div>

## 📋 <a name="table">Sumary</a>

1. 🤖 [Introdução](#introduction)
2. ⚙️ [Tech Stack](#tech-stack)
3. 🤸 [Como usar](#quick-start)
7. 🤝 [Contribuições](#contributing)
8. 👥 [Autores](#authors)
<br>

## <a name="introduction">🤖 Introdução</a>

Esse algoritmo utiliza uma função dentro da biblioteca Python chamada imagehash. Essa biblioteca é utilizada para gerar hashes perceptuais de imagens. Diferente de hashes criptográficos (como MD5 ou SHA-256), onde pequenas mudanças na entrada resultam em hashes completamente diferentes, hashes perceptuais são projetados para que imagens visualmente semelhantes tenham hashes também semelhantes.

O principal algoritmo em questão está utilizando Wavelet hash.

**Como funciona o Wavelet Hash (whash) em linhas gerais:**
___

+ Conversão para escala de cinza: A imagem colorida é convertida para uma representação em escala de cinza, pois os algoritmos de hashing perceptual geralmente se concentram na estrutura de luminância.

+ Redimensionamento: A imagem é redimensionada para um tamanho pequeno e fixo (por padrão, 8x8 pixels na biblioteca imagehash). Isso ajuda a criar um hash de tamanho consistente e a focar nas características visuais de baixa frequência.

+ Transformada Wavelet Discreta (DWT): Em vez da Transformada Discreta de Cosseno (DCT) usada em outros algoritmos como o pHash, o wHash utiliza a Transformada Wavelet Discreta. A DWT decompõe a imagem em diferentes sub-bandas de frequência.

+ Extração de características: Os coeficientes da sub-banda de menor frequência (que representa a informação mais geral da imagem) são analisados.
Criação do hash: Uma maneira comum de criar o hash a partir desses coeficientes é calcular a mediana dos valores e, para cada coeficiente, atribuir um bit 1 se for maior ou igual à mediana e um bit 0 caso contrário. 

Esses bits são então combinados para formar o hash final.

<br>

**Para que serve o imagehash.whash?**
____
O Wavelet Hash é particularmente útil para detectar imagens que são versões escalonadas (aumentadas ou diminuídas) da mesma imagem original. Ele tende a ser mais robusto a essas transformações geométricas em comparação com outros algoritmos de hashing perceptual.


<br>


## <a name="tech-stack">⚙️ Tech Stack</a>

- python 3.0
- Pillow
- ImageHash
  
<br>

## <a name="quick-start">🤸 Como usar</a>

Para iniciar o projeto, siga os seguintes passos em seu dispositivo:

**00 - Pré-requisitos**

Para usar este projeto você deve ter instalado previamente os seguintes pacotes:

- [Python 3.13.2](https://www.python.org/downloads/)
- Pillow - ```pip install Pillow```
- ImageHash - ```pip install ImageHash```
  <br/><br/>

**01 - Clonar o Repositório**

```bash
git clone https://github.com/felipecrovesy/MyScripts.git
```

**02 - Rodar o Projeto**

Na pasta do arquivo ```encontrar_repetidas.py```

```bash
python run encontrar_repetidas.py
```
Os inputs dentro do arquivo de texto ficam salvos na pasta que você direcionou para ele verificar as imagens repetidas em ```./repetidas```

<br>

## <a name="contributing">🤝 Contribuições</a>

Contriguições, issues, e novos recursos são vem vindos!

1. Faça um Fork do projeto (<https://github.com/felipecrovesy/MyScripts/fork>)
2. Crie a sua branch de feature (`git checkout -b feature/fooBar`)
3. Commit suas alterações (`git commit -am 'Add some fooBar'`)
4. Faça um Push para a branch (`git push origin feature/fooBar`)
5. Crie um novo Pull Request


## <a name="authors">👥 Autores</a>

<table style="border-collapse: collapse; table-layout: auto; text-align: left;">

  <tbody>
    <tr>
      <td style="padding: 10px; border: 1px solid #ddd;">
        <img src="https://avatars.githubusercontent.com/u/60819196?v=4" width="60" style="border-radius: 50%; display: block; margin: 0 auto;">
      </td>
      <td style="padding: 10px; border: 1px solid #ddd;">Felipe Crovesy</td>
      <td style="padding: 10px; border: 1px solid #ddd;">
        <a href="https://www.linkedin.com/in/felipe-crovesy-6a299283/" target="_blank">LinkedIn</a> |
        <a href="https://github.com/felipecrovesy" target="_blank">GitHub</a>
      </td>
    </tr>
  </tbody>
</table>
