---
type: rule
tips: ""
title: Do you know when to use Reactive Forms vs Template-driven Forms in Angular?
seoDescription: Learn the key differences between Reactive Forms and
  Template-driven Forms in Angular. Discover when to use each approach, their
  pros and cons, and why Reactive Forms are the preferred choice for complex
  projects
uri: angular-reactive-forms-vs-template-driver-forms
authors:
  - title: Charles Vionnet
    url: https://www.ssw.com.au/people/charles-vionnet/
created: 2024-07-05T07:06:37.135Z
guid: 0643130f-a25d-41c3-bfc8-3d9029cf1244
---
Angular provides two approaches to building forms: Reactive Forms and Template-driven Forms. Understanding the differences between them can help you choose the right approach for your project.

<!--endintro-->

### Template-driven Forms
Template-driven Forms are easier to implement and work with, but at the cost of less flexibility and scalability. They are more suitable for simpler forms.

When to use Template-driven Forms:
- When the form logic is simple.
- When you prefer a less structured and more declarative approach.
- When you are working on a smaller project or a quick prototype.

```ts
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  standalone: true,
  selector: 'app-template-form',
  template: `
    <form #profileForm="ngForm" (ngSubmit)="onSubmit(profileForm)">
      <div>
        <label for="firstName">First Name:</label>
        <input id="firstName" name="firstName" [(ngModel)]="personalDetails.firstName" required />
        <div *ngIf="profileForm.controls['firstName']?.invalid && profileForm.controls['firstName']?.touched">
          First Name is required.
        </div>
      </div>

      <div>
        <label for="lastName">Last Name:</label>
        <input id="lastName" name="lastName" [(ngModel)]="personalDetails.lastName" required />
        <div *ngIf="profileForm.controls['lastName']?.invalid && profileForm.controls['lastName']?.touched">
          Last Name is required.
        </div>
      </div>

      <button type="submit" [disabled]="profileForm.invalid">Submit</button>
    </form>
  `,
  imports: [FormsModule],
})
export class TemplateFormComponent {
  personalDetails = {
    firstName: '',
    lastName: ''
  };

  onSubmit(form: any): void {
    if (form.valid) {
      console.log('Form Submitted', form.value);
    }
  }
}
```
**Figure: Template-driven Forms - Example of form implementation**

### Reactive Forms
Reactive Forms are the preferred approach for complex forms. They offer more control and flexibility in form validation and data handling, though they are more complex and verbose.

When to use Reactive Forms:
- When you need more complex form validation logic.
- When the form is dynamic (fields are added or removed at runtime).
- When you prefer a more structured and predictable approach to form handling.

```ts
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';

@Component({
  standalone: true,
  selector: 'app-reactive-form',
  template: `
    <form [formGroup]="profileForm" (ngSubmit)="onSubmit()">
      <div formGroupName="personalDetails">
        <label for="firstName">First Name:</label>
        <input id="firstName" formControlName="firstName" />
        <div *ngIf="profileForm.get('personalDetails.firstName')?.invalid && profileForm.get('personalDetails.firstName')?.touched">
          First Name is required.
        </div>

        <label for="lastName">Last Name:</label>
        <input id="lastName" formControlName="lastName" />
        <div *ngIf="profileForm.get('personalDetails.lastName')?.invalid && profileForm.get('personalDetails.lastName')?.touched">
          Last Name is required.
        </div>
      </div>

      <button type="submit" [disabled]="profileForm.invalid">Submit</button>
    </form>
  `,
  imports: [ReactiveFormsModule],
})
export class ReactiveFormComponent {
  profileForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.profileForm = this.fb.group({
      personalDetails: this.fb.group({
        firstName: ['', Validators.required],
        lastName: ['', Validators.required],
      }),
    });
  }

  onSubmit(): void {
    if (this.profileForm.valid) {
      console.log(this.profileForm.value);
    }
  }
}
```
**Figure: Reactive Forms - Example of form implementation**

### Which one should I use?
Choosing between Reactive Forms and Template-driven Forms depends on the complexity of your form. Reactive Forms offer more control and flexibility, making them ideal for complex scenarios, while Template-driven Forms provide a simpler and more declarative approach, suitable for straightforward forms.

At SSW, our projects are heavily relying on complex forms, and we encourage the usage of Reactive Forms.
