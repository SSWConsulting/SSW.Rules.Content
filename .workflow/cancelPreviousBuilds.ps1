# Check environment variables exist
if ([string]::IsNullOrEmpty(($env:CANCEL_BUILD_USER)) -or [string]::IsNullOrEmpty(($env:CANCEL_BUILD_TOKEN))) {
    throw "Missing user environment variables"
    exit
}
if ([string]::IsNullOrEmpty(($env:CANCEL_BUILD_URL))) {
    throw "Missing project URL environment variables"
    exit
}

# Generate request header with auth
$creds = "$($env:CANCEL_BUILD_USER):$($env:CANCEL_BUILD_TOKEN)"
$encodedCreds = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($creds))
$basicAuthValue = "Basic $encodedCreds"
$Headers = @{
    Authorization = $basicAuthValue
}

$buildsUrl = $env:CANCEL_BUILD_URL

# Get existing builds that are in progress or haven't started
$builds = Invoke-RestMethod -Uri $buildsUrl -Method Get -Header $Headers
$buildsToStop = $builds.value.Where( { ($_.definition.name -eq "Production") -and ((($_.status -eq 'inProgress') -or ($_.status -eq 'notStarted')) -and ([string]::IsNullOrEmpty(($_.triggerInfo)))) })

$count = ($buildsToStop).count
Write-Host "Builds to cancel:"
Write-Host $count

# Cancel each exisiting build
ForEach ($build in $buildsToStop) {
    $build.status = "Cancelling"
    $body = $build | ConvertTo-Json -Depth 10
    $urlToCancel = "$($buildsUrl)/$($build.id)?api-version=5.0"
    Invoke-RestMethod -Uri $urlToCancel -Method Patch -ContentType application/json -Body $body -Header $Headers
}
