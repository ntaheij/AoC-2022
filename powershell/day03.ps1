$puzzleInput = Get-Content -Path 'inputs\input.txt'
$alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
$prioSum = 0

function getPrio {
    param([string]$inputRucksack)
    $pos = 0
    $rucksackPrio = @()
    while($pos -lt ($inputRucksack.Length)){    
        $letter = $inputRucksack.Substring($pos,1)
        $prio = $alphabet.IndexOf($letter) + 1
        $rucksackPrio += $prio
        $pos += 1
    }
    return $rucksackPrio
}

#part one
foreach ($rucksack in $puzzleInput){
    $rucksackPrio = getPrio -inputRucksack $rucksack
    $compSize = ($rucksack.Length)/2
    $rucksackPrioComp1 = $rucksackPrio | select -First $compSize
    $rucksackPrioComp2 = $rucksackPrio | select -Last $compSize
    foreach ($item in $rucksackPrioComp1){
        if ($rucksackPrioComp2 -contains $item){
            $prioSum += $item
            break    
        }
    }
}

Write-host "Answer part 1:" $prioSum

$badgeSum = 0
$groupPos = 0
while ($groupPos -lt ($puzzleInput.Length)){
    $group = $puzzleInput | select -First 3 -Skip $groupPos 
    $rucksackPrio1 = $rucksackPrio = getPrio -inputRucksack $group[0]
    $rucksackPrio2 = $rucksackPrio = getPrio -inputRucksack $group[1]
    $rucksackPrio3 = $rucksackPrio = getPrio -inputRucksack $group[2]
    foreach ($prio in $rucksackPrio1){
        if(($rucksackPrio2 -contains $prio) -and ($rucksackPrio3 -contains $prio)){
            $badge = $prio
            break
        }
    }
    $badgeSum += $badge
    $groupPos += 3
}

Write-host "Answer part 2:" $badgeSum