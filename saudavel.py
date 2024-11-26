import streamlit as st

st.title("🍎 Alimento Saudável ou Não Saudável?")

st.write("Olá! 🐥 Digite o nome de um alimento e descubra se ele é saudável ou não para sua saúde!")

saudaveis = ["maçã", "banana", "cenoura", "brócolis", "peixe", "aveia", "amêndoas", "espinafre", "abacate", "laranja", "chia", "couve-flor"
            , "castanhas", "kiwi", "manga", "alface", "repolho", "beterraba", "morango", "mirtilo", "pêssego", "ameixa", "tomate",
         "quinoa", "milho", "feijão", "lentilha", "ervilha", "ovo", "queijo branco", "rúcula", "acelga", "couve", "abobrinha", "berinjela"
            , "pepino", "pimentão", "leite de amêndoa", "arroz", "uva", "melancia", "frango grelhado", "salmão", "espinafre", "batata doce"
            , "pera", "laranja", "abóbora", "melão", "açaí", "romã", "pitanga", "água", "arroz"]
nao_saudaveis = ["batata frita", "chocolate", "refrigerante", "pizza", "sorvete", "hambúrguer", "biscoito recheado", "cachorro-quente", "bala"
                 , "pirulito", "bolo", "salsicha", "cheeps", "miojo", "margarina", "suco de caixinha", "coxinha", "fritura", "chicletes"
                 , "lasanha", "mortadela", "presunto", "jujuba", "churros", "crepe", "nuggets", "barrinha de cereal", "requeijão", "energético"
                 , "pipoca de microondas", "algodão doce", "brigadeiro", "beijinho", "Nutella", "pastel", "pudim", "bolinho de chuva", "quibe"
                 , "macarrão", "sanduíche"]

alimento = st.text_input("Digite o nome de um alimento:", "").strip().lower()


if alimento:
    if alimento in saudaveis:
        st.success(f"✅ O alimento **{alimento.capitalize()}** é saudável! 🥗")
        
    elif alimento in nao_saudaveis:
        st.error(f"❌ O alimento **{alimento.capitalize()}** não é saudável! 🍔")
        
    else:
        st.warning(f"🤔 Não sabemos se **{alimento.capitalize()}** é saudável. Tente outro alimento!")
        

st.write("### Dica 🥳:")
st.write("Sempre escolha alimentos frescos e naturais para crescer forte e saudável")
