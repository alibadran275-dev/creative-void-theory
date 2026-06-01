import numpy as np

class ConsciousnessMetrics:
    """
    تطبيق الفصل السادس: معادلة كثافة الوعي.
    C = (nu * log2(1 + R) * I_int) / (V_info * (1 + H_noise))
    """
    def __init__(self):
        pass
        
    def calculate_consciousness(self, field_delta, nu=1.0, R=2.0, noise_level=0.01):
        """
        حساب كثافة الوعي للنظام.
        """
        # I_int: المعلومات المتكاملة (نستخدم التباين كمؤشر على التعقيد/التكامل)
        I_int = np.var(field_delta)
        
        # V_info: الحجم المعلوماتي (عدد الخلايا)
        V_info = field_delta.size
        
        # H_noise: الضوضاء
        H_noise = noise_level
        
        # تطبيق المعادلة
        C = (nu * np.log2(1 + R) * I_int) / (V_info * (1 + H_noise))
        
        return C
