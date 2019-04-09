---
type: rule
title: Do you keep your domain layer independent of the data access concerns?
uri: do-you-keep-your-domain-layer-independent-of-the-data-access-concerns
created: 2019-04-09T23:15:40.0000000Z
authors:
- id: 81
  title: Jason Taylor

---



<span class='intro'> <p class="ssw15-rteElement-P">The domain layer should be independent of data access concerns. The domain layer should only change when something within the domain changes, not when the data access technology changes. Doing so ensures that the system will be easier to maintain well into the future, since changes to data access technologies won't impact the domain, and vice versa.</p><p class="ssw15-rteElement-P">This is often a problem when building systems that leverage Entity Framework, as it's common for data annotations to be added to the domain model. Data annotations, such as the Required or MinLength attributes, support validation and help Entity Framework to map objects into the relational model. In the next example, data annotations are used within the domain model&#58;<br></p> </span>

<dl class="badImage"><dt>​<img src="/PublishingImages/domain-layer-1.png" alt="domain-layer-1.png" /></dt><dd>Bad Example&#58; Domain is cluttered with data annotations</dd></dl><p>As you can see in the above example, the domain is cluttered with data annotations. If the data access technology changes, we will likely need to change all entities as all entities will have data annotations. In the following example, we will remove the data annotations from the entity and instead use a special configuration type&#58;</p><dl class="goodImage"><dt>
         <img src="/PublishingImages/domain-layer-2.png" alt="domain-layer-2.png" />
      </dt><dt>
         <img src="/PublishingImages/domain-layer-3.png" alt="domain-layer-3.png" />
      </dt><dd>Good Example&#58; Domain is lean, configuration for entity is contained within a separate configuration type</dd></dl><p>This is a big improvement! Now the customer entity is lean, and the configuration can be added to the persistence layer, completely separate of the domain. Now the domain is independent of data access concerns.</p><p>Learn more about this approach by reading about 
      <a href="https&#58;//docs.microsoft.com/en-us/ef/core/what-is-new/ef-core-2.0%22%20%5cl%20%22self-contained-type-configuration-for-code-first">self-contained configuration for code first</a>.​<br></p>


