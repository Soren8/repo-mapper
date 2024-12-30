import requests
import json

def generate_summary(file_content, llm_endpoint, api_key=None):
    """Generate a summary for a file using the LLM."""
    prompt = f"Summarize the following code file:\n\n{file_content}\n\n" \
             "Provide a Markdown summary with sections: Purpose, Key Functions, Complete Function List, Uses, Used By."
    
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    
    response = requests.post(
        llm_endpoint,
        headers=headers,
        data=json.dumps({"prompt": prompt})
    )
    
    if response.status_code == 200:
        return response.json().get("summary", "No summary generated.")
    else:
        raise Exception(f"LLM API call failed: {response.status_code}")
