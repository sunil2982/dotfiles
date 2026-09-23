return {
  -- Modern Nevovim 0.11+ LSP setup
  {
    "neovim/nvim-lspconfig",
    config = function()
      -- Configure Pyright using core vim.lsp.config
      vim.lsp.config("pyright", {
        settings = {
          python = {
            analysis = {
              typeCheckingMode = "basic",
              autoSearchPaths = true,
              useLibraryCodeForTypes = true,
            },
          },
        },
      })

      -- Configure Ruff using core vim.lsp.config
      vim.lsp.config("ruff", {})

      -- Enable the language servers so they automatically attach to matching filetypes
      vim.lsp.enable("pyright")
      vim.lsp.enable("ruff")
    end,
  },

  -- Automatically install LSPs and formatters via Mason
  {
    "williamboman/mason.nvim",
    opts = {
      ensure_installed = {
        "pyright",   -- Python Language Server
        "ruff",      -- Extremely fast Python linter & formatter
        "black",     -- Python formatter alternative
      },
    },
  },
  
  -- Auto-formatting plugin setup
  {
    "stevearc/conform.nvim",
    event = 'BufWritePre', -- format on save
    opts = {
      formatters_by_ft = {
        python = { "ruff_format", "black" },
      },
    },
  },
  {
    "nvim-tree/nvim-tree.lua",
    opts = function()
      local opts = require "nvchad.configs.nvimtree"
      opts.view.side = "left"
      return opts
    end,
  },
}
