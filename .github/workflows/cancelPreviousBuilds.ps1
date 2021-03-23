if(($args).Count -eq 0) {
    Write-Host "Missing args"
    exit
}

$pair = "$($args[0]):$($args[1])"

$encodedCreds = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($pair))

$basicAuthValue = "Basic $encodedCreds"

$Headers = @{
    Authorization = $basicAuthValue
}

$buildsUrl = $args[2]
$builds = Invoke-RestMethod -Uri $buildsUrl -Method Get -Header $Headers
$buildsToStop = $builds.value.Where( { (($_.status -eq 'inProgress') -or ($_.status -eq 'notStarted')) -and ([string]::IsNullOrEmpty(($_.triggerInfo)))})
$count = ($buildsToStop).count
Write-Host "Builds to cancel:"
Write-Host $count
ForEach ($build in $buildsToStop) {
    $build.status = "Cancelling"
    $body = $build | ConvertTo-Json -Depth 10
    $urlToCancel = "$($args[2])$($build.id)?api-version=5.0"
    Invoke-RestMethod -Uri $urlToCancel -Method Patch -ContentType application/json -Body $body -Header $Headers
}