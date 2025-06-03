import requests
import pandas as pd
from typing import List, Dict, Optional
import yaml
from app.utils._get_data import data_extract_1 as getdata
from app.models.producao import Producao as Producaomodel
from pydantic import ValidationError


class Main:
    def __init__(self):
        pass

    def main(self) -> Optional[pd.DataFrame]:
        try:
            url = yaml.safe_load(open('app/scrapping/urls.yaml', encoding='utf-8'))\
                .get('Producao', {})\
                .get('downloadurl', None)
            df_pivoted = getdata().main(url,Producaomodel)
            if not df_pivoted.empty:
                return df_pivoted
            else:
                return pd.DataFrame()
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
    ):
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

if __name__ == "__main__":
    Main.main()