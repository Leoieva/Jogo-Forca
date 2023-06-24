# Jogo-Forca

Um jogo da forca usando Python para jogar direto no terminal. 
Abaixo está uma descrição mais detalhada do código:

1. Importação de bibliotecas:
   - `random`: É usada para escolher aleatoriamente uma palavra da lista de palavras ocultas.
   - `lista_palavras`: É um módulo personalizado que contém uma lista de 19 palavras possíveis para o jogo da forca.
   - `unidecode`: É usada para remover acentos das palavras, a fim de tratar letras acentuadas como letras não acentuadas.

2. Variáveis utilizadas:
   - `palavra`: É uma palavra escolhida aleatoriamente da lista de palavras ocultas.
   - `palavra_sem_acento`: É a versão da palavra sem acentos.
   - `silhueta_palavra`: É uma lista que representa a silhueta da palavra oculta, com "_" para letras não descobertas e espaços para espaços em branco.
   - `letras_digitadas`: É uma lista que mantém o histórico das letras digitadas pelo jogador.
   - `enforcou` e `acertou`: São variáveis booleanas para indicar se o jogador perdeu ou ganhou o jogo.
   - `tentativas`: É o número de tentativas restantes para o jogador.
   - `i`: É um contador usado para iterar sobre as letras da palavra.

3. Lógica do jogo:
   - O jogo é executado em um loop while até que o jogador acerte todas as letras ou fique sem tentativas.
   - O jogador digita uma letra ou um chute a cada vez.
   - Se a letra já tiver sido digitada anteriormente, uma mensagem é exibida.
   - Se a letra digitada estiver na palavra, a silhueta da palavra é atualizada com a letra correta.
   - Se a letra não estiver na palavra, o número de tentativas é reduzido.
   - A cada iteração, a silhueta da palavra e o histórico de letras são exibidos.
   - Se o jogador acertar todas as letras antes de ficar sem tentativas, ele ganha o jogo.
   - Se o jogador ficar sem tentativas, ele perde o jogo e a palavra é revelada.

4. Jogar novamente:
   - Após o término do jogo, o jogador é questionado se deseja jogar novamente.
   - Se a resposta for "s" (sim), o jogo é reiniciado chamando a função `jogar_forca()` novamente.
   - Se a resposta for "n" (não), uma mensagem é exibida e o programa é encerrado.
   - Se a resposta for inválida, uma mensagem é exibida até que uma resposta válida seja fornecida.

Ao estudar este código, é possível aprender sobre o uso de funções, loops, listas, manipulação de strings, importação de bibliotecas, estruturas condicionais e recursão (ao jogar novamente). Além disso, o código demonstra como implementar a lógica básica do jogo da forca.
