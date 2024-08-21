senha = str(input("Digite sua senha\n"))

senha_confirm = str(input("Digite novamente sua senha\n"))
while True:
 if senha != senha_confirm:
  senha_confirm =input("Digite novamente sua senha\n")
 else:
  print("Senha criada com suscesso",senha)
  break
