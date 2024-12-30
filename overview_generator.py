import os
from llm_client import generate_summary

def generate_repo_overview(summary_dir, llm_endpoint, api_key=None):
    """Generate a high-level overview of the repository."""
    summaries = []
    for summary_file in os.listdir(summary_dir):
        if summary_file.endswith("_summary.md"):
            with open(os.path.join(summary_dir, summary_file), "r") as f:
                summaries.append(f.read())
    
    combined_summaries = "\n\n".join(summaries)
    prompt = f"Based on the following file summaries, generate a high-level overview of the repository:\n\n{combined_summaries}\n\n" \
             "Include sections for Intent, Design Patterns, Major Data Flows, and Inter-File Relationships."
    
    return generate_summary(prompt, llm_endpoint, api_key)
