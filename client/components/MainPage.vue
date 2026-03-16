<template>
    <div class="mt-main-page">
        <div class="main-card">
            <div class="card-header">
                <div class="header-left">
                    <Box :size="24" class="module-icon" />
                    <h1 class="module-title">Module Template</h1>
                </div>
            </div>

            <div class="card-content">
                <div class="welcome-section">
                    <h2 class="welcome-title">Добро пожаловать в шаблонный модуль</h2>
                    <p class="welcome-description">
                        Модуль является шаблоном для создания новых модулей в системе ERGO MS.
                        Используйте его как отправную точку для разработки собственного функционала.
                    </p>
                </div>

                <div class="features-grid">
                    <div class="feature-item">
                        <div class="feature-icon">
                            <Activity :size="20" />
                        </div>
                        <div class="feature-text">
                            <span class="feature-title">Мониторинг</span>
                            <span class="feature-desc">Health-check сервиса и БД</span>
                        </div>
                    </div>

                    <div class="feature-item">
                        <div class="feature-icon">
                            <Database :size="20" />
                        </div>
                        <div class="feature-text">
                            <span class="feature-title">База данных</span>
                            <span class="feature-desc">Изолированное подключение к БД</span>
                        </div>
                    </div>

                    <div class="feature-item">
                        <div class="feature-icon">
                            <Layers :size="20" />
                        </div>
                        <div class="feature-text">
                            <span class="feature-title">API</span>
                            <span class="feature-desc">DRF ViewSet'ы и сериализаторы</span>
                        </div>
                    </div>

                    <div class="feature-item">
                        <div class="feature-icon">
                            <Code :size="20" />
                        </div>
                        <div class="feature-text">
                            <span class="feature-title">Composables</span>
                            <span class="feature-desc">Разделение логики и представления</span>
                        </div>
                    </div>
                </div>

                <div class="action-section">
                    <router-link
                        :to="{ name: 'ModuleTemplateStatus' }"
                        class="btn btn-primary d-flex align-items-center gap-2"
                    >
                        <Activity :size="18" />
                        Проверить статус сервиса
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { Box, Activity, Database, Layers, Code } from 'lucide-vue-next'
</script>

<style lang="scss" scoped>
@import '../scss/main-page.scss';
</style>
