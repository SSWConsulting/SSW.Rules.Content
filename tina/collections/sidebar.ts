import { Collection, Template } from "tinacms";

const ruleCountBlock: Template = {
    label: 'Rule Count',
    name: 'ruleCount',
    ui: {
        defaultItem: {
            label: 'SSW Rules'
        },
    }, 
    fields: [
        {
            type: 'string',
            name: 'label',
            label: 'Label',
            required: true
        }
    ]
}

const latestRulesBlock: Template = {
    label: 'Latest Rules',
    name: 'latestRules',
    ui: {
        defaultItem: {
            label: 'Latest Rules'
        },
        previewSrc: ''
    },
    fields: [
        {
            type: 'string',
            name: 'label',
            label: 'Label',
            required: true
        }
    ]
}

const historyOfRulesBlock: Template = {
    label: 'History of Rules',
    name: 'historyOfRules',
    ui: {
        defaultItem: {
            label: 'History of Rules',
            improveOurRulesQuoteBlock: {
                label: 'Help improve our Rules',
            }
        },
        previewSrc: ''
    },
    fields: [
        {
            type: 'string',
            name: 'label',
            label: 'Label',
            required: true
        },
        {
            type: 'rich-text',
            name: 'blurb',
            label: 'Blurb',
            required: true
        },
        {
            type: 'object',
            name: 'improveOurRulesQuoteBlock',
            label: 'Improve Our Rules',
            fields: [
                {
                    type: 'string',
                    name: 'label',
                    label: 'Label',
                    required: true
                },
                {
                    type: 'rich-text',
                    name: 'quote',
                    label: 'Quote',
                    required: true
                },
                {
                    type: 'image',
                    name: 'quoteAuthorImage',
                    label: 'Quote Author Image',
                    required: true
                },
                {
                    type: 'string',
                    name: 'quoteAuthorName',
                    label: 'Quote Author Name',
                    required: true
                },
                {
                    type: 'string',
                    name: 'quoteAuthorUrl',
                    label: 'Quote Author Url',
                    description: 'URL to the quote author\'s website/People Page',
                    required: true
                },
                {
                    type: 'string',
                    name: 'quoteAuthorTitle',
                    label: 'Quote Author Title',
                    required: true
                }
            ]
        }
    ]
}

const callToActionBlock: Template = {
    label: 'Call to Action',
    name: 'callToAction',
    ui: {
        previewSrc: ''
    },
    fields: [
        {
            type: 'string',
            name: 'label',
            label: 'Label',
            required: true
        },
       {
            type: 'rich-text',
            name: 'blurb',
            label: 'Blurb',
            required: true,
            templates: [
                {
                    name: 'button',
                    label: 'Button',
                    fields: [
                        {
                            type: 'string',
                            name: 'label',
                            label: 'Label',
                            required: true
                        },
                        {
                            type: 'string',
                            name: 'url',
                            label: 'URL',
                            required: true
                        }
                    ]
                }
            ]
       }
    ]
}

export const Sidebar: Collection = {
    label: 'Sidebar',
    name: 'sidebar',
    path: '/',
    format: 'json',
    match: {
        include: 'sidebar',
    },
    ui: {
        allowedActions: {
            create: false,
            delete: false,
        }
    },
    fields: [
        {
            type: 'object',
            list: true,
            name: 'blocks',
            label: 'Sidebar Blocks',
            templates: [
                ruleCountBlock,
                latestRulesBlock,
                historyOfRulesBlock,
                callToActionBlock
            ]
        }
    ]
};
