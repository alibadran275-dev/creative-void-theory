import numpy as np

class InformationPhysics:
    """
    تطبيق الفصل الرابع: العلاقة بين المعلومات، الطاقة، والكتلة.
    m_I = (k_B * T * ln(2) / c^2) * L
    """
    def __init__(self, temperature=2.73): # درجة حرارة الخلفية الكونية كافتراض
        self.kB = 1.380649e-23  # ثابت بولتزمان
        self.c = 299792458      # سرعة الضوء
        self.T = temperature
        self.ln2 = np.log(2)
        
    def calculate_mass(self, field_delta):
        """
        حساب الكتلة المعلوماتية الناتجة عن التمايزات في الحقل.
        نعتبر كل تمايز (قيمة مطلقة لـ Delta) كأنه يمثل 'بتات' معالجة.
        """
        # عدد التمايزات (L) نفترضه يتناسب مع مجموع القيم المطلقة للتمايز في الحقل
        L = np.sum(np.abs(field_delta))
        
        # حساب الطاقة (E = L * kB * T * ln2)
        energy = L * self.kB * self.T * self.ln2
        
        # حساب الكتلة (m = E / c^2)
        mass = energy / (self.c**2)
        
        return energy, mass, L
