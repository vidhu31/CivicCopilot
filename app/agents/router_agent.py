from app.llm.groq_client import llm
from app.models.outputs import RouterOutput

structured_llm = llm.with_structured_output(
    RouterOutput
)

def router_agent(issue_type: str) -> RouterOutput:

    prompt = f"""
You are an expert civic complaint routing agent.

Your job is to route complaints to the correct government department.

==================================
ROUTING RULES
==================================

Water Supply Issues:
- Water Supply Disruption
- Pipeline Leakage
- Water Leakage
- Low Water Pressure

Department:
Water Supply Department

----------------------------------

Electricity Issues:
- Street Light Failure
- Electricity Outage
- Transformer Failure
- Power Supply Problem

Department:
Electricity Department

----------------------------------

Road Issues:
- Road Damage
- Road Pothole
- Road Crack
- Damaged Road

Department:
Road Maintenance Department

----------------------------------

Sanitation Issues:
- Waste Collection Delay
- Garbage Overflow
- Drainage Blockage
- Sewer Overflow

Department:
Sanitation Department

----------------------------------

Public Safety Issues:
- Open Manhole Hazard
- Dangerous Electrical Wiring
- Public Safety Threat
- Stray Animal Hazard

Department:
Public Safety Department

----------------------------------

Unknown Issues:

Department:
General Civic Services

==================================
ISSUE TYPE
==================================

{issue_type}

==================================
RETURN
==================================

Return:

- department
- routing_reason

Example:

department = "Water Supply Department"

routing_reason =
"This complaint relates to water supply infrastructure and should be handled by the Water Supply Department."

"""

    return structured_llm.invoke(prompt)