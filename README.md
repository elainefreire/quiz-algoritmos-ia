# Quiz de Algoritmos com IA

Programa de terminal que usa um modelo de linguagem (LLM) para gerar questões de múltipla escolha sobre um tópico de Ciência da Computação, valida a resposta do modelo e corrige o quiz localmente.

Projeto de estudo para praticar integração com LLMs: prompts, saída estruturada em JSON, validação e testes.

## Como funciona

1. Você informa um tópico (ex.: "busca binária") e um nível.
2. O programa monta um prompt pedindo questões em JSON (`quiz.py`).
3. A API do modelo é chamada (`llm.py`).
4. A resposta é extraída e validada: formato, 4 alternativas, índice da correta (`quiz.py`).
5. Se vier fora do formato, o programa tenta de novo (`main.py`).
6. A correção é feita no código, não pelo modelo.

## Como rodar

Requer Python 3.10+ e uma chave de API da Anthropic.

```bash
git clone https://github.com/elainefreire/quiz-algoritmos-ia.git
cd quiz-algoritmos-ia
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sua-chave"   # Windows (PowerShell): $env:ANTHROPIC_API_KEY="sua-chave"
python main.py
```

## Testes

```bash
pytest
```

Os testes cobrem a extração e a validação do JSON e não usam a API.

## Estrutura

| Arquivo | Função |
| --- | --- |
| `main.py` | Interface de terminal e repetição em caso de erro |
| `quiz.py` | Prompt, extração e validação do JSON |
| `llm.py` | Chamada à API (único ponto de contato com o provedor) |
| `test_quiz.py` | Testes automatizados |

## Decisões de projeto

- **Validação da saída:** modelos podem responder fora do formato, então nada é usado antes de ser validado.
- **Correção no código:** o modelo gera as questões, mas a nota é calculada localmente.
- **Provedor isolado:** trocar de modelo ou de provedor exige mudar só o `llm.py`.

## Limitações e próximos passos

- O modelo pode errar o gabarito; ainda não há checagem da correção das questões.
- Ideias: salvar histórico de notas, escolher o número de questões, exportar o quiz e comparar modelos.
