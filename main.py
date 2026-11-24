import os

TEXT = "I replied-all to say 'please stop replying-all' and got forty-seven replies agreeing with me."


def main():
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "gate: 1-200 chars, not whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
