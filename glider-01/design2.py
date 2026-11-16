# GLIDER-01 v0.2 : 100g未満への再設計 (2026-11-16, 吉田の決定: 規制を設計で回避)
# 航空法の無人航空機は100g以上。95g目標 (5gの安全マージン) で模型航空機の範囲に入る
import math
rho, g, nu = 1.225, 9.81, 1.46e-5

b, c = 1.00, 0.15
S = b*c; AR = b*b/S
Wkg = 0.095
CD0, e, CLmax = 0.028, 0.75, 0.95   # 低Re (Re~4万) を織り込んだ保守値
k = 1/(math.pi*e*AR); W = Wkg*g
def V(CL): return math.sqrt(2*W/(rho*S*CL))
def CD(CL): return CD0 + k*CL*CL
print(f"S={S:.3f} m2  AR={AR:.2f}  k={k:.4f}  翼面荷重={Wkg/S:.3f} kg/m2 ({Wkg/S*10:.1f} g/dm2)")
print(f"失速速度 Vs (CLmax={CLmax}): {V(CLmax):.2f} m/s   その時のRe={V(CLmax)*c/nu:,.0f}")
CLbg = math.sqrt(CD0/k); ld = CLbg/CD(CLbg)
print(f"最良滑空: CL={CLbg:.3f}  V={V(CLbg):.2f} m/s  L/Dmax={ld:.1f}  沈下率={V(CLbg)/ld:.3f} m/s  Re={V(CLbg)*c/nu:,.0f}")
for CL in (0.90, 0.95):
    l2 = CL/CD(CL); print(f"  CL={CL}: V={V(CL):.2f} m/s  L/D={l2:.1f}  沈下率={V(CL)/l2:.3f} m/s")
lh = 0.45; Sh, Sv = 0.028, 0.014
print(f"水平尾翼容積 VH={Sh*lh/(S*c):.2f} (標準域 0.4-0.6)")
print(f"垂直尾翼容積 VV={Sv*lh/(S*b):.3f} (標準域 0.02-0.05)")
budget = {"主翼(カーボン桁+バルサリブ+フィルム)":32, "胴体(バルサ/カーボンブーム)":15, "尾翼(バルサ+フィルム)":6,
          "受信機+サーボ一体基板":8, "1S LiPo 300mAh":8, "リンケージ":4, "接着・仕上げ":5,
          "計測ロガー(バロ)":8, "調整バラスト":5}
tot = sum(budget.values())
for n, m in budget.items(): print(f"  {n}: {m} g")
print(f"重量予算合計: {tot} g (上限100g -> マージン {100-tot} g)")
