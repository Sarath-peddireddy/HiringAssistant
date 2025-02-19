# TalentScout Hiring Assistant 🤖

An intelligent chatbot built with Streamlit and OpenAI's GPT-4 for automating the initial technical screening of candidates in the recruitment process.

## 🌟 Features

- Interactive chat interface
- Automated collection of candidate information
- Dynamic technical question generation based on tech stack
- Context-aware conversation flow
- Data privacy compliance
- Secure handling of sensitive information

## 🛠️ Tech Stack

- Python 3.8+
- Streamlit
- OpenAI GPT-4
- Python-dotenv
- Python-decouple

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Git

## 🚀 Installation

1. Clone the repository

bash
git clone https://github.com/Sarath-peddireddy/HiringAssistant.git
cd talent-scout

2. Create and activate virtual environment
Windows
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt


4. Create .env file in the project root and add your OpenAI API key
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-4
MAX_TOKENS=500
TEMPERATURE=0.7


## 🎯 Usage

1. Start the application

streamlit run app.py

2. Open your browser and navigate to `http://localhost:8501`

3. Start interviewing candidates!

## 📁 Project Structure
talent_scout/
├── .env # Environment variables (not in repo)
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── app.py # Main Streamlit application
├── src/
│ ├── init.py
│ ├── config.py # Configuration settings
│ ├── chatbot/
│ │ ├── init.py
│ │ ├── assistant.py # Core chatbot logic
│ │ ├── prompts.py # Prompt templates
│ │ └── utils.py # Helper functions
│ └── data/
│ ├── init.py
│ └── data_handler.py # Data management
└── tests/
├── init.py
└── test_assistant.py # Unit tests

## 🧪 Running Tests
python -m unittest tests/test_assistant.py


## 🔒 Security

- Environment variables are used for sensitive data
- Input validation and sanitization implemented
- Secure handling of candidate information
- GDPR-compliant data handling

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Important Notes

- Never commit your `.env` file or expose your API keys
- Ensure compliance with local data protection regulations
- Regularly update dependencies for security patches

## 🐛 Known Issues

- None currently reported

## 🔮 Future Enhancements

- [ ] Add support for multiple languages
- [ ] Implement candidate response analysis
- [ ] Add integration with ATS systems
- [ ] Implement advanced analytics dashboard
- [ ] Add support for video interviews

## 📧 Contact

Your Name - sarathpeddireddy93477@gmail.com
Project Link: [https://github.com/Sarath-peddireddy/HiringAssistant](https://github.com/Sarath-peddireddy/HiringAssistant)

## 🙏 Acknowledgments

- OpenAI for their powerful GPT models
- Streamlit for their amazing framework
