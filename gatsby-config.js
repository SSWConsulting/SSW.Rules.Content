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
    resolve: 'gatsby-plugin-breadcrumb',
    options: {
      useAutoGen: true,
      autoGenHomeLabel: 'Rules',
      useClassNames: true,
    },
  }],
}
