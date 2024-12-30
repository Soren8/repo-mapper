import os
from scanner import scan_repository
from llm_client import generate_summary
from storage import save_summary
from overview_generator import generate_repo_overview

def summarize_repository(repo_path, llm_endpoint, output_dir, skip_extensions):
    """Summarize all files in the repository and generate a final overview."""
    files = scan_repository(repo_path, skip_extensions)
    
    for file_path in files:
        with open(file_path, "r") as f:
            file_content = f.read()
        
        summary = generate_summary(file_content, llm_endpoint)
        save_summary(file_path, summary, output_dir)
    
    overview = generate_repo_overview(output_dir, llm_endpoint)
    overview_path = os.path.join(output_dir, "repo_overview.md")
    
    with open(overview_path, "w") as f:
        f.write(overview)
    
    print(overview)
