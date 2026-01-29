<template>
    <div class="ml-main-page">
        <div class="main-card">
            <div class="card-header">
                <div class="header-left">
                    <Brain :size="24" class="module-icon" />
                    <h1 class="module-title">ML</h1>
                </div>
            </div>
            
            <div class="card-content">
                <div class="welcome-section">
                    <h2 class="welcome-title">Добро пожаловать в модуль машинного обучения</h2>
                    <p class="welcome-description">
                        Модуль предоставляет инструменты для работы с ML моделями, 
                        анализа данных и автоматизации процессов машинного обучения.
                    </p>
                </div>

                <div class="features-grid">
                    <div class="feature-item">
                        <div class="feature-icon">
                            <Activity :size="20" />
                        </div>
                        <div class="feature-text">
                            <span class="feature-title">Мониторинг</span>
                            <span class="feature-desc">Отслеживание статуса сервисов</span>
                        </div>
                    </div>
                    
                    <div class="feature-item">
                        <div class="feature-icon">
                            <Database :size="20" />
                        </div>
                        <div class="feature-text">
                            <span class="feature-title">Данные</span>
                            <span class="feature-desc">Работа с наборами данных</span>
                        </div>
                    </div>
                    
                    <div class="feature-item">
                        <div class="feature-icon">
                            <Cpu :size="20" />
                        </div>
                        <div class="feature-text">
                            <span class="feature-title">Модели</span>
                            <span class="feature-desc">Управление ML моделями</span>
                        </div>
                    </div>
                    
                    <div class="feature-item">
                        <div class="feature-icon">
                            <BarChart3 :size="20" />
                        </div>
                        <div class="feature-text">
                            <span class="feature-title">Аналитика</span>
                            <span class="feature-desc">Визуализация результатов</span>
                        </div>
                    </div>
                </div>

                <div class="action-section">
                    <router-link :to="{ name: 'MLStatus' }" class="btn btn-primary d-flex align-items-center gap-2">
                        <Activity :size="18" />
                        Проверить статус сервиса
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { Brain, Activity, Database, Cpu, BarChart3 } from 'lucide-vue-next'
</script>

<style scoped>
.ml-main-page {
    padding: 24px;
    min-height: 100%;
}

.main-card {
    background: var(--bs-body-bg);
    border: 1px solid var(--bs-border-color);
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    overflow: hidden;
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 24px;
    border-bottom: 1px solid var(--bs-border-color);
    background: var(--bs-tertiary-bg);
}

.header-left {
    display: flex;
    align-items: center;
    gap: 12px;
}

.module-icon {
    color: var(--bs-primary);
}

.module-title {
    margin: 0;
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--bs-heading-color);
}

.card-content {
    padding: 32px;
}

.welcome-section {
    margin-bottom: 32px;
}

.welcome-title {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 12px;
    color: var(--bs-heading-color);
}

.welcome-description {
    color: var(--bs-secondary-color);
    font-size: 1rem;
    line-height: 1.6;
    max-width: 600px;
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
    margin-bottom: 32px;
}

.feature-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 16px;
    background: var(--bs-tertiary-bg);
    border-radius: 8px;
    border: 1px solid var(--bs-border-color);
    transition: border-color 0.2s, box-shadow 0.2s;
}

.feature-item:hover {
    border-color: var(--bs-primary);
    box-shadow: 0 2px 8px rgba(var(--bs-primary-rgb), 0.1);
}

.feature-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border-radius: 8px;
    background: var(--bs-primary-bg-subtle);
    color: var(--bs-primary);
    flex-shrink: 0;
}

.feature-text {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.feature-title {
    font-weight: 600;
    color: var(--bs-heading-color);
}

.feature-desc {
    font-size: 0.875rem;
    color: var(--bs-secondary-color);
}

.action-section {
    padding-top: 16px;
    border-top: 1px solid var(--bs-border-color);
}
</style>
