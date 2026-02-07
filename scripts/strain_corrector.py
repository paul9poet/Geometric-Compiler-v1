import numpy as np

class StrainCorrector:
    def __init__(self, alpha_geometric=137.035999):
        self.alpha_geometric = alpha_geometric
        self.lattice_stiffness = 1.42e24 # Calibration constant (lambda)
        
    def calculate_strain(self, energy_mev):
        """
        Calculates the lattice deformation (epsilon) based on the 
        energy density of the experimental probe.
        """
        # Strain is proportional to Energy / Stiffness
        strain = energy_mev / self.lattice_stiffness
        return strain

    def correct_alpha(self, experimental_alpha, energy_mev):
        """
        Back-projects the experimental alpha to the geometric rest-state.
        If the corrected value matches alpha_geometric to 12 decimal places,
        the 'error' is confirmed as lattice strain.
        """
        epsilon = self.calculate_strain(energy_mev)
        # The 'Soft Lorentz Breaking' correction factor
        corrected_alpha = experimental_alpha * (1 - epsilon)
        
        variance = abs(corrected_alpha - self.alpha_geometric)
        return corrected_alpha, variance

if __name__ == "__main__":
    corrector = StrainCorrector()
    # Example: HIgammaS 87.6 MeV resonance data
    exp_val = 137.0359992 # Simulated lab measurement
    val, var = corrector.correct_alpha(exp_val, 87.6)
    
    print(f"Corrected Alpha: {val:.12f}")
    print(f"Residual Variance: {var:.12e}")
    
    if var < 1e-9:
        print("S201: DISTORTION CORRECTED. Rest-state geometry confirmed.")
