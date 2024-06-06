#! /bin/bash
#
# CMD:
#   $1. GitHub access token 

github_org_name=sswconsulting
github_repo_name=SSW.Rules
azdo_org_name=https://ssw.visualstudio.com
azdo_project_name=ssw.rules
azdo_pipeline_name=Production
azdo_history_pipeline_name=UpdateRulesHistory
github_access_token=$1

# exit when any command fails
set -e

# ensure devops extension is available
az extension add -n azure-devops

echo "Querying GitHub..."

# Get release/x branch with the latest commit.
res=$(curl -X POST \
  https://api.github.com/graphql \
  -H "Authorization: Bearer ${github_access_token}" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "query": "{
    repository(owner: \"${github_org_name}\", name: \"${github_repo_name}\") {
      refs(
        refPrefix: \"refs/heads/release/\"
        first: 1
        orderBy: {field: TAG_COMMIT_DATE, direction: DESC}
      ) {
        edges {
          node {
            name
            target {
              ... on Commit {
                committedDate
              }
            }
          }
        }
      }
    }
  }"
}
EOF
)

# Check for cURL errors.
if [ $? -ne 0 ]; then
  echo "::error cURL request failed. Check your internet connection or GitHub API status."
  exit 1
fi

# Check if the response contains an error message.
if [ "$(jq -r '.errors' <<< "$res")" != "null" ]; then
  echo "GitHub API error: $(jq -r '.errors[0].message' <<< "$res")"
  echo "Documentation URL: $(jq -r '.errors[0].documentation_url' <<< "$res")"
  exit 1
fi

latest_release=$(jq -r '.data.repository.refs.edges[0].node.name' <<< "${res}")
latest_branch="release/${latest_release}"

# Check if latest_release is null.
if [ "$latest_release" = "null" ]; then
  echo "::error Latest branch is null. No matching release branches found."
  exit 1
fi

echo "Latest release branch: ${latest_branch}"

echo triggering AzDO update history
az pipelines build queue --org $azdo_org_name --project $azdo_project_name --definition-name $azdo_history_pipeline_name --branch main

echo triggering AzDO build
az pipelines build queue --org $azdo_org_name --project $azdo_project_name --definition-name $azdo_pipeline_name --branch $latest_branch

echo done
