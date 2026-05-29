from pathlib import Path

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent

# Pasta de dados
DATA_DIR = BASE_DIR / "data"

# Caminhos específicos
CAMINHO_DIJ10 = DATA_DIR / "dij10.txt"
CAMINHO_DIJ20 = DATA_DIR / "dij20.txt"
CAMINHO_DIJ40 = DATA_DIR / "dij40.txt"
CAMINHO_DIJ50 = DATA_DIR / "dij50.txt"

# Demais pastas
OUTPUT_DIR = BASE_DIR / "output"
RESULTS_DIR = BASE_DIR / "results"