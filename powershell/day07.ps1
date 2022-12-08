# Part 1
$historyLines = Get-Content -Path 'inputs\input.txt' | Select-Object -SkipLast 1
$structure = @{}
$structure.'/' = [System.Collections.Generic.List[object]]::New()
$currentPwd = '/'
foreach ($line in $historyLines) {
    $cmd,$operation,$dirLine,$fileName,$fileSize = $null
    switch -Regex ($line) {
        '^\$\scd\s(?<operation>.*)$' {
            $operation = $matches.operation
            break
        }
        '^(\$\sls|dir\s.*)$' {
            break
        }
        '^(?<fileSize>\d+)\s(?<fileName>.+)$' {
            [string]$fileName = $matches.fileName
            [int]$fileSize = $matches.fileSize
        }
        default { 
            #debugging..
        }
    }
    # change directory
    switch -Regex ($operation) {
        $null  {break}
        '\.\.' {
            $currentPwd,$null = $currentPwd -split '\w+/$'
            break
        }
        '/' {
            $currentPwd = '/'
            break
        }
        '\w*' {
            $currentPwd = $currentPwd,$_,'/' -join ''
        }
    }
    # ls
    if ($null -ne $fileName) {
        $fileData = [pscustomobject]@{
            Directory = $currentPwd
            FileName = $fileName
            FileSize = $fileSize
        }
        if ($null -eq $structure["$currentPwd"]) {
            $structure.$currentPwd = [System.Collections.Generic.List[object]]::New()
        }
        ($structure.$currentPwd).Add($fileData)
        # Recursively add files to get lower folder sum
        if ($currentPwd -eq '/') {continue}
        $recursecurrentPwd = $currentPwd
        do {
            $recursecurrentPwd,$null = $recursecurrentPwd -split '\w+/$'
            if ($null -eq $structure["$recursecurrentPwd"]) {
                $structure.$recursecurrentPwd = [System.Collections.Generic.List[object]]::New()
            }
            ($structure.$recursecurrentPwd).Add($fileData)
        }
        until ($recursecurrentPwd -eq '/')
    }
}

# do sums
# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
$allPathSums = foreach ($key in $structure.keys) {
    ($structure.$key | Measure-Object -Sum -Property fileSize).Sum
}
($allPathSums | Where-Object {$_ -le 100000} | Measure-Object -Sum).Sum

# Part 2
# you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space
[int]$totalUsed = ($structure.'/'.filesize | Measure-Object -Sum).Sum
[int]$diffNeeded = 70000000 - $totalUsed
[int]$mustDelete = 30000000 - $diffNeeded
$allPathSums | Where-Object {$_ -ge $mustDelete} | Sort-Object | Select-Object -First 1