import os

def save_summary(file_path, summary, output_dir):
    """Save the summary to a Markdown file, preserving relative paths under summaries/<REPO_NAME>/."""
    # Get the repository root (parent of the output_dir)
    repo_root = os.path.dirname(os.path.dirname(output_dir))  # Go up two levels: past <REPO_NAME> and summaries
    
    # Calculate relative path from repo root
    relative_path = os.path.relpath(file_path, repo_root)
    
    # Create the full output path preserving subdirectories
    summary_dir = os.path.join(output_dir, os.path.dirname(relative_path))
    os.makedirs(summary_dir, exist_ok=True)
    
    # Save the summary file
    summary_filename = os.path.basename(file_path) + "_summary.md"
    summary_path = os.path.join(summary_dir, summary_filename)
    
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary)
