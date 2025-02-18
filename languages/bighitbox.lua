local players = game:GetService("Players")
local localPlayer = players.LocalPlayer
local runService = game:GetService("RunService")
local enemyHitboxSize = 200
local myHitboxSize = 0.1
local function modifyHitbox(character, size, transparency)
    if character and character:IsA("Model") then
        local parts = {"HumanoidRootPart", "Head", "Torso", "UpperTorso", "LowerTorso","LeftLeg", "RightLeg", "LeftArm", "RightArm"}
        for _, partName in pairs(parts) do
            local part = character:FindFirstChild(partName)
            if part then
                part.Size = Vector3.new(size, size, size)
                part.Transparency = transparency
                part.BrickColor = BrickColor.new("Really black")
                part.Material = Enum.Material.Neon
                part.CanCollide = false
            end
        end
    end
end
local function updateHitboxes()
    for _, player in pairs(players:GetPlayers()) do
        if player.Character then
            if player == localPlayer then
                modifyHitbox(player.Character, myHitboxSize, 0.5)
            else
                modifyHitbox(player.Character, enemyHitboxSize, 0.9)
            end
        end
    end
end
runService.Stepped:Connect(updateHitboxes)
players.PlayerAdded:Connect(function(player)
    player.CharacterAdded:Connect(function(character)
        if player == localPlayer then
            modifyHitbox(character, myHitboxSize, 0.5)
        else
            modifyHitbox(character, enemyHitboxSize, 0.9)
        end
    end)
end)