import pandas as pd

def criar_dicionario(df:pd.DataFrame) -> dict:
    """
    Cria um dicionário de categorias com base na coluna 'control'.

    Args:
        df (pd.DataFrame): O DataFrame contendo os dados.

    Returns:
        dict: Um dicionário onde as chaves são os prefixos (antes do '_')
            e os valores são as categorias correspondentes.
    """
    categoria_dict = {}
    categoria_atual = None

    for index, row in df.iterrows():
        control = row['control']

        if "_" not in control:
            categoria_atual = row['produto'].strip()  # Encontrou uma nova categoria
        else:
            prefixo = control.split("_")[0].lower()
            categoria_dict[prefixo] = categoria_atual.strip()

    return categoria_dict