# (EI02/03CG03) Explorar formas de deslocamento no espaço (pular, saltar, dançar),
# combinando movimentos e seguindo orientações.

# ==========================================
# Regras
# ==========================================

atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG03') <= \
    (promove_a_meta(Atividade, 'expressao_corporal') & \
    promove_a_meta(Atividade, 'obedecer_regras')) | \
    (usa_parte_do_corpo(Atividade, 'pes') & \
     usa_parte_do_corpo(Atividade, 'pernas')) | \
     promove_tipo_esforco(Atividade, 'fisico')