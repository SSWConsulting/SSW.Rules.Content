---
seoDescription: To avoid an embedded "Add", open a new window (popup) for entering data when using "Add New". This approach provides better user clarity and simplifies coding. It's essential to requery after saving changes, as seen in Outlook's "New" button example.
type: rule
archivedreason:
title: Do you avoid doing an embedded 'Add'?
guid: 331893f4-0eb8-4f47-8887-99ed75fcf24e
uri: do-you-avoid-doing-an-embedded-add
created: 2014-12-01T00:01:42.0000000Z
authors: []
related: []
redirects: []
---

For any case of 'Add New', choose to open a new window (popup) for entering data.

<!--endintro-->

![Figure: The 'Add New' button changes from a view into a data entry form](../../assets/EmbeddedAdd.jpg)

::: bad  
![Figure: Bad Example - The 'Add New' button, shown in Figure 1, opened the page in the same window](../../assets/BadEmbeddedAdd.jpg)  
:::

It is better to open in a new form, reasons being:

- It is better for the user in terms of clarity. The change of view to data entry form can be a surprise
- It is better to code e.g. if you are using this control in a couple of places you may need to show or hide 'Save' buttons etc. Otherwise, it is a pain to make it behave differently in different contexts.

However, you do need to call back on save and requery it.
Use a modal form and requery it (DON'T use JavaScript, instead use the Modal Popup Form Example)
An example of this is in Outlook with the 'New' button.

::: good  
![Figure: Good Example - the 'New' button in Outlook opens a new form for you to construct your email](../../assets/GoodEmbeddedAdd.jpg)  
:::

![Figure: Adding a table in SharePoint have a popup with dimmed background](../../assets/sharepoint-add-table.jpg)
