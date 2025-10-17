import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import fitz  # PyMuPDF
import gradio as gr

# ==============================
# Load API key
# ==============================
load_dotenv()
if "OPENAI_API_KEY" not in os.environ:
    raise ValueError("❌ OPENAI_API_KEY not found. Make sure it's set in .env file.")

client = OpenAI()

# ==============================
# Load Knowledge Base
# ==============================
TXT_PATH = "me/business_summary.txt"
PDF_PATH = "me/about_business.pdf"


def load_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_pdf(path):
    text = ""
    with fitz.open(path) as doc:
        for page in doc:
            text += page.get_text()
    return text

business_text = load_txt(TXT_PATH)
business_pdf_text = load_pdf(PDF_PATH)
knowledge_base = (business_text + "\n\n" + business_pdf_text)[:10000]  # truncate if needed

# ==============================
# System Prompt
# ==============================
system_prompt = f"""
You are hamdan_bakery, a friendly neighborhood artisan bakery chatbot 🍞.
Use ONLY the information provided below to answer user questions. 
Do not make up or invent details — if you don't find the answer, 
call the record_feedback tool.

Knowledge base:
{knowledge_base}

Guidelines:
- Speak in a warm and concise tone, as if you are the bakery.
- When users ask about orders, products, or services, refer to the text above.
- Encourage users to leave their name and email for pre-orders, custom cakes, or delivery.
- If a question is outside your knowledge, log it with record_feedback(question).
"""

# ==============================
# Tools
# ==============================
def record_customer_interest(email: str, name: str, message: str):
    log = f"[LEAD] Name: {name}, Email: {email}, Message: {message}"
    print(log)
    with open("customer_leads.log", "a", encoding="utf-8") as f:
        f.write(log + "\n")

def record_feedback(question: str):
    log = f"[FEEDBACK] Unanswered question: {question}"
    print(log)
    with open("feedback.log", "a", encoding="utf-8") as f:
        f.write(log + "\n")

tools = [
    {
        "type": "function",
        "function": {
            "name": "record_customer_interest",
            "description": "Record customer leads with name, email, and message",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {"type": "string"},
                    "name": {"type": "string"},
                    "message": {"type": "string"}
                },
                "required": ["email", "name", "message"]
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "record_feedback",
            "description": "Log a question the bot cannot answer",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {"type": "string"}
                },
                "required": ["question"]
            },
        },
    }
]

# ==============================
# Agent Function
# ==============================
def run_agent(user_input, chat_history):
    messages = [{"role": "system", "content": system_prompt}] + chat_history + [
        {"role": "user", "content": user_input}
    ]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    message = response.choices[0].message
    if message.tool_calls:
        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)

            if tool_name == "record_customer_interest":
                record_customer_interest(**tool_args)
                return "Thanks for your interest! We’ve logged your info and will get back to you soon 📝"

            elif tool_name == "record_feedback":
                record_feedback(**tool_args)
                return "Hmm, I’m not sure about that — but I’ve logged your question so we can follow up 👌"

    return message.content

# ==============================
# Gradio Interface
# ==============================
chat_history = []

def chatbot_interface(user_input, history):
    global chat_history
    reply = run_agent(user_input, chat_history)
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": reply})
    return reply

demo = gr.ChatInterface(
    fn=chatbot_interface,
    title="🥐 hamdan_bakery Chatbot",
    description="Ask me about our breads, pastries, cakes, or place an order!",
)

if __name__ == "__main__":
    demo.launch()
