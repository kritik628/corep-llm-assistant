def check_consistency(corep_data: dict):
    issues = []

    values = {f["code"]: f["value"] for f in corep_data["fields"]}

    cet1 = values.get("010", 0)
    at1 = values.get("020", 0)
    tier2 = values.get("030", 0)
    total = values.get("040", 0)

    if total != cet1 + at1 + tier2:
        issues.append("Total Own Funds (040) does not equal sum of CET1 + AT1 + Tier2.")

    for code, value in values.items():
        if value < 0:
            issues.append(f"Field {code} has a negative value, which is invalid.")

    return issues
