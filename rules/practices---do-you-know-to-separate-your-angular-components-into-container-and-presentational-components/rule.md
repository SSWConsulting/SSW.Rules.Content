---
type: rule
archivedreason: 
title: Practices - Do you know to separate your Angular components into container and presentational components?
guid: 8beefebf-8aef-4821-b965-16c4a9923443
uri: practices---do-you-know-to-separate-your-angular-components-into-container-and-presentational-components
created: 2017-01-03T16:52:00.0000000Z
authors:
- id: 44
  title: Duncan Hunter
- id: 72
  title: Gabriel George
related: []

---

There are two types of components 'dumb' and 'smart' components. Dumb components normally have no dependencies and no logic and just have @Input() and @Output(). Smart components are their parent components that would have multiple dependencies and logic but not necessarily an HTML template.

<!--endintro-->

Aiming to keep the components that display data 'dumb' makes them much easy to reuse in your application and less buggy, but many people do not like the terms smart and dumb components as a dumb component may just have less logic versus none. Many people and SSW included are preferring the terms container and presentational components for these reasons.

**company-list-table.component.ts** 
@Component({
    selector: 'fbc-company-list-table',
    template: `
     &lt;table id="company-list-table" class="table table-hover table-striped company-list-table-component"&gt;
            &lt;thead&gt;
                &lt;tr&gt;
                    &lt;th&gt;Name&lt;/th&gt;
                    &lt;th&gt;Phone&lt;/th&gt;
                    &lt;th&gt;Email&lt;/th&gt;
                    &lt;th&gt;&lt;/th&gt;
                &lt;/tr&gt;
            &lt;/thead&gt;
            &lt;tbody&gt;
               &lt;tr class="item" \*ngFor="let company of companies"&gt;
                    &lt;td&gt;{{company.name}}&lt;/td&gt;
                    &lt;td&gt;{{company.phone}}&lt;/td&gt;
                    &lt;td&gt;{{company.email}}&lt;/td&gt;
                    &lt;td class="button-column"&gt;
                        &lt;button routerLink="/company/detail/{{company.id}}" class="btn btn-default" &gt;Details&lt;/button&gt;
                        &lt;button routerLink="/company/edit/{{company.id}}" class="btn btn-default" &gt;Edit&lt;/button&gt;
                        &lt;button (click)="confirmDelete(company)" class="btn btn-default"&gt;Delete&lt;/button&gt;
                    &lt;/td&gt;
                &lt;/tr&gt;
            &lt;/tbody&gt;
        &lt;/table&gt;
    `
})
export class CompanyListTableComponent {
    @Input() companies: Company[];
    @Output() deleteCompanySelected = new EventEmitter&lt;number&gt;();
     
    confirmDelete(company: Company) {
        this.deleteCompanySelected.emit(company.id);
    }
}


::: good
Figure: Good example of a presentational component with no injected dependencies

:::
