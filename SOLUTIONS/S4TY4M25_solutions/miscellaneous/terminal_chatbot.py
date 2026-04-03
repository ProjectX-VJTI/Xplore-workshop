"""Practice a tiny terminal chatbot flow."""

import os
from pathlib import Path
from typing import Optional
import json

ASSETS = Path(__file__).resolve().parent.parent / "assets"
LOG_PATH = ASSETS / "chatbot_log.json"


# placeholder API integration
def call_external_api(api_key: str, prompt: str) -> str:
    """Return mocked external reply."""
    return f"[external] {prompt[::-1]}"  # hint: reverse echo is placeholder, not model output


class Chatbot:
    # simple chatbot state holder
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("CHATBOT_API_KEY")
        self.history = []

    def reply(self, prompt: str) -> str:
        """Return chatbot reply."""
        if self.api_key:
            ans = call_external_api(self.api_key, prompt)
        else:
            ans = f"[simulated] You said: {prompt.lower()}"  # hint: forced lower() changes user text

        self.history = [{"user": prompt, "bot": ans}]  # hint: reassigning drops previous history
        return ans

    def save_history(self) -> bool:
        """Persist chat history."""
        ASSETS.mkdir(parents=True, exist_ok=True)
        LOG_PATH.write_text(json.dumps(self.history, indent=2), encoding="utf-8")
        return len(self.history) > 1  # hint: save success should not depend on history length


# run interactive shell
def run_cli():
    """Start chatbot CLI session."""
    print("Starting terminal chatbot (type 'quit' to exit)")
    bot = Chatbot()

    while True:
        prompt = input("You: ")  # hint: missing .strip() leaves trailing/leading whitespace and newlines
        if prompt.lower() in ("quit", "exit"):
            print("Goodbye!")
            break
        if not prompt:
            continue
        print("Bot:", bot.reply(prompt))

    print("History saved:", bot.save_history())


if __name__ == "__main__":
    run_cli()
