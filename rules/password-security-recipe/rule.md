---
type: rule
title: Do you know the recipe for secure passwords?
seoDescription: 
uri: password-security-recipe
authors:
  - title: Jeoffrey Fischer
    url: https://www.ssw.com.au/people/jeoffrey-fischer
  - title: Hajir Lesani
    url: https://www.ssw.com.au/people/hajir-lesani
related:
  - choosing-authentication
  - multi-factor-authentication-enabled
  - secure-password-share
  - password-complexities
created: 2025-10-10T22:40:45.273Z
guid: f89948bc-2338-4017-a915-bdcb1d15a036
---

Passwords are the keys to user accounts. Proper protection transforms them into a form that is useless to attackers, even if the database is compromised.
Here is a recipe to secure passwords using hash, salt, and pepper - the essential ingredients for keeping accounts safe.

`youtube: https://www.youtube.com/watch?v=--tnZMuoK3E`  
**Video: Password Hashing, Salts, Peppers | Explained! (4 min)**  

<!-- endintro -->

## Why are Passwords not safe enough?

Passwords alone are fragile ⛓️‍💥

Many people reuse passwords across multiple sites, so a single breach can have widespread consequences.  
Simple or common passwords are easy for attackers to guess, and stolen passwords can give direct access to user accounts.  

To protect accounts effectively, additional measures must be applied to make passwords resilient against attacks.  

## Ingredients 🥕

To build strong password security, the following components are essential:  

* A user **password** e.g., `apple123`
* A strong, slow **hashing** algorithm
* A unique, random **salt** per user  
* A secret **pepper** stored securely outside the database  

## Step 1: Hash 🔪

**What it does:** Turns a password into a secret code that cannot be reversed.

**Example:**

* Password: `apple123`
* Hash (bcrypt): `$2b$10$N9qo8uLOickgx2ZMRZoMyeIjefO6JaPDmvvse.lX5C6P3UnPxGRu`  

**✅ Why it's safer:**  

* Prevents direct access to the original password if the database is stolen.  
* Protects users from casual leaks or insider attacks.  

**❌ Remaining risks:**  

* Weak passwords can still be guessed using brute-force attacks.  
* Fast hash algorithms are vulnerable to modern cracking tools.  

::: info
**Note:** Use strong, adaptive hashing algorithms like [PBKDF2](https://cryptobook.nakov.com/mac-and-key-derivation/pbkdf2), [Argon2](https://argon2.online/), [bcrypt](https://bcrypt.online/) and [scrypt](https://www.browserling.com/tools/scrypt)  
:::

## Step 2: Add Salt 🧂

**What it does:** Adds a unique random value to each password before hashing.  

**Example:**

* Password: `apple123`  
* Salt: `blue`  
* Hash(password + salt): `$2b$10$KmH8vN3pQ9wR2sT5uV7xYzA1bC2dE3fG4hI5jK6lM7nO8pQ9rS0tU`

Another user with the same password:  

* Salt: `green`  
* Hash(password + salt): `$2b$10$ZxY9wV8uT7sR6qP5oN4mL3kJ2iH1gF0eD9cB8aZ7yX6wV5uT4sR3q`  

**✅ Why it's safer:**  

* Prevents attackers from noticing users with identical passwords.
* Makes precomputed attacks (“rainbow tables”) useless.

**❌ Remaining risks:**

* Weak passwords are still vulnerable to brute-force attacks.  
* Salts must be random and unique for each user.  

::: info
**Note:** Store the salt with the hash in the database (usually in the same record). It does not need to be secret.  
:::

## Step 3: Add Pepper 🌶️  

**What it does:** Adds a secret ingredient only the system knows, applied on top of the password + salt before hashing.  

**Example:**  

* Password: `apple123`  
* Salt: `blue`  
* Pepper (secret): `!@#secret`  
* Hash(password + salt + pepper): `$2b$10$FgH9iJ0kL1mN2oP3qR4sT5uV6wX7yZ8aB9cD0eF1gH2iJ3kL4mN5o`  

**✅ Why it's safer:**  

* Even if the database is stolen, attackers cannot recreate passwords without the pepper.  
* Acts as a “last line of defense” for stolen hashes.  

**❌ Remaining risks:**  

* If the pepper is leaked or stored insecurely, it loses its protection.  
* Weak passwords are still vulnerable to guessing attacks.  

::: info
**Note:** Keep the pepper secret and separate from the database (environment variables, secure vaults, etc.).  
:::

::: info
**Important:** Changing the pepper requires re-hashing all passwords, so it should be rarely changed and carefully managed.  
:::

## Step 4: Plating & Storage 🍽️

**✅ What to store:**  

* Final hash  
* Unique salt  

**❌ What NOT to store:**  

* Original password  
* Pepper  

Think of this step like plating your dish before serving - the “dish” (hash + salt) is safe to store and share, but the secret ingredients (pepper and original password) stay in the kitchen.  

## That's cool - what now? 🤔  

The good news is that many modern authentication frameworks and services already take care of hashing, salting, and sometimes even pepper for you. This means you don’t have to handle all the details yourself. Examples include:  

* **ASP.NET Core Identity** - hashes passwords with PBKDF2 and adds unique salts. Pepper can be added if desired.  
* **IdentityServer** - built on ASP.NET Core Identity, inherits secure password handling.  
* **Microsoft Entra ID / Azure AD** - cloud-managed hashing and salting; pepper is internally managed.  
* **Auth0 and Okta** - handle password hashing, salting, and secret management internally.  
* **Keycloak** - supports bcrypt, PBKDF2, or Argon2 with salts; pepper can be added via configuration.  

To learn more about those tools, see our rule: [Do you choose the best authentication method for every situation?](https://www.ssw.com.au/rules/choosing-authentication/)  

## Chef's note 🧑‍🍳

Hash, salt, and pepper create layers of protection - like a recipe with secret ingredients - making it much harder for attackers to steal passwords.  

The good news is that many modern authentication frameworks and services handle hashing, salting, and sometimes pepper automatically. This means you can rely on these tools to enforce strong password security without implementing every detail yourself.  

**But this doesn't mean easy or weak passwords are safe!** Combining these layers with strong password choices and Multi-Factor Authentication is what truly keeps user accounts secure - see our rule [Security - Do you have MFA (Multi-Factor Authentication) enabled?](https://www.ssw.com.au/rules/multi-factor-authentication-enabled/)
