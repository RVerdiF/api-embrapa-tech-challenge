import requests
import pandas as pd
from typing import List, Dict, Optional
import yaml
from app.models.processamento import (
    Viniferas as Viniferasmodel,
    Americanas as Americanasmodel,
    Mesa as Mesamodel,
    Outros as Outrosmodel,
)
from app.utils._get_data import data_extract_1 as getdata

class Viniferas:
    def __init__(self):
        pass

    def main(self):
        try:
            url = yaml.safe_load(open('app/scrapping/urls.yaml',encoding='utf-8'))\
                .get('Processamento', {})\
                .get('subcategoria', {})\
                .get('viníferas', {})\
                .get('downloadurl')
            df_pivoted = getdata().main(url,Viniferasmodel)
            if not df_pivoted.empty:
                return df_pivoted
            else:
                return pd.DataFrame()
        except requests.exceptions.RequestException as e:
            raise e
        except Exception as e:
            raise e

class Americanas:
    def __init__(self):
        pass

    def main(self):
        try:
            url = yaml.safe_load(open('app/scrapping/urls.yaml', encoding='utf-8'))\
                .get('Processamento', {})\
                .get('subcategoria', {})\
                .get('americanas', {})\
                .get('downloadurl')
            df_pivoted = getdata().main(url,Americanasmodel)
            if not df_pivoted.empty:
                return df_pivoted
            else:
                return pd.DataFrame()
        except requests.exceptions.RequestException as e:
            raise e
        except Exception as e:
            raise e

class Mesa:
    def __init__(self):
        pass

    def main(self):
        try:
            url = yaml.safe_load(open('app/scrapping/urls.yaml', encoding='utf-8'))\
                .get('Processamento', {})\
                .get('subcategoria', {})\
                .get('mesa', {})\
                .get('downloadurl')
            df_pivoted = getdata().main(url,Mesamodel)
            if not df_pivoted.empty:
                return df_pivoted
            else:
                return pd.DataFrame()
        except requests.exceptions.RequestException as e:
            raise e
        except Exception as e:
            raise e

class Outros:
    def __init__(self):
        pass

    def main(self):
        try:
            url = yaml.safe_load(open('app/scrapping/urls.yaml', encoding='utf-8'))\
                .get('Processamento', {})\
                .get('subcategoria', {})\
                .get('outros', {})\
                .get('downloadurl')
            df_pivoted = getdata().main(url,Outrosmodel)
            if not df_pivoted.empty:
                return df_pivoted
            else:
                return pd.DataFrame()
        except requests.exceptions.RequestException as e:
            raise e
        except Exception as e:
            raise e

class Main:
    def __init__(self):
        pass

    def main(self) -> pd.DataFrame:
        try:
            viniferas_df = Viniferas().main()
            americanas_df = Americanas().main()
            mesa_df = Mesa().main()
            outros_df = Outros().main()

            combined_df = pd.concat([viniferas_df, americanas_df, mesa_df, outros_df], ignore_index=True)
            return combined_df
        except requests.exceptions.RequestException as e:
            raise e
        except Exception as e:
            raise e
        
    def filter(
        self,
        categoria: Optional[str] = None,
        produto: Optional[str] = None,
        ano: Optional[int] = None,
        quantidade_min: Optional[int] = None,
        quantidade_max: Optional[int] = None
    ) -> pd.DataFrame:
        df = Main().main()
        if df is None or df.empty:
            return pd.DataFrame()
            
        filtered_df = df.copy()
        
        if categoria is not None:
            filtered_df = filtered_df[filtered_df['categoria'].str.upper() == categoria.upper().replace('_',' ')]
            
        if produto is not None:
            filtered_df = filtered_df[filtered_df['produto'].str.upper() == produto.upper().replace('_',' ')]
            
        if ano is not None:
            filtered_df = filtered_df[filtered_df['ano'] == ano]
            
        if quantidade_min is not None:
            filtered_df = filtered_df[filtered_df['quantidade'] >= quantidade_min]
        
        if quantidade_max is not None:
            filtered_df = filtered_df[filtered_df['quantidade'] <= quantidade_max]
            
        return filtered_df

if __name__ == '__main__':
    try:
        Main().main()
        print('Sucesso função Main')
    except Exception as e:
        print(f"Error in Viniferas: {e}")
    try:
        Viniferas().main()
        print('Sucesso função Viniferas')
    except Exception as e:
        print(f"Error in Viniferas: {e}")
    try:
        Americanas().main()
        print('Sucesso função Americanas')
    except Exception as e:
        print(f"Error in Americanas: {e}")
    try:
        Mesa().main()
        print('Sucesso função Mesa')
    except Exception as e:
        print(f"Error in Mesa: {e}")
    try:
        Outros().main()
        print('Sucesso função Outros')
    except Exception as e:
        print(f"Error in Outros: {e}")