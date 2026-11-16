# GLIDER-01 — AI設計グライダー製作記録

要求定義から飛行実測まで、設計プロセス全体を通して記録するプロジェクト。
設計：シシア（Muse）／製作：吉田

- 初号機：RC 2chグライダー。v0.2で「100g未満」に再設計し、航空法の無人航空機規制（100g以上対象）を設計の側で回避する方針に決定（2026-11-16）
- 設計の根拠：FAA基礎教本（PHAK／Weight & Balance／Aerodynamics for Naval Aviators 等、設計メソッド棚）＋ Me 323性能計算の再現実験で検証したポーラ法
- 記録の方針：計算・前提・失敗・差分を消さずに残す（信用は台帳）

## 中身
- `docs/GLIDER-01-design-v0.1.md` — 420g／1.5m案（比較基準として保存）
- `docs/GLIDER-01-design-v0.2.md` — 100g未満／1.0m案（現行）
- `design.py` / `design-output.txt` — v0.1 サイジング計算と出力
- `design2.py` / `design2-output.txt` — v0.2 再設計計算と出力
- `PROCESS.md` — 工程ごとの製作記録
