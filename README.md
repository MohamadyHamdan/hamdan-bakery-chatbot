# EventForecast - Agent-Powered Business Assistant

An intelligent chatbot representing **EventForecast**, a smart assistant that helps users plan their days by combining weather forecasts with local event recommendations.

## 🎯 Features

- **Answers business questions**: Provides information about EventForecast's services, mission, and team
- **Collects customer leads**: Records contact information when users express interest
- **Logs feedback**: Captures unanswered questions for team follow-up
- **AI-powered**: Uses OpenAI API (GPT-3.5-turbo) for natural conversations
- **Easy deployment**: Gradio interface for quick demos and deployment

## 📁 Project Structure

```
business_bot/
│
├── me/
│   ├── about_business.pdf      # Detailed business profile
│   └── business_summary.txt    # Business summary text
│
├── business_agent.ipynb        # Main notebook implementation
├── app.py                      # Standalone deployment script
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd business_bot
pip install -r requirements.txt
```

### 2. Set Up API Key

Create a `.env` file in the `business_bot` directory:

```
OPENAI_API_KEY=your_actual_api_key_here
```

Get your API key from: https://platform.openai.com/api-keys

### 3. Run the Application

**Option A: Using Jupyter Notebook**
```bash
jupyter notebook business_agent.ipynb
```
Then run all cells.

**Option B: Using Python Script**
```bash
python app.py
```

The Gradio interface will launch and provide a local URL to access the chatbot.

## 🛠️ Tool Functions

The agent has access to two main tools:

### 1. `record_customer_interest(email, name, message)`
- **Purpose**: Collect customer leads
- **Triggered when**: User provides name and email
- **Output**: Saves to `leads.log`

### 2. `record_feedback(question)`
- **Purpose**: Log unanswered questions or feedback
- **Triggered when**: Agent doesn't know the answer
- **Output**: Saves to `feedback.log`

## 💬 Example Interactions

**User**: What is EventForecast?
**Agent**: EventForecast is a smart assistant that helps you plan your days by providing accurate weather forecasts and local event recommendations in one place...

**User**: I'm interested! My name is John Doe and email is john@example.com
**Agent**: *[Calls record_customer_interest tool]* Thank you John! Your information has been recorded. We'll reach out to you at john@example.com soon.

**User**: What's the weather in Beirut?
**Agent**: Beirut has a Mediterranean climate with mild, rainy winters and hot, humid summers. In October, you can expect pleasant temperatures around 20-25°C with occasional rain. For real-time forecasts and personalized event recommendations, our EventForecast service provides live updates!

**User**: What are your pricing plans?
**Agent**: *[Calls record_feedback tool if pricing info not available]* I don't have detailed pricing information at the moment, but I've recorded your question for our team...

## 📊 Business Information

**EventForecast** - Your Daily Weather & Event Planner

- **Mission**: Make daily planning effortless by combining real-time weather insights with curated local events
- **Services**:
  - Real-time weather forecasts for any city
  - Local events and attraction recommendations
  - Personalized outfit or umbrella suggestions
  - User feedback collection

- **Team**:
  - Mohamad Hamdan — Founder & CEO
  - Lina Badran — CTO

- **Unique Value Proposition**: Combines weather updates and event discovery into a single chatbot interface

## 🌐 Deployment Options

### Local Development
```bash
python app.py
```

### HuggingFace Spaces (Bonus)

1. Create a new Space on HuggingFace
2. Upload all files from `business_bot/`
3. Add `OPENAI_API_KEY` as a secret in Space settings
4. Deploy!

## 📝 Files Generated During Use

- `leads.log` - Contains all collected customer information
- `feedback.log` - Contains all logged feedback and unanswered questions

## 🔧 Customization

To adapt this for a different business:

1. Update `me/business_summary.txt` with your business info
2. Update `me/about_business.pdf` with detailed information
3. Modify the `system_prompt` in the code to match your business tone
4. Optionally add more tool functions for specific business needs

## 📚 Technologies Used

- **OpenAI API** (GPT-3.5-turbo) - AI language model
- **Gradio** - Web interface framework
- **Python-dotenv** - Environment variable management
- **PyPDF2** - PDF text extraction

## 🎓 Assignment Context

This project was created for EECE 503P - Agent-Powered Business Assignment
**Objective**: Build a smart agent that represents a fictitious business with tool-calling capabilities.

## 📄 License

This is an educational project created for coursework.

## 👥 Contact

For questions about EventForecast:
- Email: info@eventforecast.ai
- Website: www.eventforecast.ai

---

**Note**: This is a demonstration project. EventForecast is a fictitious business created for educational purposes.
