# Repository Summarizer

A Python application that scans all files in a Git repository, generates Markdown summaries for each file, and creates a high-level overview of the repository's architecture and design.

---

## Installation

1. Ensure Python 3.7+ is installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/repo-summarizer.git
   cd repo-summarizer
   ```
3. Install the required dependencies:
   ```bash
   pip install requests
   ```

---

## Configuration

The application can be configured via **command-line arguments** or by modifying the defaults in the code.

### Command-Line Arguments

| Argument            | Description                                                                 | Default Value                          |
|---------------------|-----------------------------------------------------------------------------|----------------------------------------|
| `repo_path`         | Path to the Git repository to summarize. If not provided, the current directory is used. | Current directory (`os.getcwd()`)      |
| `--llm_endpoint`    | LLM endpoint for summarization.                                             | `openrouter/deepseek/deepseek-chat`    |
| `--output_dir`      | Directory to store summary Markdown files.                                  | `summaries`                            |
| `--skip_extensions` | File extensions to skip (e.g., binary files, images).                       | `.bin`, `.png`, `.jpg`                 |
| `--api_key`         | API key for the LLM endpoint.                                               | None                                   |

---

## Usage

1. **Run the Script**:
   - To summarize the repository in the current directory:
     ```bash
     python cli.py --api_key YOUR_API_KEY
     ```
   - To summarize a specific repository:
     ```bash
     python cli.py /path/to/repo --api_key YOUR_API_KEY
     ```

2. **Output**:
   - Per-file summaries will be saved in the `summaries` directory (or the directory specified in `--output_dir`).
   - The final repository overview will be saved as `repo_overview.md` in the same directory and printed to stdout.

3. **Custom LLM Endpoint**:
   If you want to use a different LLM endpoint (e.g., Gemini), specify it with the `--llm_endpoint` argument:
   ```bash
   python cli.py /path/to/repo --llm_endpoint your_custom_endpoint --api_key YOUR_API_KEY
   ```

4. **Skipping Files**:
   To skip additional file extensions, specify them with the `--skip_extensions` argument:
   ```bash
   python cli.py /path/to/repo --skip_extensions .bin .png .jpg .mp4 --api_key YOUR_API_KEY
   ```

---

## Example Output

### Per-File Summary (`some_file.py_summary.md`)
```markdown
# some_file.py

## Purpose
This file handles user authentication and session management.

## Key Functions
- `authenticate_user(username, password)`: Validates user credentials.
- `create_session(user_id)`: Creates a new session for the user.

## Complete Function List
- `authenticate_user(username, password)`
- `create_session(user_id)`
- `delete_session(session_id)`

## Uses
- `database.py`: For querying user data.
- `utils.py`: For logging and error handling.

## Used By
- `app.py`: Calls `authenticate_user` and `create_session`.
```

### Final Repository Overview (`repo_overview.md`)
```markdown
# Repository Overview

## Intent
This repository is a web application for user authentication and session management.

## Design Patterns
- Singleton pattern for database connections.
- Factory pattern for session creation.

## Major Data Flows
1. User credentials are validated via `authenticate_user`.
2. A session is created and stored in the database.

## Inter-File Relationships
- `app.py` depends on `auth.py` for authentication.
- `auth.py` depends on `database.py` for user data.
```

---

## Notes

- **LLM Endpoint**: Ensure the specified LLM endpoint is accessible and supports the required API format.
- **Error Handling**: If the LLM API fails, the script will raise an exception. You can add retry logic or fallback mechanisms if needed.
- **Large Repositories**: For very large repositories, consider chunking files or optimizing the LLM prompt to reduce context size.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
