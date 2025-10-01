
import streamlit as st

st.set_page_config(page_title="Quiz de Derecho Laboral Peruano", layout="centered")

st.title("⚖️ Quiz de Derecho Laboral Peruano")
st.write("Responde todas las preguntas. Si aciertas todas correctamente, verás una lluvia de medallas cayendo 🏅.")

# --- Preguntas y respuestas ---
preguntas = [
    {
        "pregunta": "¿Cuál es la jornada máxima laboral ordinaria en el Perú?",
        "alternativas": [
            "6 horas diarias o 30 semanales",
            "8 horas diarias o 48 semanales",
            "10 horas diarias o 60 semanales",
            "12 horas diarias o 72 semanales",
            "7 horas diarias o 42 semanales",
        ],
        "respuesta": "8 horas diarias o 48 semanales"
    },
    {
        "pregunta": "¿Cuál es el monto de la CTS que corresponde depositar cada semestre?",
        "alternativas": [
            "Un sueldo mensual",
            "La mitad del sueldo más 1/6 de la gratificación",
            "Dos sueldos anuales",
            "Una remuneración mínima vital",
            "Una gratificación adicional completa",
        ],
        "respuesta": "La mitad del sueldo más 1/6 de la gratificación"
    },
    {
        "pregunta": "¿Cuál es el plazo máximo de un contrato modal en el Perú?",
        "alternativas": [
            "1 año",
            "2 años",
            "3 años",
            "5 años",
            "6 meses",
        ],
        "respuesta": "5 años"
    },
    {
        "pregunta": "¿Cada cuánto tiempo corresponde la gratificación en el Perú?",
        "alternativas": [
            "Mensual",
            "Trimestral",
            "Semestral (julio y diciembre)",
            "Anual",
            "Cada 2 años",
        ],
        "respuesta": "Semestral (julio y diciembre)"
    },
    {
        "pregunta": "¿Qué beneficio laboral se recibe por trabajar en domingos o feriados sin descanso sustitutorio?",
        "alternativas": [
            "Un bono único",
            "Un descanso adicional",
            "El triple de la remuneración diaria",
            "El doble de la remuneración diaria",
            "No corresponde ningún pago",
        ],
        "respuesta": "El triple de la remuneración diaria"
    },
]

respuestas_usuario = {}
score = 0

# --- Formulario para contestar ---
with st.form("quiz_form"):
    for i, q in enumerate(preguntas):
        st.subheader(f"Pregunta {i+1}: {q['pregunta']}")
        respuesta = st.radio("Selecciona una opción:", q["alternativas"], key=f"pregunta_{i}")
        respuestas_usuario[i] = respuesta
    enviar = st.form_submit_button("Verificar respuestas")

# --- Evaluación ---
if enviar:
    correctas = 0
    for i, q in enumerate(preguntas):
        if respuestas_usuario[i] == q["respuesta"]:
            correctas += 1

    st.write(f"✅ Respuestas correctas: {correctas} de {len(preguntas)}")

    if correctas == len(preguntas):
        st.success("🎉 ¡Excelente! Has respondido todo correctamente. 🏅")

        # --- Animación de medallas cayendo ---
        falling_medals = """
        <style>
        @keyframes fall {
            0% { top: -10%; opacity: 1; }
            100% { top: 110%; opacity: 0; }
        }
        .medal {
            position: fixed;
            top: -10%;
            font-size: 35px;
            animation: fall linear infinite;
        }
        </style>
        <script>
        function createMedal() {
            const medal = document.createElement("div");
            medal.className = "medal";
            medal.innerHTML = "🏅";
            medal.style.left = Math.random() * 100 + "vw";
            medal.style.animationDuration = (2 + Math.random() * 3) + "s";
            document.body.appendChild(medal);
            setTimeout(() => { medal.remove(); }, 5000);
        }
        setInterval(createMedal, 300);
        </script>
        """
        st.markdown(falling_medals, unsafe_allow_html=True)

    else:
        st.warning("❌ No acertaste todas. Inténtalo nuevamente.")
