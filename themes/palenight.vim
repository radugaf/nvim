if (has("termguicolors"))
    set termguicolors
    hi LineNr ctermbg=NONE guibg=NONE
endif

let g:palenight_color_overrides = {
\    'black': { 'gui': '#1e2127', "cterm": "0", "cterm16": "0" },
\}

let g:palenight_terminal_italics=1


set background=dark
colorscheme palenight



