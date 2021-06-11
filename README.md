# Turing Machine Converter

Trabalho Prático de Teoria da Computacão

O objetivo desse trabalho é criar um codigo que converta as intruções de um [emulador](http://morphett.info/turing/turing.html) de maquina de turing com fita semi-infinita para uma infinita e vice versa. Com isso provar que elas são equivalentes.

**Simbolos reservados:** "£" (inicial) e "¢" (final)

**Estados reservados:** qualquer estado que contenha o simbolo "'" no nome

### Como funciona:

#### Semi-Infinita para Infinita

- Insere um codigo no inicio para marcar o inicio com **£** e volta para o inicio da palavra
- Insere um codigo em cada estado que quando vai para esquerda e lê **£** escreve **£** e vai para direita, simulando a limitação da fita a esquerda

#### Infinita para Semi-Infinita

- Insere um codigo no inicio para movimentar toda a fita um para direita, marca a celula mais a esquerda com **£**, marca a celula mais a direita com **\¢** e volta para o inicio da palavra
- Insere um codigo em cada estado que quando vai para esquerda e lê **£** desloca todo o conteudo para a direita, deixando um espaço em branco no inicio ao lado de **£**. O cabeçote para neste espaço em branco inserido.
- Insere um codigo em cada estado que quando vai para direita e lê **\¢** imprime **_** vai para direita imprime **\¢** e vai para esquerda

### Como Rodar:

> O trabalho foi desenvolvido com python 3.9.0

para executar o programa

```bash
$ python main.py arquivo_de_entrada.txt
```

neste exemplo a saida estará em arquivo_de_entrada.out.txt

