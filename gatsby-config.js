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
        //branch: 'content-migration-staging',
        branch: 'FixImages',
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
    'gatsby-plugin-sharp',
    {
      resolve: 'gatsby-transformer-remark',
      options: {
        plugins: [
          {
            resolve: 'gatsby-remark-figure-caption',
          },
          // gatsby-remark-relative-images must
          // go before gatsby-remark-images
          {
            resolve: 'gatsby-remark-relative-images',
          },
          {
            resolve: 'gatsby-remark-images',
            options: {
              // It's important to specify the maxWidth (in pixels) of
              // the content container as this plugin uses this as the
              // base for generating different widths of each image.
              maxWidth: 590,
            },
          },
        ],
      },
    },
    'gatsby-source-local-git',
  ],
};
