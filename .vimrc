"syntax off

" surround.vim settings
"
let g:surround_indent = 0
" Define replacement macros
"
" (To determine the ASCII code to use, :echo char2nr("-")).
"
" Define latin verse env macro on 'j' == 106:
let g:surround_106 = "\\begin{latin}\n\\begin{verse}\n\r\n\\end{verse}\n\\end{latin}"

" Define quote env macro on 'q' == 113:
let g:surround_113 = "\\begin{quote}%\n\r\n\\end{quote}%"
" Define latin env macro on 'L' == 76:
let g:surround_76 = "\\begin{latin}\n\r\n\\end{latin}"
" Define latin inline macro on 'l' == 108:
let g:surround_108 = "\\li{\r}"
" Define roman number macro on 'r' == 114:
let g:surround_114 = "\\rn{\r}"
" Define verse environment macro on 'v' == 118:
let g:surround_118 = "\\begin{verse}%\n\r\n\\end{verse}%"
" Define textlatin macro on 't' == 116:
let g:surround_116 = "\\textlatin{\r}"

" Latin numeral regexp:
" / [mdclxvi]\+\.
