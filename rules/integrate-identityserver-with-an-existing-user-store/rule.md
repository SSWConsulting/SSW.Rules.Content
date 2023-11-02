---
type: rule
title: Do you know how to migrate an existing user store to IdentityServer?
uri: migrate-an-existing-user-store-to-identityserver
authors:
  - title: "Dhruv Mathur "
    url: https://www.ssw.com.au/people/dhruv/
created: 2023-10-31T04:31:12.396Z
guid: 38a5988b-1740-4120-840d-116ad6e91566
---
When integrating an Identity Server with an existing ASP .NET Core application, challenges arise due to different user identification systems. 

On the Identity Server side, users are typically recognised by a unique SubId within their issued token after authentication. In contrast, an application's existing user store might use its own unique user ID, possibly combined with other data. 

The above discrepancy creates the need to effectively map or correlate the the user with SubId from the Identity Server to the corresponding user with user ID within the app's user store.

## Two essential scenarios arise when integrating the Identity Server:

### 1. Pre-existing Company Users

#### **Technical Integration & Benefits**

**Addressing users already registered with company emails in the existing application user store now authenticating through the Identity Server:**

* **SubId Check**:

  * Begin by verifying if the user has an external login associated with the SubId from the Identity Server in your application's user store. If found, proceed with authentication by handling the request gracefully.

```csharp
var existingUserByExternalLogin = await _userManager.FindByLoginAsync("IdentityServer", subId);
```

::: good
Figure: Retrieving existing user by using the associated external login provider info which in this case is IdentityServer.
:::

* **Existing Users by Email Verification**:

  * If there's no associated SubId, check if the email (provided by the Identity Server during authentication available as one of the claims in the JWT token) exists in your application's user store.

```csharp
var userByUserName = await _userManager.FindByEmailAsync(emailFromIdentityServer);
```

* For users known to your application but not authenticated via the Identity Server:

  * Retrieve the SubId from the Identity Server.
  * Use ASP .NET Core Identity's [`AddLoginAsync()`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.usermanager-1.addloginasync?view=aspnetcore-8.0)  method to associate this SubId as an external login with the user's record.


```chsarp
var subId = token.Claims.FirstOrDefault(c => c.Type == "sub");
await _userManager.AddLoginAsync(newUser, new UserLoginInfo("IdentityServer", subId));
```
* **Future Authentications**:

  * For all subsequent logins, employ the [`FindAsync(new UserLoginInfo())`](https://learn.microsoft.com/en-us/previous-versions/aspnet/dn497605(v=vs.108)) method.

**Benefits**: 

* Seamless authentication experience for existing users.
* Centralised and consistent handling of user identities using native ASP .NET Core Identity methods.
* Avoids custom fields in the ApplicationUser model, leveraging existing ASP .NET Identity Core methods like [`AddLoginAsync`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.usermanager-1.addloginasync?view=aspnetcore-8.0) and [`FindAsync`](https://learn.microsoft.com/en-us/previous-versions/aspnet/dn497605(v=vs.108)).

### 2. New Identity Server Registrants

#### **Technical Integration & Benefits**

**Incorporating users who are new to both the Identity Server and the application:**

* **Email Verification**:

  * Check if the email provided by the Identity Server during authentication exists in your application's user store by using ASP .NET Identity Core methods like [`FindByEmailAsync()`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.usermanager-1.findbyemailasync?view=aspnetcore-7.0).
  * If it doesn't, this indicates the user is new.

```csharp
  var existingUser = await _userManager.FindByEmailAsync(emailFromIdentityServer);
```

::: good
Figure: Good example - An example ASP .NET Core Idenitity code snippet demonstrating use of FindByEmailAsync method provided by the UserManager class. 
:::

* **User Creation & SubId Association**:

  * Register by creating a new user in your application's store using claims provided by the Identity Server (e.g., first name, last name, email).

```csharp
 var newUser = new Domain.Entities.ApplicationUser
 {
     UserName = token.Claims.FirstOrDefault(c => c.Type == "email");,
     FirstName = token.Claims.FirstOrDefault(c => c.Type == "first_name");,
     LastName = token.Claims.FirstOrDefault(c => c.Type == "given_name");,
     CreatedDateTime = DateTime.UtcNow,
     Culture = "en",
 };

 // Create new user in the database
 var createNewUserResult = await _userManager.CreateAsync(newUser);
```

::: greybox
Note: In the example above extraction of claims may vary based on how you access the token.
:::

* Extract the SubId from the JWT token (typically the "sub" claim) and use ASP .NET Core Identity's [`AddLoginAsync`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.usermanager-1.addloginasync?view=aspnetcore-8.0) method to associate this SubId as an external login with the newly created user record.

```chsarp
var subId = token.Claims.FirstOrDefault(c => c.Type == "sub");
await _userManager.AddLoginAsync(newUser, new UserLoginInfo("IdentityServer", subId));
```

::: greybox
Note: In the example above the "IdentityServer" should not be a magic string and has to be replaced by a constant.
:::

* **Future Authentications**:

  * For all subsequent logins to check if the user already exists, employ the [`FindByLoginAsync()`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.usermanager-1.findbyloginasync?view=aspnetcore-7.0) method.

```csharp
var existingUser = await _userManager.FindByLoginAsync("IdentityServer", subId));
```

**Benefits**:

* Facilitates the smooth inclusion of entirely new users to the ecosystem.
* Consistent user experience for new users, leveraging native ASP .NET Core Identity methods.
* Streamlined process, avoiding manual or ad-hoc registration steps.