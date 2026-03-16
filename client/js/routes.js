export default {
  ModuleTemplate: {
    path: '/module-template',
    name: 'ModuleTemplateMain',
    redirect: { name: 'ModuleTemplateStatus' },
    component: '@/modules/module_template/client/ParentLayout.vue',
    meta: {
      title: 'Module Template',
      requiresAuth: true,
    },
    children: [
      {
        path: '',
        name: 'ModuleTemplateMain',
        component: '@/modules/module_template/client/components/MainPage.vue',
        meta: {
          title: 'Главная',
        },
      },
      {
        path: 'status',
        name: 'ModuleTemplateStatus',
        component: '@/modules/module_template/client/components/StatusPage.vue',
        meta: {
          title: 'Статус сервиса',
        },
      },
    ],
  },
}
