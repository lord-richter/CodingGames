-- The while loop represents the game.
-- Each iteration represents a turn of the game
-- where you are given inputs (the heights of the mountains)
-- and where you have to print an output (the index of the mountain to fire on)
-- The inputs you are given are automatically updated according to your last actions.


-- game loop
while true do
    max = -1
    mountain = -1
    for i=0,8-1 do
        mountainH = tonumber(io.read()) -- represents the height of one mountain.
        if mountainH>max then
            max = mountainH
            mountain = i
        end
    end
    
    -- Write an action using print()
    -- To debug: io.stderr:write("Debug message\n")
    
    print(mountain) -- The index of the mountain to fire on.
end