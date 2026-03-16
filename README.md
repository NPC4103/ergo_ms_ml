# Module Template

Шаблонный модуль для системы ERGO MS. Используйте его как отправную точку при создании новых модулей.

## Структура модуля

```
module_template/
├── api/
│   ├── __init__.py
│   ├── apps.py               # AppConfig: name, label, verbose_name
│   ├── config.py             # Константы модуля (DB alias, версия, USE_GPU)
│   ├── models.py             # Модель TemplateItem
│   ├── serializers.py        # TemplateItemSerializer
│   ├── views.py              # TemplateItemViewSet, HealthViewSet
│   ├── urls.py               # URL маршруты (namespace = module_template)
│   ├── admin.py              # Регистрация TemplateItem в Django admin
│   ├── routers.py            # DB router для изолированного подключения
│   └── migrations/
├── client/
│   ├── js/
│   │   ├── routes.js         # Маршруты Vue Router
│   │   ├── menu-config.json  # Конфигурация меню
│   │   ├── endpoints.js      # API эндпоинты
│   │   └── useModuleTemplate.js  # Composable: логика health-check
│   ├── components/
│   │   ├── MainPage.vue      # Главная страница модуля
│   │   └── StatusPage.vue    # Страница статуса сервиса
│   ├── scss/
│   │   ├── main-page.scss    # Стили MainPage
│   │   └── status-page.scss  # Стили StatusPage
│   ├── assets/
│   │   ├── svg/              # SVG-иконки модуля
│   │   ├── images/           # Изображения модуля
│   │   └── styles/           # Дополнительные стили (опционально)
│   └── ParentLayout.vue      # Лейаут модуля
├── ergoms.conf               # Команды ergoms модуля
├── .gitignore
└── README.md
```

## API Endpoints

### GET /api/module_template/health/health/

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

### /api/module_template/items/

CRUD-эндпоинты для модели `TemplateItem` (DRF ModelViewSet).

Поддерживает фильтрацию через query param `?active=true|false`.

## Клиентские маршруты

| Путь | Название | Описание |
|------|----------|----------|
| `/module-template` | ModuleTemplate | Редирект на статус |
| `/module-template` (index) | ModuleTemplateMain | Главная страница |
| `/module-template/status` | ModuleTemplateStatus | Страница статуса сервиса |

## Команды ergoms

```bash
# Применить миграции модуля
ergoms module_template:migrate
```

## Установка и запуск

Модуль автоматически обнаруживается системой ERGO MS при наличии файла `api/apps.py` с классом `AppConfig`.

Применить миграции:

```bash
ergoms module_template:migrate
```

## Архитектура клиентской части

### Composable

Логика запросов к API вынесена в `client/js/useModuleTemplate.js`:

```javascript
import { useModuleTemplateStatus } from '../js/useModuleTemplate'

const { loading, statusData, refreshStatus, formatTime } = useModuleTemplateStatus()
```

### Стили

Стили компонентов вынесены в отдельные SCSS-файлы в `client/scss/`:

```vue
<style lang="scss" scoped>
@use '../scss/main-page.scss';
</style>
```

### Эндпоинты

```javascript
import { moduleTemplateEndpoints } from '../js/endpoints'
// moduleTemplateEndpoints.moduleTemplate.health
// moduleTemplateEndpoints.moduleTemplate.models.list
// moduleTemplateEndpoints.moduleTemplate.models.detail(id)
```

## Соглашения об импортах

**API (Python):**
- Внутри модуля: относительные импорты (`from .models import TemplateItem`)
- Из ядра: полные пути (`from src.core...`)

**Client (JavaScript/Vue):**
- Из ядра: абсолютные пути (`import { apiClient } from '@/js/api/manager'`)
- Внутри модуля: относительные пути (`import { moduleTemplateEndpoints } from '../js/endpoints'`)

## Расширение модуля

### Добавление новых страниц

1. Создай компонент в `client/components/`
2. Добавь маршрут в `client/js/routes.js`
3. При необходимости обнови `client/js/menu-config.json`
4. Создай SCSS-файл в `client/scss/`

### Добавление API endpoints

1. Создай ViewSet в `api/views.py`
2. Зарегистрируй в роутере в `api/urls.py`
3. Добавь эндпоинт в `client/js/endpoints.js`

### Добавление Celery задач

1. Создай `api/tasks.py` с задачами
2. Создай `api/celery_config.py` с конфигурацией очередей
3. При необходимости создай `api/celery_beat_config.py` для периодических задач
