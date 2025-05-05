# Flashcard Generator / Flashcard Oluşturucu

A modern web application that generates educational flashcards using Google's Gemini AI. The application features a clean, dark-themed interface and provides an interactive chat-like experience.

Google'ın Gemini AI'sini kullanan, eğitici flashcard'lar oluşturan modern bir web uygulaması. Uygulama, temiz ve koyu temalı bir arayüze sahiptir ve interaktif bir sohbet deneyimi sunar.

## Features / Özellikler

- 🤖 Powered by Google Gemini AI / Google Gemini AI ile desteklenir
- 🎨 Modern dark theme interface / Modern koyu tema arayüzü
- 💬 Interactive chat-like experience / İnteraktif sohbet benzeri deneyim
- 📚 Customizable number of flashcards / Özelleştirilebilir flashcard sayısı
- 🔒 Secure API key management / Güvenli API anahtarı yönetimi
- 🌐 Bilingual support (Turkish/English) / İki dilli destek (Türkçe/İngilizce)

## Installation / Kurulum

1. Clone the repository / Depoyu klonlayın:
```bash
git clone https://github.com/yourusername/flashcard_generator.git
cd flashcard_generator
```

2. Create a virtual environment / Sanal ortam oluşturun:
```bash
python -m venv venv
```

3. Activate the virtual environment / Sanal ortamı aktifleştirin:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Install dependencies / Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the root directory and add your Google API key / Kök dizinde `.env` dosyası oluşturun ve Google API anahtarınızı ekleyin:
```
GOOGLE_API_KEY=your_api_key_here
```

## Usage / Kullanım

1. Start the application / Uygulamayı başlatın:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to / Web tarayıcınızı açın ve şu adrese gidin:
```
http://localhost:8501
```

3. Enter a topic and select the number of flashcards you want to generate / Bir konu girin ve oluşturmak istediğiniz flashcard sayısını seçin

4. Click the "Generate" button to create your flashcards / Flashcard'larınızı oluşturmak için "Oluştur" düğmesine tıklayın

## Environment Variables / Ortam Değişkenleri

The application requires the following environment variable / Uygulama aşağıdaki ortam değişkenine ihtiyaç duyar:

- `GOOGLE_API_KEY`: Your Google Gemini API key / Google Gemini API anahtarınız

## Dependencies / Bağımlılıklar

- streamlit==1.32.0
- google-generativeai==0.3.2
- python-dotenv==1.0.1

## Contributing / Katkıda Bulunma

1. Fork the repository / Depoyu fork edin
2. Create your feature branch / Özellik dalınızı oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit your changes / Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch / Dalı push edin (`git push origin feature/AmazingFeature`)
5. Open a Pull Request / Bir Pull Request açın

## License / Lisans

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## Acknowledgments / Teşekkürler

- Google Gemini AI for providing the AI capabilities / AI yeteneklerini sağladığı için Google Gemini AI'ya
- Streamlit for the web framework / Web framework'ü sağladığı için Streamlit'e
- All contributors who have helped improve this project / Bu projeyi geliştirmeye yardımcı olan tüm katkıda bulunanlara

---

# Türkçe Açıklamalar

## Özellikler
Bu uygulama, Google'ın Gemini AI teknolojisini kullanarak eğitici flashcard'lar oluşturur. Modern ve koyu temalı arayüzü ile kullanıcı dostu bir deneyim sunar. İstediğiniz konuda, istediğiniz sayıda flashcard oluşturabilir ve bunları interaktif bir sohbet arayüzünde görüntüleyebilirsiniz.

## Kurulum Adımları
1. Öncelikle projeyi bilgisayarınıza indirin
2. Python sanal ortamı oluşturun ve aktifleştirin
3. Gerekli kütüphaneleri yükleyin
4. Google API anahtarınızı `.env` dosyasına ekleyin

## Kullanım Kılavuzu
1. Uygulamayı başlatın
2. Web tarayıcınızda `http://localhost:8501` adresine gidin
3. Flashcard oluşturmak istediğiniz konuyu girin
4. İstediğiniz flashcard sayısını seçin (1-10 arası)
5. "Oluştur" düğmesine tıklayın

## Gereksinimler
Uygulamanın çalışması için aşağıdaki bileşenlere ihtiyaç vardır:
- Python 3.7 veya daha yüksek bir sürüm
- Google Gemini API anahtarı
- İnternet bağlantısı

## Katkıda Bulunma
Projeye katkıda bulunmak isterseniz:
1. Projeyi fork edin
2. Yeni bir özellik dalı oluşturun
3. Değişikliklerinizi commit edin
4. Pull Request gönderin

## Lisans
Bu proje MIT Lisansı altında dağıtılmaktadır. Detaylı bilgi için lisans dosyasına bakabilirsiniz.

## Teşekkürler
Bu projenin geliştirilmesinde emeği geçen herkese teşekkürler:
- Google Gemini AI ekibine
- Streamlit geliştiricilerine
- Projeye katkıda bulunan tüm kişilere 
