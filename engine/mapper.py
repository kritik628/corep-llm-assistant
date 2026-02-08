def map_to_template(corep_data: dict) -> str:
    lines = []
    lines.append("COREP C 01.00 — Own Funds (Extract)")
    lines.append("-" * 50)
    lines.append(f"Entity: {corep_data['reporting_entity']}")
    lines.append(f"Reporting Date: {corep_data['reporting_date']}")
    lines.append("")
    lines.append(f"{'Code':<6} {'Field':<25} {'Value (GBP)':>15}")
    lines.append("-" * 50)

    for field in corep_data["fields"]:
        lines.append(f"{field['code']:<6} {field['field_name']:<25} {field['value']:>15,.0f}")

    return "\n".join(lines)
