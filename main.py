import numpy as np
import matplotlib.pyplot as plt
from core_physics import DifferentiationField
from information_mass import InformationPhysics
from spacetime_weaver import SpacetimeWeaver
from consciousness_metrics import ConsciousnessMetrics

def run_simulation(steps=500, size=50):
    # إعداد المحاكاة
    field = DifferentiationField(size=size, alpha=-0.5, beta=1.0, Dc=0.1)
    info_phys = InformationPhysics()
    weaver = SpacetimeWeaver()
    cons_metrics = ConsciousnessMetrics()
    
    # لتخزين البيانات التاريخية
    history = {
        'mean_abs': [],
        'variance': [],
        'instability': [],
        'mass': [],
        'consciousness': [],
        'alpha': []
    }
    
    print("بدء محاكاة الفراغ المبدع...")
    
    for t in range(steps):
        # زيادة تدريجية في alpha لمحاكاة عبور العتبة الحرجة
        # تبدأ من -0.5 وتصل إلى 0.5
        current_alpha = -0.5 + (1.0 * t / steps)
        
        # تحديث الحقل
        field.update(alpha_override=current_alpha)
        
        # حساب المقاييس
        m_abs, var, inst = field.get_metrics(current_alpha)
        _, mass, _ = info_phys.calculate_mass(field.delta)
        C = cons_metrics.calculate_consciousness(field.delta)
        
        # حفظ التاريخ
        history['mean_abs'].append(m_abs)
        history['variance'].append(var)
        history['instability'].append(inst)
        history['mass'].append(mass)
        history['consciousness'].append(C)
        history['alpha'].append(current_alpha)
        
        if t % 100 == 0:
            print(f"الخطوة {t}: Alpha = {current_alpha:.2f}, التباين = {var:.4f}, الوعي = {C:.6e}")

    # رسم النتائج
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    
    # 1. التباين ونشوء التمايز
    axs[0, 0].plot(history['alpha'], history['variance'], color='blue')
    axs[0, 0].set_title('نشوء التمايز (التباين الإحصائي)')
    axs[0, 0].set_xlabel('Alpha (العتبة الحرجة)')
    axs[0, 0].set_ylabel('التباين')
    axs[0, 0].grid(True)
    
    # 2. الكتلة المعلوماتية
    axs[0, 1].plot(history['alpha'], history['mass'], color='red')
    axs[0, 1].set_title('الكتلة المعلوماتية المكافئة')
    axs[0, 1].set_xlabel('Alpha')
    axs[0, 1].set_ylabel('الكتلة (كجم)')
    axs[0, 1].grid(True)
    
    # 3. كثافة الوعي
    axs[1, 0].plot(history['alpha'], history['consciousness'], color='green')
    axs[1, 0].set_title('تطور كثافة الوعي')
    axs[1, 0].set_xlabel('Alpha')
    axs[1, 0].set_ylabel('C (كثافة الوعي)')
    axs[1, 0].grid(True)
    
    # 4. خريطة حرارية نهائية للحقل
    im = axs[1, 1].imshow(field.delta, cmap='RdBu')
    axs[1, 1].set_title('خريطة حقل التمايز النهائية')
    fig.colorbar(im, ax=axs[1, 1])
    
    plt.tight_layout()
    plt.savefig('simulation_results.png')
    print("\nتم حفظ نتائج المحاكاة في 'simulation_results.png'")
    
    # إثبات آلية BIA (المسافة والمعلومات)
    region_a = field.delta[0:10, 0:10]
    region_b = field.delta[size-10:size, size-10:size]
    mi = weaver.calculate_mutual_information(region_a, region_b)
    dist = weaver.get_info_distance(mi)
    print(f"\n--- تحليل الزمكان (BIA) ---")
    print(f"المعلومات المتبادلة بين منطقتين بعيدتين: {mi:.4f}")
    print(f"المسافة المعلوماتية المحسوبة: {dist:.4f}")

if __name__ == "__main__":
    run_simulation()
