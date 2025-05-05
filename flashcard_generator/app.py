import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# Sayfa yapılandırması
st.set_page_config(
    page_title="Flashcard Asistanı",
    page_icon="💭",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Gemini API yapılandırması
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    st.error("API anahtarı bulunamadı. Lütfen .env dosyasını kontrol edin.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# Model kurulumu
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_flashcards(topic, num_cards=5):
    try:
        # Daha detaylı prompt
        prompt = f"""Sen bir eğitim asistanısın. Lütfen {topic} konusu hakkında {num_cards} adet eğitici flashcard oluştur.
        Her flashcard için bir soru ve cevap içermeli.
        Format şu şekilde olmalı:
        S: [Soru]
        C: [Cevap]
        
        İçerik eğitici, net ve özlü olmalı. Türkçe yanıt ver."""
        
        # API çağrısı
        response = model.generate_content(prompt)
        
        # Yanıtı kontrol et
        if response and response.text:
            return response.text
        else:
            return "Üzgünüm, şu anda yanıt oluşturulamıyor. Lütfen tekrar deneyin."
            
    except Exception as e:
        st.markdown(f"<div style='color: #ffffff; background-color: #1a1a1a; padding: 10px; border-radius: 5px;'>Bir hata oluştu: {str(e)}</div>", unsafe_allow_html=True)
        return f"Flashcard oluşturulurken bir hata oluştu. Lütfen tekrar deneyin."

# Ana stil
st.markdown("""
<style>
    /* Genel sayfa stili */
    .stApp {
        background-color: #343541;
        color: #ffffff;
    }
    
    /* Başlık stili */
    h1 {
        color: #ffffff !important;
        text-align: center;
        font-size: 2em;
        margin-bottom: 1em;
    }
    
    /* Input alanı stili */
    .stTextInput>div>div>input {
        background-color: #40414f;
        color: #ffffff;
        border: 1px solid #565869;
        border-radius: 5px;
        padding: 10px;
    }
    
    /* Slider stili */
    .stSlider>div>div>div {
        background-color: #10a37f;
    }
    
    /* Buton stili */
    .stButton>button {
        width: 100%;
        background-color: #10a37f;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-weight: 500;
    }
    
    .stButton>button:hover {
        background-color: #0d8c6d;
    }
    
    /* Mesaj kutuları stili */
    .user-message {
        background-color: #40414f;
        color: #ffffff;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    
    .assistant-message {
        background-color: #444654;
        color: #ffffff;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    
    /* Uyarı mesajları stili */
    .warning-message {
        background-color: #1a1a1a;
        color: #ffffff;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    
    /* Spinner stili */
    .stSpinner>div {
        color: #10a37f;
    }
</style>
""", unsafe_allow_html=True)

# Ana başlık
st.markdown("<h1>Flashcard Asistanı</h1>", unsafe_allow_html=True)

# Sohbet geçmişi için session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Kullanıcı girişi
user_input = st.text_input("", placeholder="Hangi konu hakkında flashcard oluşturmak istersiniz?")

# Flashcard sayısı seçimi
num_cards = st.slider("", 1, 10, 5, help="Oluşturulacak flashcard sayısı")

# Flashcard oluşturma butonu
if st.button("Oluştur", type="primary"):
    if user_input:
        # Kullanıcı mesajını ekle
        st.session_state.messages.append({"role": "user", "content": f"Konu: {user_input}\nFlashcard Sayısı: {num_cards}"})
        
        # AI yanıtını al
        with st.spinner("Oluşturuluyor..."):
            try:
                response = generate_flashcards(user_input, num_cards)
                if response:
                    st.session_state.messages.append({"role": "assistant", "content": response})
                else:
                    st.markdown("<div class='warning-message'>Yanıt alınamadı. Lütfen tekrar deneyin.</div>", unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f"<div class='warning-message'>Bir hata oluştu: {str(e)}</div>", unsafe_allow_html=True)
        
        # Mesajları göster
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"<div class='user-message'><b>Siz:</b> {message['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='assistant-message'><b>Asistan:</b> {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='warning-message'>Lütfen bir konu girin!</div>", unsafe_allow_html=True) 