getgenv().setting = {
    Fov = 25,
    Color = Color3.fromRGB(191, 255, 209),
    LockPlayers = true,
    LockPlayersBind = Enum.KeyCode.L,
    resetPlayersBind = Enum.KeyCode.P,
}
local Playersaimbot = nil
local mouse = game.Players.LocalPlayer:GetMouse()
local players = game:GetService("Players")
local localPlayer = players.LocalPlayer
local currentCamera = game:GetService("Workspace").CurrentCamera
spawn(function()
    while wait() do
        for _, v in pairs(players:GetPlayers()) do
            if v ~= localPlayer and v.Character and v.Character:FindFirstChild("HumanoidRootPart") then
                local pos = currentCamera:WorldToViewportPoint(v.Character.HumanoidRootPart.Position)
                local magnitude = (Vector2.new(pos.X, pos.Y) - Vector2.new(mouse.X, mouse.Y)).magnitude
                if magnitude < (getgenv().setting['Fov'] * 6 - 8) / 2 then
                    if (v.Character.HumanoidRootPart.Position - localPlayer.Character.HumanoidRootPart.Position).magnitude <= 1000 then
                        Playersaimbot = v.Name
                    end
                end
            end
        end
    end
end)
spawn(function()
    while wait() do
        for _, v in pairs(players:GetPlayers()) do
            if v.Name == Playersaimbot then
                PlayersPosition = v.Character.HumanoidRootPart.Position
            end
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