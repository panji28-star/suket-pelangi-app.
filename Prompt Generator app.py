import streamlit as st # PASTIKAN BARIS INI ADA DI PALING ATAS!
from datetime import datetime # PASTIKAN BARIS INI JUGA ADA DI PALING ATAS!

# Set page configuration
st.set_page_config(page_title="🎬 Suket Pelangi Deal Prompt Generator", layout="centered")

# Title and caption
st.title("🎬 Suket Pelangi Deal - Prompt Generator")
st.caption("Buat prompt absurd-komedi sinematik 8 detik gaya Suroboyoan dalam sekejap!")

# Sidebar metadata
with st.sidebar:
    st.markdown("### 🧾 Metadata")
    author = st.text_input("Penulis Prompt", value="Anonim")
    timestamp = datetime.now().strftime("%d %B %Y, %H:%M")
    st.markdown(f"Tanggal/Waktu: {timestamp}")

# Step 1: Scene Selector
st.header("1. Pilih Scene")
scene = st.selectbox("Scene", [
    "Scene 1: Secret Offer",
    "Scene 2: Deal & Lick",
    "Scene 3: Masjavas Shock",
    "Scene 4: Absurd Punchline"
])

# Step 2: Characters
st.header("2. Karakter & Dialog")
characters = st.multiselect("Karakter yang Muncul", ["MASJAVAS", "JANOKO", "JILBABGADING"], default=["JANOKO", "JILBABGADING"])
expression = st.selectbox("Ekspresi Dominan", ["Sly", "Surprised", "Mischievous", "Frustrated", "Content", "Panicked"])
dialogue = st.text_input("Dialog (Jawa-Suroboyoan)", placeholder="Contoh: Sukete pelangi... rasa coklat!")

# Step 3: Visual & Audio
st.header("3. Visual & Efek Suara")
camera = st.selectbox("Tipe Kamera", ["Medium Shot", "Close-Up", "Extreme Close-Up", "Wide Shot"])
sound_fx = st.selectbox("Efek Suara Akhir", ["None", "Record Scratch", "Wah-Wah-Wah", "Comedic Zoom", "Bloop"])

# Prompt generator function
def generate_prompt(scene, characters, expression, dialogue, camera, sound_fx, author, timestamp):
    char_str = ", ".join(characters) if characters else "Karakter tidak dipilih"
    sf = sound_fx if sound_fx != "None" else "Tidak ada"
    
    # Construct the full prompt string
    prompt_output = f"""
📽️ Prompt Video: {scene}
👤 Penulis: {author if author else "Anonim"}
🗓️ Tanggal/Waktu: {timestamp}
🎭 Karakter: {char_str}

🎥 **Shot Detail:**
    - Tipe Kamera: {camera}
    - Ekspresi Dominan: {expression}
    - Dialog: "{dialogue}"
🔊 **Efek Suara Akhir:** {sf}

Tambahan: Video pendek absurd-komedi 8 detik dengan nuansa Suroboyoan. Pastikan transisi mulus dan punchline terasa kuat.
"""
    return prompt_output

# Step 4: Result
st.header("4. Hasil Prompt")

# Button to generate prompt
if st.button("Generate Prompt"):
    generated_text = generate_prompt(scene, characters, expression, dialogue, camera, sound_fx, author, timestamp)
    st.text_area("Prompt Anda:", value=generated_text, height=300)
else:
    st.info("Tekan 'Generate Prompt' untuk membuat prompt Anda.")
