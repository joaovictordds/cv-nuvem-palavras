import streamlit as st
import pandas as pd 
import pdfplumber as pdf
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud

nltk.download('stopwords')
nltk.download('punkt')

# CABEÇALHO
st.set_page_config(page_title = 'Nuvem de palavras', 
				   layout = 'centered', 
				   initial_sidebar_state = 'auto')


st.sidebar.write('''
# Nuvem de palavras de currículos
---
''')

paginas = ['Home', 'GERAR NUVEM', 'Sobre']
pagina = st.sidebar.radio('Selecione uma página:', paginas)

#st.sidebar.markdown('---')

uploaded_file = ('https://github.com/joaovictordds/joaovictordds/blob/main/cv-joaovictor-dds.pdf')

if pagina == 'Home':

	st.write('''

	## NUVEM DE PALAVRAS DE CURRÍCULOS
	''')	

	st.image('contratado.jpg')
	
	st.write('''
	Crie uma nuvem de palavras a partir das palavras que sairam do seu currículo e faça uma auto-análise: 
	- Está bom? 
	- Está atrativo? 
	- Presta?
	- Eu me daria uma chance de participar de um processo seletivo com este material de 'boas-vindas'?

	Se você é um recrutador e não gostaria de perder seus valiosos 6 segundos de análise de um currículo, insira  o arquivo
	do seu pretendente e avalie o que sai desse material.

	### COMO FUNCIONA?

	- Clique no botão *GERAR NUVEM* ao lado
	- Faça o upload do arquivo do cv em formato pdf. (*Lembrando que apenas currículos padrão (de uma página e no formato PDF) poderão ser lidos por este aplicativo.*)
	- Clique no botão 'GERAR NUVEM'
	
	VOILÀ!

	''')	

	st.image('thats-all.gif')

if pagina == 'GERAR NUVEM':

	st.header('Upload do currículo:')
    
	uploaded_file = st.file_uploader("Somente arquivos de UMA página, no formato PDF:", type=["pdf"])

	if st.button(label = '-> Clique aqui! <-', help = 'É só clicar ali'):

		cv = pdf.open(uploaded_file)
		pagina1 = cv.pages[0] # pagina 0 é a primeira
		texto = pagina1.extract_text()

		lista_de_palavras = nltk.tokenize.word_tokenize(texto) # coloca cada palavra em uma linha

		# Padronizando as palavras em lowercase (apenas letras minúsculas)
		lista_de_palavras = [palavra.lower() for palavra in lista_de_palavras] #deixando tudo minusculo

		#Criando uma lista que contém pontuação que desejamos remover
		pontuacao = ['(', ')', ';', ':', '[', ']', ',', "'", '.', '-', '•']

		#Criando uma lista de stop words "a", "de", "um"que não tem valor como palavra
		stop_words = nltk.corpus.stopwords.words('portuguese')

		#criando uma lista de palavra sem stopword e pontuacoes
		keywords = [palavra for palavra in lista_de_palavras if not palavra in stop_words and not palavra in pontuacao]

		# concatenar as palavras
		textocv = " ".join(s for s in keywords)

		wordcloud = WordCloud(background_color = '#0f54c9', max_font_size = 150, width = 1280, height = 720, colormap= 'Blues').generate(textocv) 

		# mostrar a imagem final
		fig, ax = plt.subplots(figsize=(50, 20))
		ax.imshow(wordcloud)
		ax.set_axis_off()
		plt.imshow(wordcloud)
		wordcloud.to_file("wordcloud.png")
		st.image('wordcloud.png')

if pagina == 'Streamlit Widgets':
	
	st.markdown('Guardam valores **True** ou **False**')
	
	st.button(label = '-> Clique aqui! <-', help = 'É só clicar ali')
	st.code("st.checkbox('Clique para me selecionar', help = 'Clique e desclique quando quiser')")
	st.checkbox('Clique para me selecionar', help = 'Clique e desclique quando quiser')
	st.radio('Botões de Rádio', options = [100, 'Python', print, [1, 2, 3]], index = 1, help = 'Ajuda')
	st.multiselect('Selecione quantas opções desejar', options = ['A', 'B', 'C', 'D', 'E'])
	st.select_slider('Slide to select', options=[1,'2'])
		
	st.number_input('Entre com um número')

if pagina == 'Sobre':

	st.image('vaww.gif')

	st.write('''
	
	Caso queira dicas de como elaborar um bom currículo veja os links de sites especializados: [AQUI](https://blogcarreiras.cruzeirodosuleducacional.edu.br/9-dicas-que-vao-te-ajudar-a-elaborar-um-bom-curriculo/), [AQUI](https://fia.com.br/blog/como-fazer-um-bom-curriculo/) e 
	[AQUI](https://blog.unicesumar.edu.br/como-fazer-um-bom-curriculo).
	

	---
	''')

	st.write('''

	Acesse o [meu portfólio](https://joaovictordds.github.io/Portfolio/) de Data Science para outros materiais de outros assuntos como mercado financeiro, exploração de dados, machine learning, algoritmos e 
	demais projetos que forem aparecendo.


	*postado em 09/07/2021.*

	''')

	st.write('''
	   

	*Esse aplicativo foi inspirado em uma aula da professora Juliana Scudilio, do curso de Machine Learning da [FLAI](https://www.flai.com.br/)*

	''')
