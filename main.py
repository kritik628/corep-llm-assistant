from engine.retriever import simple_retrieve
from engine.generator import generate_corep_output
from engine.validator import validate_corep_output
from engine.mapper import map_to_template
from engine.rules_validator import check_consistency
from engine.audit import generate_audit_log


if __name__ == "__main__":
    query = "How should the bank report its own funds?"
    scenario = "Example Bank has 120 million GBP CET1, 30 million GBP AT1, and 20 million GBP Tier 2 capital."

    retrieved = simple_retrieve(query)

    print("\nRetrieved Rules:")
    for r in retrieved:
        print("-", r)

    result = generate_corep_output(query, scenario, retrieved)

    print("\nGenerated COREP Output:")
    print(result)

    is_valid, error = validate_corep_output(result)

    if not is_valid:
        print("\nSchema Validation: FAILED ❌")
        print(error)
        exit()

    print("\nSchema Validation: PASSED ✅")

    print("\nFormatted Template:\n")
    print(map_to_template(result))

    issues = check_consistency(result)

    if issues:
        print("\nConsistency Issues ⚠️")
        for issue in issues:
            print("-", issue)
    else:
        print("\nConsistency Check: PASSED ✅")

print("\nAudit Log:\n")
print(generate_audit_log(result))

