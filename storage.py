import os

def save_summary(file_path, summary, output_dir):
    """Save the summary to a Markdown file."""
    summary_filename = os.path.basename(file_path) + "_summary.md"
    summary_path = os.path.join(output_dir, summary_filename)
    
    with open(summary_path, "w") as f:
        f.write(summary)
