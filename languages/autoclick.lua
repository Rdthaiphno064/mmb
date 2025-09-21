local VirtualInputManager = game:GetService("VirtualInputManager")
local RunService = game:GetService("RunService")
local VP = game:GetService("Workspace").CurrentCamera.ViewportSize
while true do
    wait(1)
    VirtualInputManager:SendMouseButtonEvent(VP.X / 2, VP.Y / 2, 0, true, game, 1)
    VirtualInputManager:SendMouseButtonEvent(VP.X / 2, VP.Y / 2, 0, false, game, 1)
end
