---
type: rule
title: Do you know how to mask secrets from GitHub Actions logs?
uri: mask-secrets-in-github-actions
authors:
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
  - title: Aman Kumar
    url: https://ssw.com.au/people/aman-kumar
related:
  - enterprise-secrets-in-pipelines
created: 2023-10-10T10:33:21.000Z
guid: bcb27bdf-9553-48e1-9a36-45ac327bdd06

---

When working with GitHub Actions, there are instances where we need to pull a secret value from a CLI tool and use it within our workflow. 

However, this practice can inadvertently expose the secret in the GitHub Actions logs if not handled securely. To prevent such exposure, it is crucial to redact the secret from the logs using the add-mask workflow command provided by GitHub.

This command ensures that the secret value is replaced with asterisks (****) in the logs, thereby preventing any unintended disclosure of the secret.

<!--endintro-->

**Example:**

Consider the scenario where we need to retrieve a secret from Azure Key Vault (there is no pre-built action to do this from Microsoft) and use it in our GitHub Actions workflow. In the following bad example, the secret is exposed in the logs:


``` yaml
      
- name: keyVault - Secrets
        shell: pwsh
        id: KeyVaultSecrets
        run: |

        $GoogleRecaptchaSiteKey = (az keyvault secret show --name Google-Recaptcha-Site-KEY --vault-name ${{ env.KEY_VAULT}} --query value -o tsv)
        echo "GoogleRecaptchaSiteKey=$GoogleRecaptchaSiteKey" >> $env:GITHUB_OUTPUT

```

<img width="791" alt="SecretsInPipelineWithoutMask" src="https://github.com/SSWConsulting/SSW.Rules.Content/assets/71385247/04f31744-08e4-4661-bb50-47e23e28a8dd">

::: bad 
Figure: Bad example - The secret is exposed in the GitHub logs
:::


``` yaml      
- name: keyVault - Secrets
        shell: pwsh
        id: KeyVaultSecrets
        run: |

        $GoogleRecaptchaSiteKey = (az keyvault secret show --name Google-Recaptcha-Site-KEY --vault-name ${{ env.KEY_VAULT}} --query value -o tsv)
        echo "::add-mask::$GoogleRecaptchaSiteKey"

        echo "GoogleRecaptchaSiteKey=$GoogleRecaptchaSiteKey" >> $env:GITHUB_OUTPUT

```
<img width="755" alt="SecretsInPipelineWithMask" src="https://github.com/SSWConsulting/SSW.Rules.Content/assets/71385247/23e5b399-d48c-4190-b1af-2060c16a9a11">

::: good 
Figure: Good example - We are masking the secrets and then outputting them
:::
