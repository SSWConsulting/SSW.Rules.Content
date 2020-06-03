---
type: rule
title: Do You Serialize View Models (aka DTOs), not Domain Entities?
uri: do-you-serialize-view-models-aka-dtos-not-domain-entities
created: 2019-03-05T19:04:34.0000000Z
authors:
- id: 34
  title: Brendan Richards

---



<span class='intro'> <p class="ssw15-rteElement-P">When building a simple API based on Entity Framework, It can be tempting to keep it simple and bind persistent entities directly to WebAPI output.<br></p> </span>

<dl class="badImage"><dt>​<img src="/PublishingImages/bad-webapi.png" alt="bad-webapi.png" /></dt><dd>Figure&#58; Bad Example -​ A naive&#160;WebAPI implementation</dd></dl><p>Although this code is very simple to write, there can be a number of potential problems&#58;<br></p><ul><li>All fields in the entity will be sent to the client. Often there can be for-internal-use-only fields in a domain entity / database table that you do not want sent to the client. Or the particular client use-case does not require the full set of fields<br></li><li>This might not a performant way of retrieving this data as, by default, the entity will be loaded into dbContext and change tracked. This tracking is unnecessary as the DbContext will be disposed when the request is finished<br></li><li>Often domain entities can have bidirectional navigation properties and these will fail to serialize to JSON<br></li><li>If your domain object contains computed properties, they get will be executed when serializing the object<br></li></ul><p>Update operations can be even more problematic&#58;</p><dl class="badImage"><dt> 
      <img src="/PublishingImages/bad-webapi-operation.png" alt="bad-webapi-operation.png" /> 
   </dt><dd>Figure&#58; Bad Example - A naive&#160;update operation</dd></dl><p>Consider the Product object that is received as a [FromBody] parameter by the action.</p><p class="ssw15-rteElement-P">At the start of the action this is not a persistent entity that has been loaded from the database and attached to a DBContext. Instead it is an entirely new object that has been created by the MVC databinding system.</p><div><p class="ssw15-rteElement-P">​The next call to the DbContext will take that object – exactly as received and de-serialized from the network – and attach it as-is to the DBContext in the “Modified” state, to be later saved by the call to SaveChangesAsync()<br></p><p>Any fields that did not survive the &quot;round-trip&quot; from the server -&gt; client-&gt; server will be overwritten / lost. The mapping from &quot;Object received from the web&quot; to &quot;Object saved&#160;into&#160;the database&quot; is entirely implicit here.</p><p>For all these reasons, the use of DTOs or View Models is highly recommended&#58;<br></p><p></p><ul><li>Complex domain objects can be simplified to contain only the exact set of fields required for a view<br></li><li>Aggregate models can be created that simplify the results from joining related domain objects<br></li><li>View Models can contain additional information or&#160;metadata&#160;required by the client such as value lookups<br></li><li>View&#160;models&#160;can be extended&#160;containing&#160;details specific to the current user context such as &quot;Does the current user have the required permissions to delete this item?&quot;<br></li><li>Update operations can become far more explicit<br></li><li>Validation rules can be written against the view model and for the specific context the view model exists for<br></li><li>Consider this to be a case where the Single Responsibility Principle (SRP) generally outweighs Don’t Repeat Yourself (DRY)<br></li><li>Read operations can be optimised by selecting from DBSets directly into view models<br></li></ul><dl class="goodImage"><dt>
         <img src="/PublishingImages/good-webapi-1.png" alt="good-webapi-1.png" /> 
      </dt><dt>
         <img src="/PublishingImages/good-webapi-2.png" alt="good-webapi-2.png" /> 
      </dt><dd>Figure&#58; Good Example - Update an Entity from a submitted View Model</dd></dl><p>This approach requires a bit more boiler-plate code as the fields to be updated are applied manually, but there is far less risk of unintended side effects.</p>As the complexity of the code increases, it will be much easier for developers to keep a clear distinction between ViewModel objects that were received from web requests, and persistent entities that came from Entity Framework.
   <dl class="goodImage"><dt> 
         <img src="/PublishingImages/good-webapi-operation-1.png" alt="good-webapi-operation-1.png" />​ 
      </dt><dt> 
         <img src="/PublishingImages/good-webapi-operation-2.png" alt="good-webapi-operation-2.png" /> 
      </dt><dd>Figure&#58; Good Example - A Read Operation that selects directly into a view model</dd></dl><p>For the above read, Entity Framework will execute an SQL select statement containing only the fields that have been projected via .Select() &#160;<br>This will also prevent change tracking on the source entity.</p><p>The above example also demonstrates how a projection / mapping from an entity to a view model can be reused by creating an Expression&lt;Func&lt;EntityType, ViewModelType&gt;&gt;<br><br></p></div>


