import os
from scanner import scan_repository
from llm_client import generate_summary
from storage import save_summary
from overview_generator import generate_repo_overview

def summarize_repository(repo_path, llm_endpoint, output_dir, skip_extensions, api_key=None):
    """Summarize all files in the repository and generate a final overview."""
    files = scan_repository(repo_path, skip_extensions)
    print(f"Found {len(files)} files to summarize in the repository.")
    
    # Ask for confirmation before proceeding
    proceed = input("Proceed with summarization? (y/n): ").strip().lower()
    if proceed != "y":
        print("Summarization canceled.")
        return
    
    for i, file_path in enumerate(files, 1):
        print(f"Processing file {i}/{len(files)}: {file_path}")
        
        with open(file_path, "r") as f:
            file_content = f.read()
        
        summary = generate_summary(file_content, llm_endpoint, api_key)
        save_summary(file_path, summary, output_dir)
        print(f"Summary saved for {file_path}")
    
    print("Generating repository overview...")
    overview = generate_repo_overview(output_dir, llm_endpoint)
    overview_path = os.path.join(output_dir, "repo_overview.md")
    
    with open(overview_path, "w") as f:
        f.write(overview)
    
    print("Repository overview saved to repo_overview.md")
    print("\n--- Repository Overview ---")
    print(overview)
