---
type: rule
title: Do you know when to use value objects?
uri: do-you-know-when-to-use-value-objects
created: 2019-04-14T23:25:14.0000000Z
authors:
- id: 81
  title: Jason Taylor

---



<span class='intro'> <p class="ssw15-rteElement-P">When defining a domain, entities are created and consist of properties and methods. The properties represent the internal state of the entity and the methods are the actions that can be performed. The properties typically use primitive types such as strings, numbers, dates, and so on.​​<br></p> </span>

<p>As an example, consider an AD account. An AD Account consists of a domain name and user name, e.g. SSW\Jason. It is a string so using the 
   <strong>string</strong> type makes sense. Or does it?</p><dl class="badImage"><dt>
      <img src="/PublishingImages/when-use-value-bad.png" alt="when-use-value-bad.png" style="margin&#58;5px;" />
   </dt><dd>Figure&#58; Bad Example - Storing an AD Account as a String (AD Account is a complex type)</dd></dl><p>An AD Account is a complex type. Only certain strings are valid AD accounts. Sometimes you will want the string representation (SSW\Jason), sometimes you will need the domain name (SSW), and sometimes just the user name (Jason). All of this requires logic and validation, and the logic and validation cannot be provided by the string primitive type. Clearly, what is required is a more complex type such as a value object.</p><dl class="goodImage"><dt><img src="/PublishingImages/when-use-value-good.png" alt="when-use-value-good.png" />​<br></dt><dd>Figure&#58; Good Example - Storing an AD Account as a Value Object to Support Logic and Validation</dd></dl><p>The underlying implementation for the 
   <strong>AdAccount</strong> class is as follows&#58;</p><dl class="goodImage"><dt>
      <img src="/PublishingImages/when-use-value-good-2.png" alt="when-use-value-good-2.png" />
   </dt><dd>Figure&#58; Good Example - Implementation of the AdAccount Value Object Supports Logic and Validation</dd></dl><p>The 
   <strong>AdAccount</strong> type is based on the 
   <strong>ValueObject</strong> type, which you can view here; 
   <a href="https&#58;//github.com/SSWConsulting/NorthwindTraders/blob/master/Northwind.Domain/Infrastructure/ValueObject.cs">https&#58;//github.com/SSWConsulting/NorthwindTraders/blob/master/Northwind.Domain/Infrastructure/ValueObject.cs</a>. </p><p>Working with the AD accounts will now be easy. You can construct a new 
   <strong>AdAccount</strong> with the factory method 
   <strong>For </strong>as follows&#58;</p><dl class="image"><dt>
      <img src="/PublishingImages/when-use-value-eg-1.png" alt="when-use-value-eg-1.png" />
   </dt></dl><p>The factory method 
   <strong>For</strong> ensures only valid AD accounts can be constructed and for invalid AD account strings, exceptions are meaningful, i.e. 
   <strong>AdAccountInvalidException</strong> rather than 
   <strong>IndexOutOfRangeException</strong>.</p><p>Given an 
   <strong>AdAccount</strong> named account, you can access&#58;</p><ol><li>The domain name using; account.Domain</li><li>The user name using; account.Name</li><li>The full account name using; account.ToString()</li></ol><p>The value object also supports implicit and explicit conversion operators. You can&#58;<br></p><ol><li>Implicitly convert from 
      <strong>AdAccount</strong> to 
      <strong>string</strong> using; (string)account</li><li>Explicitly convert from 
      <strong>string </strong>to 
      <strong>AdAccount</strong> using; (AdAccount)&quot;SSW\\Jason&quot;</li></ol><p>If you're using Entity Framework Core, you should also configure the type as follows&#58;</p><dl class="image"><dt>
      <img src="/PublishingImages/when-use-value-eg-2.png" alt="when-use-value-eg-2.png" />
   </dt><dd>Figure&#58; Using Entity Framework Core to Configure Value Objects as Owned Entity Types</dd></dl><p>​With the above configuration in place, EF Core will name the database columns for the properties of the owned entity type as 
   <strong>AdAccount_Domain</strong> and 
   <strong>AdAccount_Name</strong>. You can learn more about 
   <a href="https&#58;//docs.microsoft.com/en-us/ef/core/modeling/owned-entities">Owned Entity Types</a> by reviewing the EF Core documentation.​<br></p><p>Next time you are building an entity, consider carefully if the type you are defining is a primitive type or a complex type. Primitive types work well for storing simple state such as first name or order count, complex types work best when defining types that include complex logic or validation such as postal or email addresses. Using a value object to encapsulate logic and validation will simplify your overall design.<br></p> 
<br>


