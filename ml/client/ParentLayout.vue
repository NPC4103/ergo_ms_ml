<template>
    <div class="ml">
        <router-view :key="$route.name" />
    </div>
</template>

<script setup>
</script>

<style scoped>
.ml {
    min-height: 100%;
}
</style>