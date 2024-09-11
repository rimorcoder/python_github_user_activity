# GitHub User Activity
 
https://roadmap.sh/projects/github-user-activity

This script queries GitHub's event activity API to retrieve and display recent activity for a specified GitHub username.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Ensure you have Python 3 installed. If not, download and install it from the [official Python website](https://www.python.org/).
2. Create a virtual environment using the following command:
    ```
    python -m venv .venv
    ```
3. Activte the virtual environment:
    ```
    .\.venv\Scripts\activate    
    ```
4. Install the `requests` library using pip:
   ```
   pip install requests
   ```

## Usage
1. Save the script to a file named `github_activity.py`.
2. Open your terminal or command prompt.
3. Run the script with the GitHub username you want to query. For example:

    ```
    python github_activity.py <github-username>
    ```
    Replace <github-username> with the actual GitHub username.

## Output
The script will output recent GitHub events for the specified user. Each event will include:

- Event Type: The type of GitHub event.
- Repository: The repository associated with the event.
- Date: The date and time when the event occurred.

Example output:
```
Event Type: PushEvent
Repository: <github-username>/Hello-World
Date: 2024-09-10T12:34:56Z
----------------------------------------
Event Type: PullRequestEvent
Repository: <github-username>/Hello-World
Date: 2024-09-09T08:22:34Z
----------------------------------------
```

## Notes
- Ensure the username you provide is valid and exists on GitHub.
- The script retrieves public event data, so private repositories or private activities will not be included.