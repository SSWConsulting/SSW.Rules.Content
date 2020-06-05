/*eslint quotes: ["warn", "backtick"]*/
const path = require(`path`);

module.exports = {
  siteTitle: `SSW.Rules`,
  siteTitleShort: `SSW.Rules`,
  siteDescription: ``,
  siteUrl: `https://ssw.com.au/rules`,
  themeColor: `#cc4141`,
  backgroundColor: `#fff`,
  pathPrefix: null,
  logo: path.resolve(__dirname, `src/images/icon.png`),
  social: {
    twitter: `SSW_TV`,
    fbAppId: `120920301257947`,
  },
  parentSiteUrl: `https://ssw.com.au`,
};
