import requests
import json

def generate_summary(file_content, llm_endpoint, api_key=None, llm_model="deepseek/deepseek-chat", yes=False):
    """Generate a summary for a file using the LLM."""
    # Let the LLM determine if the file is a core code file
    prompt = f"Analyze the following file content and determine if it is a core code file. If it is a core code file, provide a Markdown summary with sections: Key Functions, Complete Function List, Uses, and Used By. If it is not a core code file, provide a very concise summary (1-2 sentences) describing its purpose and relevance. **Do not include any preamble or explanation in your response.**\n\nFile Content:\n\n{file_content}"
    
    headers = {
        "Authorization": f"Bearer {api_key}",  # Required
        "Content-Type": "application/json",   # Required
        "HTTP-Referer": "https://github.com/yourusername/repo-summarizer",  # Optional, for OpenRouter rankings
        "X-Title": "Repo Summarizer"  # Optional, for OpenRouter rankings
    }
    
    payload = {
        "model": llm_model,  # Use the specified LLM model
        "messages": [{"role": "user", "content": prompt}]
    }
    
    # Skip confirmation if --yes flag is set
    if not yes:
        proceed = input(f"Send API request for summarization? (y/n): ").strip().lower()
        if proceed != "y":
            print("API request canceled.")
            return None
    
    response = requests.post(
        llm_endpoint,
        headers=headers,
        json=payload  # Use `json` instead of `data=json.dumps(payload)`
    )
    
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No summary generated.")
    else:
        raise Exception(f"LLM API call failed: {response.status_code}, {response.text}")
