"""
歩留まりとチップ単価をPythonで計算する｜1枚のウェハから何個取れるか

元記事: https://semiconductor.yurufuwa.work/learn/yield-cost-python
ゆるふわ半導体 (semiconductor.yurufuwa.work) の解説記事から抜粋したコードです。
"""

import numpy as np

def dies_per_wafer(die_area_mm2, wafer_diameter_mm=300):
    r = wafer_diameter_mm / 2
    wafer_area = np.pi * r**2
    # 縁で欠ける分を補正する定番の近似式
    dies = wafer_area / die_area_mm2 - np.pi * wafer_diameter_mm / np.sqrt(2 * die_area_mm2)
    return int(dies)

for area in [50, 100, 400, 800]:
    print(f"ダイ面積 {area:>3}mm²: {dies_per_wafer(area):>4} 個")

def murphy_yield(die_area_mm2, defect_density_per_cm2=0.1):
    A = die_area_mm2 / 100          # mm²→cm²
    AD = A * defect_density_per_cm2
    return ((1 - np.exp(-AD)) / AD) ** 2

for area in [50, 100, 400, 800]:
    y = murphy_yield(area)
    print(f"ダイ面積 {area:>3}mm²: 歩留まり {y*100:5.1f}%")

def chip_cost(die_area_mm2, wafer_cost_usd=15000, defect_density=0.1):
    good = dies_per_wafer(die_area_mm2) * murphy_yield(die_area_mm2, defect_density)
    return wafer_cost_usd / good

for area in [50, 100, 400, 800]:
    print(f"ダイ面積 {area:>3}mm²: ${chip_cost(area):6.2f} / 個")
