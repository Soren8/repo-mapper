import argparse
import os
from summarizer import summarize_repository

def main():
    parser = argparse.ArgumentParser(description="Generate summaries for a Git repository.")
    parser.add_argument("repo_path", type=str, help="Path to the Git repository.")
    parser.add_argument("--llm_endpoint", type=str, default="openrouter/deepseek/deepseek-chat",
                        help="LLM endpoint for summarization.")
    parser.add_argument("--output_dir", type=str, default="summaries",
                        help="Directory to store summary Markdown files.")
    parser.add_argument("--skip_extensions", type=str, nargs="+", default=[".bin", ".png", ".jpg"],
                        help="File extensions to skip.")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.repo_path):
        print(f"Error: Repository path '{args.repo_path}' does not exist.")
        return
    
    os.makedirs(args.output_dir, exist_ok=True)
    
    summarize_repository(args.repo_path, args.llm_endpoint, args.output_dir, args.skip_extensions)

if __name__ == "__main__":
    main()
