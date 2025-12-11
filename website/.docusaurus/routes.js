import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/cmfo-universe/markdown-page',
    component: ComponentCreator('/cmfo-universe/markdown-page', 'fcc'),
    exact: true
  },
  {
    path: '/cmfo-universe/docs',
    component: ComponentCreator('/cmfo-universe/docs', '94a'),
    routes: [
      {
        path: '/cmfo-universe/docs',
        component: ComponentCreator('/cmfo-universe/docs', '1c7'),
        routes: [
          {
            path: '/cmfo-universe/docs',
            component: ComponentCreator('/cmfo-universe/docs', 'da1'),
            routes: [
              {
                path: '/cmfo-universe/docs/category/tutorial---basics',
                component: ComponentCreator('/cmfo-universe/docs/category/tutorial---basics', '195'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/cmfo-universe/docs/category/tutorial---extras',
                component: ComponentCreator('/cmfo-universe/docs/category/tutorial---extras', '5de'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/cmfo-universe/docs/intro',
                component: ComponentCreator('/cmfo-universe/docs/intro', '00f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/cmfo-universe/docs/tutorial-basics/congratulations',
                component: ComponentCreator('/cmfo-universe/docs/tutorial-basics/congratulations', '2b4'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/cmfo-universe/docs/tutorial-basics/create-a-blog-post',
                component: ComponentCreator('/cmfo-universe/docs/tutorial-basics/create-a-blog-post', '968'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/cmfo-universe/docs/tutorial-basics/create-a-document',
                component: ComponentCreator('/cmfo-universe/docs/tutorial-basics/create-a-document', 'c5b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/cmfo-universe/docs/tutorial-basics/create-a-page',
                component: ComponentCreator('/cmfo-universe/docs/tutorial-basics/create-a-page', '6f0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/cmfo-universe/docs/tutorial-basics/deploy-your-site',
                component: ComponentCreator('/cmfo-universe/docs/tutorial-basics/deploy-your-site', 'e2c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/cmfo-universe/docs/tutorial-basics/markdown-features',
                component: ComponentCreator('/cmfo-universe/docs/tutorial-basics/markdown-features', 'ee9'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/cmfo-universe/docs/tutorial-extras/manage-docs-versions',
                component: ComponentCreator('/cmfo-universe/docs/tutorial-extras/manage-docs-versions', '02b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/cmfo-universe/docs/tutorial-extras/translate-your-site',
                component: ComponentCreator('/cmfo-universe/docs/tutorial-extras/translate-your-site', '2ae'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/cmfo-universe/',
    component: ComponentCreator('/cmfo-universe/', 'bb4'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
