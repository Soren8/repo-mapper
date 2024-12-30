import os

def scan_repository(repo_path, skip_extensions):
    """Scan the repository for files, skipping specified extensions."""
    relevant_files = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if not any(file.endswith(ext) for ext in skip_extensions):
                relevant_files.append(os.path.join(root, file))
    return relevant_files
