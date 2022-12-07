$data = Get-Content -Path 'inputs\input.txt'

$score = 0
$data | ForEach-Object {
    # Write-Host "*********************"
    $left = $_.Split(',')[0]
    $leftStart = [int]$left.Split('-')[0]
    $leftEnd = [int]$left.Split('-')[1]
    # Write-Host "Left " $left #"     " $leftStart $leftEnd

    $right = $_.Split(',')[1]
    $rightStart = [int]$right.Split('-')[0]
    $rightEnd = [int]$right.Split('-')[1]
    # Write-Host "Right" $right #"     " $rightStart $rightEnd

    if (($leftStart -ge $rightStart) -and ($leftStart -le $rightEnd)) {
        $score++
        # Write-Host "============ L in R $score"
    }
    elseif (($rightStart -ge $leftStart) -and ($rightStart -le $leftEnd)) {
        $score++
        # Write-Host "============ R in L $score"
    }
}
Write-Host " There were $score matches."