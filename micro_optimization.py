# I-AIAEM Micro Optimization Example
import numpy as np
from scipy.optimize import minimize

# تابع تولید فرضی
def production(W, F, L):
    return 4.1 * (W**0.5) * (F**0.3) * (L**0.2)  # مدل Cobb-Douglas

# تابع سود
def profit(x, P=50000, C_W=6000, C_F=12000, C_L=15000):
    W, F, L = x
    return -(P * production(W, F, L) - (C_W * W + C_F * F + C_L * L))  # منفی برای حداکثر‌سازی

# قیود
constraints = ({'type': 'ineq', 'fun': lambda x: 100 - (x[0] + x[1] + x[2])})  # مجموع منابع ≤ 100
bounds = [(0, None), (0, None), (0, None)]  # مقادیر غیرمنفی

# بهینه‌سازی
initial_guess = [50, 30, 20]
result = minimize(profit, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)

# نتایج
W_opt, F_opt, L_opt = result.x
Y_opt = production(W_opt, F_opt, L_opt)
print(f"تخصیص بهینه: آب={W_opt:.2f}, کود={F_opt:.2f}, نیروی کار={L_opt:.2f}")
print(f"تولید بهینه: {Y_opt:.2f} تن/هکتار")
print(f"سود: {-result.fun:.2f} تومان")