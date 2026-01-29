export default {
  ML: {
    path: '/ml',
    name: 'MLMain',
    redirect: { name: 'MLMain' },
    component: '@/modules/ml/client/ParentLayout.vue',
    meta: {
      title: 'ML',
      requiresAuth: true,
    },
    children: [
      {
        path: '',
        name: 'MLMain',
        component: '@/modules/ml/client/components/MainPage.vue',
        meta: {
          title: 'Главная',
        },
      },
      {
        path: 'status',
        name: 'MLStatus',
        component: '@/modules/ml/client/components/StatusPage.vue',
        meta: {
          title: 'Статус сервиса',
        },
      },
    ],
  },
}
