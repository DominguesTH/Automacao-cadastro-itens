import pyautogui

# 1 - Clicar e digitar o usuario
pyautogui.click(674, 382, duration=0.5)
pyautogui.write('thiago')
# 2 - clicar e digitar senha
pyautogui.click(695, 407, duration=0.5)
pyautogui.write('123')
# 3 - Clicar em "Entrar"
pyautogui.click(587, 438, duration=0.5)
# 4 - Extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preço = linha.split(',')[2]
        # 1 - clicar e digitar produtothiago
        pyautogui.click(438, 371, duration=0.1)
        pyautogui.write(produto)
        # 2 - clicar e digitar quantidade
        pyautogui.click(438, 399, duration=0.1)
        pyautogui.write(quantidade)
        # 4 - clicar e digitar preço
        pyautogui.click(449, 417, duration=0.1)
        pyautogui.write(preço)
        # 5 - Clicar em registrar
        pyautogui.click(317, 576, duration=0.1)
