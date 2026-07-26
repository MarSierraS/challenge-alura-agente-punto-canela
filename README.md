# ☕ Agente Inteligente - Punto Canela

Proyecto desarrollado para el **Challenge Alura Agente**, del programa **ONE AI for Tech** (Oracle + Alura Latam).

## 📋 Descripción general del proyecto

Este proyecto es un **agente inteligente** capaz de responder preguntas en lenguaje natural sobre el **programa de fidelización de Punto Canela**, una cafetería ficticia donde los clientes acumulan sellos escaneando un código QR en cada compra y obtienen un café gratis al completar 5 sellos.

El agente utiliza una base de conocimiento en formato CSV (con preguntas y respuestas frecuentes sobre el programa, política de privacidad y términos y condiciones) para responder de forma automática a las dudas de los clientes.

## 🏗️ Arquitectura de la solución

El proyecto sigue una arquitectura simple de **recuperación de información (retrieval-based)**:

1. **Base de conocimiento (CSV):** contiene pares de pregunta/respuesta sobre el programa de fidelización.
2. **Vectorización (TF-IDF):** las preguntas de la base de conocimiento se convierten en vectores numéricos usando `TfidfVectorizer` de scikit-learn.
3. **Comparación por similitud de coseno:** cuando el usuario hace una pregunta, esta también se convierte en vector y se compara contra todas las preguntas de la base de conocimiento.
4. **Selección de la mejor respuesta:** el agente devuelve la respuesta correspondiente a la pregunta más parecida (mayor similitud). Si ninguna pregunta es lo suficientemente parecida (por debajo de un umbral de confianza), el agente indica que no tiene información sobre ese tema, evitando respuestas inventadas.Pregunta del usuario
│
▼
Vectorización TF-IDF
│
▼
Similitud de coseno contra la base de conocimiento
│
▼
¿Similitud > umbral?
│             │
Sí            No
│             │
▼             ▼
Respuesta    "No tengo información
del CSV       sobre eso todavía"## 🛠️ Tecnologías y herramientas utilizadas

- **Python 3**
- **pandas** — carga y manejo de la base de conocimiento (CSV)
- **scikit-learn** — vectorización TF-IDF y cálculo de similitud de coseno
- **Google Colab** — entorno de desarrollo y pruebas
- **Oracle Cloud Infrastructure (OCI)** — despliegue de la aplicación en la nube

## ▶️ Instrucciones para ejecutar el proyecto

### Opción 1: Google Colab (recomendado)
1. Abre [Google Colab](https://colab.research.google.com/)
2. Sube el archivo `punto_canela_base_conocimiento.csv` a tu entorno
3. Copia y pega el contenido de `agente_punto_canela.py` en una celda
4. Ejecuta la celda con el botón ▶️
5. El agente probará automáticamente algunas preguntas de ejemplo

### Opción 2: Localmente
1. Clona este repositorio:
```bash
   git clone https://github.com/MarSierraS/challenge-alura-agente-punto-canela.git
   cd challenge-alura-agente-punto-canela
```
2. Instala las dependencias:
```bash
   pip install pandas scikit-learn
```
3. Ejecuta el script:
```bash
   python agente_punto_canela.py
```

## 💬 Ejemplos de preguntas que el agente puede responder

- ¿Cómo funciona el programa de fidelización de Punto Canela?
- ¿Cuál es el monto mínimo para obtener un sello?
- ¿Cuántos sellos necesito para el café gratis?
- ¿Los sellos caducan?
- ¿Qué datos personales recopila Punto Canela?
- ¿Punto Canela comparte mis datos con terceros?
- ¿El café gratis se puede combinar con otras promociones?

## 📝 Ejemplos de respuestas generadas por el agente

**Pregunta:** ¿Cómo funciona lo del café gratis?
**Respuesta:** Al alcanzar 5 sellos, muestra tu código QR en caja y selecciona la opción de canje antes de realizar tu siguiente pedido.

**Pregunta:** ¿Cuánto tengo que gastar para ganar un sello?
**Respuesta:** El monto mínimo de compra para obtener un sello es de $100 pesos.

**Pregunta:** ¿Comparten mis datos con otras empresas?
**Respuesta:** No, Punto Canela no comparte, vende ni cede tus datos personales a terceras empresas.

## ☁️ Despliegue en OCI

*(Sección a completar con el enlace público de la aplicación desplegada y captura de pantalla como evidencia)*

- **Enlace de la aplicación:** _pendiente_
- **Captura de pantalla:** _pendiente_

## 📁 Estructura del repositoriochallenge-alura-agente-punto-canela/
├── README.md                              # Este archivo
├── agente_punto_canela.py                 # Código del agente inteligente
└── punto_canela_base_conocimiento.csv     # Base de conocimiento (preguntas y respuestas)## 👤 Autora

Proyecto desarrollado como parte del programa **ONE AI for Tech** (Grupo 10) - Oracle & Alura Latam.
