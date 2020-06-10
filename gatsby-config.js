const siteConfig = require('./site-config');

require('dotenv').config({
  path: `.env.${process.env.NODE_ENV}`,
});

module.exports = {
  pathPrefix: '/rules',
  siteMetadata: {
    ...siteConfig,
  },
  plugins: [
    'gatsby-plugin-react-helmet',
    'gatsby-plugin-sitemap',
    'gatsby-transformer-json',
    'gatsby-plugin-postcss',
    {
      resolve: 'gatsby-source-git',
      options: {
        name: 'categories',
        remote: 'https://github.com/SSWConsulting/SSW.Rules.git',
        // Optionally supply a branch. If none supplied, you'll get the default branch.
        //53120-CreateIndexTemplate
        branch: 'content-migration-staging',
        // Tailor which files get imported eg. import the docs folder from a codebase.
        patterns: ['categories/**/*.md', 'rules/**/*'],
      },
    },
    {
      resolve: 'gatsby-plugin-breadcrumb',
      options: {
        useAutoGen: true,
        autoGenHomeLabel: 'Rules',
        useClassNames: true,
      },
    },
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        name: 'content',
        path: `${__dirname}/content`,
      },
    },
    { resolve: 'gatsby-transformer-remark' },
  ],
};
