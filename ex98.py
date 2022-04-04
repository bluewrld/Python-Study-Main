#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(txt):
    t = len(txt) + 4
    print('~' * t)
    print(f'{txt:^{t}}')
    print('~' * t)
escreva('oi')
escreva('eu amo batata frita')
escreva('gosto de viajar')