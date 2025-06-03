# API Embrapa - Vitivinicultura

API para extração e consulta de informações referentes à vitivinicultura, baseada em dados da Embrapa.

## Descrição

Este projeto consiste em uma API RESTful desenvolvida com FastAPI que fornece acesso a dados sobre vitivinicultura. A API extrai dados do portal Vitibrasil da Embrapa e os disponibiliza em formato JSON através de endpoints estruturados.

## Fluxograma geral do Projeto

![Fluxograma da API Embrapa](assets\fluxograma_api.png)

## Diagrama de sequencia do Projeto

![Diagrama de sequencia da API Embrapa](assets\diagrama_de_sequencia.png)

## Categorias de Dados

A API fornece informações sobre:

- **Produção**: Dados sobre a produção de uvas e derivados
- **Comercialização**: Informações sobre a comercialização de produtos vitivinícolas
- **Processamento**: Dados sobre o processamento de uvas (viníferas, americanas, mesa e outros)
- **Exportação**: Estatísticas de exportação (vinhos de mesa, espumantes, uvas frescas e sucos)
- **Importação**: Estatísticas de importação (vinhos de mesa, espumantes, uvas frescas, passas e sucos)

## Tecnologias Utilizadas

- **FastAPI**: Framework web para construção de APIs
- **Docker**: Containerização da aplicação
- **Pandas**: Manipulação e análise de dados
- **Pydantic**: Validação de dados
- **PyYAML**: Processamento de arquivos YAML para configuração

## Requisitos

- Docker e Docker Compose
- Python 3.10+ (para desenvolvimento local)

## Instalação e Execução

### Usando Docker (Recomendado)

1. Clone o repositório:
   ```
   git clone <url-do-repositorio>
   cd embrapa-api
   ```

2. Crie um arquivo `.env` baseado no `.env.example`:
   ```
   cp .env.example .env
   ```

3. Para ambiente de desenvolvimento (com hot-reload):
   ```
   ./start-dev.bat
   ```
   ou
   ```
   docker-compose -f docker-compose.dev.yml up --build
   ```

4. Para ambiente de produção:
   ```
   ./start-prod.bat
   ```
   ou
   ```
   docker-compose up --build
   ```

### Instalação Local (Desenvolvimento)

1. Clone o repositório:
   ```
   git clone <url-do-repositorio>
   cd embrapa-api
   ```

2. Execute o script de instalação e inicialização:
   ```
   main.bat
   ```

   O script irá automaticamente criar um ambiente virtual, instalar as dependências necessárias e iniciar a aplicação.

## Uso da API

A API estará disponível em `http://localhost:8000`.

### Documentação Swagger

Acesse a documentação interativa da API em:
- `http://localhost:8000/docs`

### Endpoints Principais

- **GET /v1/producao**: Retorna dados de produção
- **GET /v1/comercializacao**: Retorna dados de comercialização
- **GET /v1/processamento**: Retorna dados de processamento
- **GET /v1/exportacao**: Retorna dados de exportação
- **GET /v1/importacao**: Retorna dados de importação

### Exemplos de Filtros

Cada categoria possui endpoints para filtrar dados:

- **Por categoria**: `/v1/producao/categoria/{categoria}`
- **Por produto**: `/v1/producao/produto/{produto}`
- **Por ano**: `/v1/producao/ano/{ano}`
- **Por quantidade mínima**: `/v1/producao/quantidade/min/{quantidade}`
- **Por quantidade máxima**: `/v1/producao/quantidade/max/{quantidade}`
- **Filtros combinados**: `/v1/producao/filter?categoria=X&produto=Y&ano=2022`

## Estrutura do Projeto

```
./
├── app/
│   ├── models/            # Modelos de dados Pydantic
│   ├── routers/           # Rotas da API
│   ├── scrapping/         # Módulos para extração de dados
│   └── utils/             # Funções utilitárias
├── docker-compose.dev.yml # Configuração Docker para desenvolvimento
├── docker-compose.yml     # Configuração Docker para produção
├── Dockerfile             # Definição da imagem Docker
├── main.bat               # Script para execução local em Windows
├── main.py                # Ponto de entrada da aplicação
├── start-dev.bat          # Script para iniciar ambiente de desenvolvimento
├── start-prod.bat         # Script para iniciar ambiente de produção
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

## Fonte dos Dados

Os dados são extraídos do portal Vitibrasil da Embrapa:
- [http://vitibrasil.cnpuv.embrapa.br/](http://vitibrasil.cnpuv.embrapa.br/)

## Deploy em Máquina Virtual

### Pré-requisitos
- Uma máquina virtual com Linux
- Docker e Docker Compose instalados
- Acesso SSH à máquina virtual

### Passo a Passo Simplificado

1. **Conecte-se à VM e instale Docker**:
   ```bash
   ssh usuario@endereco-da-vm
   sudo apt update && sudo apt install -y docker.io docker-compose
   sudo systemctl enable docker && sudo systemctl start docker
   ```

2. **Clone e execute a aplicação**:
   ```bash
   git clone <url-do-repositorio> && cd embrapa-api
   cp .env.example .env
   docker-compose up -d
   ```

3. **Configure um proxy reverso (opcional)**:
   ```bash
   sudo apt install -y nginx
   sudo nano /etc/nginx/sites-available/embrapa-api
   # Adicione a configuração básica do Nginx
   sudo ln -s /etc/nginx/sites-available/embrapa-api /etc/nginx/sites-enabled/
   sudo systemctl restart nginx
   ```

## Exemplo de Uso para Machine Learning

### Caso de Uso: Previsão de Produção de Uvas

Este exemplo conceitual demonstra como utilizar os dados da API para criar um modelo preditivo de machine learning:

#### Fluxo de Trabalho

1. **Coleta de Dados**: Utilize o endpoint `/producao/filter?categoria=VINHO_DE_MESA&produto=TINTO` para obter dados históricos de produção de vinho tinto.

2. **Preparação dos Dados**: 
   - Converta os dados para formato numérico
   - Crie features adicionais como produção do ano anterior e variação percentual
   - Codifique variáveis categóricas
   - Divida os dados em conjuntos de treino e teste

3. **Treinamento do Modelo**:
   - Utilize um algoritmo como Random Forest Regressor
   - Treine o modelo com dados históricos
   - Avalie o desempenho usando métricas como MSE e R²

4. **Visualização e Análise**:
   - Identifique as features mais importantes para a previsão
   - Compare valores reais vs. previstos
   - Analise tendências por região e tipo de produto

5. **Previsões Futuras**:
   - Utilize o modelo treinado para prever a produção do próximo ano
   - Gere previsões por estado e produto
   - Crie relatórios para auxiliar no planejamento da produção

Este fluxo de trabalho permite que produtores e empresas do setor vitivinícola utilizem os dados históricos disponibilizados pela API para tomar decisões baseadas em dados e antecipar tendências de mercado.