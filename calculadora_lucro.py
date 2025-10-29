import streamlit as st
from time import sleep

# Título centralizado
st.markdown("<h1 style='text-align: center;'>CALCULADORA DO LUCRO</h1>", unsafe_allow_html=True)
st.write("="*88)

# Inputs do usuário
valor_aposta = st.number_input('Insira o valor da aposta (R$):', min_value=0.0, step=5.00)
valor_total = st.number_input('Insira o valor total (inclui a aposta ) (R$):', min_value=0.0, step=5.00)

# Botão para calcular
if st.button('Calcular Lucro'):
    st.write("⏳ Processando a porcentagem, por favor aguarde...")
    sleep(1.5)

    lucro = valor_total - valor_aposta
    porcentagem = 0.3  # sua parte do lucro

    st.write("-"*88)
    if lucro > 0:
        lucro_cliente = lucro * porcentagem
        lucro_pessoal = lucro - lucro_cliente
        st.success("✅ LUCRO DETECTADO!")
        st.write(f"Lucro total: R${lucro:>10.2f}")
        st.write(f"Lucro do Investidor (30%): R${lucro_cliente:>10.2f}")
        st.write(f"Lucro do Apostador (70%): R${lucro_pessoal:>10.2f}")
    elif lucro == 0:
        st.info("😐 Não houve lucro nem prejuízo")
    else:
        st.error(f"❌ Infelizmente, houve prejuízo de R${abs(lucro):.2f}")
    st.write("-"*88)