---
type: rule
title: Do you know how to migrate an existing user store to an ExternalAuthProvider?
uri: migrate-an-existing-user-store-to-an-externalauthprovider
authors:
  - title: "Dhruv Mathur"
    url: https://www.ssw.com.au/people/dhruv/
created: 2023-10-31T04:31:12.396Z
guid: 38a5988b-1740-4120-840d-116ad6e91566
redirects:
- integrate-identityserver-with-an-existing-user-store
- migrate-an-existing-user-store-to-an-externalauthprovider

---

When integrating an external authentication provider (IdentityServer, Azure AD or Microsoft Entra ID etc.) with an existing ASP .NET Core application which uses ASP .NET Core Identity, challenges arise due to different user identification systems.

On the ExternalAuthProvider side, users are typically recognised by a unique SubId within their issued token after authentication. In contrast, an application's existing user store might use its own unique user ID, possibly combined with other data.

The above discrepancy creates the need to effectively map or correlate the the user with SubId from the ExternalAuthProvider to the corresponding user with user ID within the app's user store.

Two essential scenarios arise when integrating the ExternalAuthProvider:

## 1. Pre-existing company users

Addressing users already registered with company emails in the existing application user store now authenticating through the ExternalAuthProvider:

#### SubId check

Begin by verifying if the user has an external login associated with the SubId from the ExternalAuthProvider in your application's user store using the [`FindByLoginAsync()`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.usermanager-1.findbyloginasync?view=aspnetcore-7.0) method. If found, proceed with authentication by handling the request gracefully.

```csharp
var existingUserByExternalLogin = await _userManager.FindByLoginAsync(EXTERNAL_AUTH_PROVIDER, subId);
```

#### Existing users by email verification

If there's no associated SubId, check if the email (provided by the ExternalAuthProvider during authentication available as one of the claims in the JWT token) exists in your application's user store.

```csharp
var userByUserName = await _userManager.FindByEmailAsync(emailFromIdentityServer);
```

::: good
Figure: Retrieving existing user by using the Email claim from the JWT token utilising the FindByEmailAsync() from the UserManager class.
:::

#### Users known to the application but not authenticated via ExternalAuthProvider

Retrieve the SubId from the JWT token provided by the ExternalAuthProvider. Use ASP .NET Core Identity's [`AddLoginAsync()`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.usermanager-1.addloginasync?view=aspnetcore-8.0)  method to associate this SubId as an external login with the user's record.

```csharp
var subId = token.Claims.FirstOrDefault(c => c.Type == "sub");
await _userManager.AddLoginAsync(newUser, new UserLoginInfo(EXTERNAL_AUTH_PROVIDER, subId));
```

::: greybox
**Note**: In the example above the "EXTERNAL\_AUTH\_PROVIDER" is a constant which contains the identifier for your external authentication provider. e.g. IDENTITY\_SERVER\_EXTERNAL\_LOGIN = "IdentityServer"
:::

#### Future Authentications

For all subsequent logins, employ the [`FindAsync(new UserLoginInfo())`](https://learn.microsoft.com/en-us/previous-versions/aspnet/dn497605(v=vs.108)) method.

### ✅ Benefits

* Seamless authentication experience for existing users
* Avoids custom fields in the ApplicationUser model, leveraging existing ASP .NET Identity Core methods like [`AddLoginAsync`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.usermanager-1.addloginasync?view=aspnetcore-8.0) and [`FindAsync`](https://learn.microsoft.com/en-us/previous-versions/aspnet/dn497605(v=vs.108))

## 2. New ExternalAuthProvider registrants

Incorporating users who are new to both the ExternalAuthProvider and the application:

#### Email verification

Check if the email provided by the ExternalAuthProvider during authentication exists in your application's user store by using ASP .NET Identity Core methods like [`FindByEmailAsync()`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.usermanager-1.findbyemailasync?view=aspnetcore-7.0). If it doesn't, this indicates the user is new.

```csharp
  var existingUser = await _userManager.FindByEmailAsync(emailFromIdentityServer);
```

#### User creation & SubId association

Register by creating a new user in your application's store using claims provided by the ExternalAuthProvider (e.g., first name, last name, email).

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
**Note**: In the example above extraction of claims may vary based on how you access the token.
:::

Extract the SubId from the JWT token (typically the "sub" claim) and use ASP .NET Core Identity's [`AddLoginAsync`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.usermanager-1.addloginasync?view=aspnetcore-8.0) method to associate this SubId as an external login with the newly created user record.

```csharp
var subId = token.Claims.FirstOrDefault(c => c.Type == "sub");
await _userManager.AddLoginAsync(newUser, new UserLoginInfo(EXTERNAL_AUTH_PROVIDER, subId));
```

#### Future Authentications

Finally for all subsequent logins use the [`FindByLoginAsync()`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.usermanager-1.findbyloginasync?view=aspnetcore-7.0) method to check if the user already exists.

```csharp
var existingUser = await _userManager.FindByLoginAsync(EXTERNAL_AUTH_PROVIDER, subId));
```

### ✅ Benefits

* Facilitates the seamless integration of new users to the ecosystem.
* Consistent user experience for new users, leveraging native ASP .NET Core Identity methods.
* Streamlined process, avoiding manual or ad-hoc registration steps.
