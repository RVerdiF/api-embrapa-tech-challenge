import pandas as pd

def extrair_categorias_hierarquicas(df:pd.DataFrame, categoria_dict: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Extrai as categorias e subcategorias do DataFrame, utilizando um dicionário de categorias.

    Args:
        df (pd.DataFrame): O DataFrame contendo os dados.
        categoria_dict (dict): Um dicionário mapeando prefixos de subcategorias para categorias.

    Returns:
        pd.DataFrame: O DataFrame com as colunas 'Categoria' e 'Subcategoria' adicionadas.
    """
    categorias = []
    subcategorias = []
    categoria_atual = None

    for index, row in df.iterrows():
        control = row['control']
        produto = row['produto']

        if "_" not in control:
            categoria_atual:str = produto
            categoria:str = categoria_atual
            subcategoria:str = produto
        else:
            prefixo = control.split("_")[0].lower()
            categoria:str = categoria_dict.get(prefixo, "Outros")
            subcategoria:str = produto

        categorias.append(categoria.strip().upper())
        subcategorias.append(subcategoria.strip().upper())

    # df['Categoria'] = categorias
    # df['Subcategoria'] = subcategorias
    return categorias, subcategorias