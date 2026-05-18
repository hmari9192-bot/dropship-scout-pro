# 🔥 Dropship Scout AI Pro (Pakistan Edition)

A powerful Streamlit application to find winning Shopify products with AI-powered analysis, competition metrics, and viral score predictions. Specifically optimized for the Pakistan dropshipping market.

## 🌟 Features

- **Product Discovery**: Search across multiple niches (beauty, kitchen, gadgets, electronics, fashion)
- **Viral Score Analysis**: AI-powered scoring system (40-98 range)
- **Competition Analysis**: Pakistan-specific market competition levels
- **Profit Estimation**: Real-time profit calculations based on cost multipliers
- **Winning Badge System**: Automatic product classification
- **Daily Mode**: Get one recommended winning product daily
- **CSV Export**: Export results for further analysis
- **Favorites System**: Save and track your favorite products
- **Enhanced UI**: Beautiful, responsive interface with emojis and badges

## 📋 Requirements

- Python 3.8+
- Streamlit 1.28+
- pandas 2.0+
- requests 2.31+

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/hmari9192-bot/dropship-scout-pro.git
cd dropship-scout-pro
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📦 Project Structure

```
dropship-scout-pro/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
├── README.md             # This file
├── config.py             # Configuration settings
├── data/
│   ├── products.csv      # Product database
│   └── trends.json       # Trend data cache
├── modules/
│   ├── scoring.py        # Scoring algorithms
│   ├── analytics.py      # Analytics functions
│   └── api_client.py     # API integrations
├── tests/
│   ├── test_scoring.py   # Unit tests
│   └── test_app.py       # Integration tests
└── docs/
    └── API.md            # API documentation
```

## 🎯 How It Works

### 1. **Viral Score Calculation**
- Trend search volume (40%)
- Social media mentions (30%)
- Historical performance (20%)
- Current market demand (10%)

### 2. **Competition Analysis**
- Pakistan market saturation
- Similar products available
- Price competition level
- Seller reviews analysis

### 3. **Profit Estimation**
- AliExpress cost base
- Shopify markup (2.5x - 5x)
- Platform fees calculation
- Shipping cost consideration

### 4. **Winning Badge Logic**
- 🏆 **WINNING PRODUCT**: Viral Score > 80 + LOW Competition
- 🔥 **GOOD PRODUCT**: Viral Score > 65
- ⚠️ **TEST FIRST**: Viral Score ≤ 65

## 📊 Niche Categories

| Niche | Products | Avg Cost | Best Season |
|-------|----------|----------|-------------|
| Beauty | 20+ | $2-5 | Year-round |
| Kitchen | 15+ | $1-6 | Summer |
| Gadgets | 18+ | $3-10 | Holiday |
| Electronics | 12+ | $5-15 | Year-round |
| Fashion | 25+ | $2-8 | Seasonal |

## 🔌 API Integrations (Future)

- **Google Trends API**: Track product search trends
- **Shopify API**: Real product data and pricing
- **AliExpress API**: Actual supplier costs
- **TikTok API**: Viral potential analysis
- **Instagram API**: Social engagement metrics

## 💾 Export Formats

- **CSV**: Import into Excel/Google Sheets
- **PDF**: Professional reports
- **JSON**: API integration

## 👥 User Features

- **Save Favorites**: Build your product watchlist
- **Compare Products**: Side-by-side analysis
- **History Tracking**: See past searches
- **Custom Alerts**: Get notified of trending products

## 🔐 Data Privacy

- All data is stored locally on your machine
- No personal data collection
- Optional cloud sync (disabled by default)
- GDPR compliant

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Connect GitHub repository
4. Deploy with one click

### Deploy to Heroku

```bash
heroku create your-app-name
git push heroku main
```

### Deploy to AWS/GCP

See `docs/deployment.md` for detailed instructions

## 📝 Configuration

Edit `config.py` to customize:
- Default niche categories
- Profit multipliers
- Competition thresholds
- API keys
- UI theme colors

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_scoring.py

# Run with coverage
pytest --cov=modules tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details

## 🆘 Troubleshooting

### App won't start
```bash
pip install --upgrade streamlit
streamlit run app.py --logger.level=debug
```

### Import errors
```bash
pip install -r requirements.txt --upgrade
```

### API connection issues
- Check internet connection
- Verify API keys in `config.py`
- Check API rate limits

## 📞 Support

- 📧 Email: support@dropshipscoutpro.com
- 🐛 Report bugs: GitHub Issues
- 💬 Discussions: GitHub Discussions
- 📚 Documentation: https://docs.dropshipscoutpro.com

## 🗺️ Roadmap

- [ ] Real-time trend API integration
- [ ] Machine learning predictions
- [ ] Multi-user authentication
- [ ] Advanced analytics dashboard
- [ ] Mobile app
- [ ] AI chatbot assistant
- [ ] Automated email reports
- [ ] TikTok trend monitoring

## 📈 Version History

### v1.0.0 (Current)
- Initial release
- Product discovery
- Viral scoring
- Competition analysis
- CSV export
- Favorites system

### v2.0.0 (Coming Soon)
- API integrations
- User authentication
- Advanced analytics
- Real-time trending

## 💝 Donate

If this tool helps you find winning products, consider supporting development:
- ⭐ Star this repository
- 🍕 Buy me coffee
- 🤝 Contribute code

---

**Made with ❤️ for Dropshippers in Pakistan**

Last Updated: May 2026
