---
type: rule
title: Do you store your GitHub secrets in Azure KeyVault
uri: store-github-secrets-in-keyvault
authors:
  - title: Warwick Leahy
    url: ssw.com.au/people/warwick-leahy
created: 2022-10-27T21:38:53.087Z
guid: 6191828c-2049-46ef-93f8-d5eb90426d56
---
When creating pipelines for a company there is often secrets that need to be used by more than 1 repository.  This is something that GitHub can't do natively.  A developer is also unable to read the secrets in GitHub once they are entered.  Although this is for security a simple typo can't be found and instead the entire secret needs to be reentered. There is also no visible history for GitHub secrets and no ability to revert to an earlier version of a secret.
            
Solution - Store them in Azure KeyVault.
            
<!--endintro-->

## Create the KeyVaults
1. Create a separate Resource Group in Azure
2. Add 1 x shared KeyVault - These will store any values that would be the same no matter which environment you are deploying to.
3. Add 1 KeyVault for each environment you will deploy to - These are to store any values that are specific to the development environment (i.e. dev, staging, prod)

## Use the KeyVaults in your CICD pipeline
1. From YAML 
2. From Bicep
3. From PowerShell
