let s:current_dir=expand("<sfile>:p:h")
py import sys, vim
py if not vim.eval('s:current_dir') in sys.path:
	\ sys.path.append(vim.eval('s:current_dir'))
py import mathvim

function! Testt()
	py mathvim.init()
	while 1
		let g:math_key = getchar()
		py mathvim.processKey()
		redraw
	endwhile
endfunction
