LLM-Assisted PRA COREP Reporting Assistant (Prototype)

This project demonstrates a prototype of an LLM-assisted regulatory reporting assistant for UK bank prudential reporting under the PRA Rulebook. The system focuses on a simplified version of COREP C 01.00 (Own Funds) and showcases how Large Language Models can support structured regulatory reporting in a controlled, auditable manner.

🎯 Objective

Preparing COREP returns requires analysts to interpret complex regulatory rules and map them accurately to structured reporting templates. This prototype demonstrates an end-to-end workflow where an LLM is used as a reasoning component, while the surrounding system enforces structure, validation, and traceability.

🧠 System Overview

Pipeline:

User Question + Scenario
→ Regulatory Text Retrieval
→ Structured LLM Output
→ JSON Schema Validation
→ Template Mapping
→ Consistency Checks
→ Audit Log Generation

🧩 Key Features
1. Regulatory Retrieval (RAG)

The system retrieves relevant PRA Rulebook excerpts and COREP instructions from a local knowledge base and provides them to the LLM as context.

2. Structured LLM Output

The LLM is instructed to produce output aligned with a predefined JSON schema representing COREP C 01.00 fields.

3. Schema Validation

All LLM outputs are validated using a JSON schema to ensure:

Required fields are present

Data types are correct

Only valid COREP row codes are used

4. Template Mapping

Validated structured output is converted into a human-readable extract of the COREP C 01.00 template.

5. Consistency Checks

Basic business rules are applied, such as verifying that Total Own Funds = CET1 + AT1 + Tier 2.

6. Audit Log (Traceability)

For each populated field, the system records the regulatory rule references used by the LLM. This provides transparency and supports explainability — a critical requirement in regulated environments.

🚀 How to Run

Create virtual environment

Install dependencies:

pip install google-genai python-dotenv jsonschema


Add your Gemini API key to .env:

GEMINI_API_KEY=your_key_here


Run:

python main.py


🏁 Prototype Scope

This prototype focuses on:

A simplified subset of COREP (C 01.00 – Own Funds)

Demonstrating system design, structure, and explainability

Not a production or fully compliant regulatory reporting system

💡 Design Philosophy

The LLM is treated as an assistive reasoning component, not a trusted authority. All outputs are:

Structured

Validated

Traceable

Checked for logical consistency

This reflects how AI systems must be designed in highly regulated financial environments.

Project Structure
corep_llm_assistant/
│
├── data/                     # Mock PRA & COREP texts
├── schemas/                  # JSON schema for COREP output
├── engine/
│   ├── retriever.py          # Regulatory text retrieval
│   ├── generator.py          # LLM structured generation
│   ├── validator.py          # JSON schema validation
│   ├── mapper.py             # COREP template formatter
│   ├── rules_validator.py    # Logical consistency checks
│   └── audit.py              # Audit log generation
│
├── main.py                   # End-to-end demo
└── README.md