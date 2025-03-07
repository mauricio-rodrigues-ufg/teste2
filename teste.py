import streamlit as st
import random

def main():
    st.title("Curso de Inglês Online")
    st.sidebar.title("Navegação")
    pagina = st.sidebar.radio("Escolha uma seção:", ["Início", "Aulas", "Exercícios", "Quiz"])

    if pagina == "Início":
        mostrar_inicio()
    elif pagina == "Aulas":
        mostrar_aulas()
    elif pagina == "Exercícios":
        mostrar_exercicios()
    elif pagina == "Quiz":
        mostrar_quiz()

def mostrar_inicio():
    st.header("Bem-vindo ao Curso de Inglês Online!")
    st.write("Este curso foi criado para ajudá-lo a aprender inglês de maneira interativa e divertida.")
    st.image("https://images.unsplash.com/photo-1557426272-fc759fdf7a8d", caption="Aprenda Inglês Conosco")

def mostrar_aulas():
    st.header("Aulas de Inglês")
    st.write("Assista às aulas abaixo para melhorar seu inglês:")
    
    st.subheader("Aula 1: Introdução ao Inglês")
    st.video("https://www.youtube.com/watch?v=V74l_zS1x8E")
    
    st.subheader("Aula 2: Verbos Básicos")
    st.video("https://www.youtube.com/watch?v=Zj9Y6aP8Y4E")

def mostrar_exercicios():
    st.header("Exercícios Práticos")
    st.write("Complete as frases abaixo preenchendo com as palavras corretas.")
    
    palavra_faltando = st.text_input("Complete: I ___ a student.", "")
    if palavra_faltando.lower() == "am":
        st.success("Correto!")
    elif palavra_faltando:
        st.error("Tente novamente!")

def mostrar_quiz():
    st.header("Quiz de Inglês")
    
    perguntas = {
        "Qual é a tradução de 'House'?": ["Casa", "Carro", "Escola", "Árvore"],
        "Como se diz 'Obrigado' em inglês?": ["Thank you", "Please", "Hello", "Goodbye"],
    }
    
    for pergunta, opcoes in perguntas.items():
        resposta = st.radio(pergunta, opcoes)
        if resposta == opcoes[0]:
            st.success("Correto!")
        else:
            st.error("Errado. Tente novamente!")

if __name__ == "__main__":
    main()