from app.llm.groq_client import llm
from app.models.outputs import ClassifierOutput

structured_llm = llm.with_structured_output(
    ClassifierOutput
)

def classifier_agent(text: str) -> ClassifierOutput:

    prompt = f"""
You are an expert civic complaint classifier.

Your job is to understand citizen complaints,
even when they are written in:

- Formal English
- Casual English
- Broken English
- Hindi
- Hinglish
- Typo-filled text

==================================
EXAMPLES
==================================

Complaint:
Water leakage near my society

Category:
Water Supply

Complaint:
I have water problem in my area

Category:
Water Supply

Complaint:
No water coming from tap

Category:
Water Supply

Complaint:
Water is not coming since morning

Category:
Water Supply

Complaint:
Mere area me pani nahi aa raha

Category:
Water Supply

Complaint:
मेरे इलाके में पानी नहीं आ रहा

Category:
Water Supply

Complaint:
Street light not working

Category:
Electricity

Complaint:
Street light not wrking

Category:
Electricity

Complaint:
Bijli nahi aa rahi

Category:
Electricity

Complaint:
Power cut since morning

Category:
Electricity

Complaint:
Road pe bada khadda hai

Category:
Road Maintenance

Complaint:
Pothole outside my house

Category:
Road Maintenance

Complaint:
Road damaged near market

Category:
Road Maintenance

Complaint:
Garbage not collected for 3 days

Category:
Sanitation

Complaint:
Kachra nahi uthaya gaya

Category:
Sanitation

Complaint:
Drain blockage near school

Category:
Sanitation

Complaint:
Open manhole on road

Category:
Public Safety

Complaint:
Stray dogs creating danger

Category:
Public Safety

Complaint:
Broken electric wire hanging

Category:
Public Safety

==================================
CATEGORY HINTS
==================================

Water Supply:
- water problem
- water issue
- no water
- low water pressure
- water leakage
- pipe burst
- pipeline leakage
- pani problem
- pani nahi aa raha
- jal supply issue

Electricity:
- light issue
- street light off
- power cut
- electricity issue
- electric pole damage
- transformer issue
- bijli problem

Road Maintenance:
- pothole
- khadda
- road broken
- road damage
- road crack
- damaged road

Sanitation:
- garbage
- kachra
- waste collection
- dirty area
- drain blockage
- sewer overflow

Public Safety:
- open manhole
- dangerous wiring
- stray dogs
- accident risk
- unsafe area
- broken electric wire

==================================
AVAILABLE CATEGORIES
==================================

- Water Supply
- Electricity
- Road Maintenance
- Sanitation
- Public Safety
- Other

==================================
ISSUE TYPE RULES
==================================

Use professional issue names.

Examples:

water problem
→ Water Supply Disruption

water leakage
→ Pipeline Leakage

no water supply
→ Water Supply Disruption

light problem
→ Street Light Failure

power cut
→ Electricity Outage

road problem
→ Road Damage

pothole
→ Road Pothole

garbage issue
→ Waste Collection Delay

drain blockage
→ Drainage Blockage

open manhole
→ Open Manhole Hazard

==================================
URGENCY SCALE
==================================

1 = Minor inconvenience

2 = Small issue affecting few citizens

3 = Normal civic complaint

4 = Serious disruption affecting many citizens

5 = Emergency, flooding,
fire hazard,
open manhole,
exposed electrical wires,
public safety threat

==================================
IMPORTANT RULES
==================================

- Never leave fields empty.
- Always choose the closest category.
- Always generate a professional issue_type.
- Understand Hindi and Hinglish.
- Understand spelling mistakes.
- Return urgency between 1 and 5 only.
- Provide a clear severity_reason.

==================================
COMPLAINT
==================================

{text}

"""

    return structured_llm.invoke(prompt)