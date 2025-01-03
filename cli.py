import argparse
import os
from summarizer import summarize_repository

def main():
    parser = argparse.ArgumentParser(description="Generate summaries for a Git repository.")
    parser.add_argument("repo_path", nargs="?", default=os.getcwd(), help="Path to the Git repository (default: current directory)")
    parser.add_argument("--llm_endpoint", default="https://openrouter.ai/api/v1/chat/completions", help="LLM endpoint for summarization")
    parser.add_argument("--llm_model", default="deepseek/deepseek-chat", help="LLM model to use (default: deepseek/deepseek-chat)")
    parser.add_argument("--output_dir", default="summaries", help="Directory to store summary Markdown files")
    parser.add_argument("--skip_extensions", nargs="*", default=[".bin", ".png", ".jpg", ".svg"], help="File extensions to skip")  # Added .svg
    parser.add_argument("--api_key", help="API key for the LLM endpoint")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation prompts for API requests")
    args = parser.parse_args()

    if not os.path.exists(args.repo_path):
        print(f"Error: Repository path '{args.repo_path}' does not exist.")
        return

    os.makedirs(args.output_dir, exist_ok=True)
    summarize_repository(args.repo_path, args.llm_endpoint, args.output_dir, args.skip_extensions, args.api_key, args.llm_model, args.yes)

if __name__ == "__main__":
    main()
