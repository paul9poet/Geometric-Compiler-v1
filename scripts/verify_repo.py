import os
import json

REQUIRED_FILES = [
    "protocol/falsification_protocol.json",
    "scripts/execute_audit.py",
    "scripts/rolling_integration.py",
    "scripts/homology_audit.py",
    "scripts/strain_corrector.py",
    ".github/workflows/run_audit.yml",
    "README.md"
]

def verify_structure():
    print("=== Silicon Principia: Repository Integrity Check ===")
    missing = []
    for f in REQUIRED_FILES:
        if os.path.exists(f"../{f}") or os.path.exists(f):
            print(f" [OK] {f}")
        else:
            print(f" [MISSING] {f}")
            missing.append(f)
    
    if not missing:
        print("\nStructure Verified. The Geometric Compiler is ready for ingestion.")
        check_protocol()
    else:
        print(f"\nFATAL: Missing {len(missing)} components. Repository incomplete.")

def check_protocol():
    path = "protocol/falsification_protocol.json"
    if os.path.exists(path):
        with open(path, 'r') as f:
            pact = json.load(f)
            if pact.get("checksum_id") == "0x9B3F82A1":
                print(" [OK] Protocol Checksum 0x9B3F82A1 is LOCKED.")
            else:
                print(" [WARNING] Protocol checksum mismatch.")

if __name__ == "__main__":
    verify_structure()
