# News Automation Script

## Overview
This Python script automates the process of collecting the latest news headlines from India using the NewsAPI. It fetches, processes, and saves the news headlines to a timestamped Excel file every 10 minutes. This simulates a real-world scenario where businesses need up-to-date news data for analysis and decision-making.

## Prerequisites
1. **Python** (version 3.7 or higher)
2. **NewsAPI Account**: Register for an API key at [NewsAPI](https://newsapi.org/register).

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```


2. **Install Required Libraries**:
   The required Python libraries are listed in the `requirements.txt` file. You can install them using `pip`.

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**

Create a `.env` file in the project root directory to securely store your API key.

```plaintext
NEWS_API_KEY=<your_newsapi_key_here>
```

## Running the Script

1. **Run the Automation Script**: 
   The script will fetch news headlines immediately upon starting and then repeat every 10 minutes.

   ```bash
   python main.py