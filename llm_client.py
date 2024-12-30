import requests
import json

def generate_summary(file_content, llm_endpoint, api_key=None):
    """Generate a summary for a file using the LLM."""
    prompt = f"Summarize the following code file:\n\n{file_content}\n\n" \
             "Provide a Markdown summary with sections: Purpose, Key Functions, Complete Function List, Uses, Used By."
    
    headers = {
        "Authorization": f"Bearer {api_key}",  # Required
        "Content-Type": "application/json",   # Required
        "HTTP-Referer": "https://github.com/yourusername/repo-summarizer",  # Optional, for OpenRouter rankings
        "X-Title": "Repo Summarizer"  # Optional, for OpenRouter rankings
    }
    
    payload = {
        "model": "deepseek/deepseek-chat",  # Correct model format: provider/model
        "messages": [{"role": "user", "content": prompt}]
    }
    
    # Ask for confirmation before sending the API request
    proceed = input(f"Send API request for summarization? (y/n): ").strip().lower()
    if proceed != "y":
        print("API request canceled.")
        return "No summary generated (API request canceled)."
    
    response = requests.post(
        llm_endpoint,
        headers=headers,
        json=payload  # Use `json` instead of `data=json.dumps(payload)`
    )
    
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No summary generated.")
    else:
        raise Exception(f"LLM API call failed: {response.status_code}, {response.text}")
