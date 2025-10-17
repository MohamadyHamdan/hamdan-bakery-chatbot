📄 README.md
# 🥐 Hamdan Bakery Chatbot

An AI-powered business assistant built for a **fictional artisan bakery**, Hamdan Bakery.  
This chatbot can answer questions about the bakery, collect customer leads (name, email, message), and log unanswered questions — all powered by OpenAI's API and Gradio.

---

## 📌 Features
- 💬 Answers questions using content from `business_summary.txt` and `about_business.pdf`
- 📝 Logs unanswered questions through a feedback tool
- ✉️ Collects customer leads through a lead tool
- 🤖 Deployed with Gradio for a simple web interface
- 🧠 All responses come **only** from the PDF/TXT knowledge base (no internet or external sources)

---

## 📂 Project Structure



BUSINESS_BOT/
├── me/
│ ├── about_business.pdf # Detailed business profile
│ └── business_summary.txt # Summary description
├── app.py # Optional deployment file (Gradio app)
├── business_agent.ipynb # Google Colab / Jupyter Notebook implementation
├── requirements.txt # Dependencies
├── .gitignore
└── .env # API key (NOT COMMITTED)


---

## 🚀 Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/hamdan-bakery-chatbot.git
cd hamdan-bakery-chatbot

2️⃣ Create a .env file with your OpenAI API key
OPENAI_API_KEY=sk-xxxxxx

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the Gradio app
python app.py


Then open the URL shown in your terminal — usually http://127.0.0.1:7860
 or a public Gradio link.

🧠 How It Works

The chatbot loads text from the PDF and TXT files in me/

It sets a system prompt instructing it to stay “in character” as Hamdan Bakery

The OpenAI API is used for chat completions

Tool calls:

record_customer_interest → logs name, email, message

record_feedback → logs questions the bot couldn’t answer