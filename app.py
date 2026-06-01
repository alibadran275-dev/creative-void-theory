import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from core_physics import DifferentiationField
from information_mass import InformationPhysics
from spacetime_weaver import SpacetimeWeaver
from consciousness_metrics import ConsciousnessMetrics

st.set_page_config(page_title="Creative Void Lab", layout="wide")

st.title("🌌 Creative Void: Digital Physics Laboratory")
st.markdown("""
This interactive lab demonstrates the **Creative Void Theory (v4.0)**. 
Explore how existence, mass, and consciousness emerge from the impossibility of absolute nothingness.
""")

# Sidebar controls
st.sidebar.header("Simulation Parameters")
size = st.sidebar.slider("Field Size", 20, 100, 50)
steps = st.sidebar.slider("Time Steps", 100, 1000, 500)
dc = st.sidebar.slider("Diffusion Coefficient (Dc)", 0.01, 0.5, 0.1)
beta = st.sidebar.slider("Structural Inhibition (Beta)", 0.1, 5.0, 1.0)
alpha_range = st.sidebar.slider("Alpha Range (Threshold)", -1.0, 1.0, (-0.5, 0.5))

if st.sidebar.button("Run Simulation"):
    field = DifferentiationField(size=size, alpha=alpha_range[0], beta=beta, Dc=dc)
    info_phys = InformationPhysics()
    cons_metrics = ConsciousnessMetrics()
    
    history = {'variance': [], 'mass': [], 'consciousness': [], 'alpha': []}
    
    progress_bar = st.progress(0)
    
    for t in range(steps):
        current_alpha = alpha_range[0] + (alpha_range[1] - alpha_range[0]) * t / steps
        field.update(alpha_override=current_alpha)
        
        _, var, _ = field.get_metrics(current_alpha)
        _, mass, _ = info_phys.calculate_mass(field.delta)
        C = cons_metrics.calculate_consciousness(field.delta)
        
        history['variance'].append(var)
        history['mass'].append(mass)
        history['consciousness'].append(C)
        history['alpha'].append(current_alpha)
        
        if t % (steps // 10) == 0:
            progress_bar.progress(t / steps)

    progress_bar.progress(1.0)

    # Display Results
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Symmetry Breaking (Variance)")
        fig1, ax1 = plt.subplots()
        ax1.plot(history['alpha'], history['variance'], color='blue')
        ax1.set_xlabel("Alpha (Critical Threshold)")
        ax1.set_ylabel("Variance (Differentiation)")
        st.pyplot(fig1)
        st.info("As Alpha crosses zero, the field transitions from symmetry to differentiation.")

    with col2:
        st.subheader("2. Informational Mass")
        fig2, ax2 = plt.subplots()
        ax2.plot(history['alpha'], history['mass'], color='red')
        ax2.set_xlabel("Alpha")
        ax2.set_ylabel("Mass (kg)")
        st.pyplot(fig2)
        st.info("Mass emerges as an energetic byproduct of information processing.")

    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("3. Consciousness Density")
        fig3, ax3 = plt.subplots()
        ax3.plot(history['alpha'], history['consciousness'], color='green')
        ax3.set_xlabel("Alpha")
        ax3.set_ylabel("C (Consciousness Density)")
        st.pyplot(fig3)
        st.info("Consciousness arises from integrated information and self-referential depth.")

    with col4:
        st.subheader("4. Final Differentiation Field")
        fig4, ax4 = plt.subplots()
        im = ax4.imshow(field.delta, cmap='RdBu')
        plt.colorbar(im)
        st.pyplot(fig4)
        st.info("The spatial map of existence: Red/Blue represent polarized differentiations.")

else:
    st.write("Adjust parameters in the sidebar and click **Run Simulation** to begin.")

st.markdown("---")
st.markdown("Developed based on the **Creative Void Theory** by Aaron.")
