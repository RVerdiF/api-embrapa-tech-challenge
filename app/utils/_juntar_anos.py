import pandas as pd

def agrupar_colunas_por_ano(df:pd.DataFrame) -> pd.DataFrame:
    # Identificar colunas numéricas (anos)
    colunas_anos = {}
    
    # Agrupar colunas pelo ano base
    for col in df.columns:
        # Verificar se a coluna começa com um número (potencialmente um ano)
        if isinstance(col, str) and col.split('.')[0].isdigit():
            ano_base = col.split('.')[0]  # Pega a parte antes do ponto
            if ano_base not in colunas_anos:
                colunas_anos[ano_base] = []
            colunas_anos[ano_base].append(col)
        elif isinstance(col, (int, float)) or (isinstance(col, str) and col.isdigit()):
            # Caso a coluna seja diretamente um número ou string numérica
            ano_base = str(int(float(col)))
            if ano_base not in colunas_anos:
                colunas_anos[ano_base] = []
            colunas_anos[ano_base].append(col)
    
    # Criar um novo DataFrame com as colunas não-numéricas
    colunas_nao_numericas = [col for col in df.columns if col not in [c for sublist in colunas_anos.values() for c in sublist]]
    df_novo = df[colunas_nao_numericas].copy()
    
    # Adicionar as colunas de anos somadas
    for ano, colunas in colunas_anos.items():
        # Converter todas as colunas para numérico, tratando valores não numéricos
        for col in colunas:
            if df[col].dtype == 'object':
                df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '.'), errors='coerce').fillna(0)
        
        # Somar as colunas do mesmo ano
        df_novo[ano] = df[colunas].sum(axis=1)
    
    return df_novo