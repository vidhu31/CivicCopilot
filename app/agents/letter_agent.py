from app.llm.groq_client import llm
from app.models.outputs import LetterOutput

structured_llm = llm.with_structured_output(
    LetterOutput
)

def letter_agent(
    issue_type: str,
    location: str,
    department: str
):

    prompt = f"""
You are a government complaint letter generator.

Generate:

- subject
- letter

Issue:
{issue_type}

Location:
{location}

Department:
{department}

Return a formal complaint letter.
"""

    return structured_llm.invoke(prompt)