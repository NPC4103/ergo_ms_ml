export const mlEndpoints = {
    ml: {
        health: 'ml/health/',
        models: {
            list: 'ml/models/',
            detail: (id) => `ml/models/${id}/`,
        }
    }
}
