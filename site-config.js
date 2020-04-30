/*eslint quotes: ["warn", "backtick"]*/
const path = require(`path`);

module.exports = {
  siteTitle: `SSW.People | Australia's Leading .NET and Azure Consultants`,
  siteTitleShort: `SSW.People | Australia's Leading .NET and Azure Consultants`,
  siteDescription:
    `We work together to form an amazing collective brain - SSW is made up of a great team of staff that are passionate about technology and how it meets business needs!` +
    `We're enthusiastic and have a "Make it happen" culture.`,
  siteUrl: `https://ssw.com.au/people`,
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
