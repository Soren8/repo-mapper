import os

def scan_repository(repo_path, skip_extensions):
    """Scan the repository for files, skipping specified extensions and ignored paths."""
    ignored_paths = {".git", "__pycache__", "summaries", ".aider*"}
    
    # Read .gitignore if it exists
    gitignore_path = os.path.join(repo_path, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):  # Skip comments and empty lines
                    ignored_paths.add(line)
    
    relevant_files = []
    for root, dirs, files in os.walk(repo_path):
        # Remove ignored directories from traversal
        dirs[:] = [d for d in dirs if d not in ignored_paths and not any(d.startswith(p.rstrip("*")) for p in ignored_paths)]
        
        for file in files:
            file_path = os.path.join(root, file)
            # Skip files with ignored extensions or in ignored paths
            if (not any(file.endswith(ext) for ext in skip_extensions) and
                not any(part in ignored_paths for part in file_path.split(os.sep))):
                relevant_files.append(file_path)
    return relevant_files
