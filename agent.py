import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get the API key from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print("Loaded API Key:", GROQ_API_KEY)  # For debug

# ✅ Define the correct API URL
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Set headers for the POST request
headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

# System instructions to guide the assistant
instructions = """
You are a flight travel expert focused only on flights. Given a query, provide 3 flight options including:

- Airline
- Stops
- Flight Duration
- Flight Number
- Class
- Estimated Cost (in USD)

Do not provide hotel, tour, or restaurant suggestions.
Keep answers structured and short.
"""

# Function to ask the AI
def ask_agent(user_query):
    body = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": instructions},
            {"role": "user", "content": user_query}
        ],
        "temperature": 0.7
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=body)

    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        return content
    else:
        return f"Error: {response.status_code} - {response.text}"

# Run the script
if __name__ == "__main__":
    query = "Find me a flight from Hyderabad to New York on 15th April 2025 under $1000."
    reply = ask_agent(query)
    print("\n✈️ Suggested Flights:\n")
    print(reply)
