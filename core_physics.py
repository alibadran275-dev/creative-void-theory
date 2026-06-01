import numpy as np
from scipy.ndimage import laplace

class DifferentiationField:
    """
    Represents the Differentiation Field based on Chapter 3 of the 'Creative Void' theory.
    Solves the field differential equation: ∂Δ/∂t = Dc∇²Δ + αΔ - βΔ³ + η
    """
    def __init__(self, size=50, Dc=0.1, alpha=-0.1, beta=1.0, dt=0.01, noise_level=0.01):
        self.size = size
        self.Dc = Dc
        self.alpha = alpha
        self.beta = beta
        self.dt = dt
        self.noise_level = noise_level
        
        # Initialize field with small random values (Initial perturbation η)
        self.delta = np.random.normal(0, noise_level, (size, size))
        
    def update(self, alpha_override=None):
        """Update the field for one time step."""
        alpha = alpha_override if alpha_override is not None else self.alpha
        
        # Calculate spatial coupling (Laplacian)
        lap = laplace(self.delta, mode='wrap')
        
        # Calculate change (dΔ/dt)
        # dΔ = Dc*∇²Δ + αΔ - βΔ³
        d_delta = self.Dc * lap + alpha * self.delta - self.beta * (self.delta**3)
        
        # Update field values
        self.delta += self.dt * d_delta
        
        return self.delta

    def get_metrics(self, current_alpha=None):
        """Calculate statistical metrics for the field."""
        alpha = current_alpha if current_alpha is not None else self.alpha
        mean_abs = np.mean(np.abs(self.delta))
        variance = np.var(self.delta)
        # Instability index: average |αΔ - βΔ³|
        instability = np.mean(np.abs(alpha * self.delta - self.beta * (self.delta**3)))
        return mean_abs, variance, instability
