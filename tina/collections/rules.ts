import { Collection, TinaField } from "tinacms";
import bodySchema from "./schemas/bodySchema.json";


export const Rules: Collection = {
  label: 'Rules',
  name: 'rules',
  path: '/rules',
  format: 'md',
  defaultItem: () => {
    return {
      guid: generateGuid(),
      //TODO – remove the "created" field, as it may no longer be used
      //TECH DEBT – this may be outdated. See https://github.com/SSWConsulting/SSW.Rules/issues/1543.
      created: new Date().toISOString(),
      filename: 'rule',
    }
  },
  ui: {
    filename: {
      readonly: true,
    },
  },
  fields: [
    {
      type: 'string',
      name: 'title',
      label: 'Title',
      required: true,
      description: 'This is used as the major heading for the rule.',
    },
    {
      type: 'string',
      name: 'uri',
      label: 'Uri',
      description: 'The URI of the rule – this defines the slug and refereces.',
      required: true,
    },
    {
      type: 'object',
      name: 'authors',
      label: 'Authors',
      description: 'The list of contributors for this rule.',
      list: true,
      ui: {
        itemProps: (item) => {
          return { label: '👤 ' + (item?.title ?? "Author") };
        },
      },
      fields: [
        {
          type: 'string',
          name: 'title',
          description: 'The full name of the contributor, as it should appear on the rule.',
          label: 'Name',
        },
        {
          type: 'string',
          description: 'The SSW People link for the contributor – e.g. https://ssw.com.au/people/sebastien-boissiere',
          name: 'url',
          label: 'Url',
        },
      ],
    },
    {
      type: 'string',
      label: 'Related Rules',
      name: 'related',
      description: 'The URIs of rules that should be suggested based on the content of this rule.',
      list: true,
    },
    {
      type: 'string',
      name: 'redirects',
      label: 'Redirects',
      list: true,
    },
      //TODO – remove the "created" field, as it may no longer be used
      //TECH DEBT – this may be outdated. See https://github.com/SSWConsulting/SSW.Rules/issues/1543.
    {
      type: 'datetime',
      name: 'created',
      description: 'If you see this field, contact a dev immediately 😳 (should be a hidden field generated in the background).',
      label: 'Created',
      ui: {
        component: 'hidden',

      }
    },
    {
      type: 'string',
      name: 'archivedreason',
      label: 'Archived Reason',
      description: 'If this rule has been archived, summarise why here.',
    },
    {
      type: 'string',
      name: 'guid',
      label: 'Guid',
      description: 'If you see this field, contact a dev immediately 😳 (should be a hidden field generated in the background).',
      ui: {
        component: 'hidden',

      }
    },
    {
      type: 'string',
      name: 'seoDescription',
      label: 'SEO Description',
      description: 'A summary of the page content, used for SEO purposes. This can be generated automatically with AI.',

    },
    bodySchema as TinaField<false>
  ],
};
