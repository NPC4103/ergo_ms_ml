<template>
    <div class="mt-status-page">
        <div class="header d-flex justify-content-between align-items-center mb-4">
            <h1 class="d-flex align-items-center gap-2">
                <Activity :size="28" />
                Статус сервиса
            </h1>
            <button
                class="btn btn-primary d-flex align-items-center gap-2"
                @click="refreshStatus"
                :disabled="loading"
            >
                <RefreshCw :size="18" :class="{ 'spin': loading }" />
                Обновить
            </button>
        </div>

        <div class="row g-4 mb-4">
            <div class="col-md-6 col-xl-3">
                <div class="card h-100 border-0 shadow-sm">
                    <div class="card-body">
                        <div class="d-flex align-items-center gap-3">
                            <div
                                class="status-icon rounded-circle d-flex align-items-center justify-content-center"
                                :class="statusData.status === 'ok' ? 'bg-success-subtle' : 'bg-danger-subtle'"
                            >
                                <CheckCircle v-if="statusData.status === 'ok'" :size="24" class="text-success" />
                                <XCircle v-else :size="24" class="text-danger" />
                            </div>
                            <div>
                                <p class="text-muted mb-0 small">Статус сервиса</p>
                                <p class="fw-bold mb-0">{{ statusData.status === 'ok' ? 'Работает' : 'Ошибка' }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-md-6 col-xl-3">
                <div class="card h-100 border-0 shadow-sm">
                    <div class="card-body">
                        <div class="d-flex align-items-center gap-3">
                            <div
                                class="status-icon rounded-circle d-flex align-items-center justify-content-center"
                                :class="statusData.db === 'ok' ? 'bg-success-subtle' : 'bg-danger-subtle'"
                            >
                                <Database :size="24" :class="statusData.db === 'ok' ? 'text-success' : 'text-danger'" />
                            </div>
                            <div>
                                <p class="text-muted mb-0 small">База данных</p>
                                <p class="fw-bold mb-0">{{ statusData.db === 'ok' ? 'Подключена' : 'Недоступна' }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-md-6 col-xl-3">
                <div class="card h-100 border-0 shadow-sm">
                    <div class="card-body">
                        <div class="d-flex align-items-center gap-3">
                            <div class="status-icon rounded-circle d-flex align-items-center justify-content-center bg-primary-subtle">
                                <Clock :size="24" class="text-primary" />
                            </div>
                            <div>
                                <p class="text-muted mb-0 small">Время сервера</p>
                                <p class="fw-bold mb-0">{{ formatTime(statusData.time) }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-md-6 col-xl-3">
                <div class="card h-100 border-0 shadow-sm">
                    <div class="card-body">
                        <div class="d-flex align-items-center gap-3">
                            <div class="status-icon rounded-circle d-flex align-items-center justify-content-center bg-info-subtle">
                                <Tag :size="24" class="text-info" />
                            </div>
                            <div>
                                <p class="text-muted mb-0 small">Версия</p>
                                <p class="fw-bold mb-0">{{ statusData.app_version }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="card border-0 shadow-sm">
            <div class="card-header bg-transparent border-0 pt-3">
                <h5 class="mb-0 d-flex align-items-center gap-2">
                    <Info :size="20" />
                    О модуле
                </h5>
            </div>
            <div class="card-body">
                <p class="mb-3">Шаблонный модуль для системы ERGO MS. Используйте его как базу для создания новых модулей.</p>

                <h6 class="mt-4 mb-3">Функциональность модуля:</h6>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item d-flex align-items-center gap-2 border-0 px-0">
                        <Check :size="18" class="text-success" />
                        API endpoint <code>/api/module_template/health/health/</code>
                    </li>
                    <li class="list-group-item d-flex align-items-center gap-2 border-0 px-0">
                        <Check :size="18" class="text-success" />
                        Клиентская страница статуса сервиса
                    </li>
                    <li class="list-group-item d-flex align-items-center gap-2 border-0 px-0">
                        <Check :size="18" class="text-success" />
                        CRUD-эндпоинты для TemplateItem
                    </li>
                </ul>
            </div>
        </div>

        <div v-if="loading" class="mt-loading-overlay">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Загрузка...</span>
            </div>
        </div>
    </div>
</template>

<script setup>
import {
    Activity,
    RefreshCw,
    CheckCircle,
    XCircle,
    Database,
    Clock,
    Tag,
    Info,
    Check,
} from 'lucide-vue-next'

import { useModuleTemplateStatus } from '../js/useModuleTemplate'

const { loading, statusData, refreshStatus, formatTime } = useModuleTemplateStatus()
</script>

<style lang="scss" scoped>
@import '../scss/status-page.scss';
</style>
