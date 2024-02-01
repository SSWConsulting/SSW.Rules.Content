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
  - title: Chris Clement
    url: https://www.ssw.com.au/people/chris-clement/
related: []
redirects:
  - practices-do-you-know-to-separate-your-angular-components-into-container-and-presentational-components
created: 2017-01-03T16:52:00.000Z
archivedreason: null
guid: 8beefebf-8aef-4821-b965-16c4a9923443
---
There are 2 general types of components according its complexity: presentational and smart components. Presentational component is a component that is purely driven by its input data. Smart component on the other hand, is more complex - it can have business logic, dependencies, and also store its own state.



<!--endintro-->

Aiming to have more presentational components makes building applications easier; it provides high reusability, and they are easier to debug since they have the same output for the same input.

Smart components are harder to debug since they now have dependencies and state that need to be taken into account when debugging.



```typescript
// company-list-table.component.ts

@Component({
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