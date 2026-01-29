# Module Example

Пример модуля для системы ERGO MS, демонстрирующий базовую структуру и функциональность.

## Описание

Модуль предоставляет базовый функционал для проверки здоровья сервиса и статуса базы данных. Используйте его как шаблон для создания новых модулей в системе ERGO MS.

### Возможности

- API endpoint `/health` для проверки статуса сервиса
- Клиентская страница статуса сервиса на Vue.js
- Заглушки для будущего ML функционала

## Структура модуля

```
module_example/
├── api/                        # Серверная часть (Django приложение)
│   ├── __init__.py
│   ├── apps.py                 # Конфигурация AppConfig
│   ├── models.py               # Модели данных
│   ├── urls.py                 # URL маршруты
│   ├── views.py                # ViewSet'ы и представления
│   ├── serializers.py          # DRF сериализаторы
│   ├── ml_service.py           # Сервис машинного обучения (заглушки)
│   └── migrations/             # Миграции БД
├── client/                     # Клиентская часть (Vue.js)
│   └── src/
│       ├── js/
│       │   ├── routes.js       # Маршруты Vue Router
│       │   ├── menu-config.json # Конфигурация меню
│       │   └── endpoints.js    # API эндпоинты
│       └── components/         # Vue компоненты
│           ├── ModuleExample.vue
│           └── StatusPage.vue
├── reports/                    # Отчёты (опционально)
└── README.md                   # Документация модуля
```

## API Endpoints

### GET /api/module_example/health/health/

Проверка здоровья сервиса и базы данных.

**Ответ (200 OK):**
```json
{
  "status": "ok",
  "db": "ok",
  "time": "2026-01-29T10:00:00Z",
  "app_version": "dev"
}
```

**Ответ (503 Service Unavailable):**
```json
{
  "status": "fail",
  "db": "fail",
  "time": "2026-01-29T10:00:00Z",
  "app_version": "dev"
}
```

## Клиентские маршруты

| Путь | Название | Описание |
|------|----------|----------|
| `/module-example` | ModuleExample | Главная страница модуля (редирект на статус) |
| `/module-example/` | ModuleExampleStatus | Страница статуса сервиса |

## Установка и запуск

Модуль автоматически обнаруживается системой ERGO MS при наличии файла `api/apps.py` с классом `AppConfig`.

### Применение миграций

```bash
ergoms api makemigrations module_example
ergoms api migrate
```

## Разработка

Модуль следует стандартам архитектуры ERGO MS:

- **API часть**: Django REST Framework с ViewSet'ами
- **Клиентская часть**: Vue.js 3 с Composition API и Bootstrap 5
- **Автообнаружение**: через `ModuleDiscoverer` (API) и `ModuleManager` (Client)
- **Изоляция**: модуль независим от других модулей и ядра системы

### Соглашения об импортах

**API (Python):**
- Внутри модуля: относительные импорты (`from . import views`)
- Из ядра: полные пути (`from src.core...`)

**Client (JavaScript/Vue):**
- Из ядра: абсолютные пути (`import { apiClient } from '@/js/api/manager'`)
- Внутри модуля: относительные пути (`import { moduleExampleEndpoints } from '../js/endpoints'`)

## ML функционал

В модуле предусмотрены заглушки для будущего ML функционала в файле `api/ml_service.py`:

| Функция | Описание |
|---------|----------|
| `load_model(version)` | Загрузка модели машинного обучения |
| `predict(payload)` | Выполнение предсказания |
| `get_model_meta()` | Получение метаданных модели |

## Расширение модуля

### Добавление новых страниц

1. Создайте компонент в `client/src/components/`
2. Добавьте маршрут в `client/src/js/routes.js`
3. При необходимости обновите `client/src/js/menu-config.json`

### Добавление API endpoints

1. Создайте ViewSet в `api/views.py`
2. Зарегистрируйте в роутере в `api/urls.py`
3. Добавьте эндпоинт в `client/src/js/endpoints.js`

### Добавление Celery задач

1. Создайте `api/tasks.py` с задачами
2. Создайте `celery_config.py` с конфигурацией очередей
3. При необходимости создайте `celery_beat_config.py` для периодических задач

## Лицензия

См. основной репозиторий ERGO MS.
