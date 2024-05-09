import google.generativeai as genai

# Configuração da chave de API do Google (hipotética)
GOOGLE_API_KEY = "SUA_CHAVE_API_GOOGLE" 
genai.configure(api_key=GOOGLE_API_KEY)

# Função para aconselhamento de carreira
def plataforma_aconselhamento_carreira():
    """Plataforma de aconselhamento de carreira para estudantes."""

    # Mensagem de boas-vindas e instruções
    print("Bem-vindo à Plataforma de Aconselhamento de Carreira para Estudantes!")
    print("Você pode explorar diferentes recursos e informações sobre carreiras.")

    # Instanciando o modelo gemini-pro
    model = genai.GenerativeModel('gemini-pro')

    while True:
        # Opções para o estudante
        print("\nOpções disponíveis:")
        print("1. Explorar informações sobre carreiras")
        print("2. Sair da plataforma")

        opcao = input("Escolha uma opção (1-2): ")

        if opcao == "1":
            # Explorar informações sobre carreiras
            pergunta = input("Qual carreira você gostaria de saber mais? ")
            resposta = model.generate_content(pergunta)
            print(resposta.text.strip())  # Mostrar apenas o texto gerado
        elif opcao == "2":
            print("Obrigado por usar nossa plataforma de aconselhamento de carreira. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 2.")

# Executar a plataforma
plataforma_aconselhamento_carreira()