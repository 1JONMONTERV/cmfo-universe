// docusaurus.config.js
// Configuración oficial del sitio CMFO–UNIVERSE v∞

module.exports = {
  title: 'CMFO–UNIVERSE v∞',
  tagline: 'Computación, Física y Lenguaje Unificados en un Autómata Fractal 7D',

  // URL base (GitHub Pages)
  url: 'https://1jonmonterv.github.io',
  baseUrl: '/cmfo-universe/',
  trailingSlash: false,

  organizationName: '1jonmonterv',
  projectName: 'cmfo-universe',
  deploymentBranch: 'gh-pages',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  favicon: 'img/favicon.ico',

  i18n: {
    defaultLocale: 'es',
    locales: ['es'],
  },

  presets: [
    [
      'classic',
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          routeBasePath: '/docs',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'CMFO–UNIVERSE v∞',
      logo: {
        alt: 'CMFO Logo',
        src: 'img/logo.svg',
      },
      items: [
        { to: '/docs/intro', label: 'Documentación', position: 'left' },
        {
          href: 'https://github.com/1jonmonterv/cmfo-universe',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },

    footer: {
      style: 'dark',
      copyright: `
        CMFO–UNIVERSE v∞ © ${new Date().getFullYear()} • Sistema Fractal Unificado
      `,
    },
  },
};
