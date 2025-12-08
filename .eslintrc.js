module.exports = {
    root: true,
    plugins: ["mdx", "react"],
    overrides: [
      {
        files: ["**/*.mdx"],
        parser: "eslint-mdx",
        extends: [
          "plugin:mdx/recommended",
        ],
        parserOptions: {
          ecmaVersion: 2020,
          sourceType: "module",
          ecmaFeatures: { jsx: true }
        },
        rules: {
          "mdx/remark": [
            "warn",
            {
              plugins: [
                ["lint-heading-style", "atx"],              // MD003
                ["lint-list-item-bullet-style", "asterisk"],// MD004
                ["lint-code-block-style", false],           // MD046
                ["lint-line-length", false],                // MD013
                ["lint-inline-html", false],                // MD033
                ["lint-code-blocks", false],                // MD036
                ["lint-no-html", false],                    // MD055
                ["lint-no-duplicate-heading", false]        // MD024
              ]
            }
          ],

          "react/jsx-no-undef": "off",
          "react/jsx-uses-vars": "warn",
          "react/self-closing-comp": "warn",
          "react/jsx-no-comment-textnodes": "warn",
        }
      }
    ]
};