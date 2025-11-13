# atividade_testes_webdriver

Script de testes automatizados usando Selenium WebDriver para validar o fluxo condicional da página hospedada em [GitHub Pages](https://matheus-forte-melo.github.io/atividade_testes_webdriver/index_ex.html).

## Pré-requisitos

- Python 3.10 ou superior instalado e disponível no `PATH`.
- Google Chrome ou Chromium instalado.

## Preparando o ambiente virtual

No diretório raiz do projeto (`aula05/`), execute os comandos abaixo. Os exemplos usam Linux ou macOS com `bash`/`zsh`.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Para Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

## Executando o teste

Com o ambiente virtual ativado:

```bash
python test.py
```

O script abre o Chrome em modo headless, envia valores positivos e negativos e valida que a página correta é exibida. Ajuste os valores ou parâmetros no código conforme necessário para novos cenários.

## Desativando o ambiente virtual

Quando terminar, execute:

```bash
deactivate
```
