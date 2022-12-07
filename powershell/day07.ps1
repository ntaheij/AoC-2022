# Part 1
$historyLines = Get-Content -Path 'inputs\input.txt' | Select -SkipLast 1
$structure = @{}
$structure.'/' = [System.Collections.Generic.List[object]]::New()
$pwd = '/'
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
            $pwd,$null = $pwd -split '\w+/$'
            break
        }
        '/' {
            $pwd = '/'
            break
        }
        '\w*' {
            $pwd = $pwd,$_,'/' -join ''
        }
    }
    # ls
    if ($null -ne $fileName) {
        $fileData = [pscustomobject]@{
            Directory = $pwd
            FileName = $fileName
            FileSize = $fileSize
        }
        if ($null -eq $structure["$pwd"]) {
            $structure.$pwd = [System.Collections.Generic.List[object]]::New()
        }
        ($structure.$pwd).Add($fileData)
        # Recursively add files to get lower folder sum
        if ($pwd -eq '/') {continue}
        $recursepwd = $pwd
        do {
            $recursepwd,$null = $recursepwd -split '\w+/$'
            if ($null -eq $structure["$recursepwd"]) {
                $structure.$recursepwd = [System.Collections.Generic.List[object]]::New()
            }
            ($structure.$recursepwd).Add($fileData)
        }
        until ($recursepwd -eq '/')
    }
}

# do sums
# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
$allPathSums = foreach ($key in $structure.keys) {
    ($structure.$key | Measure -Sum -Property fileSize).Sum
}
($allPathSums | Where {$_ -le 100000} | Measure -Sum).Sum

# Part 2
# you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space
[int]$totalUsed = ($structure.'/'.filesize | Measure -Sum).Sum
[int]$diffNeeded = 70000000 - $totalUsed
[int]$mustDelete = 30000000 - $diffNeeded
$allPathSums | Where {$_ -ge $mustDelete} | Sort | Select -First 1