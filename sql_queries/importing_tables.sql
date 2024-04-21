-- viagem    
    -- Identificador do processo de viagem : 0000000000017821923
    -- Número da Proposta (PCDP)           : 000001/23-1C
    -- Situação                            : Realizada
    -- Viagem Urgente                      : NÃO
    -- Justificativa Urgência Viagem       : Sem informação
    -- Código do órgão superior            : 26000
    -- Nome do órgão superior              : Ministério da Educação
    -- Código órgão solicitante            : 26352
    -- Nome órgão solicitante              : Fundação Universidade Federal do ABC
    -- CPF viajante                        : ***.875.238-**
    -- Nome                                : PRISCILA LEAL DA SILVA
    -- Cargo                               : PROFESSOR DO MAGISTERIO SUPERIOR
    -- Função                              : -1
    -- Descrição Função                    : Sem informação
    -- Período - Data de início            : 01/01/2023
    -- Período - Data de fim               : 02/12/2023
    -- Destinos                            : Loughborough/Reino Unido
    -- Motivo                              : Intercâmbio acadêmico PCDP anterior 07/21-3C
    -- Valor diárias                       : 0,00
    -- Valor passagens                     : 0,00
    -- Valor devolução                     : 0,00
    -- Valor outros gastos                 : 0,00

create table ptransp_vg.viagens_2018 (
    pss_id serial primary key,
    identificador text,
    num_propost text,
    situacao text,
    viagem_urgente text,
    justificativa_urgencia text,
    cod_org_sup text,
    nome_org_sup text,
    cod_org_solicitante text,
    nome_org_solicitante text,
    cpf_viajante text,
    nome text,
    cargo text,
    funcao text,
    descricao_funcao text,
    periodo_data_inicio text,
    periodo_data_fim text,
    destinos text,
    motivo text,
    valor_diarias text,
    valor_passagens text,
    valor_devolucao text,
    valor_outros_gastos text
);

copy ptransp_vg.viagens_2018 (
    identificador,
    num_propost,
    situacao,
    viagem_urgente,
    justificativa_urgencia,
    cod_org_sup,
    nome_org_sup,
    cod_org_solicitante,
    nome_org_solicitante,
    cpf_viajante,
    nome,
    cargo,
    funcao,
    descricao_funcao,
    periodo_data_inicio,
    periodo_data_fim,
    destinos,
    motivo,
    valor_diarias,
    valor_passagens,
    valor_devolucao,
    valor_outros_gastos
) from 'C:\Users\viagens\files\2018_20240419_Viagens\2018_Viagem.csv' 
with (format csv, header true, delimiter ';', encoding 'latin1');


-- Trecho
    -- Identificador do processo de viagem  : 0000000000013501576
    -- Número da Proposta (PCDP)            : Sem informaçã
    -- Sequência Trecho                     : 1
    -- Origem - Data                        : 10/02/2018
    -- Origem - País                        : Brasil
    -- Origem - UF                          : Rio de Janeiro
    -- Origem - Cidade                      : Rio de Janeiro
    -- Destino - Data                       : 02/03/2018
    -- Destino - País                       : Portugal
    -- Destino - UF                         :
    -- Destino - Cidade                     : Coimbra
    -- Meio de transporte                   : Aéreo
    -- Número Diárias                       : 0,00
    -- Missao?                              : Sim

create table ptransp_vg.trechos_2018 (
    pss_id serial primary key,
    identificador text,
    num_propost text,
    sequencia_trecho text,
    origem_data text,
    origem_pais text,
    origem_uf text,
    origem_cidade text,
    destino_data text,
    destino_pais text,
    destino_uf text,
    destino_cidade text,
    meio_transporte text,
    num_diarias text,
    missao text
);

copy ptransp_vg.trechos_2018 (
    identificador,
    num_propost,
    sequencia_trecho,
    origem_data,
    origem_pais,
    origem_uf,
    origem_cidade,
    destino_data,
    destino_pais,
    destino_uf,
    destino_cidade,
    meio_transporte,
    num_diarias,
    missao
) from 'C:\Users\viagens\files\2018_20240419_Viagens\2018_Trecho.csv'
with (format csv, header true, delimiter ';', encoding 'latin1');


-- Passagem
    -- Identificador do processo de viagem : 0000000000014046485
    -- Número da Proposta (PCDP)           : Sem informaçã
    -- Meio de transporte                  : Rodoviário
    -- País - Origem ida                   : Brasil
    -- UF - Origem ida                     : Ceará
    -- Cidade - Origem ida                 : Fortaleza
    -- País - Destino ida                  : Brasil
    -- UF - Destino ida                    : Ceará
    -- Cidade - Destino ida                : Sobral
    -- País - Origem volta                 : Sem informação
    -- UF - Origem volta                   : Sem informação
    -- Cidade - Origem volta               : Sem informação
    -- Pais - Destino volta                : Sem informação
    -- UF - Destino volta                  : Sem informação
    -- Cidade - Destino volta              : Sem informação
    -- Valor da passagem                   : 40,95
    -- Taxa de serviço                     : 13,51
    -- Data da emissão/compra              :
    -- Hora da emissão/compra              : 00:00

create table ptransp_vg.passagens_2018 (
    pss_id serial primary key,
    identificador text,
    num_propost text,
    meio_transporte text,
    pais_origem_ida text,
    uf_origem_ida text,
    cidade_origem_ida text,
    pais_destino_ida text,
    uf_destino_ida text,
    cidade_destino_ida text,
    pais_origem_volta text,
    uf_origem_volta text,
    cidade_origem_volta text,
    pais_destino_volta text,
    uf_destino_volta text,
    cidade_destino_volta text,
    valor_passagem text,
    taxa_servico text,
    data_emissao_compra text,
    hora_emissao_compra text
);

copy ptransp_vg.passagens_2018 (
    identificador,
    num_propost,
    meio_transporte,
    pais_origem_ida,
    uf_origem_ida,
    cidade_origem_ida,
    pais_destino_ida,
    uf_destino_ida,
    cidade_destino_ida,
    pais_origem_volta,
    uf_origem_volta,
    cidade_origem_volta,
    pais_destino_volta,
    uf_destino_volta,
    cidade_destino_volta,
    valor_passagem,
    taxa_servico,
    data_emissao_compra,
    hora_emissao_compra
) from 'C:\Users\viagens\files\2018_20240419_Viagens\2018_Passagem.csv'
with (format csv, header true, delimiter ';', encoding 'latin1');


-- Pagamento
    -- Identificador do processo de viagem : 0000000000014046485
    -- Número da Proposta (PCDP)           : Sem informaçã
    -- Código do órgão superior            : 26000
    -- Nome do órgão superior              : Ministério da Educação
    -- Codigo do órgão pagador             : 26405
    -- Nome do órgao pagador               : Instituto Federal do Ceará
    -- Código da unidade gestora pagadora  : 158133
    -- Nome da unidade gestora pagadora    : INST.FED.DE EDUC.,CIENC.E TEC.DO CEARA
    -- Tipo de pagamento                   : DIÁRIAS
    -- Valor                               : 537,50

create table ptransp_vg.pagamentos_2023 (
    pss_id serial primary key,
    identificador text,
    num_propost text,
    cod_org_sup text,
    nome_org_sup text,
    cod_org_pagador text,
    nome_org_pagador text,
    cod_unidade_gestora_pagadora text,
    nome_unidade_gestora_pagadora text,
    tipo_pagamento text,
    valor text
);

copy ptransp_vg.pagamentos_2023 (
    identificador,
    num_propost,
    cod_org_sup,
    nome_org_sup,
    cod_org_pagador,
    nome_org_pagador,
    cod_unidade_gestora_pagadora,
    nome_unidade_gestora_pagadora,
    tipo_pagamento,
    valor
) from 'C:\Users\viagens\files\2023_20240419_Viagens\2023_Pagamento.csv'
with (format csv, header true, delimiter ';', encoding 'latin1');



------------------------------------------------------------------------------------------------------------
-- OrcaemntoDespesa
    -- EXERCÍCIO                    : 2018
    -- CÓDIGO ÓRGÃO SUPERIOR        : 03000
    -- NOME ÓRGÃO SUPERIOR          : Tribunal de Contas da União
    -- CÓDIGO ÓRGÃO SUBORDINADO     : 03000
    -- NOME ÓRGÃO SUBORDINADO       : Tribunal de Contas da União - Unidades com vínculo direto
    -- CÓDIGO UNIDADE ORÇAMENTÁRIA  : 03101
    -- NOME UNIDADE ORÇAMENTÁRIA    : TRIBUNAL DE CONTAS DA UNIAO
    -- CÓDIGO FUNÇÃO                : 01
    -- NOME FUNÇÃO                  : Legislativa
    -- CÓDIGO SUBFUNÇÃO             : 032
    -- NOME SUBFUNÇÃO               : Controle externo
    -- CÓDIGO PROGRAMA ORÇAMENTÁRIO : 0550
    -- NOME PROGRAMA ORÇAMENTÁRIO   : CONTROLE EXTERNO
    -- CÓDIGO AÇÃO                  : 4018
    -- NOME AÇÃO                    : FISCALIZACAO DA APLICACAO DOS RECURSOS PUBLICOS FEDERAIS
    -- CÓDIGO CATEGORIA ECONÔMICA   : 3
    -- NOME CATEGORIA ECONÔMICA     : DESPESAS CORRENTES
    -- CÓDIGO GRUPO DE DESPESA      : 3
    -- NOME GRUPO DE DESPESA        : Outras Despesas Correntes
    -- CÓDIGO ELEMENTO DE DESPESA   : 39
    -- NOME ELEMENTO DE DESPESA     : Outros Serviços de Terceiros - Pessoa Jurídica
    -- ORÇAMENTO INICIAL (R$)       : 0,00
    -- ORÇAMENTO ATUALIZADO (R$)    : 0,00
    -- ORÇAMENTO EMPENHADO (R$)     : 856984,65
    -- ORÇAMENTO REALIZADO (R$)     : 775620,02

create table ptransp_orc.orcamento_2023 (
    pss_id serial primary key,
    exercicio text,
    cod_org_sup text,
    nome_org_sup text,
    cod_org_sub text,
    nome_org_sub text,
    cod_unidade_orcamentaria text,
    nome_unidade_orcamentaria text,
    cod_funcao text,
    nome_funcao text,
    cod_subfuncao text,
    nome_subfuncao text,
    cod_prog_orcamentario text,
    nome_prog_orcamentario text,
    cod_acao text,
    nome_acao text,
    cod_categoria_economica text,
    nome_categoria_economica text,
    cod_grupo_despesa text,
    nome_grupo_despesa text,
    cod_elemento_despesa text,
    nome_elemento_despesa text,
    orcamento_inicial text,
    orcamento_atualizado text,
    orcamento_empenhado text,
    orcamento_realizado text
);

copy ptransp_orc.orcamento_2023 (
    exercicio,
    cod_org_sup,
    nome_org_sup,
    cod_org_sub,
    nome_org_sub,
    cod_unidade_orcamentaria,
    nome_unidade_orcamentaria,
    cod_funcao,
    nome_funcao,
    cod_subfuncao,
    nome_subfuncao,
    cod_prog_orcamentario,
    nome_prog_orcamentario,
    cod_acao,
    nome_acao,
    cod_categoria_economica,
    nome_categoria_economica,
    cod_grupo_despesa,
    nome_grupo_despesa,
    cod_elemento_despesa,
    nome_elemento_despesa,
    orcamento_inicial,
    orcamento_atualizado,
    orcamento_empenhado,
    orcamento_realizado
) from 'C:\Users\orcamento_despesa\files\2023_OrcamentoDespesa.csv'
with (format csv, header true, delimiter ';', encoding 'latin1');

-- Receitas
    -- CÓDIGO ÓRGÃO SUPERIOR     : 63000
    -- NOME ÓRGÃO SUPERIOR       : Advocacia-Geral da União
    -- CÓDIGO ÓRGÃO              : 63000
    -- NOME ÓRGÃO                : Advocacia-Geral da União - Unidades com vínculo direto
    -- CÓDIGO UNIDADE GESTORA    : 110060
    -- NOME UNIDADE GESTORA      : COORD. GERAL DE ORC. FIN. E ANAL. CONT. - AGU
    -- CATEGORIA ECONÔMICA       : Receitas Correntes
    -- ORIGEM RECEITA            : Receita de Serviços
    -- ESPÉCIE RECEITA           : Serviços Administrativos e Comerciais Gerais
    -- DETALHAMENTO              : INSCR.EM CONCURSOS E PROC.SELETIVOS-PRINCIPAL
    -- VALOR PREVISTO ATUALIZADO : 0,00
    -- VALOR LANÇADO             : 0,00
    -- VALOR REALIZADO           : 126919,99
    -- PERCENTUAL REALIZADO      : 0,00
    -- DATA LANÇAMENTO           : 15/10/2018
    -- ANO EXERCÍCIO             : 2018

create table ptransp_orc.receitas_2023 (
    pss_id serial primary key,
    cod_org_sup text,
    nome_org_sup text,
    cod_org text,
    nome_org text,
    cod_unidade_gestora text,
    nome_unidade_gestora text,
    categoria_economica text,
    origem_receita text,
    especie_receita text,
    detalhamento text,
    valor_previsto_atualizado text,
    valor_lancado text,
    valor_realizado text,
    percentual_realizado text,
    data_lancamento text,
    ano_exercicio text
);

copy ptransp_orc.receitas_2023 (
    cod_org_sup,
    nome_org_sup,
    cod_org,
    nome_org,
    cod_unidade_gestora,
    nome_unidade_gestora,
    categoria_economica,
    origem_receita,
    especie_receita,
    detalhamento,
    valor_previsto_atualizado,
    valor_lancado,
    valor_realizado,
    percentual_realizado,
    data_lancamento,
    ano_exercicio
) from 'C:\Users\receitas\files\2023_Receitas.csv'
with (format csv, header true, delimiter ';', encoding 'latin1');
