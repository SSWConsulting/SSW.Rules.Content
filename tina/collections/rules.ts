import { Collection, TinaField } from "tinacms";
import bodySchema from "../../schemas/bodySchema.json";


export const Rules: Collection = {
  label: 'Rules',
  name: 'rules',
  path: '/rules',
  format: 'md',
  fields: [
    {
      type: 'string',
      name: 'title',
      label: 'Title',
      required: true,
    },
    {
      type: 'string',
      name: 'uri',
      label: 'Uri',
      required: true,
    },
    {
      type: 'object',
      name: 'authors',
      label: 'Authors',
      list: true,
      fields: [
        {
          type: 'string',
          name: 'title',
          label: 'Name',
        },
        {
          type: 'string',
          name: 'url',
          label: 'Url',
        },
      ],
    },
    {
      type: 'string',
      label: 'Related Rules',
      name: 'related',
      list: true,
    },
    {
      type: 'string',
      name: 'redirects',
      label: 'Redirects',
      list: true,
    },
    {
      type: 'datetime',
      name: 'created',
      label: 'Created',
    },
    {
      type: 'string',
      name: 'archivedreason',
      label: 'Archived Reason',
    },
    {
      type: 'string',
      name: 'guid',
      label: 'Guid',
    },
    {
      type: 'string',
      name: 'seoDescription',
      label: 'SEO Description',
    },
    bodySchema as TinaField<false>
  ]
};