import { Collection } from "tinacms";
import { embedTemplates } from "@/components/embeds";
import { generateGuid } from "@/utils/guidGenerationUtils";

export const Rules: Collection = {
  name: "rule",
  label: "Rules",
  path: "/rules",
  format: "md",
  defaultItem() {
    return {
      guid: generateGuid(),
      filename: "rule",
    };
  },
  ui: {
    filename: {
      readonly: true,
    },
  },
  fields: [
    {
      type: "string",
      name: "title",
      label: "Title",
      required: true,
    },
    {
      type: "string",
      name: "uri",
      label: "Uri",
      required: true,
    },
    {
      type: "object",
      name: "authors",
      label: "Authors",
      description: "The list of contributors for this rule.",
      list: true,
      ui: {
        itemProps: (item) => {
          return { label: "👤 " + (item?.title ?? "Author") };
        },
      },
      fields: [
        {
          type: "string",
          name: "title",
          description:
            "The full name of the contributor, as it should appear on the rule.",
          label: "Name",
        },
        {
          type: "string",
          description:
            "The SSW People link for the contributor - e.g. https://ssw.com.au/people/sebastien-boissiere",
          name: "url",
          label: "Url",
        },
      ],
    },
    {
      type: "string",
      label: "Related Rules",
      name: "related",
      list: true,
    },
    {
      type: "string",
      name: "redirects",
      label: "Redirects",
      list: true,
    },
    {
      type: "datetime",
      name: "created",
      label: "Created",
    },
    {
      type: "string",
      name: "archivedreason",
      label: "Archived Reason",
    },
    {
      type: "string",
      name: "guid",
      label: "Guid",
    },
    {
      type: "string",
      name: "seoDescription",
      label: "SEO Description",
    },
    {
      type: "rich-text",
      name: "body",
      label: "Body",
      isBody: true,
      templates: embedTemplates,
    },
  ],
};
