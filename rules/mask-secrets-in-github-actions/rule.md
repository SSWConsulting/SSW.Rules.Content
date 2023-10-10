---
type: rule
title: Do you know how to mask secrets from GitHub Actions logs?
uri: mask-secrets-in-github-actions
authors:
  - title: Aman Kumar
    url: https://ssw.com.au/people/aman-kumar
related: []
created: 2023-10-10T10:33:21.000Z
guid: bcb27bdf-9553-48e1-9a36-45ac327bdd06

---

We often use third party secret stores (i.e Azure Key Vault) when adding secrets into our pipelines but do we know if we are injecting them securely into GitHub Actions?

<!--endintro-->


``` yaml
      
- name: keyVault - Secrets
        shell: pwsh
        id: KeyVaultSecrets
        run: |

        $GoogleRecaptchaSiteKey = (az keyvault secret show --name Google-Recaptcha-Site-KEY --vault-name ${{ env.KEY_VAULT}} --query value -o tsv)
        echo "GoogleRecaptchaSiteKey=$GoogleRecaptchaSiteKey" >> $env:GITHUB_OUTPUT

```
::: bad 
Figure: Bad example - We are injecting the secrets then outputting them in plain text
:::

In example above, secrets can be seen by anyone in the GitHub logs. Here is a more secure way by adding the `add-mask` workflow command:

``` yaml      
- name: keyVault - Secrets
        shell: pwsh
        id: KeyVaultSecrets
        run: |

        $GoogleRecaptchaSiteKey = (az keyvault secret show --name Google-Recaptcha-Site-KEY --vault-name ${{ env.KEY_VAULT}} --query value -o tsv)
        echo "::add-mask::$GoogleRecaptchaSiteKey"

        echo "GoogleRecaptchaSiteKey=$GoogleRecaptchaSiteKey" >> $env:GITHUB_OUTPUT

```
::: good 
Figure: Good example - We are masking the secrets and then outputting them
:::
