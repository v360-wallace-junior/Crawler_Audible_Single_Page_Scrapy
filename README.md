# Scrapy Curso 01

Projeto de estudo com Scrapy para coletar dados populacionais do site
[Worldometer](https://www.worldometers.info/world-population/population-by-country/).

O spider `worldmeters` acessa a página de população por país, segue os links
dos países e extrai das tabelas de cada página os campos `year` e
`population`.

## Requisitos

- Python instalado
- `pip`

As dependências do projeto estão listadas em [`requirements.txt`](requirements.txt).

## Instalação

Na raiz do repositório, crie e ative um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

No Windows (PowerShell), ative o ambiente virtual com:

```powershell
.venv\Scripts\Activate.ps1
```

## Executar o spider

O projeto Scrapy está dentro da pasta `spider/`. Execute o comando a partir dela:

```bash
cd spider
scrapy crawl worldmeters -O population.json
```

O arquivo `population.json` será criado na pasta `spider/`. A opção `-O`
substitui o arquivo caso ele já exista. Para acrescentar resultados a um arquivo
existente, use `-o`:

```bash
scrapy crawl worldmeters -o population.json
```

Cada registro exportado contém os campos `year` e `population`. A configuração
atual também respeita `robots.txt` e aplica um intervalo de um segundo entre
requisições ao mesmo domínio.

## Estrutura

```text
.
├── requirements.txt
└── spider/
    ├── scrapy.cfg
    └── spider/
        ├── settings.py
        └── spiders/
            └── worldmeters.py
```
   
   