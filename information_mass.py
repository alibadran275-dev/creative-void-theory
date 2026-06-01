import numpy as np

class InformationPhysics:
    """
    Implementation of Chapter 4: Relationship between Information, Energy, and Mass.
    m_I = (k_B * T * ln(2) / c^2) * L
    """
    def __init__(self, temperature=2.73): # Cosmic microwave background temperature as default
        self.kB = 1.380649e-23  # Boltzmann constant
        self.c = 299792458      # Speed of light
        self.T = temperature
        self.ln2 = np.log(2)
        
    def calculate_mass(self, field_delta):
        """
        Calculate the informational mass resulting from differentiations in the field.
        We consider each differentiation (absolute value of Delta) as representing processed 'bits'.
        """
        # L: Number of differentiations (assumed proportional to the sum of absolute values in the field)
        L = np.sum(np.abs(field_delta))
        
        # Calculate Energy (E = L * kB * T * ln2)
        energy = L * self.kB * self.T * self.ln2
        
        # Calculate Mass (m = E / c^2)
        mass = energy / (self.c**2)
        
        return energy, mass, L
