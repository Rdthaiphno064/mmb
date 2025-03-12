for _, v in ipairs(workspace:GetDescendants()) do
    pcall(function()
        if v:IsA("BasePart") or v:IsA("Decal") or v:IsA("Texture") then
            v.Transparency = 1
            v.Material = Enum.Material.SmoothPlastic
            v.CanCollide = false
        elseif v:IsA("ParticleEmitter") or v:IsA("Trail") or v:IsA("Fire") or v:IsA("Smoke") or v:IsA("Sparkles") then
            v:Destroy()
        end
    end)
end
for _, v in ipairs(getnilinstances()) do
    pcall(function()
        if v:IsA("BasePart") then
            v.Transparency = 1
            v.Material = Enum.Material.SmoothPlastic
            v.CanCollide = false
        elseif v:IsA("ParticleEmitter") or v:IsA("Trail") or v:IsA("Fire") or v:IsA("Smoke") or v:IsA("Sparkles") then
            v:Destroy()
        end
        for _, v1 in ipairs(v:GetDescendants()) do
            pcall(function()
                if v1:IsA("BasePart") then
                    v1.Transparency = 1
                    v1.Material = Enum.Material.SmoothPlastic
                    v1.CanCollide = false
                elseif v1:IsA("ParticleEmitter") or v1:IsA("Trail") or v1:IsA("Fire") or v1:IsA("Smoke") or v1:IsA("Sparkles") then
                    v1:Destroy()
                end
            end)
        end
    end)
end
workspace.DescendantAdded:Connect(function(v)
    pcall(function()
        if v:IsA("BasePart") or v:IsA("Decal") or v:IsA("Texture") then
            v.Transparency = 1
            v.Material = Enum.Material.SmoothPlastic
            v.CanCollide = false
        elseif v:IsA("ParticleEmitter") or v:IsA("Trail") or v:IsA("Fire") or v:IsA("Smoke") or v:IsA("Sparkles") then
            v:Destroy()
        end
    end)
end)
_G.Settings = {
    Players = {
        ["Ignore Me"] = true,
        ["Ignore Others"] = true,
        ["Ignore Tools"] = true
    },
    Meshes = {
        NoMesh = true,
        NoTexture = true,
        Destroy = true
    },
    Images = {
        Invisible = true,
        Destroy = true
    },
    Explosions = {
        Smaller = true,
        Invisible = true,
        Destroy = true
    },
    Particles = {
        Invisible = true,
        Destroy = true
    },
    TextLabels = {
        LowerQuality = true,
        Invisible = true,
        Destroy = true
    },
    MeshParts = {
        LowerQuality = true,
        Invisible = true,
        NoTexture = true,
        NoMesh = true,
        Destroy = true
    },
    Other = {
        ["FPS Cap"] = 60, 
        ["No Camera Effects"] = true,
        ["No Clothes"] = true,
        ["Low Water Graphics"] = true,
        ["No Shadows"] = true,
        ["Low Rendering"] = true,    
        ["Low Quality Parts"] = true,
        ["Low Quality Models"] = true,
        ["Reset Materials"] = true,
    }
}
for _, v in ipairs(game:GetService("Lighting"):GetChildren()) do
    pcall(function()
        v:Destroy()
    end)
end
game:GetService("Lighting").WaterWaveSize = 0
game:GetService("Lighting").WaterWaveSpeed = 0
game:GetService("Lighting").WaterReflectance = 0
game:GetService("Lighting").WaterTransparency = 1
game:GetService("Lighting").GlobalShadows = false
game:GetService("Lighting").FogEnd = 9e9
game:GetService("Lighting").Brightness = 0
