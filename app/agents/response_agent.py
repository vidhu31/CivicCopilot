from app.llm.groq_client import llm
from app.models.outputs import ResponseOutput

structured_llm = llm.with_structured_output(
    ResponseOutput
)

def response_agent(
    issue_type: str,
    department: str,
    urgency: int
) -> ResponseOutput:

    prompt = f"""
You are a civic grievance response officer.

Generate a professional response for the citizen.

Complaint Details:

Issue Type:
{issue_type}

Department:
{department}

Urgency:
{urgency}

Instructions:

- Be polite
- Be professional
- Reassure the citizen
- Mention the department
- Mention expected action
- Keep response under 80 words

Return:

- citizen_response
"""

    return structured_llm.invoke(prompt)