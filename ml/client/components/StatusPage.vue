<template>
    <div class="status-page">
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

        <!-- Карточки статуса -->
        <div class="row g-4 mb-4">
            <!-- Статус сервиса -->
            <div class="col-md-6 col-xl-3">
                <div class="card h-100 border-0 shadow-sm">
                    <div class="card-body">
                        <div class="d-flex align-items-center gap-3">
                            <div 
                                class="status-icon rounded-circle d-flex align-items-center justify-content-center"
                                :class="statusData.status === 'ok' ? 'bg-success-subtle' : 'bg-danger-subtle'"
                            >
                                <CheckCircle 
                                    v-if="statusData.status === 'ok'" 
                                    :size="24" 
                                    class="text-success" 
                                />
                                <XCircle 
                                    v-else 
                                    :size="24" 
                                    class="text-danger" 
                                />
                            </div>
                            <div>
                                <p class="text-muted mb-0 small">Статус сервиса</p>
                                <p class="fw-bold mb-0 text-capitalize">
                                    {{ statusData.status === 'ok' ? 'Работает' : 'Ошибка' }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Статус БД -->
            <div class="col-md-6 col-xl-3">
                <div class="card h-100 border-0 shadow-sm">
                    <div class="card-body">
                        <div class="d-flex align-items-center gap-3">
                            <div 
                                class="status-icon rounded-circle d-flex align-items-center justify-content-center"
                                :class="statusData.db === 'ok' ? 'bg-success-subtle' : 'bg-danger-subtle'"
                            >
                                <Database 
                                    :size="24" 
                                    :class="statusData.db === 'ok' ? 'text-success' : 'text-danger'" 
                                />
                            </div>
                            <div>
                                <p class="text-muted mb-0 small">База данных</p>
                                <p class="fw-bold mb-0 text-capitalize">
                                    {{ statusData.db === 'ok' ? 'Подключена' : 'Недоступна' }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Время сервера -->
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

            <!-- Версия приложения -->
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

        <!-- Информационная карточка -->
        <div class="card border-0 shadow-sm">
            <div class="card-header bg-transparent border-0 pt-3">
                <h5 class="mb-0 d-flex align-items-center gap-2">
                    <Info :size="20" />
                    О модуле
                </h5>
            </div>
            <div class="card-body">
                <p class="mb-3">
                    Модуль машинного обучения для системы ERGO MS. 
                    Предоставляет функциональность для работы с ML моделями.
                </p>
                
                <h6 class="mt-4 mb-3">Функциональность модуля:</h6>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item d-flex align-items-center gap-2 border-0 px-0">
                        <Check :size="18" class="text-success" />
                        API endpoint <code>/api/ml/health/</code> для проверки статуса
                    </li>
                    <li class="list-group-item d-flex align-items-center gap-2 border-0 px-0">
                        <Check :size="18" class="text-success" />
                        Клиентская страница статуса сервиса
                    </li>
                    <li class="list-group-item d-flex align-items-center gap-2 border-0 px-0">
                        <Check :size="18" class="text-success" />
                        Заглушки для будущего ML функционала
                    </li>
                </ul>
            </div>
        </div>

        <!-- Состояние загрузки -->
        <div v-if="loading" class="loading-overlay">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Загрузка...</span>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { apiClient } from '@/js/api/manager'
import { useToast } from 'vue-toastification'
import { 
    Activity, 
    RefreshCw, 
    CheckCircle, 
    XCircle, 
    Database, 
    Clock, 
    Tag, 
    Info, 
    Check 
} from 'lucide-vue-next'

import { mlEndpoints } from '../js/endpoints'

const toast = useToast()
const loading = ref(false)

const statusData = ref({
    status: 'unknown',
    db: 'unknown',
    time: null,
    app_version: '-'
})

const refreshStatus = async () => {
    loading.value = true
    try {
        const response = await apiClient.get(mlEndpoints.ml.health)
        
        if (response.success) {
            statusData.value = response.data
            toast.success('Статус обновлён')
        } else {
            if (response.data) {
                statusData.value = response.data
            }
            toast.warning(response.message || 'Сервис недоступен')
        }
    } catch (error) {
        statusData.value = {
            status: 'fail',
            db: 'fail',
            time: null,
            app_version: '-'
        }
        toast.error('Ошибка подключения к серверу')
        console.error('Health check error:', error)
    } finally {
        loading.value = false
    }
}

const formatTime = (isoString) => {
    if (!isoString) return '-'
    try {
        return new Date(isoString).toLocaleString('ru-RU', {
            day: '2-digit',
            month: '2-digit',
            year: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        })
    } catch {
        return isoString
    }
}

onMounted(() => {
    refreshStatus()
})
</script>

<style scoped>
.status-page {
    padding: 20px;
    position: relative;
}

.status-icon {
    width: 48px;
    height: 48px;
    flex-shrink: 0;
}

.spin {
    animation: spin 1s linear infinite;
}

@keyframes spin {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}

.loading-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(255, 255, 255, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

code {
    background: var(--bs-gray-100);
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.875em;
}
</style>
