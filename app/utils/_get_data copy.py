import pandas as pd
import requests
from io import StringIO,BytesIO,TextIOWrapper
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from app.utils._criar_categoria import extrair_categorias_hierarquicas
from app.utils._criar_dicionario import criar_dicionario
from pydantic import ValidationError, BaseModel

class data_extract:
    def __init__(self) -> None:
        self.base_url = 'http://vitibrasil.cnpuv.embrapa.br/'

    def getdata(self,url:str) -> pd.DataFrame:
        try:
            
            # session = requests.Session()
            # retry_strategy = Retry(connect=3, backoff_factor=0.5)
            # adapter = HTTPAdapter(max_retries=retry_strategy)
            # session.mount("http://", adapter)
            # session.mount("https://", adapter)
            # response = session.get(self.base_url, timeout=10,verify=False)
            # response.raise_for_status()
            # response = session.get(url, timeout=10, verify=False)
            # response.raise_for_status()
            
            session = requests.Session()
            retry_strategy = Retry(
                total=3,
                backoff_factor=0.5,
                status_forcelist=[429, 500, 502, 503, 504],
                allowed_methods=["GET"]
            )
            adapter = HTTPAdapter(max_retries=retry_strategy)
            session.mount("http://", adapter)
            session.mount("https://", adapter)

            # Make a single request to the target URL
            response = session.get(self.base_url, timeout=10, verify=False)
            response.raise_for_status()
            
            response = session.get(url, timeout=10, verify=False)
            response.raise_for_status()
            
            bio = BytesIO(response.content)
            wrapper = TextIOWrapper(bio, encoding='utf-8')
            df = pd.read_csv(wrapper, sep=None, engine='python', encoding='utf-8')
            
            session.close()
            return df
        except Exception as e:
            raise e

def _filter_comercializacao(df:pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={'cultivar': 'produto'})
    df['control'] = df['control'].fillna(df['produto'])
    for col in df.columns:
        if col.isdigit():
            df[col] = df[col].astype(str).replace('*','0').replace('nd','0').fillna('0').str.replace(',','.').astype(float)
    return df

def _filter_processamento(df:pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={'cultivar': 'produto'})
    df['control'] = df['control'].fillna(df['produto'])
    for col in df.columns:
        if col.isdigit():
            df[col] = df[col].astype(str).replace('*','0').replace('nd','0').str.replace('+','0').fillna('0').str.replace(',','.').astype(float)
    return df

def main(url:str,model:BaseModel) -> pd.DataFrame:
    dataextract = data_extract()

    try:
        df = dataextract.getdata(url)
    except requests.exceptions.RequestException as e:
        raise e
    
    if df.empty:
        return pd.DataFrame()
    
    df.columns = df.columns.str.lower()

    if 'comercio' in url.lower():
        df = _filter_comercializacao(df)
    if 'processa' in url.lower():
        df = _filter_processamento(df)
               
    categoria_dict = criar_dicionario(df)
    categorias, subcategorias = extrair_categorias_hierarquicas(df,categoria_dict)
    df['categoria'] = categorias
    df['produto'] = subcategorias

    # Remove as linhas onde Categoria e Subcategoria são iguais
    df = df[df['categoria'] != df['produto']]
    df = df.drop(columns=['id', 'control',])
    
    df_pivoted = df.melt(id_vars=[col for col in df.columns if not col.isdigit()], 
        var_name='ano', 
        value_name='quantidade'
    ).reset_index(drop=False)
    
    validated_records = []
    
    for _, row in df_pivoted.iterrows():
        try:
            validated_record = model(
                index=row['index'],
                categoria=row['categoria'],
                produto=row['produto'],
                quantidade=row['quantidade'],
                ano=row['ano']
            )
            validated_records.append(validated_record.model_dump())
        except ValidationError as e:
            print(f"Validation error in row: {e}")
            continue
    df_pivoted = pd.DataFrame(validated_records)
    return df_pivoted