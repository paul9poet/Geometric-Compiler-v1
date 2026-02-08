# scripts/prediction_engine.py
# Propagates Lattice Strain into Experimental Energy Targets

def get_prediction(epsilon=0.0340, epsilon_unc=0.0020):
    E_base = 1200.0  # eV Baseline
    E_split = E_base * (1 + epsilon)
    E_unc = E_base * epsilon_unc
    
    print(f"--- MSLA PREDICTION ---")
    print(f"Lattice Strain: {epsilon} +/- {epsilon_unc}")
    print(f"Predicted Triplet Split: {E_split:.2f} +/- {E_unc:.2f} eV")
    print(f"Wavenumber equivalent: {E_split * 8065.544:.0f} cm^-1")
    print(f"95% Confidence Window: {E_split - 2*E_unc:.1f} to {E_split + 2*E_unc:.1f} eV")

if __name__ == "__main__":
    get_prediction()
