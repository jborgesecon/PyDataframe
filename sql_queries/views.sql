-- viagens
    CREATE OR REPLACE VIEW main_views.total_viagens AS
    SELECT * FROM ptransp_vg.viagens_2018
    UNION ALL
    SELECT * FROM ptransp_vg.viagens_2019
    UNION ALL
    SELECT * FROM ptransp_vg.viagens_2020
    UNION ALL
    SELECT * FROM ptransp_vg.viagens_2021
    UNION ALL
    SELECT * FROM ptransp_vg.viagens_2022
    UNION ALL
    SELECT * FROM ptransp_vg.viagens_2023;

-- trechos
    CREATE OR REPLACE VIEW main_views.total_trechos AS
    SELECT * FROM ptransp_vg.trechos_2018
    UNION ALL
    SELECT * FROM ptransp_vg.trechos_2019
    UNION ALL
    SELECT * FROM ptransp_vg.trechos_2020
    UNION ALL
    SELECT * FROM ptransp_vg.trechos_2021
    UNION ALL
    SELECT * FROM ptransp_vg.trechos_2022
    UNION ALL
    SELECT * FROM ptransp_vg.trechos_2023;

-- passagens
    CREATE OR REPLACE VIEW main_views.total_passagens AS
    SELECT * FROM ptransp_vg.passagens_2018
    UNION ALL
    SELECT * FROM ptransp_vg.passagens_2019
    UNION ALL
    SELECT * FROM ptransp_vg.passagens_2020
    UNION ALL
    SELECT * FROM ptransp_vg.passagens_2021
    UNION ALL
    SELECT * FROM ptransp_vg.passagens_2022
    UNION ALL
    SELECT * FROM ptransp_vg.passagens_2023;

-- pagamentos
    CREATE OR REPLACE VIEW main_views.total_pagamentos AS
    SELECT * FROM ptransp_vg.pagamentos_2018
    UNION ALL
    SELECT * FROM ptransp_vg.pagamentos_2019
    UNION ALL
    SELECT * FROM ptransp_vg.pagamentos_2020
    UNION ALL
    SELECT * FROM ptransp_vg.pagamentos_2021
    UNION ALL
    SELECT * FROM ptransp_vg.pagamentos_2022
    UNION ALL
    SELECT * FROM ptransp_vg.pagamentos_2023;

-- orcamento
    CREATE OR REPLACE VIEW main_views.total_orcamento AS
    SELECT * FROM ptransp_orc.orcamento_2018
    UNION ALL
    SELECT * FROM ptransp_orc.orcamento_2019
    UNION ALL
    SELECT * FROM ptransp_orc.orcamento_2020
    UNION ALL
    SELECT * FROM ptransp_orc.orcamento_2021
    UNION ALL
    SELECT * FROM ptransp_orc.orcamento_2022
    UNION ALL
    SELECT * FROM ptransp_orc.orcamento_2023;

-- receitas
    CREATE OR REPLACE VIEW main_views.total_receitas AS
    SELECT * FROM ptransp_orc.receitas_2018
    UNION ALL
    SELECT * FROM ptransp_orc.receitas_2019
    UNION ALL
    SELECT * FROM ptransp_orc.receitas_2020
    UNION ALL
    SELECT * FROM ptransp_orc.receitas_2021
    UNION ALL
    SELECT * FROM ptransp_orc.receitas_2022
    UNION ALL
    SELECT * FROM ptransp_orc.receitas_2023;


SELECT count(*) FROM main_views.total_viagens;