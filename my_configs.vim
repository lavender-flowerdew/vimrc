" Start with nerd open if no file specified
" autocmd StdinReadPre * let s:std_in=1
" autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
" autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" My mappings
map <Leader><Leader> :nohl<cr>
map <Leader>si :SortScalaImports<cr>
map <Leader>ss :ToggleWhitespace<cr>
map <Leader>sw :StripWhitespace<cr>
autocmd FileType scala autocmd BufEnter <buffer> EnableStripWhitespaceOnSave
map <Leader>n :set invnumber <bar> :GitGutterToggle<CR>
map <Leader>g :grep! "\b<C-R><C-W>\b"<CR>:cw<CR>
" map <Leader><Leader> :!clear<CR>:exe '!cat %'<CR>
map <Leader>gs :GStatus<CR>
map <Leader>gc :GRead<CR>
nnoremap <C-Right> <C-]>
vnoremap <C-Right> <C-]>
nnoremap <C-Left> <C-T>
vnoremap <C-Left> <C-T>
map <C-n> :tn<CR>
map <C-p> :tp<CR>
nmap <leader>

" CTags
set tags=tags-dep,./tags;,tags

" Colors
set t_Co=256
"uncomment next two lines if using in tmux
"set t_8f=\[[38;2;%lu;%lu;%lum
"set t_8b=\[[48;2;%lu;%lu;%lum
set termguicolors
set background=dark
set colorcolumn=160
let g:solarized_termtrans=1
let g:solarized_statusline="low"
let g:solarized_diffmode="high"
let g:solarized_term_italics=0
color solarized8_dark_sea
color gruvbox
