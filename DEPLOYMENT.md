# Deployment Guide - Dropship Scout AI Pro

## 🚀 Deployment Options

Choose one of these platforms to deploy your app:

### Option 1: Streamlit Cloud (RECOMMENDED - Easiest!)

**Time**: 2 minutes | **Cost**: FREE

1. **Push code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Go to Streamlit Cloud**
   - Visit https://streamlit.io/cloud
   - Sign in with GitHub

3. **Deploy**
   - Click "New app"
   - Select `hmari9192-bot/dropship-scout-pro`
   - Branch: `main`
   - File: `app.py`
   - Click "Deploy"

4. **Done!** 🎉 Your app is live!

---

### Option 2: Docker

**Time**: 10 minutes | **Cost**: Variable

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 8501
   CMD ["streamlit", "run", "app.py"]
   ```

2. **Build image**
   ```bash
   docker build -t dropship-scout-pro .
   ```

3. **Run container**
   ```bash
   docker run -p 8501:8501 dropship-scout-pro
   ```

4. **Access app**
   - Open http://localhost:8501

---

### Option 3: Heroku

**Time**: 5 minutes | **Cost**: $5-7/month

1. **Create Procfile**
   ```
   web: streamlit run app.py
   ```

2. **Create runtime.txt**
   ```
   python-3.9.16
   ```

3. **Deploy**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

4. **Access app**
   - https://your-app-name.herokuapp.com

---

### Option 4: AWS EC2

**Time**: 20 minutes | **Cost**: $5-50/month

1. **Launch EC2 Instance**
   - Ubuntu 22.04 LTS
   - t2.micro (free tier eligible)

2. **SSH into instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Install dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip git
   git clone https://github.com/hmari9192-bot/dropship-scout-pro.git
   cd dropship-scout-pro
   pip install -r requirements.txt
   ```

4. **Run with systemd**
   ```bash
   streamlit run app.py --server.port=80
   ```

---

### Option 5: Google Cloud Platform (GCP)

**Time**: 20 minutes | **Cost**: $100+/month

1. **Create project** on Google Cloud Console

2. **Deploy to Cloud Run**
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   gcloud run deploy dropship-scout-pro \
     --source . \
     --platform managed \
     --region us-central1
   ```

3. **Access app**
   - URL provided by GCP

---

## ✅ Pre-Deployment Checklist

- [ ] All dependencies listed in `requirements.txt`
- [ ] `.env.example` configured
- [ ] Tests passing (`pytest tests/`)
- [ ] Code committed to GitHub
- [ ] README.md complete
- [ ] No hardcoded secrets
- [ ] `.gitignore` configured

---

## 🔐 Security Checklist

- [ ] Environment variables for secrets
- [ ] `.env` in `.gitignore`
- [ ] No API keys in code
- [ ] HTTPS enabled (auto on Streamlit Cloud)
- [ ] Error messages don't expose sensitive info
- [ ] Rate limiting configured (if applicable)
- [ ] User input validated
- [ ] Data storage is secure

---

## 📊 Performance Optimization

### Cache Data
```python
@st.cache_data
def load_products():
    return PRODUCTS_DB
```

### Use Session State
```python
if 'data' not in st.session_state:
    st.session_state.data = load_data()
```

### Limit API Calls
```python
@st.cache_data(ttl=3600)
def get_trends():
    return fetch_trends()
```

---

## 🚨 Troubleshooting

### App Won't Start
```bash
# Check Python version
python --version

# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Run with debug
streamlit run app.py --logger.level=debug
```

### Import Errors
```bash
# Install missing packages
pip install streamlit pandas requests python-dotenv

# Check paths
python -c "import modules.scoring"
```

### Memory Issues
- Use `@st.cache_data` for expensive operations
- Limit data loaded to viewport
- Stream results instead of loading all

### Slow Performance
- Enable caching
- Reduce database queries
- Use lighter data structures
- Profile with `cProfile`

---

## 📈 Scaling

### For 100+ Concurrent Users
1. Move data to cloud storage (AWS S3, Google Cloud Storage)
2. Use database (PostgreSQL, MongoDB)
3. Add caching layer (Redis)
4. Load balance with multiple instances
5. Use CDN for static files

### Database Setup
```python
import psycopg2

conn = psycopg2.connect(
    host="your-db-host",
    database="dropship_scout",
    user="postgres",
    password="your-password"
)
```

---

## 🎯 Next Steps After Deployment

1. **Monitor Performance**
   - Check app logs
   - Monitor error rates
   - Track user engagement

2. **Gather Feedback**
   - Add feedback form
   - Monitor usage patterns
   - Iterate on features

3. **Scale Features**
   - Add API integrations
   - Build user accounts
   - Create mobile app

4. **Marketing**
   - Share on Product Hunt
   - Post on Reddit
   - Create demo video
   - Write blog posts

---

## 💡 Pro Tips

- **Streamlit Cloud**: Best for quick deployment
- **Docker**: Best for flexibility
- **Heroku**: Best for simplicity
- **AWS**: Best for scale
- **GCP**: Best for Google integration

---

## 📞 Support

- **Streamlit Docs**: https://docs.streamlit.io
- **GitHub Issues**: https://github.com/hmari9192-bot/dropship-scout-pro/issues
- **Community Forum**: https://discuss.streamlit.io

---

**Choose your platform and deploy today! 🚀**
