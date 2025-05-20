import { Collection } from "tinacms";

export function generateGuid() {
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) {
    var r = (Math.random() * 16) | 0,
      v = c == "x" ? r : (r & 0x3) | 0x8;
    return v.toString(16);
  });
}

const Category: Collection = {
  name: "category",
  label: "Categories",
  path: "/categories",
  format: "md",
  ui: {
    filename: {
      readonly: true,
      slugify: (values) => {
        if (values?._template === "top_category") {
          return "index";
        } else {
          return `${values?.title
            ?.toLowerCase()
            .trim()
            .replace(/ /g, "-")
            .replace("?", "")}`;
        }
      },
      description:
        'If it is the top level category, then the filename will be "index", otherwise the title will be used to create filename',
    },
  },
  templates: [
    {
      name: "top_category",
      label: "Top Level Category",
      fields: [
        {
          type: "string",
          label: "Title",
          name: "title",
          isTitle: true,
          required: true,
        },
        {
          type: "object",
          label: "Categories",
          name: "index",
          list: true,
          ui: {
            itemProps: (item) => {
              const name = item.category?.split("/");
              return {
                label: name
                  ? name[name.length - 1].split(".")[0]
                  : "Category is not selected",
              };
            },
          },
          fields: [
            {
              type: "reference",
              label: "Category",
              name: "category",
              collections: ["category"],
              ui: {
                optionComponent: (props: { name: string }, _internalSys) => {
                  return _internalSys.path;
                },
              },
            },
          ],
        },
      ],
    },

    {
      name: "category",
      label: "Category",
      ui: {
        defaultItem: () => {
          return {
            guid: generateGuid(),
          };
        },
      },
      fields: [
        {
          type: "string",
          label: "Title",
          name: "title",
          isTitle: true,
          required: true,
        },
        {
          type: "string",
          name: "guid",
          label: "Guid",
          description:
            "If you see this field, contact a dev immediately 😳 (should be a hidden field generated in the background).",
          ui: {
            component: "hidden",
          },
        },
        {
          type: "string",
          name: "consulting",
          label: "Consulting link",
          description: "Add Consulting link here",
        },
        {
          type: "string",
          name: "experts",
          label: "Experts link",
          description: "Add Experts link here",
        },
        {
          type: "string",
          name: "redirects",
          label: "Redirects",
          list: true,
        },
        {
          type: "object",
          label: "Rules",
          name: "index",
          list: true,
          ui: {
            itemProps: (item) => {
              const name = item.rule?.split("/");
              return {
                label: name
                  ? name[name.length - 1].split(".")[0]
                  : "Rule is not selected",
              };
            },
          },
          fields: [
            {
              type: "reference",
              label: "Rule",
              name: "rule",
              collections: ["rule"],
              ui: {
                optionComponent: (props: { name: string }, _internalSys) => {
                  return _internalSys.path;
                },
              },
            },
          ],
        },
        {
          type: "rich-text",
          name: "body",
          label: "Body",
          isBody: true,
          description: "This is description of the category",
        },
      ],
    },
  ],
};

export default Category;
