import subprocess
import string

cmd = "valgrind --trace-children=yes --tool=callgrind ./chal program < flag.txt 2>&1 | grep refs | cut -d ' ' -f11"

flag = 'uiuctf{'

for i in range(64):
	if flag[-1] == '}':
		break
	for char in string.printable:
		with open('./flag.txt', 'w') as f:
			f.write(flag + char)
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
		res = p.communicate()[0].strip().decode()
		res = int(res.replace(',', ''))
	
		print(flag, char, res)
		if char == string.printable[0]:
			last = res
		else:
			if res > last + 100:
				flag += char
				break
			elif last > res + 100:
				flag += string.printable[0]
				break
	else:
		print('BRUH')
else:
	print('BRUH pt.2')

print(flag)

# uiuctf{ar3_y0u_4_r3al_vm_wh3r3_(gpt_g3n3r4t3d_th1s_f14g)}
