from app.models.outputs import TaskOutput


def task_agent(issue_type: str) -> TaskOutput:

    issue = issue_type.lower()

    # Water Related
    if any(word in issue for word in [
        "pipeline leakage",
        "water leakage",
        "leak"
    ]):
        return TaskOutput(
            task_title="Inspect and repair pipeline leakage",
            priority="High",
            estimated_resolution="24 hours"
        )

    elif any(word in issue for word in [
        "water supply disruption",
        "water supply",
        "no water"
    ]):
        return TaskOutput(
            task_title="Investigate water supply disruption",
            priority="High",
            estimated_resolution="24 hours"
        )

    # Electricity Related
    elif any(word in issue for word in [
        "street light failure",
        "street light",
        "electricity outage",
        "power cut"
    ]):
        return TaskOutput(
            task_title="Repair electrical infrastructure",
            priority="Medium",
            estimated_resolution="48 hours"
        )

    # Road Related
    elif any(word in issue for word in [
        "road pothole",
        "pothole",
        "road damage",
        "road crack"
    ]):
        return TaskOutput(
            task_title="Inspect and repair damaged road",
            priority="Medium",
            estimated_resolution="3 days"
        )

    # Sanitation Related
    elif any(word in issue for word in [
        "waste collection delay",
        "garbage",
        "drainage blockage",
        "sewer overflow"
    ]):
        return TaskOutput(
            task_title="Deploy sanitation maintenance team",
            priority="Medium",
            estimated_resolution="24 hours"
        )

    # Public Safety
    elif any(word in issue for word in [
        "open manhole hazard",
        "dangerous wiring",
        "public safety threat"
    ]):
        return TaskOutput(
            task_title="Dispatch emergency safety inspection team",
            priority="High",
            estimated_resolution="12 hours"
        )

    # Default
    return TaskOutput(
        task_title=f"Resolve {issue_type}",
        priority="Medium",
        estimated_resolution="48 hours"
    )