---
type: rule
title: Practices - Do you know to separate your Angular components into
  container and presentational?
uri: separate-your-angular-components-into-container-and-presentational
authors:
  - title: Duncan Hunter
    url: https://ssw.com.au/people/duncan-hunter
  - title: Gabriel George
    url: https://ssw.com.au/people/gabriel-george
related: []
redirects:
  - practices-do-you-know-to-separate-your-angular-components-into-container-and-presentational-components
created: 2017-01-03T16:52:00.000Z
archivedreason: null
guid: 8beefebf-8aef-4821-b965-16c4a9923443
---

There are 2 types of components 'dumb' and 'smart' components. Dumb components normally have no dependencies and no logic and just have @Input() and @Output(). Smart components are their parent components that would have multiple dependencies and logic but not necessarily an HTML template.

<!--endintro-->

Aiming to keep the components that display data 'dumb' makes them much easy to reuse in your application and less buggy, but many people do not like the terms smart and dumb components as a dumb component may just have less logic versus none. Many people and SSW included are preferring the terms container and presentational components for these reasons.

```js
company-list-table.component.ts @Component({
    selector: 'fbc-company-list-table',
    template: `
     <table id="company-list-table" class="table table-hover table-striped company-list-table-component">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Phone</th>
                    <th>Email</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
               <tr class="item" *ngFor="let company of companies">
                    <td>{{company.name}}</td>
                    <td>{{company.phone}}</td>
                    <td>{{company.email}}</td>
                    <td class="button-column">
                        <button routerLink="/company/detail/{{company.id}}" class="btn btn-default" >Details</button>
                        <button routerLink="/company/edit/{{company.id}}" class="btn btn-default" >Edit</button>
                        <button (click)="confirmDelete(company)" class="btn btn-default">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
    `
})
export class CompanyListTableComponent {
    @Input() companies: Company[];
    @Output() deleteCompanySelected = new EventEmitter<number>();
     
    confirmDelete(company: Company) {
        this.deleteCompanySelected.emit(company.id);
    }
}
```
::: good
Figure: Good example - A presentational component with no injected dependencies
:::
