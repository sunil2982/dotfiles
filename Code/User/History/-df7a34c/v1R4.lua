require "nvchad.mappings"

-- add yours here

local map = vim.keymap.set

map("n", ";", ":", { desc = "CMD enter command mode" })
map("i", "jk", "<ESC>")
-- Shift + Arrows selection for Normal Mode
vim.keymap.set('n', '<S-Up>', 'v<Up>', { desc = "Select up" })
vim.keymap.set('n', '<S-Down>', 'v<Down>', { desc = "Select down" })
vim.keymap.set('n', '<S-Left>', 'v<Left>', { desc = "Select left" })
vim.keymap.set('n', '<S-Right>', 'v<Right>', { desc = "Select right" })

-- Extend selection while already in Visual Mode
vim.keymap.set('v', '<S-Up>', '<Up>', { desc = "Extend selection up" })
vim.keymap.set('v', '<S-Down>', '<Down>', { desc = "Extend selection down" })
vim.keymap.set('v', '<S-Left>', '<Left>', { desc = "Extend selection left" })
vim.keymap.set('v', '<S-Right>', '<Right>', { desc = "Extend selection right" })

-- Shift + Arrows selection while typing in Insert Mode
vim.keymap.set('i', '<S-Up>', '<Esc>v<Up>', { desc = "Select up from insert" })
vim.keymap.set('i', '<S-Down>', '<Esc>v<Down>', { desc = "Select down from insert" })
vim.keymap.set('i', '<S-Left>', '<Esc>v<Left>', { desc = "Select left from insert" })
vim.keymap.set('i', '<S-Right>', '<Esc>v<Right>', { desc = "Select right from insert" })

-- map({ "n", "i", "v" }, "<C-s>", "<cmd> w <cr>")
