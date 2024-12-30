import os
from llm_client import generate_summary

def generate_repo_overview(summary_dir, llm_endpoint, api_key=None):
    """Generate a high-level overview of the repository."""
    summaries = []
    
    # Include the contents of README.md
    readme_path = os.path.join(os.path.dirname(summary_dir), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            summaries.append(f"# README.md\n\n{f.read()}")
    
    # Include per-file summaries
    for summary_file in os.listdir(summary_dir):
        if summary_file.endswith("_summary.md"):
            with open(os.path.join(summary_dir, summary_file), "r", encoding="utf-8") as f:
                summaries.append(f.read())
    
    combined_summaries = "\n\n".join(summaries)
    prompt = f"Based on the following file summaries and README.md, generate a high-level overview of the repository:\n\n{combined_summaries}\n\n" \
             "Include sections for Intent, Design Patterns, Major Data Flows, and Inter-File Relationships.\n\n" \
             "**Note**: Focus on high-level details. Do not include granular information like a complete function list. Instead, link to the individual summary files for more details."
    
    return generate_summary(prompt, llm_endpoint, api_key)
