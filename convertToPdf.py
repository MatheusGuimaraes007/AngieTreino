# Importe a biblioteca
from fpdf import FPDF

# Função para coletar os dados (Essa tu manja)
def coletar_dados():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    telefone = input("Digite seu telefone: ")
    return nome, idade, telefone


# Aqui tem uma função para gerar o pdf, pode editar nome e tal
def gerar_pdf(nome, idade, telefone, arquivo_pdf="dados_usuario.pdf"):
    # Aqui você cria um objeto novo 
    pdf = FPDF()
    # Vai definir a quebra automatica de página e também define a margem para 15 (Pode alterar se quiser)
    pdf.set_auto_page_break(auto=True, margin=15)
    # Adiciona uma página nova ao arquivo
    pdf.add_page()

    # Define uma fonte, o "B" é para negrito, e o tamanho da fonte
    pdf.set_font("Arial", "B", 16)
    # Aqui estamos criando a frase, com uma largura 200 e uma altura 10, é o posicionamento
    # ln=true significa que o cursor vai para próxima linha após criar a frase
    # e o align="C" vai ir para o centro (Odeio CSS)
    pdf.cell(200, 10, "Ficha de Cadastro", ln=True, align="C")
    
    # Aqui pula 5 pontos para o espaçamento
    pdf.ln(5)
    # Aqui vai definir a espessura da linha
    pdf.set_line_width(0.5)
    # E aqui desenha a linha, o pdf.gey_y() pega a posição atual do cursor, e desenha uma linha de x=10 até x=200
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())

    # Pula novamente, como expliquei lá em cima
    pdf.ln(5)
    # Odeio CSS - explicado lá em cima
    pdf.set_font("Arial", "", 12)
    # Mais CSS = Eca ;( - explicado lá em cima
    pdf.cell(200, 10, "Informações do Usuário", ln=True, align="C")
    pdf.ln(5)

    # CSS novamente
    pdf.set_font("Arial", "", 12)
    # pdf.cell() cria uma linha com os dados, ln=true faz o texto ir para a próxima linha 
    pdf.cell(0, 10, f"Nome: {nome}", ln=True)
    pdf.cell(0, 10, f"Idade: {idade}", ln=True)
    pdf.cell(0, 10, f"Telefone: {telefone}", ln=True)

    # Salva o PDF
    pdf.output(arquivo_pdf)
    print(f"PDF gerado com sucesso: {arquivo_pdf}")

# Esse aqui se manja, pq te conheço 
if __name__ == "__main__":
    dados = coletar_dados()
    gerar_pdf(*dados)
