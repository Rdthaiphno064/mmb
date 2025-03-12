local water = workspace.Map:FindFirstChild("WaterBase-Plane")
if water then
    water.CanCollide = true
    water.Anchored = true
    game:GetService("RunService").Stepped:Connect(function()
        water.Size = Vector3.new(1000, 112, 1000)
    end)
end