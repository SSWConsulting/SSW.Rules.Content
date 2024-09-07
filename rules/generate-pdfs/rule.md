---
seoDescription: Learn how to generate PDFs for download using various .NET libraries and browser testing tools. From paid solutions like PDFTron and IronPDF to free options like Playwright, discover the pros and cons of each approach.
type: rule
title: Do you know how to generate PDFs for download?
uri: generate-pdfs
authors:
  - title: Alex Rothwell
    url: https://www.ssw.com.au/people/alex-rothwell
  - title: Chris Clement
    url: https://www.ssw.com.au/people/chris-clement
created: 2023-01-20T05:49:19.944Z
guid: ae1c8bfc-0adc-4066-a70e-30749f42a36d
---

Some projects call for being able to export data as a PDF. In these instances, it's great to be able to fully generate the file in the back-end and then provide it for download.

As with most software problems, there's many ways to achieve the same end result, each with their pros and cons.

<!--endintro-->

### Paid libraries

There are many paid .NET libraries available which can generate PDFs for you like:

- [PDFTron](https://www.pdftron.com)
- [Syncfusion](https://www.syncfusion.com/document-processing/pdf-framework/net-core/pdf-library)
- [IronPDF](https://ironpdf.com)

If the project has budget for a paid PDF solution, these are great and will get you generating PDFs quickly.

**Pros:**

✅ Mostly works out-of-the-box  
✅ Potential for commercial support from the library developer

**Cons:**

❌ Project might not have the budget for such an option  
❌ Is often closed source ([see more](/why-use-open-source))

### Free libraries

Unfortunately, the vast majority of libraries which can generate PDFs directly are paid. To get around this, the PDF generation function of a browser testing library can be used instead. Using this method, the desired content is rendered in a headless browser and that browser is then used to generate a PDF.

**Pros:**

✅ Free!  
✅ [Open source](/why-use-open-source)  
✅ Can easily reuse existing web layouts

**Cons:**

❌ Support is often limited  
❌ May require more configuration to get working

### Example

One library which makes this really easy (and is free!) is [Playwright](https://playwright.dev/dotnet).

Generating a PDF here takes just a few lines, see the [demo](https://try.playwright.tech/?e=generate-pdf) and [docs](https://playwright.dev/dotnet/docs/api/class-page#page-pdf) for more info.

```csharp
public async Task<byte[]> ExportView(string url, CancellationToken cancellationToken)
{
    var playwright = await Playwright.CreateAsync();
    var browser = await playwright.Chromium.LaunchAsync();
    var page = await browser.NewPageAsync();
    await page.GotoAsync(url);
    if (cancellationToken.IsCancellationRequested) { return Array.Empty<byte>(); }

    return await page.PdfAsync(new PagePdfOptions { Format = "A4" });
}
```

**Figure: A simple method to return a PDF using Playwright**
