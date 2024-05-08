# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.5

# abrir o navegador (Edge)
pyautogui.press("win")
time.sleep(1)
pyautogui.write("edge")    
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=703, y=389)
# escrever o seu email
pyautogui.write("testedeautomacaopython@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("12345")

pyautogui.press("tab") # passando pro proximo campo
pyautogui.press("enter")


# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("./produtos.csv")

print(tabela)

        # codigo       marca        tipo  categoria  preco_unitario  custo               obs
        # 0    MOLO000251    Logitech       Mouse          1           25.95    6.5               NaN
        # 1    MOLO000192    Logitech       Mouse          2           19.95    5.0               NaN
        # 2    CAHA000251     Hashtag      Camisa          1           25.00   11.0               NaN
        # 3    CAHA000252     Hashtag      Camisa          2           25.00   11.0  Conferir estoque
        # 4    MOMU000111  Multilaser       Mouse          1           11.99    3.4               NaN
        # ..          ...         ...         ...        ...             ...    ...               ...
        # 288  ACAP000192       Apple  Acessorios          2           19.00    3.8               NaN
        # 289  ACSA0009.3     Samsung  Acessorios          3            9.55    2.1               NaN
        # 290  CEMO000271    Motorola     Celular          1          279.00   72.5               NaN
        # 291  FOMO000152    Motorola        Fone          2          150.00   33.0               NaN
        # 292  CEMO000223    Motorola     Celular          3          229.00   55.0               NaN


# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim.  
  
