# 🎓 AI Curriculum Generator

An intelligent curriculum generation system powered by OpenAI Agents SDK that creates structured, high-quality learning outlines for any topic.

## ✨ Features

- **AI-Powered Generation**: Uses OpenAI's advanced language models to create comprehensive curricula
- **Quality Assurance**: Built-in curriculum checker to ensure content meets learning objectives
- **Detailed Lesson Planning**: Generates specific lessons with explanations, examples, and practice questions
- **Async Processing**: Efficient asynchronous workflow for faster generation
- **Structured Output**: Uses Pydantic models for consistent, reliable data structures

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kobowood1/ai-agents-curriculum-generator.git
   cd ai-agents-curriculum-generator
   ```

2. **Install dependencies**
   ```bash
   pip install openai-agents pydantic python-dotenv
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   
   **Note**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

### Getting Your OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Create a new API key
4. Copy the key to your `.env` file

## 📖 Usage

### Basic Usage

Run the curriculum generator:

```bash
python curriculum_agents.py
```

The program will generate a curriculum for the default learning goal defined in the code. To customize the learning goal, modify the `learning_goal` variable in the `main()` function:

```python
async def main():
    learning_goal = input("What do you want to learn? ")
    # ... rest of the code
```

### Example Output

The system generates:
1. **Initial Curriculum**: Structured outline with goals and topics
2. **Quality Check**: Verification that the curriculum meets objectives
3. **Detailed Lessons**: Comprehensive lessons for each section

## 🏗️ Project Structure

```
curriculum-generator/
├── curriculum_agents.py    # Main application file
├── .env                   # Environment variables (not in repo)
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── requirements.txt      # Python dependencies (optional)
```

## 🧠 How It Works

The system uses three specialized AI agents:

1. **Curriculum Agent**: Generates the initial structured curriculum outline
2. **Curriculum Checker**: Validates quality and alignment with learning goals  
3. **Lesson Writer**: Creates detailed lessons for each curriculum section

### Agent Workflow

```
Learning Goal → Curriculum Agent → Curriculum Checker → Lesson Writer → Final Output
```

## 🛠️ Development

### Running in Development Mode

For development, you can modify the agents' instructions or add new functionality:

1. Edit agent configurations in `curriculum_agents.py`
2. Modify the Pydantic models for different output structures
3. Add new agents for specialized tasks

### Adding New Features

- **Custom Templates**: Modify agent instructions for different curriculum styles
- **Multiple Formats**: Add output options (PDF, HTML, etc.)
- **Interactive Mode**: Create a CLI interface for dynamic input
- **GUI Interface**: Integrate with Streamlit or Gradio for web interface

## 📋 Requirements

Create a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

Current dependencies:
- `openai-agents`
- `pydantic`
- `python-dotenv`
- `asyncio` (built-in)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the GNU Lesser General Public License v2.1 - see the [LICENSE](LICENSE) file for details.

## ⚠️ Important Notes

- **API Costs**: This project uses OpenAI's API which incurs costs based on usage
- **Rate Limits**: Be aware of OpenAI's rate limiting policies
- **Security**: Never commit your API key or share it publicly

## 🐛 Troubleshooting

### Common Issues

**Import Error: No module named 'agents'**
```bash
pip install openai-agents
```

**API Key Error**
- Ensure your `.env` file is in the project root
- Verify your API key is correct and has sufficient credits
- Check that `python-dotenv` is installed

**Permission Errors**
- Ensure you have proper file permissions
- On Windows, run PowerShell as Administrator if needed

## 📞 Support

If you encounter issues:
1. Check the [OpenAI Agents SDK Documentation](https://openai.github.io/openai-agents-python/)
2. Review the troubleshooting section above
3. Open an issue on GitHub

## 🎯 Future Enhancements

- [ ] Web-based GUI with Streamlit
- [ ] Multiple curriculum formats (PDF, DOCX export)
- [ ] Integration with educational platforms
- [ ] Multi-language support
- [ ] Curriculum templates for different subjects
- [ ] Progress tracking and assessment generation

---

**Made with ❤️ using OpenAI Agents SDK**