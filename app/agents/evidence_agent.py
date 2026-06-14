from app.llm.groq_client import llm
from app.models.outputs import EvidenceOutput

structured_llm = llm.with_structured_output(
    EvidenceOutput
)

def evidence_agent(text: str) -> EvidenceOutput:

    prompt = f"""
You are an expert civic evidence extraction agent.

Your job is to extract useful evidence from citizen complaints.

The complaint may be written in:

- Formal English
- Casual English
- Broken English
- Hindi
- Hinglish
- Typo-filled text

==================================
EXTRACT
==================================

Extract:

- location
- issue
- duration
- landmarks

==================================
IMPORTANT RULES
==================================

1. landmarks MUST ALWAYS be a list.
2. If landmarks are not mentioned return [].
3. Never return a string for landmarks.
4. Never leave fields empty.
5. If duration is missing return:
   "not specified"
6. If location is missing return:
   "not specified"
7. Understand Hindi and Hinglish.
8. Extract landmarks separately from location.

==================================
EXAMPLES
==================================

Complaint:
Water leakage near Saraswati School

Output:
location = "near Saraswati School"
issue = "water leakage"
duration = "not specified"
landmarks = ["Saraswati School"]

Complaint:
Water leakage near school for 3 days

Output:
location = "near school"
issue = "water leakage"
duration = "3 days"
landmarks = ["school"]

Complaint:
Pothole near railway station for 2 weeks

Output:
location = "near railway station"
issue = "pothole"
duration = "2 weeks"
landmarks = ["railway station"]

Complaint:
Garbage not collected near market

Output:
location = "near market"
issue = "garbage not collected"
duration = "not specified"
landmarks = ["market"]

Complaint:
I have water problem in my area

Output:
location = "my area"
issue = "water problem"
duration = "not specified"
landmarks = []

Complaint:
Water issue

Output:
location = "not specified"
issue = "water issue"
duration = "not specified"
landmarks = []

Complaint:
Mere area me pani nahi aa raha

Output:
location = "mere area"
issue = "water supply problem"
duration = "not specified"
landmarks = []

Complaint:
Mere area me 3 din se pani nahi aa raha

Output:
location = "mere area"
issue = "water supply problem"
duration = "3 days"
landmarks = []

Complaint:
मेरे इलाके में पानी नहीं आ रहा

Output:
location = "मेरे इलाके में"
issue = "पानी की समस्या"
duration = "not specified"
landmarks = []

Complaint:
मेरे इलाके में 2 दिन से बिजली नहीं है

Output:
location = "मेरे इलाके में"
issue = "बिजली की समस्या"
duration = "2 days"
landmarks = []

Complaint:
सड़क पर बड़ा गड्ढा है रेलवे स्टेशन के पास

Output:
location = "रेलवे स्टेशन के पास"
issue = "road pothole"
duration = "not specified"
landmarks = ["रेलवे स्टेशन"]

==================================
COMPLAINT
==================================

{text}

"""

    return structured_llm.invoke(prompt)