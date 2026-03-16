import { ref, onMounted } from 'vue'
import { apiClient } from '@/js/api/manager'
import { useToast } from 'vue-toastification'

import { moduleTemplateEndpoints } from './endpoints'

export function useModuleTemplateStatus() {
    const toast = useToast()
    const loading = ref(false)
    const statusData = ref({
        status: 'unknown',
        db: 'unknown',
        time: null,
        app_version: '-',
    })

    const refreshStatus = async () => {
        loading.value = true
        try {
            const response = await apiClient.get(moduleTemplateEndpoints.moduleTemplate.health)

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
            statusData.value = { status: 'fail', db: 'fail', time: null, app_version: '-' }
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
                second: '2-digit',
            })
        } catch {
            return isoString
        }
    }

    onMounted(() => refreshStatus())

    return { loading, statusData, refreshStatus, formatTime }
}
