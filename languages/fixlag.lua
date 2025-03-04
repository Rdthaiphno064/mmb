game:GetService("RunService"):Set3dRenderingEnabled(false)
setfpscap(10)
for i,v in next, workspace:GetDescendants() do
    pcall(function()
        v.Transparency = 1
    end)
end
for i,v in next, getnilinstances() do
    pcall(function()
        v.Transparency = 1
        for i1,v1 in next, v:GetDescendants() do
            v1.Transparency = 1
        end
    end)
end
a = workspace
a.DescendantAdded:Connect(function(v)
    pcall(function()
        v.Transparency = 1
    end)
end)
for _, v in pairs(game:GetDescendants()) do
    if v:IsA("Sound") then
        v.Volume = 0
    end
end
game.DescendantAdded:Connect(function(v)
    if v:IsA("Sound") then
        v.Volume = 0
    end
end)
