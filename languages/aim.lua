getgenv().setting = {
    LockPlayers = true,
    LockPlayersBind = Enum.KeyCode.L,
    resetPlayersBind = Enum.KeyCode.P,
}
local Playersaimbot = nil
local PlayersPosition = nil
local mouse = game.Players.LocalPlayer:GetMouse()
local players = game:GetService("Players")
local localPlayer = players.LocalPlayer
local currentCamera = game:GetService("Workspace").CurrentCamera
spawn(function()
    while wait() do
        local closest = nil
        local closestDist = math.huge

        for _, v in pairs(players:GetPlayers()) do
            if v ~= localPlayer and v.Character and v.Character:FindFirstChild("HumanoidRootPart") then
                local dist = (v.Character.HumanoidRootPart.Position - localPlayer.Character.HumanoidRootPart.Position).Magnitude
                if dist < closestDist then
                    closestDist = dist
                    closest = v
                end
            end
        end

        if closest then
            Playersaimbot = closest.Name
            PlayersPosition = closest.Character.HumanoidRootPart.Position
        end
    end
end)
spawn(function()
    local mt = getrawmetatable(game)
    local old = mt.__namecall
    setreadonly(mt, false)
    mt.__namecall = newcclosure(function(...)
        local method = getnamecallmethod()
        local args = {...}
        if tostring(method) == "FireServer" then
            if tostring(args[1]) == "RemoteEvent" then
                if tostring(args[2]) ~= "true" and tostring(args[2]) ~= "false" then
                    if Playersaimbot then
                        args[2] = PlayersPosition
                        return old(unpack(args))
                    end
                end
            end
        end
        return old(...)
    end)
end)
mouse.Button1Down:Connect(function()
    pcall(function()
        if Playersaimbot then
            local args = {
                [1] = PlayersPosition,
                [2] = players:FindFirstChild(Playersaimbot).Character.HumanoidRootPart
            }
            localPlayer.Character[localPlayer.Character:FindFirstChildOfClass("Tool").Name].RemoteFunctionShoot:InvokeServer(unpack(args))
        end
    end)
end)
