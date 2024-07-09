## Resolução 1920p x 1080p ##

from time import sleep # Biblioteca --> Tempo
import pyautogui as pag # Biblioteca --> Automação
import pandas as pd # Biblioteca --> Manipulação de dados

#Tempo de execução entre cada comando pag. será de 0.5 seg
pag.PAUSE = 0.5

# Lendo a tabela CSV com pandas
tabela = pd.read_csv('produtos.csv')

# Passo 1 -> Abrir nosso navegador e acessar a página
def openavigator() -> None:
    pag.press('win')
    pag.write('google chrome')
    pag.press('enter')

    sleep(1.5)

    # Entrando no sistema da empresa
    pag.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
    pag.press('enter')

# Passo 2 -> Efetuar o login
def login() -> None:
    # Tempo para página carregar tranquilamente
    sleep(3)

    pag.press('tab')
    pag.write('emailficticio@gmail.com') # Suas credenciais -> Email

    pag.press('tab')
    pag.write('senhadousuario') # Suas credenciais -> Senha

    pag.press('tab')
    pag.press('enter')
    # LOGIN EFETUADO

    sleep(1)

# Função auxiliar para preencher os campos
def pushinfo(linha, nome):
    if nome == 'codigo':
        pag.click(x=837, y=255) # Seleciona o campo do código
        pag.hotkey('ctrl', 'a') # Seleciona todo o conteúdo do campo
    else:
        pag.press('tab') # Navega para o próximo campo
        
    campo = str(tabela.loc[linha, f'{nome}']) # Obtém o valor do campo da tabela
    if nome == 'obs':
        if not campo == 'nan':
            pag.write(campo) # Escreve o valor do campo no formulário
    else:
        pag.write(campo) # Escreve o valor do campo no formulário
    
# Passo 3 -> Preencher as informações de cada produto
def getinformations():
    for linha in tabela.index:
        pushinfo(linha, 'codigo')
        pushinfo(linha, 'marca')
        pushinfo(linha, 'tipo')
        pushinfo(linha, 'categoria')
        pushinfo(linha, 'preco_unitario')
        pushinfo(linha, 'custo')
        pushinfo(linha, 'obs')
        pag.press('tab') # Navega para o botão de enviar
        pag.press('enter') # Envia o formulário
        pag.scroll(5000) # Role a página para cima

# Função principal para executar o script
def main() -> None:
    openavigator() # Passo 1 -> Abrir navegador e acessar a página
    login() # Passo 2 -> Efetuar o login
    getinformations() # Passo 3 -> Preencher as informações

# Executa o script se este arquivo for executado diretamente
if __name__ == "__main__":
    main()
