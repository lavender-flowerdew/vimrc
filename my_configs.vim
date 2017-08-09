" Start with nerd open if no file specified
" autocmd StdinReadPre * let s:std_in=1
" autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
" autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" My mappings
map <Leader><Leader><Leader> :nohl<cr>
map <C-m> %
map <leader>q :qa!<cr>
imap <Leader>si :SortScalaImports<cr>
imap <Leader>ss :ToggleWhitespace<cr>
imap <Leader>sw :StripWhitespace<cr>
autocmd FileType scala autocmd BufEnter <buffer> EnableStripWhitespaceOnSave
map <Leader>n :set invnumber <bar> :GitGutterToggle<CR>
map <Leader>g :grep! "\b<C-R><C-W>\b"<CR>:cw<CR>
" map <Leader><Leader> :!clear<CR>:exe '!cat %'<CR>
nmap <Leader>gs :Gstatus<CR>
nmap <Leader>gc :Gread<CR>
nnoremap <S-Right> <C-]>
vnoremap <S-Right> <C-]>
nnoremap <S-Left> <C-T>
vnoremap <S-Left> <C-T>
map <C-n> :tn<CR>
map <C-p> :tp<CR>

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

:GitGutterAll
set number
