# 🌦️ Weather Bot Projesi

![Python](https://img.shields.io/badge/python-3.10+-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/Rikanymore/weather-bot)
![GitHub repo size](https://img.shields.io/github/repo-size/Rikanymore/weather-bot)

Telegram ve Discord üzerinden çoklu kaynaktan hava durumu bilgisi sağlayan Python tabanlı bot.

<div align="center">
  <img src="https://i.imgur.com/JQ5X1zP.png" width="400" alt="Bot Örnek Çıktısı">
</div>

## ✨ Öne Çıkan Özellikler
- **3 Farklı API** entegrasyonu (OpenWeatherMap, WeatherAPI, Weatherbit)
- **Konum bazlı** tahminler
- **Gerçek zamanlı** veri çekme
- Çapraz platform desteği (Telegram + Discord)
- Otomatik güncelleme desteği

## 🚀 Hızlı Kurulum

### Ön Koşullar
- Python 3.10+
- Telegram/Discord bot tokenları

```bash
# Repoyu klonla
git clone https://github.com/Rikanymore/weather-bot.git
cd weather-bot

# Sanal ortam oluştur ve aktif et
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows

# Bağımlılıkları yükle
pip install -r requirements.txt
⚙️ Yapılandırma
.env dosyası oluşturun:

ini
TELEGRAM_TOKEN=your_telegram_token
DISCORD_TOKEN=your_discord_token
OPENWEATHERMAP_API_KEY=your_api_key
API key'lerinizi alın:

OpenWeatherMap

Telegram Bot Token

Discord Bot Token

🖥️ Kullanım
Telegram Botu

python bots/telegram_bot.py
Komutlar:

/start - Botu başlat

/weather <konum> - Hava durumu sorgula

/compare <konum> - API'ları karşılaştır

Discord Botu

python bots/discord_bot.py
Komutlar:

!hava <konum> - Temel hava durumu

!detay <konum> - Ayrıntılı rapor

🏗️ Proje Yapısı

weather-bot/
├── bots/               # Bot implementasyonları
├── config/             # Yapılandırma dosyaları
├── services/           # API servisleri
├── tests/              # Test dosyaları
├── .gitignore
├── README.md
├── requirements.txt
└── main.py             # Ana uygulama
🤖 Otomatik Güncelleme
GitHub Actions ile günlük veri güncellemesi:


on:
  schedule:
    - cron: '0 8 * * *'  # Her gün 08:00 UTC
👥 Katkıda Bulunma
Repoyu fork edin

Yeni branch oluşturun (git checkout -b feature)

Değişikliklerinizi commit edin (git commit -am 'Yeni özellik')

Branch'i pushlayın (git push origin feature)

Pull Request açın

📜 Lisans
MIT Lisansı - Detaylar için LICENSE dosyasına bakın.
