"""
Lista dentro de listas
"""
# ----------- 0 -------- 1 -----
sala = [ ["Hellena", "Marta"], # 0
# ---------- 0 -------- 1 ---- 
        ["Otávio", "Marcos"], # 1
# ---------- 0 -------- 1 -------------- 2 ------------ 
        ["Felipe", "Carlos", (0, 10, 20, 30, 40, 50)] # 2
                            ]


linha_3 = sala[2][2]
buscar_20 = sala[2][2][2]

print(linha_3[2])
print(buscar_20)