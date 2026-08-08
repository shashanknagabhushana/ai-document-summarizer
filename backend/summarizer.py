def summarize_text(text: str) -> str:
    """
    Temporary local summarizer.

    This will be replaced with an AI model later.
    """

    if not text.strip():
        return "No text was found in the document."

    sentences = [
        sentence.strip()
        for sentence in text.replace("\n", " ").split(".")
        if sentence.strip()
    ]

    if len(sentences) <= 3:
        return ". ".join(sentences) + "."

    summary = ". ".join(sentences[:3])

    return (
        "Summary:\n\n"
        + summary
        + ".\n\n"
        + f"Original document: {len(text)} characters."
    )
