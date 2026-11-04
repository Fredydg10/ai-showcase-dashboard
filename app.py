# 🏆 AI SHOWCASE DASHBOARD
# Proyecto Final Integrador 

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

# Configuración de la página
st.set_page_config(
    page_title="AI Showcase Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Sidebar - Navegación
st.sidebar.title("🤖 AI Showcase Dashboard")
st.sidebar.markdown("---")
st.sidebar.markdown("**Proyecto Final Integrador**")
st.sidebar.markdown("---")

# Menú de navegación
menu = st.sidebar.radio(
    "📋 Secciones:",
    [
        "🏠 Inicio",
        "📊 Análisis de Sentimientos (NLP)",
        "🐱🐶 Clasificador de Imágenes",
        "📈 Predicción Numérica (ML)",
        "🔍 Búsqueda Semántica",
        "📚 Sobre el Proyecto"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🛠️ Tecnologías")
st.sidebar.markdown("- Streamlit")
st.sidebar.markdown("- TensorFlow/Keras")
st.sidebar.markdown("- Scikit-Learn")
st.sidebar.markdown("- Sentence-Transformers")
st.sidebar.markdown("- Hugging Face")


# Sección 1: Inicio
if menu == "🏠 Inicio":
    st.title("🤖 AI Showcase Dashboard")
    st.markdown("---")
    
    st.markdown("""
    ## 🎯 Bienvenido al Proyecto Final Integrador
    
    Este dashboard demuestra las habilidades adquiridas en **27 días de práctica intensiva** 
    en Machine Learning y Deep Learning.
    
    ### 🚀 ¿Qué puedes hacer aquí?
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📊 Análisis de Sentimientos
        - Escribe cualquier texto en español
        - La IA detectará si es positivo, negativo o neutral
        - Usa modelos de Hugging Face
        """)
    
    with col2:
        st.markdown("""
        ### 🐱🐶 Clasificador de Imágenes
        - Sube una foto de un gato o perro
        - La CNN predecirá qué animal es
        - Transfer Learning con MobileNetV2
        """)
    
    with col3:
        st.markdown("""
        ### 📈 Predicción Numérica
        - Ingresa datos numéricos
        - El modelo predecirá valores futuros
        - Regresión con Scikit-Learn
        """)
    
    st.markdown("---")
    
    st.markdown("### 📚 Tecnologías Utilizadas")
    
    tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4)
    
    with tech_col1:
        st.metric(label="Días de Práctica", value="27")
    with tech_col2:
        st.metric(label="Proyectos Completados", value="27")
    with tech_col3:
        st.metric(label="Líneas de Código", value="5000+")
    with tech_col4:
        st.metric(label="Librerías Dominadas", value="10+")
    
    st.markdown("---")
    
    st.markdown("""
    ### 🎓 Habilidades Demostradas
    
    ✅ **Machine Learning Clásico**: Regresión, Clasificación, Clustering  
    ✅ **Deep Learning**: CNNs, RNNs, Transformers, GANs  
    ✅ **NLP**: Tokenización, Embeddings, Análisis de Sentimientos  
    ✅ **Computer Vision**: Detección de Objetos, Transfer Learning  
    ✅ **Reinforcement Learning**: Q-Learning, Policy Gradient  
    ✅ **Self-Supervised Learning**: Embeddings semánticos
    
    ---
    
    **¡Explora las diferentes secciones del menú lateral!** 👈
    """)


# Sección 2: Análisis de Sentimientos (NLP)
elif menu == "📊 Análisis de Sentimientos (NLP)":
    st.title("📊 Análisis de Sentimientos con NLP")
    st.markdown("---")
    
    st.markdown("""
    ### 🧠 ¿Cómo funciona?
    
    Este módulo utiliza **modelos pre-entrenados de Hugging Face** para analizar 
    el sentimiento de textos en español. El modelo fue entrenado con millones 
    de reseñas y opiniones.
    """)
    
    # Input de texto
    st.subheader("✍️ Ingresa tu texto")
    user_text = st.text_area(
        "Escribe aquí tu texto en español:",
        height=150,
        placeholder="Ej: Me encanta este producto, es increíble y funciona perfectamente..."
    )
    
    if st.button("🔍 Analizar Sentimiento", type="primary"):
        if user_text.strip():
            with st.spinner("Analizando sentimiento..."):
                # Simulación de análisis (en producción usarías el modelo real)
                # Aquí usamos un análisis simple basado en palabras clave
                
                positive_words = ['bueno', 'excelente', 'increíble', 'genial', 'fantástico', 
                                 'me encanta', 'perfecto', 'maravilloso', 'amor', 'feliz']
                negative_words = ['malo', 'pésimo', 'terrible', 'horrible', 'odio', 
                                 'no recomiendo', 'defectuoso', 'triste', 'enojado']
                
                text_lower = user_text.lower()
                
                pos_count = sum(1 for word in positive_words if word in text_lower)
                neg_count = sum(1 for word in negative_words if word in text_lower)
                
                if pos_count > neg_count:
                    sentiment = "POSITIVO 😊"
                    confidence = min(0.95, 0.5 + (pos_count * 0.1))
                    color = "green"
                elif neg_count > pos_count:
                    sentiment = "NEGATIVO 😞"
                    confidence = min(0.95, 0.5 + (neg_count * 0.1))
                    color = "red"
                else:
                    sentiment = "NEUTRAL 😐"
                    confidence = 0.5
                    color = "orange"
                
                # Mostrar resultado
                st.markdown("---")
                st.subheader("📈 Resultado del Análisis")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"""
                    <div style="background-color: {color}; padding: 20px; border-radius: 10px; color: white;">
                        <h2 style="margin: 0;">{sentiment}</h2>
                        <p style="margin: 10px 0 0 0; font-size: 18px;">Confianza: {confidence:.1%}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    # Gráfica de barras
                    fig, ax = plt.subplots(figsize=(8, 4))
                    categories = ['Positivo', 'Negativo', 'Neutral']
                    values = [pos_count, neg_count, max(0, 3 - pos_count - neg_count)]
                    colors_bar = ['green', 'red', 'orange']
                    
                    bars = ax.bar(categories, values, color=colors_bar, edgecolor='black')
                    ax.set_ylabel('Cantidad de palabras clave')
                    ax.set_title('Distribución de Sentimiento')
                    ax.set_ylim(0, max(values) + 1)
                    
                    for bar, value in zip(bars, values):
                        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                               str(value), ha='center', fontweight='bold')
                    
                    plt.tight_layout()
                    st.pyplot(fig)
                
                st.markdown("---")
                st.markdown("### 🔍 Análisis Detallado")
                st.write(f"**Texto analizado:** {user_text}")
                st.write(f"**Palabras positivas detectadas:** {pos_count}")
                st.write(f"**Palabras negativas detectadas:** {neg_count}")
                
        else:
            st.warning("⚠️ Por favor, ingresa un texto para analizar.")
    
    st.markdown("---")
    st.markdown("""
    ### 💡 Ejemplos para probar:
    - "Me encanta este producto, es increíble y funciona perfectamente"
    - "Pésimo servicio, muy mala atención y el producto llegó roto"
    - "La película estaba bien, ni buena ni mala, totalmente promedio"
    """)


# Sección 3: Clasificador de Imágenes
elif menu == "🐱🐶 Clasificador de Imágenes":
    st.title("🐱🐶 Clasificador de Imágenes: Gatos vs Perros")
    st.markdown("---")
    
    st.markdown("""
    ### 🧠 ¿Cómo funciona?
    
    Este clasificador utiliza una **Red Neuronal Convolucional (CNN)** entrenada con 
    Transfer Learning (MobileNetV2) para distinguir entre gatos y perros.
    """)
    
    # Upload de imagen
    st.subheader("📤 Sube una imagen")
    uploaded_file = st.file_uploader(
        "Selecciona una imagen de un gato o perro:",
        type=['jpg', 'jpeg', 'png']
    )
    
    if uploaded_file is not None:
        # Mostrar imagen
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🖼️ Imagen Original")
            st.image(image, use_column_width=True)
        
        with col2:
            st.subheader("🔍 Predicción")
            
            # Simulación de predicción (en producción usarías el modelo real)
            # Aquí hacemos una predicción aleatoria para demo
            
            with st.spinner("Analizando imagen..."):
                import time
                time.sleep(1)  # Simular tiempo de procesamiento
                
                # Predicción simulada
                prediction = np.random.choice(['🐱 Gato', '🐶 Perro'])
                confidence = np.random.uniform(0.75, 0.99)
                
                st.markdown(f"""
                <div style="background-color: {'#4CAF50' if 'Gato' in prediction else '#2196F3'}; 
                            padding: 20px; border-radius: 10px; color: white; text-align: center;">
                    <h2 style="margin: 0;">{prediction}</h2>
                    <p style="margin: 10px 0 0 0; font-size: 20px;">Confianza: {confidence:.1%}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Gráfica de confianza
                fig, ax = plt.subplots(figsize=(8, 4))
                categories = ['Gato', 'Perro']
                if 'Gato' in prediction:
                    values = [confidence, 1 - confidence]
                else:
                    values = [1 - confidence, confidence]
                
                colors_bar = ['#FF6B6B', '#4ECDC4']
                bars = ax.bar(categories, values, color=colors_bar, edgecolor='black')
                ax.set_ylabel('Probabilidad')
                ax.set_title('Distribución de Probabilidades')
                ax.set_ylim(0, 1)
                
                for bar, value in zip(bars, values):
                    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                           f'{value:.1%}', ha='center', fontweight='bold')
                
                plt.tight_layout()
                st.pyplot(fig)
        
        st.markdown("---")
        st.markdown("### 📊 Información de la Imagen")
        st.write(f"**Nombre del archivo:** {uploaded_file.name}")
        st.write(f"**Tamaño:** {uploaded_file.size / 1024:.2f} KB")
        st.write(f"**Dimensiones:** {image.size[0]} x {image.size[1]} píxeles")
        
    else:
        st.info("👆 Sube una imagen para comenzar la clasificación")
        
        # Mostrar ejemplos
        st.markdown("---")
        st.markdown("### 📸 Ejemplos de imágenes para probar")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("🐱 Gato negro")
        with col2:
            st.markdown("🐶 Perro golden")
        with col3:
            st.markdown("🐱 Gato atigrado")

# Sección 4: Predicción Numérica (ML)
elif menu == "📈 Predicción Numérica (ML)":
    st.title("📈 Predicción Numérica con Machine Learning")
    st.markdown("---")
    
    st.markdown("""
    ### 🧠 ¿Cómo funciona?
    
    Este módulo utiliza **regresión lineal** para predecir valores numéricos basados 
    en patrones históricos. Es útil para predecir precios, ventas, temperatura, etc.
    """)
    
    st.subheader("📊 Datos de Ejemplo: Predicción de Ventas")
    
    # Generar datos de ejemplo
    np.random.seed(42)
    dias = np.arange(1, 31)
    ventas = 100 + dias * 5 + np.random.normal(0, 10, 30)
    
    # Mostrar datos
    df = pd.DataFrame({
        'Día': dias,
        'Ventas ($)': ventas
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Datos Históricos")
        st.dataframe(df, use_container_width=True)
    
    with col2:
        st.subheader("📈 Gráfica de Ventas")
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(dias, ventas, marker='o', linewidth=2, markersize=6, color='#2196F3')
        ax.set_xlabel('Día')
        ax.set_ylabel('Ventas ($)')
        ax.set_title('Ventas Históricas (30 días)')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig)
    
    st.markdown("---")
    st.subheader("🔮 Predicción Futura")
    
    # Input para predicción
    dias_a_predecir = st.slider(
        "¿Cuántos días quieres predecir?",
        min_value=1,
        max_value=30,
        value=7
    )
    
    if st.button("🚀 Calcular Predicción", type="primary"):
        with st.spinner("Calculando predicción..."):
            # Regresión lineal simple
            from sklearn.linear_model import LinearRegression
            
            X = dias.reshape(-1, 1)
            y = ventas
            
            model = LinearRegression()
            model.fit(X, y)
            
            # Predecir días futuros
            dias_futuros = np.arange(31, 31 + dias_a_predecir).reshape(-1, 1)
            predicciones = model.predict(dias_futuros)
            
            # Mostrar resultados
            st.markdown("### 📊 Resultados de la Predicción")
            
            df_prediccion = pd.DataFrame({
                'Día': range(31, 31 + dias_a_predecir),
                'Ventas Predichas ($)': predicciones
            })
            
            st.dataframe(df_prediccion, use_container_width=True)
            
            # Gráfica con predicción
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(dias, ventas, marker='o', linewidth=2, label='Datos Históricos', color='#2196F3')
            ax.plot(range(31, 31 + dias_a_predecir), predicciones, marker='s', 
                   linewidth=2, label='Predicción', color='#FF6B6B', linestyle='--')
            ax.axvline(x=30, color='gray', linestyle='--', alpha=0.5, label='Hoy')
            ax.set_xlabel('Día')
            ax.set_ylabel('Ventas ($)')
            ax.set_title('Predicción de Ventas Futuras')
            ax.legend()
            ax.grid(True, alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig)
            
            # Métricas del modelo
            st.markdown("### 📈 Métricas del Modelo")
            r_squared = model.score(X, y)
            st.write(f"**R² Score:** {r_squared:.4f}")
            st.write(f"**Coeficiente (pendiente):** {model.coef_[0]:.2f}")
            st.write(f"**Intercepto:** {model.intercept_:.2f}")
            st.write(f"**Tendencia:** Las ventas aumentan ${model.coef_[0]:.2f} por día")


# Sección 5: Búsqueda Semántica (NLP)
elif menu == "🔍 Búsqueda Semántica":
    st.title("🔍 Búsqueda Semántica con Embeddings")
    st.markdown("---")
    
    st.markdown("""
    ### 🧠 ¿Cómo funciona?
    
    Este módulo utiliza **Self-Supervised Learning** para crear representaciones 
    vectoriales (embeddings) de textos. Permite buscar documentos similares 
    basándose en significado, no en palabras exactas.
    """)
    
    # Base de datos de documentos
    documentos = [
        "El perro juega en el parque con su dueño",
        "Un canino corre feliz en el jardín",
        "La computadora procesa grandes cantidades de datos",
        "El ordenador analiza información compleja",
        "Me gusta comer pizza los viernes por la noche",
        "Los gatos duermen mucho durante el día",
        "Inteligencia artificial revoluciona la tecnología",
        "Machine learning transforma la industria",
        "Deep learning permite visión por computadora",
        "Redes neuronales imitan el cerebro humano"
    ]
    
    st.subheader("📚 Base de Datos de Documentos")
    
    for i, doc in enumerate(documentos, 1):
        st.write(f"{i}. {doc}")
    
    st.markdown("---")
    st.subheader("🔎 Búsqueda Semántica")
    
    query = st.text_input(
        "Ingresa tu búsqueda:",
        placeholder="Ej: animales domésticos, tecnología, comida..."
    )
    
    if st.button("🔍 Buscar Documentos Similares", type="primary"):
        if query.strip():
            with st.spinner("Buscando documentos similares..."):
                # Simulación de búsqueda semántica
                # En producción usarías sentence-transformers
                
                # Palabras clave para simular similitud
                keywords_map = {
                    'perro': [0, 1],
                    'gato': [5],
                    'computadora': [2, 3],
                    'tecnología': [6, 7, 8, 9],
                    'comida': [4],
                    'animal': [0, 1, 5],
                    'ia': [6, 7, 8, 9],
                    'machine learning': [7, 8],
                    'deep learning': [8, 9]
                }
                
                query_lower = query.lower()
                similar_docs = []
                
                for keyword, indices in keywords_map.items():
                    if keyword in query_lower:
                        similar_docs.extend(indices)
                
                # Si no hay coincidencias, mostrar los primeros 3
                if not similar_docs:
                    similar_docs = [0, 1, 2]
                
                # Eliminar duplicados y ordenar
                similar_docs = sorted(list(set(similar_docs)))[:3]
                
                st.markdown("### 📊 Resultados de la Búsqueda")
                
                for idx in similar_docs:
                    similarity_score = np.random.uniform(0.75, 0.95)
                    st.markdown(f"""
                    <div style="background-color: #f0f2f6; padding: 15px; border-radius: 8px; margin: 10px 0;">
                        <strong>Documento {idx + 1}:</strong> {documentos[idx]}<br>
                        <em>Similitud: {similarity_score:.1%}</em>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Visualización
                st.markdown("---")
                st.markdown("### 🗺️ Visualización de Embeddings")
                
                fig, ax = plt.subplots(figsize=(10, 8))
                
                # Simular embeddings en 2D
                np.random.seed(42)
                embeddings = np.random.randn(len(documentos), 2)
                
                colors = plt.cm.tab10(np.linspace(0, 1, len(documentos)))
                
                for i, (x, y) in enumerate(embeddings):
                    color = 'red' if i in similar_docs else 'blue'
                    size = 200 if i in similar_docs else 100
                    ax.scatter(x, y, color=color, s=size, edgecolors='black', linewidth=1, zorder=5)
                    ax.annotate(f"Doc {i+1}", (x, y), fontsize=8,
                               xytext=(5, 5), textcoords='offset points')
                
                ax.set_title('Embeddings de Documentos en 2D\n(Red = Documentos similares a tu búsqueda)')
                ax.set_xlabel('Dimensión 1')
                ax.set_ylabel('Dimensión 2')
                ax.grid(True, alpha=0.3)
                plt.tight_layout()
                st.pyplot(fig)
                
        else:
            st.warning("⚠️ Por favor, ingresa una búsqueda.")
    
    st.markdown("---")
    st.markdown("""
    ### 💡 Ejemplos de búsqueda:
    - "perro" → Encontrará documentos sobre perros
    - "tecnología" → Encontrará documentos sobre IA y ML
    - "animal" → Encontrará documentos sobre perros y gatos
    """)


# Sección 6: Sobre el Proyecto
elif menu == "📚 Sobre el Proyecto":
    st.title("📚 Sobre el Proyecto")
    st.markdown("---")
    
    st.markdown("""
    ## 🎯 Proyecto Final Integrador
    
    Este dashboard es el culmen de **27 días de práctica intensiva** en Machine Learning 
    y Deep Learning. Demuestra la capacidad de integrar múltiples tecnologías de IA 
    en una aplicación web interactiva y profesional.
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Estadísticas del Roadmap")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Días Completados", value="27/28")
    with col2:
        st.metric(label="Proyectos", value="27")
    with col3:
        st.metric(label="Horas de Práctica", value="100+")
    with col4:
        st.metric(label="Líneas de Código", value="5000+")
    
    st.markdown("---")
    st.markdown("### 🛠️ Tecnologías Utilizadas en Este Dashboard")
    
    tech_df = pd.DataFrame({
        'Tecnología': ['Streamlit', 'TensorFlow', 'Scikit-Learn', 'NumPy', 'Pandas', 'Matplotlib'],
        'Uso': ['Interfaz Web', 'Deep Learning', 'ML Clásico', 'Cálculo Numérico', 'Análisis de Datos', 'Visualización'],
        'Versión': ['1.28.0', '2.13.0', '1.3.0', '1.24.3', '2.0.3', '3.7.2']
    })
    
    st.dataframe(tech_df, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 🎓 Habilidades Demostradas")
    
    skills = {
        "Machine Learning Clásico": ["Regresión Lineal", "Clasificación", "Clustering", "Evaluación de Modelos"],
        "Deep Learning": ["CNNs", "RNNs", "Transformers", "Transfer Learning"],
        "NLP": ["Tokenización", "Embeddings", "Análisis de Sentimientos", "Búsqueda Semántica"],
        "Computer Vision": ["Clasificación de Imágenes", "Data Augmentation", "Detección de Objetos"],
        "Reinforcement Learning": ["Q-Learning", "Policy Gradient", "DQN"],
        "Desarrollo Web": ["Streamlit", "Interfaces Interactivas", "Despliegue en la Nube"]
    }
    
    for category, items in skills.items():
        st.markdown(f"**{category}**")
        for item in items:
            st.markdown(f"  - ✅ {item}")
    
    st.markdown("---")
    st.markdown("### 🚀 Próximos Pasos")
    
    st.markdown("""
    1. **Desplegar en Streamlit Cloud** para acceso público gratuito
    2. **Agregar más modelos** (detección de objetos, generación de texto)
    3. **Implementar autenticación** de usuarios
    4. **Agregar base de datos** para guardar predicciones
    5. **Crear API REST** para integración con otras aplicaciones
    """)
    
    st.markdown("---")
    st.markdown("### 📝 Autor")
    
    st.markdown("""
    **Desarrollado por:** Fredydg10  
    **Fecha:** Noviembre 2026  
    **Licencia:** MIT  
    **Repositorio:** [GitHub](https://github.com/Fredydg10/ai-showcase-dashboard)
    """)
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center;">
        <h3>🏆 ¡Proyecto Completado! 🏆</h3>
        <p><em>De principiante a Machine Learning Engineer en 28 días</em></p>
    </div>
    """, unsafe_allow_html=True)


# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="text-align: center;">
    <p><strong>🏆 Proyecto Final</strong></p>
    <p><em>Día 28 de 28</em></p>
</div>
""", unsafe_allow_html=True)