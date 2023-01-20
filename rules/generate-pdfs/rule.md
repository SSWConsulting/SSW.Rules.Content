---
type: rule
title: Do you know how to generate PDFs for download?
uri: generate-pdfs
authors:
  - title: Alex Rothwell
    url: https://www.ssw.com.au/people/alex-rothwell
created: 2023-01-20T05:49:19.944Z
guid: ae1c8bfc-0adc-4066-a70e-30749f42a36d
---
Some projects call for being able to export data as a PDF. In these instances, it's great to be able to fully generate the file in the back-end and then provide it for download

As with most software problems, there's many ways to achieve the same end result, each with their pros and cons        

<!--endintro-->

## Paid Libraries

There are many paid .NET libraries available which can generate PDFs for you like [PDFTron](https://www.pdftron.com/), [Syncfusion](https://www.syncfusion.com/document-processing/pdf-framework/net-core/pdf-library) and [IronPDF](https://ironpdf.com/).
If the project has budget for a paid PDF solution, these are great and will get you generating PDFs quickly.

## Free Libraries

An alternative method is to render the desired content in a headless browser and use that browser to generate a PDF.
One library which makes this really easy (and is free!) is [Playwright](https://playwright.dev/dotnet/).

```csharp
using Microsoft.Playwright;
using System.Threading.Tasks;

class Program
{
    public static async Task Main()
    {
        using var playwright = await Playwright.CreateAsync();
        await using var browser = await playwright.Chromium.LaunchAsync();
        var page = await browser.NewPageAsync();
        await page.GotoAsync("https://github.com/microsoft/playwright");
        await page.PdfAsync(new PagePdfOptions { Path = "page.pdf" });
    }
}
```