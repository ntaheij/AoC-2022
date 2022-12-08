$puzzleInput = Get-Content -Path 'inputs\input.txt' | Select-Object -SkipLast 1

# Part 1
[string[]]$grid = $puzzleInput
[int]$visible = ($grid.Length * 2) + (($grid.count - 2) * 2)
$yMidCount = $grid.count - 2
$xMidLen = $grid.Length - 2
$yCount = $grid.count -1
$xLen = $grid.Length -1
for ($y=1; $y -le $yMidCount; $y++) {
    for ($x=1; $x -le $xMidLen; $x++) {
        $isVisible = $false
        switch ($grid[$y][$x]) {
            {($grid[$($y-1)..0] | ForEach-Object {$_[$x] -ge $grid[$y][$x]}) -notcontains $true} {$isVisible = $true;break}
            {($grid[$($y+1)..$yCount] | ForEach-Object {$_[$x] -ge $grid[$y][$x]}) -notcontains $true} {$isVisible = $true;break}
            {($grid[$y][$($x-1)..0] | ForEach-Object {$_ -ge $grid[$y][$x]}) -notcontains $true} {$isVisible = $true;break}
            {($grid[$y][$($x+1)..$xLen] | ForEach-Object {$_ -ge $grid[$y][$x]}) -notcontains $true} {$isVisible = $true;break}
        }
        if ($isVisible -eq $true) {$visible++}
    }
}
$visible

# Part 2
$scenicScore = @{}
for ($y=1; $y -le $yMidCount; $y++) {
    for ($x=1; $x -le $xMidLen; $x++) {
        $upScore = 0
        $downScore = 0
        $leftScore = 0
        $rightScore = 0

        # Check up
        $up = $y
        do {$upScore++;$up--}
        until (($grid[$up][$x] -ge $grid[$y][$x]) -or ($up -eq 0))

        # Check down
        $down = $y
        do {$downScore++;$down++}
        until (($grid[$down][$x] -ge $grid[$y][$x]) -or ($down -eq $yCount))

        # Check left
        $left = $x
        do {$leftScore++;$left--}
        until (($grid[$y][$left] -ge $grid[$y][$x]) -or ($left -eq 0))

        # Check right
        $right = $x
        do {$rightScore++;$right++}
        until (($grid[$y][$right] -ge $grid[$y][$x]) -or ($right -eq $xLen))
        $scenicScore["$y,$x"] = $upScore * $downScore * $leftScore * $rightScore
    }
}
$scenicScore.Values | Sort-Object | Select-Object -Last 1