import { defineConfig } from "tinacms"
import { Rules } from "./collection/rule"

// Your hosting provider likely exposes this as an environment variable
const branch =
  process.env.CONTENT_BRANCH ||
  process.env.GITHUB_BRANCH ||
  process.env.VERCEL_GIT_COMMIT_REF ||
  process.env.HEAD ||
  "main"

export default defineConfig({
  // Required as per https://tina.io/docs/frameworks/gatsby/#workaround-for-graphql-mismatch-issue
  client: { skip: true },

  clientId: process.env.TINA_CLIENT_ID,
  token: process.env.TINA_TOKEN,
  localContentPath: "../../SSW.Rules.Content",

  branch: "tina/sample-content",

  build: {
    outputFolder: "admin",
    publicFolder: "static",
  },
  media: {
    tina: {
      mediaRoot: "",
      publicFolder: "static",
    },
  },
  // See docs on content modeling for more info on how to setup new content models: https://tina.io/docs/schema/
  schema: {
    collections: [Rules],
  },
})
