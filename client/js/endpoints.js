export const moduleTemplateEndpoints = {
  moduleTemplate: {
    health: 'module_template/health/',
    models: {
      list: 'module_template/models/',
      detail: (id) => `module_template/models/${id}/`,
    },
  },
}
