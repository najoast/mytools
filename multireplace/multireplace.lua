
-- 把输入的文件，根据词典替换文本
--[[
SIMIC	CMake
开元	开源
魔术	魔兽
Mac口	MySQL
Mexico	MySQL
第一微	dev
播放	不放
bill的	build
SUDO	sudo
CHOWN	chown
和数	核数
变音器	编译器
现成	线程
全站	全栈
]]
local dict = {
	["SIMIC"] = "cmake",
	["SIMI可"] = "cmake",
	["开元"] = "开源",
	["魔术"] = "魔兽",
	["Mac口"] = "MySQL",
	["Mexico"] = "MySQL",
	["第一微"] = "dev",
	["播放"] = "不放",
	["bill的"] = "build",
	["SUDO"] = "sudo",
	["CHOWN"] = "chown",
	["和数"] = "核数",
	["变音器"] = "编译器",
	["现成"] = "线程",
	["全站"] = "全栈",
	["folk"] = "fork",
	["收口"] = "SQL",
	["circle"] = "sql",
	["s l n"] = "sln",
	["Reno的"] = "reload",
	["变异"] = "编译",
}

local function replace_line(line)
	for k, v in pairs(dict) do
		line = string.gsub(line, k, v)
	end
	return line
end

local function replace_file(file)
	local f = io.open(file, "r")
	local lines = {}
	for line in f:lines() do
		line = replace_line(line)
		table.insert(lines, line)
	end
	f:close()

	f = io.open(file, "w")
	for _, line in ipairs(lines) do
		f:write(line, "\n")
	end
	f:close()
end

local fileName = ...

replace_file(fileName)