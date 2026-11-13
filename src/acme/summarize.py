"""Summarize driver delay notes with Claude.

Run: python -m acme.summarize            (needs ANTHROPIC_API_KEY in .env or the environment)
Phase 4 exercise: improve the prompt, build a small eval set, and expose this via the API.
"""

import anthropic
from dotenv import load_dotenv

from acme.ingest import DATA_DIR

MODEL = "claude-opus-5-5"

SYSTEM_PROMPT = """You help a logistics operations team understand why shipments were late.
You will get raw driver and dispatcher notes. For each shipment ID, give:
- root cause category: one of carrier, shipper, receiver, weather/road, equipment, unknown
- a one-sentence plain-English explanation
Then give the top recurring cause across all shipments and one suggested action.
If the notes don't say why something was late, say "unknown". Do not guess."""


def load_notes() -> str:
    return (DATA_DIR / "delay_notes.txt").read_text()


def summarize_notes(notes: str, client: anthropic.Anthropic | None = None) -> str:
    if not notes.strip():
        return "No delay notes to summarize."
    client = client or anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
    response = client.beta.messages.create(
        model=MODEL,
        max_tokens=16000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"<notes>\n{notes}\n</notes>"}],
        output_config={"effort": "low"},
        # If the model declines, the API retries on a fallback model in the same call.
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    )
    if response.stop_reason == "refusal":
        return "The model declined to summarize these notes."
    return "".join(block.text for block in response.content if block.type == "text")


def main() -> None:
    load_dotenv()
    try:
        print(summarize_notes(load_notes()))
    except anthropic.AuthenticationError:
        print("Set ANTHROPIC_API_KEY in .env (see .env.example).")
    except anthropic.RateLimitError:
        print("Rate limited; wait a moment and retry.")
    except anthropic.APIConnectionError:
        print("Could not reach the Claude API; check your network.")


if __name__ == "__main__":
    main()
