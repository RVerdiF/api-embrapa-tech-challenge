import requests
import pandas as pd
from typing import List, Dict, Optional
import yaml
from app.models.exportacao import (
    Mesa as Mesamodel,
    Espumantes as Espumantesmodel,
    Frescas as Frescasmodel,
    Sucos as Sucosmodel,
)
from app.utils._get_data import data_extract_2 as getdata

class Mesa:
    def __init__(self):
        pass
        
    def main(self):
        try:
            url = yaml.safe_load(open('app/scrapping/urls.yaml',encoding='utf-8'))\
                .get('Exportacao', {})\
                .get('subcategoria', {})\
                .get('mesa', {})\
                .get('downloadurl')
            df_pivoted = getdata('Vinho de mesa').main(url,Mesamodel)
            if not df_pivoted.empty:
                return df_pivoted
            else:
                return pd.DataFrame()
        except requests.exceptions.RequestException as e:
            raise e
        except Exception as e:
            raise e
        
class Espumantes:
    def __init__(self):
        pass

    def main(self):
        try:
            url = yaml.safe_load(open('app/scrapping/urls.yaml',encoding='utf-8'))\
                .get('Exportacao', {})\
                .get('subcategoria', {})\
                .get('espumantes', {})\
                .get('downloadurl')
            df_pivoted = getdata('Espumantes').main(url,Espumantesmodel)
            if not df_pivoted.empty:
                return df_pivoted
            else:
                return pd.DataFrame()
        except requests.exceptions.RequestException as e:
            raise e
        except Exception as e:
            raise e
        
class Frescas:
    def __init__(self):
        pass

    def main(self):
        try:
            url = yaml.safe_load(open('app/scrapping/urls.yaml',encoding='utf-8'))\
                .get('Exportacao', {})\
                .get('subcategoria', {})\
                .get('frescas', {})\
                .get('downloadurl')
            df_pivoted = getdata('Uvas Frescas').main(url,Frescasmodel)
            if not df_pivoted.empty:
                return df_pivoted
            else:
                return pd.DataFrame()
        except requests.exceptions.RequestException as e:
            raise e
        except Exception as e:
            raise e
        
class Sucos:
    def __init__(self):
        pass

    def main(self):
        try:
            url = yaml.safe_load(open('app/scrapping/urls.yaml',encoding='utf-8'))\
                .get('Exportacao', {})\
                .get('subcategoria', {})\
                .get('sucos', {})\
                .get('downloadurl')
            df_pivoted = getdata('Sucos').main(url,Mesamodel)
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
            espumantes_df = Espumantes().main()
            frescas_df = Frescas().main()
            mesa_df = Mesa().main()
            sucos_df = Sucos().main()

            combined_df = pd.concat([espumantes_df, frescas_df, mesa_df, sucos_df], ignore_index=True)
            return combined_df
        except requests.exceptions.RequestException as e:
            raise e
        except Exception as e:
            raise e
        
    def filter(
        pais: Optional[str] = None,
        produto: Optional[str] = None,
        ano: Optional[int] = None,
        quantidade_min: Optional[int] = None,
        quantidade_max: Optional[int] = None
    ) -> pd.DataFrame:
        df = Main().main()
        if df is None or df.empty:
            return pd.DataFrame()
            
        filtered_df = df.copy()
        
        if pais is not None:
            filtered_df = filtered_df[filtered_df['país'] == pais.upper().replace('_',' ')]
            
        if produto is not None:
            filtered_df = filtered_df[filtered_df['produto'] == produto.upper().replace('_',' ')]
            
        if ano is not None:
            filtered_df = filtered_df[filtered_df['ano'] == ano]
            
        if quantidade_min is not None:
            filtered_df = filtered_df[filtered_df['quantidade'] >= quantidade_min]
        
        if quantidade_max is not None:
            filtered_df = filtered_df[filtered_df['quantidade'] <= quantidade_max]
            
        return filtered_df
    
if __name__ == '__main__':
    try:
        Espumantes().main()
        print('Sucesso função Espumantes')
    except Exception as e:
        print(f"Error in Espumantes: {e}")
    try:
        Frescas().main()
        print('Sucesso função Frescas')
    except Exception as e:
        print(f"Error in Frescas: {e}")
    try:
        Mesa().main()
        print('Sucesso função Mesa')
    except Exception as e:
        print(f"Error in Mesa: {e}")
    try:
        Sucos().main()
        print('Sucesso função Sucos')
    except Exception as e:
        print(f"Error in Sucos: {e}")
    try:
        Main().main()
        print('Sucesso função Main')
    except Exception as e:
        print(f"Error in Main: {e}")