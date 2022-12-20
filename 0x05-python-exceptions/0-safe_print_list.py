<<<<<<< HEAD
#!/urs/bin/python3
def safe_print_list(my_list=[], x=0):
	count = 0

	for i in range(x):
		try:
			print("{}".format(my_list[i]), end=' ')
		except:
			break
		else:
			count += 1

	print()
	return (count)
=======
#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end=' ')
        except:
            break
        else:
            count += 1

        print()
        return (count)
>>>>>>> e4667039a0aaa14f75ad4b30a61e5e8dfceaf68a
