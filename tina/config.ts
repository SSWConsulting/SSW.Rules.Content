import { defineConfig } from 'tinacms';
import { Rules } from './collections/rules';
import { Sidebar } from './collections/sidebar';

// Your hosting provider likely exposes this as an environment variable
const branch = process.env.TINA_CONTENT_BRANCH ?? 'main';
const localContentPath = process.env.LOCAL_CONTENT_RELATIVE_PATH ?? undefined;
const clientId = process.env.TINA_CLIENT_ID;
const token = process.env.TINA_TOKEN;
const basePath = process.env.TINA_BASE_PATH ?? undefined;

export default defineConfig({
  // Required as per https://tina.io/docs/frameworks/gatsby/#workaround-for-graphql-mismatch-issue
  client: { skip: true },
  clientId,
  token,

  branch,

  localContentPath,

  build: {
    basePath,
    outputFolder: 'admin',
    publicFolder: 'static',
  },
  media: {
    tina: {
      mediaRoot: '',
      publicFolder: 'static',
    },
  },
  // See docs on content modeling for more info on how to setup new content models: https://tina.io/docs/schema/
  schema: {
    collections: [Rules, Sidebar],
  },
});
