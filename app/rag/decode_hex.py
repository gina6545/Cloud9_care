import json
import os

results = {
    "eab8b0ed8380": bytes.fromhex("eab8b0ed8380").decode("utf-8"),
    "ec868ced9994eab8b020eca788ed9998": bytes.fromhex("ec868ced9994eab8b020eca788ed9998").decode("utf-8"),
    "ed98b8ed9da1eab8b020eca788ed9998": bytes.fromhex("ed98b8ed9da1eab8b020eca788ed9998").decode("utf-8"),
    "ec8898eba9b420eca788ed9998": bytes.fromhex("ec8898eba9b420eca788ed9998").decode("utf-8"),
    "eca095ec8ba0eab1b4eab09520ebb08f20ec8898eba9b420eca788ed9998": bytes.fromhex("eca095ec8ba0eab1b4eab09520ebb08f20ec8898eba9b420eca788ed9998").decode("utf-8"),
    "eab7bceab3a8eab2a9eab38420eca788ed9998": bytes.fromhex("eab7bceab3a8eab2a9eab38420eca788ed9998").decode("utf-8"),
    "ec8ba0eab2bdeab38420eca788ed9998": bytes.fromhex("ec8ba0eab2bdeab38420eca788ed9998").decode("utf-8"),
    "eab3b5ed86b520ec839ded999cec8ab5eab480": bytes.fromhex("eab3b5ed86b520ec839ded999cec8ab5eab480").decode("utf-8"),
}

with open(r"d:\healthcare_web\app\rag\decoded_groups.txt", "w", encoding="utf-8") as f:
    for h, s in results.items():
        f.write(f"{h} -> {s}\n")
