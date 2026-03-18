import json
import os

file_path = r"d:\healthcare_web\app\rag\data\merged_documents.jsonl"
group_map = {}

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    doc = json.loads(line)
                    group = doc.get("metadata", {}).get("disease_group", "n/a")
                    disease = doc.get("metadata", {}).get("disease", "n/a")
                    if group not in group_map:
                        group_map[group] = set()
                    group_map[group].add(disease)
                except:
                    pass

print("--- Group to Disease Mapping ---")
for g, diseases in group_map.items():
    # Print hex for group name to be sure
    g_hex = g.encode('utf-8').hex()
    print(f"Group: {g} (hex: {g_hex})")
    print(f"Diseases: {list(diseases)}")
    print("-" * 20)
