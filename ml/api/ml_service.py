from typing import Optional, Dict


def load_model(version: Optional[str] = None):
    # Заглушка: возвращает None
    return None


def predict(payload: Dict) -> Dict:
    # Заглушка: возвращает пустое предсказание
    return {"prediction": None}


def get_model_meta() -> Dict:
    # Заглушка: возвращает метаданные по умолчанию
    return {"model_version": "none"}
