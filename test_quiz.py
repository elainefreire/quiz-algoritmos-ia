import pytest

from quiz import extrair_json, validar

VALIDA = {
    "questoes": [
        {
            "enunciado": "Qual a complexidade da busca binária?",
            "alternativas": ["O(n)", "O(log n)", "O(n^2)", "O(1)"],
            "correta": 1,
            "explicacao": "Cada passo divide o espaço de busca pela metade.",
        }
    ]
}


def test_extrair_json_ignora_texto_em_volta():
    texto = 'Aqui está:\n```json\n{"a": 1}\n```'
    assert extrair_json(texto) == {"a": 1}


def test_extrair_json_sem_json():
    with pytest.raises(ValueError):
        extrair_json("sem chaves aqui")


def test_validar_aceita_questao_correta():
    assert len(validar(VALIDA)) == 1


def test_validar_rejeita_tres_alternativas():
    ruim = {"questoes": [{**VALIDA["questoes"][0], "alternativas": ["a", "b", "c"]}]}
    with pytest.raises(ValueError):
        validar(ruim)


def test_validar_rejeita_indice_fora_do_intervalo():
    ruim = {"questoes": [{**VALIDA["questoes"][0], "correta": 7}]}
    with pytest.raises(ValueError):
        validar(ruim)


def test_validar_rejeita_lista_vazia():
    with pytest.raises(ValueError):
        validar({"questoes": []})
