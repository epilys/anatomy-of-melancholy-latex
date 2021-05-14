"syntax off
" Define replacement macros for surround.vim:
"
" (To determine the ASCII code to use, :echo char2nr("-")).
"
" Define latin inline macro on 'l' == 108:
let g:surround_108 = "\\li{\r}"
" Define roman number macro on 'r' == 114:
let g:surround_114 = "\\rn{\r}"
" Define verse environment macro on 'v' == 118:
let g:surround_118 = "\\begin{verse}\n\r\n\\end{verse}"

" Latin numeral regexp:
" / [mdclxvi]\+\.
