# 🍽️ Foodie Tour Planner

A Julep AI workflow that creates personalized one-day foodie tours for multiple cities, considering local weather conditions and iconic dishes. Available in both **Node.js** and **Python** implementations.

![Workflow Status](https://img.shields.io/badge/status-working-brightgreen)
![Node.js](https://img.shields.io/badge/Node.js-18+-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)

## 🌟 Features

- **Multi-city Support**: Generate tours for multiple cities simultaneously
- **Weather Integration**: Indoor/outdoor dining recommendations based on current weather
- **Local Cuisine Discovery**: Automatically finds 3 iconic dishes per city
- **Restaurant Recommendations**: Locates top-rated restaurants serving local specialties
- **Complete Itineraries**: Provides breakfast, lunch, and dinner plans with narratives

## 🏗️ Project Structure

```
foodie-planner/
├── foodie-tour-nodejs/ # Node.js implementation
├── foodie-tour-python/ # Python implementation
└── README.md # This file
```

## 🚀 Quick Start

### Prerequisites

**For Node.js version:**
- Node.js 18+ ([Download](https://nodejs.org/))
- npm (comes with Node.js)

**For Python version:**
- Python 3.8+ ([Download](https://python.org/))
- pip (comes with Python)

**Required API Keys:**
- [Julep API Key](https://app.julep.ai) - AI workflow platform
- [OpenWeather API Key](https://openweathermap.org/api) - Weather data
- [Brave Search API Key](https://brave.com/search/api/) - Web search

### 🔧 Installation & Setup

# 1. Clone the repository
```
git clone <your-repo-url>
cd foodie-tour-workflow
```

# 2. Choose your implementation

# --- Node.js Setup ---
```
cd foodie-tour-nodejs
npm install
cp .env.example .env
# Edit .env with your API keys
# Then to run:
node index.js

# --- OR ---

# --- Python Setup ---
cd foodie-tour-python
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
# Then to run:
python main.py
```

## 📋 Sample Output

The workflow generates detailed foodie tours like this:

============================
NEW YORK FOODIE TOUR
🌤️ Weather: Partly cloudy, 72°F - Perfect for outdoor dining!

🥯 BREAKFAST (8:00 AM)
Russ & Daughters - Classic NYC Bagel with Lox
Recommendation: Outdoor seating to enjoy the morning atmosphere
Narrative: Start your day like a true New Yorker with this iconic breakfast...

🍕 LUNCH (1:00 PM)
Joe's Pizza - New York Style Pizza Slice
Recommendation: Quick indoor bite between sightseeing
Narrative: No NYC food tour is complete without authentic pizza...

🥩 DINNER (7:00 PM)
Peter Luger Steak House - Dry-Aged Porterhouse
Recommendation: Indoor fine dining experience
Narrative: End your day with the legendary steakhouse experience...


## 🛠️ Technical Details

### Workflow Architecture

The workflow consists of 4 main steps:
1. **Weather Check** - Gets current weather for each city
2. **Dish Discovery** - Finds 3 iconic local dishes per city  
3. **Restaurant Search** - Locates top-rated restaurants for each dish
4. **Itinerary Generation** - Creates personalized tour narratives

### API Integrations

- **Julep AI**: Workflow orchestration and LLM processing
- **OpenWeatherMap**: Real-time weather data
- **Brave Search**: Web search for dishes and restaurants

### Performance

- **Processing Time**: 5-15 minutes for 5 cities
- **Parallelism**: Step 3 runs with parallelism=3 for faster processing
- **Rate Limiting**: Handles API rate limits gracefully

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues

**Workflow runs for a longer time:**
- Check API key validity
- Verify rate limits aren't exceeded
- Try with fewer cities for testing

**"422 Unprocessable Entity" error:**
- Ensure YAML syntax is correct
- Verify API key field names match integration requirements

**Import errors:**
- Ensure all dependencies are installed
- Check Python/Node.js versions meet requirements

### Getting Help

- Check the [Issues](../../issues) page for known problems
- Create a new issue with detailed error information
- Include your environment details and steps to reproduce

## 🙏 Acknowledgments

- [Julep AI](https://julep.ai) for the workflow platform
- [OpenWeatherMap](https://openweathermap.org) for weather data
- [Brave Search](https://brave.com/search/api/) for search capabilities

---

**Built with ❤️ for food lovers and travelers**
Environment Template Files
Create .env.example in the root and each implementation folder:

text
# Copy this file to .env and fill in your actual API keys

# Julep AI Platform
JULEP_API_KEY=your_julep_api_key_here

# Weather API
OPENWEATHER_API_KEY=your_openweather_api_key_here

# Search API  
BRAVE_API_KEY=your_brave_search_api_key_here
Git Commands to Commit
bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit with descriptive message
git commit -m "Add Julep foodie tour workflow with Node.js and Python implementations

- Multi-city foodie tour generation
- Weather-based dining recommendations  
- Local cuisine discovery and restaurant search
- Complete breakfast/lunch/dinner itineraries
- Secure API key handling with .env files
- Comprehensive documentation and setup instructions"

# Add remote and push
git remote add origin <your-github-repo-url>
git push -u origin main
