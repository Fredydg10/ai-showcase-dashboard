import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Showcase Dashboard", page_icon="🤖", layout="wide")

st.title("🤖 AI Showcase Dashboard")
st.markdown("---")

st.success("✅ ¡Proyecto Final del Día 28 - Cargado Exitosamente!")

st.markdown("""
## 🎯 Bienvenido al Proyecto Final Integrador

Este dashboard demuestra las habilidades adquiridas en **27 días de práctica intensiva** 
en Machine Learning y Deep Learning.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Días Completados", value="28")
with col2:
    st.metric(label="Proyectos", value="28")
with col3:
    st.metric(label="Líneas de Código", value="5000+")

st.markdown("---")
st.markdown("### 📊 Demostración de Gráficas")

# Gráfica simple de demostración
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4, 5], [1, 4, 2, 5, 3])
ax.set_title('Gráfica de Prueba - Matplotlib Funciona')
st.pyplot(fig)

st.markdown("---")
st.markdown("### 🏆 ¡Felicitaciones! Has completado los 28 días")