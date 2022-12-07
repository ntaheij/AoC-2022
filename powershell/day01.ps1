$aInput = Get-Content "inputs\input.txt"
$aElves = @()
$iElvesId = 0
for($i = 0; $i -lt $aInput.Length; $i++){
    if($aInput[$i].Length -eq 0) {
        if($ob) {
            $aElves += $ob
            Remove-Variable ob
        }
        $iElvesId++
        $ob = New-Object psobject -Property @{
            Id = $iElvesId
            Calories = 0
        }
    }
    else {
        $ob.Calories += $aInput[$i]
    }
}

## PART 1
$aElves | Sort-Object -Property Calories -Descending | Select-Object -First 1

## PART 2
$bestElvesCalories = 0
$bestElves = $aElves | Sort-Object -Property Calories -Descending | Select-Object -First 3
foreach($elf in $bestElves) {
    $bestElvesCalories += $elf.Calories
}
$bestElvesCalories