Get-Content 'inputs\input.txt' | ForEach-Object {
    @{
     'A X' = 3 + 1  # draw, rr
     'A Y' = 6 + 2  # win,  rp
     'A Z' = 0 + 3  # loss, rs
     'B X' = 0 + 1  # loss, pr
     'B Y' = 3 + 2  # draw, pp
     'B Z' = 6 + 3  # win,  ps
     'C X' = 6 + 1  # win,  sc
     'C Y' = 0 + 2  # loss, sp
     'C Z' = 3 + 3  # draw, ss
    }[$_]} | Measure-Object -sum

Get-Content 'inputs\input.txt' | ForEach-Object {
    @{
        'A Y' = 3 + 1
        'A X' = 0 + 3
        'A Z' = 6 + 2
        'B Y' = 3 + 2
        'B Z' = 6 + 3
        'B X' = 0 + 1
        'C Y' = 3 + 3
        'C Z' = 6 + 1
        'C X' = 0 + 2
    }[$_]} | Measure-Object -sum