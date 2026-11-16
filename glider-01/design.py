# GLIDER-01 初号グライダー サイジング計算 v0.1 (2026-11-16)
# 方法: 棚1の基礎式 (PHAK Ch.4/5/11, Naval Aviators) + 実験1で検証したポーラ法
# ポーラ: CD = CD0 + k*CL^2, k = 1/(pi*e*AR)
import math
rho, g = 1.225, 9.81

# --- 要求・前提 (v0.1 提案値) ---
b   = 1.50      # 翼幅 m
c   = 0.18      # 翼弦 m (矩形翼換算)
S   = b*c       # 翼面積 m2
AR  = b*b/S
Wkg = 0.42      # 目標全備重量 kg
CD0 = 0.025     # 形状抗力係数 (模型グライダー標準域 0.02-0.03 の中値)
e   = 0.80      # Oswald効率 (模型の標準域 0.75-0.85)
CLmax = 1.10    # 低Reでの最大揚力係数 (Clark Y級)
k = 1/(math.pi*e*AR)
W = Wkg*g

def V(CL): return math.sqrt(2*W/(rho*S*CL))
def CD(CL): return CD0 + k*CL*CL

print(f"S={S:.3f} m2  AR={AR:.2f}  k={k:.4f}  翼面荷重={Wkg/S:.2f} kg/m2 ({Wkg/S*10:.1f} g/dm2)")
print(f"失速速度 Vs (CLmax={CLmax}): {V(CLmax):.2f} m/s")
CLbg = math.sqrt(CD0/k)
print(f"最良滑空: CL={CLbg:.3f}  V={V(CLbg):.2f} m/s  L/Dmax={CLbg/CD(CLbg):.1f}  沈下率={V(CLbg)/(CLbg/CD(CLbg)):.3f} m/s")
CLms = math.sqrt(3*CD0/k)
print(f"最小沈下の理論CL={CLms:.3f} (CLmax超過のため実効は失速直前)")
for CL in (1.00, 1.05):
    print(f"  CL={CL}: V={V(CL):.2f} m/s  L/D={CL/CD(CL):.1f}  沈下率={V(CL)/(CL/CD(CL)):.3f} m/s")
print("速度スイープ: V [m/s] / CL / L/D / 沈下率 [m/s]")
CL = 0.30
while CL <= 1.101:
    vv = V(CL); ld = CL/CD(CL)
    print(f"  CL={CL:.2f}  V={vv:5.2f}  L/D={ld:5.1f}  sink={vv/ld:.3f}")
    CL += 0.10

# --- 尾翼 (尾翼容積係数, PHAK/Naval Aviators の標準域で照合) ---
lh = 0.65                       # 重心〜尾翼空力中心 m (全長~0.95m想定)
Sh, Sv = 0.045, 0.025           # 水平/垂直尾翼面積 m2
VH = Sh*lh/(S*c); VV = Sv*lh/(S*b)
print(f"水平尾翼容積 VH={VH:.2f} (標準域 0.4-0.6)")
print(f"垂直尾翼容積 VV={VV:.3f} (標準域 0.02-0.05)")

# --- 重量予算 (合計=目標重量に閉じるか) ---
budget = {"主翼(3分割・桁・リブ・被覆)":150, "胴体(ポッド+テールブーム)":90, "尾翼":30,
          "受信機+サーボx2":45, "バッテリー(2S LiPo小容量)":35, "リンケージ・接着・仕上げ":40, "調整バラスト":30}
tot = sum(budget.values())
for name, m in budget.items(): print(f"  {name}: {m} g")
print(f"重量予算合計: {tot} g (目標 {int(Wkg*1000)} g -> {'一致' if tot==int(Wkg*1000) else '不一致'})")
