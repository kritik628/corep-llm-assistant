def generate_audit_log(corep_data: dict) -> str:
    lines = []
    lines.append("Audit Log — Rule Traceability")
    lines.append("-" * 50)

    for field in corep_data["fields"]:
        refs = ", ".join(field.get("rule_references", []))
        lines.append(f"Field {field['code']} ({field['field_name']}):")
        lines.append(f"  Value: {field['value']:,} {field['unit']}")
        lines.append(f"  Rule References: {refs if refs else 'None'}")
        lines.append("")

    return "\n".join(lines)
