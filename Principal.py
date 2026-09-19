print("Bem Vindo ao GScan")

repositorio = input("Digite o endereço do seu Repositório: ")

print(repositorio)
print(repositorio.startswith("https://github.com/"))

if repositorio == "":
    print("Nenhum repositório foi informado")
else:
# Verifica se o endereço informado começa com o GitHub
    if repositorio.startswith("https://github.com/"):
        print("Repositório válido")

# Divide o endereço do repositório em partes
        partes = repositorio.split("/")

        usuario = partes [3]
        repositorio_nome = partes[4]

        print(f"Usuario: {usuario}")
        print(f"Repositório: {repositorio_nome}")

        print("Iniciando análise...")

# Verifica se existe uma possível informação sensível
        codigo = "minha senha é 123456"

        if "senha" in codigo:
         print("Risco encontrado!")

    else:
        print("Endereço de repositório inválido")
        

        